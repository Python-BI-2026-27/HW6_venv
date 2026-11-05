
# Instruction how to run 'pain.py'

## Tested environment
- Platform: Google Colab (Linux, x86_64)
- Python: 3.14.10, installed in an isolated virtual environment using `uv`
- No GPU is required, CPU is enough.
The original 'pain.py' is left unchanged.

## Setup and run
Open a Linux shell in the root directory of this repository (the directory containing `pain.py` and `requirements.txt`). Run the following steps in order.

### 1. Create a Python 3.14 virtual environment
```bash
python3 -m pip install uv
uv venv --python 3.14 .venv
```
**python3 -m pip install uv** — Installs uv, a tool for managing Python versions and virtual environments.
**uv venv --python 3.14 .venv** — Creates a virtual environment named .venv using Python 3.14.

### 2. Install the Python dependencies
```bash
uv pip install --python .venv/bin/python -r requirements.txt
```
Installs all dependencies listed in requirements.txt into the .venv virtual environment using uv.

### 3. Restore the legacy 'Bio.SubsMat.MatrixInfo' module
'pain.py' imports 'Bio.SubsMat.MatrixInfo'. This module was present in Biopython 1.79 but is not included in Biopython 1.86. Download the **original** 'MatrixInfo.py' from the official Biopython repository into the installed package directory:
```bash
SITE_PACKAGES="$(.venv/bin/python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
mkdir -p "$SITE_PACKAGES/Bio/SubsMat"
curl -fL https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/MatrixInfo.py -o "$SITE_PACKAGES/Bio/SubsMat/MatrixInfo.py"
touch "$SITE_PACKAGES/Bio/SubsMat/__init__.py"
```
- SITE_PACKAGES=... — Finds the directory where Python packages are installed in the virtual environment.
- mkdir -p ... — Creates the missing Bio/SubsMat directory.
- curl -fL ... — Downloads the original MatrixInfo.py file from Biopython 1.79.
- touch ... — Creates an __init__.py file to make the directory a Python package.
Purpose: Restores the legacy Bio.SubsMat module required by pain.py without modifying the original script.

### 4. Allow a set as a DataFrame index in the installed pandas package
'pain.py' passes a set (`{1, 2, 3, 4}`) to `pandas.DataFrame(index=...)`. Pandas 2.3.3 rejects sets because they have no defined order. For this particular script, replace that error with a conversion to a sorted list **inside the installed pandas package**. The original 'pain.py' is not modified.
```bash
.venv/bin/python - <<'PY'
from pathlib import Path
import sysconfig

frame = Path(sysconfig.get_paths()["purelib"]) / "pandas/core/frame.py"
source = frame.read_text(encoding="utf-8")
old = 'raise ValueError("index cannot be a set")'
new = 'index = sorted(index)'

if old in source:
    frame.write_text(source.replace(old, new, 1), encoding="utf-8")
    print("Patched installed pandas.")
elif new in source:
    print("Pandas has already been patched.")
else:
    raise RuntimeError("Unexpected pandas source: the patch could not be applied.")
PY
```

### 5. Run the unchanged script
```bash
source .venv/bin/activate
python pain.py
```
The expected output includes following text:
✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
```

**Google Colab note:** Shell commands in separate `!` cells do not share an activated virtual environment. Instead, run the script with `!.venv/bin/python pain.py` in a Colab cell. When pasting the multi-line shell steps above into Colab, use a cell starting with `%%bash` (without `!` on each line).

## Why these steps are necessary
- Python 3.14 provides the standard-library `annotationlib` module and other modern syntax/features used by the script.
- Modern Biopython provides Python 3.14 support; the missing `MatrixInfo.py` is restored from genuine Biopython 1.79 source code.
- The pandas change converts an unordered set into a deterministic index without editing the assignment's script.

## Part 2: Rest this week
This week, I went to the cinema to watch *Twilight*. It was so cringe that when I got home, I decided to watch the exact same movie again, but with the Goblin revoicing. Honestly, the second version was much better. I also survived a three-hour workout at the gym and collected some beautiful autumn leaves in the park.
8/10 rest experience. 🍂
