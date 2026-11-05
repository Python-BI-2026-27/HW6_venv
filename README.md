# HW6

## Part 1: running `pain.py`

Tested on: macOS 14.1.2, Apple M2, conda, Python 3.14.

### Prerequisites

- conda
- A C compiler, needed to build Biopython from source
- Internet access

Run all commands from the project directory (the one containing `pain.py` and `environment.yaml`).

### 1. Create and activate the environment

```bash
conda env create -f environment.yaml
conda activate pain_env
```

This installs Python 3.14, pandas 2.3.3, numpy, pyarrow, opencv-python and google-api-core.

- Python 3.14 is required because `pain.py` imports `annotationlib`, which is new in 3.14.

### 2. Patch pandas

`pain.py` creates a `DataFrame` with a `set` as the index. pandas 2.3.3 and 3.1.1
both reject this with `ValueError: index cannot be a set`. The check is
removed in the installed pandas:

```bash
python - <<'EOF'
import pandas, pathlib
p = pathlib.Path(pandas.__file__).parent / "core" / "frame.py"
s = p.read_text()
old = 'raise ValueError("index cannot be a set")'
assert old in s
p.write_text(s.replace(old, "pass"))
EOF
```

Do this after the environment is created.

### 3. Install a patched Biopython 1.78

`pain.py` imports `Bio.SubsMat`, which is deprecated in newer
Biopython releases, so Biopython 1.78 is used. It has no
wheel for Python 3.14, and building it from source fails because
`Bio/cpairwise2module.c` calls `PyEval_CallObject`, which was removed from the
CPython C API in 3.13. `PyObject_CallObject` has the same signature, so `PyEval_CallObject` can be
replaced by it in the sources.

Create a directory, download the Biopython 1.78 sources and extract them:

```bash
mkdir bp178
cd bp178
pip download biopython==1.78 --no-deps --no-binary :all:
tar xzf biopython-1.78.tar.gz
cd biopython-1.78
```

Patch `Bio/cpairwise2module.c` by replacing `PyEval_CallObject` with `PyObject_CallObject`:

```bash
python - <<'EOF'
import pathlib
p = pathlib.Path("Bio/cpairwise2module.c")
s = p.read_text()
assert "PyEval_CallObject" in s
p.write_text(s.replace("PyEval_CallObject", "PyObject_CallObject"))
EOF
```

Install the patched Biopython:

```bash
pip install .
```

Return to the project directory:

```bash
cd ../..
```

### 4. Run

```bash
python pain.py
```

## Part 2
Photo with friends from a desert in Abu Dhabi
![Photo with friends from a desert in Abu Dhabi](photo.jpeg)
