# Reproducibility Pipeline: Joe's Nature Publication (`pain.py`)

This repository provides environment specifications and step-by-step instructions to reproduce the analysis pipeline from hw6 without modifying the original script `pain.py`.

## System Specifications

* **Operating System:** Linux (`x86_64`)
* **Environment & Package Manager:** [Pixi](https://pixi.sh/) (workspace-based conda/pixi package manager)
* **Base Python Version:** Python 3.13 (`python=3.13.*`)

## Technical Analysis of Conflicts & Solutions

1. **Python 3.13 Syntax & Built-ins:**
   * **Nested f-strings:** Reusing identical quotes within expressions (`f"{", ".join(series)}"`, nested recursions) requires the PEP 701 PEG parser (Python 3.12+).
   * **`glob.translate()`:** Added in Python 3.13.
   * **`typing.TypeIs`:** Formalized in PEP 742 (Python 3.13).

2. **Standard Library `annotationlib` Module:**
   * The import `from annotationlib import get_annotations, Format` corresponds to a standard module introduced in Python 3.14 (PEP 649 / PEP 749). It is not distributed on PyPI.
   * *Solution:* The reference implementation from CPython is retrieved directly, adapting Python 3.14 template string syntax (`_Template = type(t"")` $\to$ `_Template = None`) so that it parses and runs smoothly under Python 3.13.

3. **Legacy Biopython Submodules (`Bio.pairwise2` & `Bio.SubsMat`):**
   * Modern Biopython releases (1.80+) removed both `Bio.pairwise2` and `Bio.SubsMat`.
   * Building legacy `biopython==1.79` fails under Python 3.13 due to internal C-API changes.
   * *Solution:* Modern `biopython` is installed via `conda-forge`. The pure-Python legacy modules (`pairwise2.py` and `SubsMat/MatrixInfo.py`) from Biopython 1.79 are imported into the active environment's `site-packages`. The circular dependency in `SubsMat/__init__.py` is resolved by stripping the unused `FreqTable` import.

4. **Pandas 2.x `set` Validation:**
   * The script initializes `pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})`. In Pandas 2.x, passing a `set` directly to `DataFrame.__init__` raises `ValueError: index cannot be a set`.
   * *Solution:* `pandas/core/frame.py` is patched in-place to convert the incoming set to a list (`index = list(index)`).

## Prerequisites

Install Pixi:
```bash
curl -fsSL https://pixi.sh/install.sh | bash
export PATH="$HOME/.pixi/bin:$PATH"
```

---

## Step-by-Step Reproduction Recipe

### Step 1: Place `pixi.toml` in the Project Root

The configuration file `pixi.toml` **must be located in the root directory** alongside `pain.py`:

```text
pain-hw6/
├── pain.py
├── pixi.toml
└── README.md
```

You can create and write the `pixi.toml` file directly using:

```bash
cat << 'EOF' > pixi.toml
[workspace]
name = "pain-hw6"
version = "0.1.0"
description = "Reproducible environment for Joe's Nature code (pain.py)"
authors = ["Prokopenko AV"]
channels = ["conda-forge", "bioconda"]
platforms = ["linux-64"]

[dependencies]
python = "3.13.*"
pandas = ">=2.2.0"
pyarrow = "*"
opencv = "*"
protobuf = "*"
biopython = ">=1.83"
EOF
```

---

### Step 2: Initialize and Install the Environment

From the project root directory, run:

```bash
pixi install
```

---

### Step 3: Supply `annotationlib.py` from CPython

Fetch the official standard library module and adapt the template-string syntax for Python 3.13:

```bash
curl -fsSL https://raw.githubusercontent.com/python/cpython/main/Lib/annotationlib.py | sed 's/_Template = type(t"")/_Template = None/' > .pixi/envs/default/lib/python3.13/site-packages/annotationlib.py
```

---

### Step 4: Restore Missing Legacy Biopython Modules

Download `pairwise2.py` and `SubsMat/MatrixInfo.py` from the official Biopython 1.79 release:

```bash
# 1. Download pairwise2
curl -fsSL https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/pairwise2.py -o .pixi/envs/default/lib/python3.13/site-packages/Bio/pairwise2.py

# 2. Create SubsMat directory
mkdir -p .pixi/envs/default/lib/python3.13/site-packages/Bio/SubsMat

# 3. Download SubsMat __init__.py
curl -fsSL https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/__init__.py -o .pixi/envs/default/lib/python3.13/site-packages/Bio/SubsMat/__init__.py

# 4. Download SubsMat MatrixInfo.py
curl -fsSL https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/MatrixInfo.py -o .pixi/envs/default/lib/python3.13/site-packages/Bio/SubsMat/MatrixInfo.py

# 5. Remove the unused FreqTable import to prevent circular import errors
sed -i '/FreqTable/d' .pixi/envs/default/lib/python3.13/site-packages/Bio/SubsMat/__init__.py
```

---

### Step 5: Patch Set Index Handling in Pandas

Allow sets to be passed as indices in `pandas/core/frame.py`:

```bash
sed -i 's/raise ValueError("index cannot be a set")/index = list(index)/g' .pixi/envs/default/lib/python3.13/site-packages/pandas/core/frame.py
```

---

## Running the Pipeline

Run the pipeline using Pixi:

```bash
pixi run python pain.py
```

### Expected Output
```text
✨❤️ Всё работает, ты больш(ой/ая) молодец!!! ✨❤️
```

---

## Part 2: Rest & Recreation Proof 🌿

> **How I rested this week:**
- Ловила белок
![Ловила белок](photos/belka.jpg)
- Чилила с котом
![Чилила с котом](photos/kot.jpg)
- Чухала кошку
![Чухала кошку](photos/koshka.jpg)
- Жевала пятнистый арбуз
![Жевала пятнистый арбуз](photos/watermelon.jpg)

