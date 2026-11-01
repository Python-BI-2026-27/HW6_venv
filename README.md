# Reproducing `pain.py` (HW 6 — Virtual environments)

**Tested on:** Ubuntu 24.04 via WSL2 on Windows 11, x86_64,
Python 3.14.10 (conda-forge), gcc 15.3 (conda-forge `compilers`).

`pain.py` is **not modified**. Everything is fixed via environment
setup, package versions, and two small edits to *installed* modules
(explicitly allowed by the assignment: "you may need to edit installed
modules").

## Why each pin

- **Python 3.14** — the script uses `annotationlib` (3.14+),
  `iter(..., stop_exception=...)` (3.14+), `typing.TypeIs` (3.13+),
  `glob.translate` (3.13+), `typing.override` (3.12+), and PEP 701
  f-strings with same-type nested quotes (3.12+).
- **biopython==1.76** — `Bio.pairwise2` was removed in 1.80,
  `Bio.SubsMat` in 1.78.
- **google-api-core** — `import google` needs the `google/`
  namespace package. The PyPI package `google==3.0.0` only creates
  `googlesearch/` and does **not** provide `import google`.
- **pyarrow** — required by `dtype="float32[pyarrow]"`.
- **opencv (conda-forge)** — provides `cv2`.

## Step-by-step

### 1. Create the environment

```bash
mamba env create -f environment.yaml
mamba activate joe-pain
python --version    # 3.14.x
```

If `mamba activate` complains about an uninitialized shell:

```bash
eval "$(mamba shell hook --shell bash)"
mamba activate joe-pain
```

### 2. Build Biopython 1.76 in pure-Python mode

The C extension `Bio.cpairwise2` uses `PyEval_CallObject`, which was
removed in Python 3.13+, so it cannot compile under 3.14. Biopython
ships a pure-Python fallback for `pairwise2`, which is sufficient for
`pain.py`.

```bash
pip install "setuptools<70" wheel

mkdir -p ~/bio-build && cd ~/bio-build
pip download --no-deps --no-binary :all: biopython==1.76
tar xf biopython-1.76.tar.gz
cd biopython-1.76

python - <<'PY'
import pathlib, re
p = pathlib.Path("setup.py")
s = p.read_text()
s2, n = re.subn(r"ext_modules\s*=\s*EXTENSIONS", "ext_modules=[]", s)
assert n == 1, f"substitutions: {n}"
p.write_text(s2)
print("patched setup.py: ext_modules=[]")
PY

pip install --no-build-isolation --no-deps .
cd ~
```

Verify:

```bash
python -c "import Bio; print(Bio.__version__)"     # 1.76
python -c "from Bio import pairwise2; from Bio.SubsMat import MatrixInfo; print('bio ok')"
```

### 3. Install the remaining pip deps

```bash
pip install google-api-core
python -c "import google, cv2, pandas, pyarrow; print('deps ok')"
```

(`google.__file__` is `None` because `google` is a PEP 420 namespace
package created by `google-api-core`. `import google` succeeds — that
is all `pain.py` needs.)

### 4. Patch `Bio/pairwise2.py` (installed module)

Under Python 3.14 the pure-Python fallback of Biopython 1.76 returns
plain tuples `(seqA, seqB, score, begin, end)` from
`pairwise2.align.*`, while `pain.py` expects `x.score`. The historical
Biopython 1.76 API returns a namedtuple `Alignment`. We append a small
shim that wraps `_align` and `_clean_alignments` so their results are
re-wrapped as `collections.namedtuple("Alignment", "seqA seqB score begin end")`:

```bash
PAIRWISE=$(python -c "import Bio.pairwise2 as p; print(p.__file__)" 2>/dev/null)
cat >> "$PAIRWISE" <<'PY'

# ---- HW6 shim: ensure .score attribute on align.* results ----
import collections as _collections
_Alignment = _collections.namedtuple("Alignment", "seqA seqB score begin end")

def _hw6_coerce(res):
    if isinstance(res, list):
        out = []
        for x in res:
            if isinstance(x, tuple) and len(x) == 5 and not hasattr(x, "score"):
                out.append(_Alignment(*x))
            else:
                out.append(x)
        return out
    return res

if "_align" in globals():
    _hw6_orig_align = _align
    def _align(*args, **kwargs):
        return _hw6_coerce(_hw6_orig_align(*args, **kwargs))

if "_clean_alignments" in globals():
    _hw6_orig_clean = _clean_alignments
    def _clean_alignments(tracebacks):
        return _hw6_coerce(_hw6_orig_clean(tracebacks))
PY
```

Verify:

```bash
python - <<'PY'
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
res = list(pairwise2.align.globalds("ATATCTCGATCGCTACGTC", "CTAGCTCGCTGCTCAGCATC",
                                    matlist.blosum62, -10, -0.5))
print(type(res[0]), hasattr(res[0], "score"), res[0].score)
PY
# <class 'Bio.pairwise2.Alignment'> True 70.0
```

### 5. Patch `pandas/core/frame.py` (installed module)

`pain.py` does `pd.DataFrame([1,2,3,4], index={1,2,3,4})`. pandas 3.x
rejects a `set` as `index` (`ValueError: index cannot be a set`), while
pandas 2.x silently converted it. We restore the 2.x behaviour by
replacing the `raise` with a conversion:

```bash
FRAME=$(python -c "import pandas.core.frame as f; print(f.__file__)")
python - "$FRAME" <<'PY'
import sys, pathlib
p = pathlib.Path(sys.argv[1])
s = p.read_text()
old = '            raise ValueError("index cannot be a set")'
new = '            index = list(index)'
assert old in s, "pattern not found"
s = s.replace(old, new, 1)
p.write_text(s)
print("patched:", p)
PY
```

Verify:

```bash
python - <<'PY'
import pandas as pd
df = pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})
print(df)
print("pandas", pd.__version__)
PY
```

### 6. Run

```bash
cd ~/HW6_venv
python pain.py
```

Expected output:

```
✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
```

The `BiopythonWarning: Import of C module failed. Falling back to pure
Python implementation.` message from `pairwise2` is expected and
harmless.

## Summary of the two patches

| File (installed module) | Why | What |
|---|---|---|
| `Bio/pairwise2.py` | pure-Python fallback returns plain 5-tuples; `pain.py` uses `x.score` | Append shim wrapping `_align` and `_clean_alignments` to return `namedtuple("Alignment", ...)` |
| `pandas/core/frame.py` | pandas 3.x rejects `index={...}` | Replace `raise ValueError("index cannot be a set")` with `index = list(index)` |

`pain.py` is unchanged in both cases.

## Part 2 — Rest

I added a photo and a brief comment about the rest.
![Rest 1](rest1.jpg)

![Rest 2](rest2.jpg)
