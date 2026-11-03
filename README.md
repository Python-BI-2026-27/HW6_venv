# HW6: Running `pain.py`

Instructions for setting up an environment in which `pain.py` runs without modifying the script.

## System

The solution was tested on:

- OS: Ubuntu 22.04.5 LTS (x86_64)
- Package manager: micromamba 2.10.0 (standalone, no `sudo`)

## Why Python 3.14

`pain.py` uses language and standard-library features that appeared only in recent Python versions:

| Line | Feature | Minimum Python |
| --- | --- | --- |
| 4, 28 | `typing.override` | 3.12 |
| 9, 12 | nested f-strings with the same quotes (PEP 701) | 3.12 |
| 6 | `glob.translate` | 3.13 |
| 24 | `typing.TypeIs` | 3.13 |
| 15 | `annotationlib` module | 3.14 |

The strictest requirement is `annotationlib`, so Python 3.14 is needed. This also fixes the rest of the setup: the old Biopython and pandas that the script was written for are not installable on 3.14, so two of their pieces are restored/patched in steps 2–3 instead.

## Requirements

[Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html). No system Python is modified — 3.14 lives only inside the env. Run all commands in **one** terminal from the repository root; after step 1 the prompt must show `(pain)` on the left (without it the steps below would write into the system Python).

## Steps

### 1. Create and activate the environment

```bash
micromamba env create -f environment.yaml
micromamba activate pain
python --version   # Python 3.14.10
which python       # .../envs/pain/bin/python  (NOT /usr/bin/python3)
```

If the first run stalls on the conda-forge index (`Download error (28) ... repodata.json.zst` / `Subdir conda-forge/noarch not loaded` — a slow link, not a dependency issue), recreate the env pulling the index from a fast conda-forge mirror (e.g. `--override-channels -c https://mirrors.aliyun.com/anaconda/cloud/conda-forge/` with `python=3.14 pip -y`), then `pip install` the same pinned libs listed in `environment.yaml`. Do not `Ctrl+C` while progress timers move — a growing timer is a live download.

### 2. Restore the `Bio.SubsMat` module

`pain.py:41` imports `Bio.SubsMat`, removed from Biopython after 1.79. Biopython 1.79 cannot be installed on 3.14 (its `setup.py` uses the dropped `distutils` and 2019 C extensions that will not build on this ABI), so the module is copied from the 1.79 *source* tarball — fetched from PyPI's JSON API, no build — into the installed Biopython 1.88. The block self-skips if the import already works:

```bash
BIODIR="$(python -c 'import Bio, os; print(os.path.dirname(Bio.__file__))')"
if python -c "from Bio.SubsMat import MatrixInfo" 2>/dev/null; then
    echo "SubsMat already present, skipping transplant"
else
    WORK=/tmp/bio179; rm -rf "$WORK"; mkdir -p "$WORK"; cd "$WORK"
    SDIST_URL="$(curl -s https://pypi.org/pypi/biopython/1.79/json \
      | python -c 'import sys,json; d=json.load(sys.stdin); print(next(u["url"] for u in d["urls"] if u["packagetype"]=="sdist"))')"
    curl -LsO "$SDIST_URL"
    tar -xzf biopython-1.79.tar.gz
    rm -f "$BIODIR/SubsMat.py"
    cp -r biopython-1.79/Bio/SubsMat "$BIODIR/"
    cd - >/dev/null
fi
python -c "from Bio.SubsMat import MatrixInfo; print('blosum62 pairs =', len(MatrixInfo.blosum62))"   # 276
```

A `BiopythonDeprecationWarning` on the last line is expected (it is the warning the script's own `catch_warnings` block suppresses), not an error. `Bio.pairwise2` is left untouched — it still imports in 1.88.

### 3. Patch pandas

`pain.py:46` builds a `DataFrame` with a `set` as its index, which pandas rejects with `ValueError("index cannot be a set")` (since PR GH47215); pandas before that change is unavailable for 3.14. So the one failing branch in the installed `pandas/core/frame.py` is relaxed to convert the set to a list, as older pandas did. The patch keys on the exact `raise` text (stable across minors), not a line number, is idempotent, and aborts loudly if the marker ever moves:

```bash
PD="$(python -c 'import pandas, os; print(os.path.dirname(pandas.__file__))')"
python - "$PD/core/frame.py" <<'PY'
import sys, io
path = sys.argv[1]
src = io.open(path, encoding="utf-8").read()
OLD  = 'raise ValueError("index cannot be a set")'
NEW  = 'index = list(index)  # patched for pain.py:46'
MARK = '# patched for pain.py:46'
if MARK in src:
    print("already patched, nothing to do"); sys.exit(0)
n = src.count(OLD)
if n == 0:
    print("ERROR: marker not found — pandas changed"); sys.exit(1)
if n != 1:
    print(f"ERROR: marker found {n} times, expected 1 — aborting"); sys.exit(1)
io.open(path, "w", encoding="utf-8").write(src.replace(OLD, NEW))
print(f"patched OK ({n} replacement)")
PY
```

Only the `index` branch changes; the `columns` check and the rest of the constructor stay intact. With `{1,2,3,4}` (small ints, hash == value) iteration order is deterministic, so the index matches `data` and the frame is valid.

### 4. Run the script

```bash
python pain.py
```

Expected output (exit code 0, no traceback):

```
Всё работает, ты больш(ой/ая) молодец!!!
```
## Part 2

Here is how my sailing team and me closed sail's season in Moscow:

![my_team](images/IMG_0563.JPG)
![sailing_boat](images/IMG_0556.jpg)
![on water](images/IMG_4138.jpeg)
