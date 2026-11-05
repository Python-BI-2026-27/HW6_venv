# Running pain.py in Python 3.14

A step-by-step guide to executing `pain.py`—a compatibility stress-test script requiring Python 3.14 features alongside legacy library behaviors—without modifying the original script source.

---

## Prerequisites

- Mamba (or Conda but why would you) package manager
- Linux / WSL environment

---

## Setup Instructions

### 1. Environment Setup

Create and activate an isolated Python 3.14 environment:

```
mamba create -n pain_env -c conda-forge python=3.14 -y
mamba activate pain_env

# Core data processing & Apache Arrow backend
mamba install -y pandas pyarrow
```
# Additional libraries checked by the script

```
python -m pip install protobuf google-api-python-client opencv-python biopython

```

Modern libraries have removed or restricted legacy features targeted by the script. Apply the following two in-place runtime patches:

Bio.SubsMat was removed in Biopython 1.78+. Register an in-memory replacement pointing to modern substitution matrices:
Disable restriction of a set as index in modern pandas in pandas/core/frame.py (Change if to if else function):



```
echo "import sys; from Bio.Align import substitution_matrices as sm; sys.modules['Bio.SubsMat'] = type('', (), {'MatrixInfo': type('', (), {'blosum62': sm.load('BLOSUM62')})})" >> $(python -c "import Bio; print(Bio.__file__)")


sed -i 's/if isinstance(index, set):/if False:/' $(python -c "import pandas; print(pandas.core.frame.__file__)")
```

Now you are done and ready to go!

```
python pain.py
```