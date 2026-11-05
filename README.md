# Rain outside, pain inside

This project was tested on Ubuntu 24.04.4 LTS with Python 3.14.10 using a Mamba environment

## Installation and setup

### 1. Create and activate the environment

```bash
mamba env create -f environment.yaml
mamba activate pain
``` 

### 2. Restore the legacy Bio.SubsMat module

Recent versions of Biopython no longer include Bio.SubsMat. The following compatibility module restores 
the MatrixInfo.blosum62 interface required by the original script.

```bash
BIO_PATH=$(python -c "import Bio; print(Bio.__path__[0])")

mkdir -p "$BIO_PATH/SubsMat"

cat > "$BIO_PATH/SubsMat/__init__.py" <<'EOF'
from Bio.Align import substitution_matrices

class MatrixInfo:
    blosum62 = substitution_matrices.load("BLOSUM62")
EOF
```

### 3. Pandas compatibility adjustment

The original script passes a Python set as a DataFrame index. Pandas 3.1.1 does not support sets as indexes.
To improve it, you need to do some corrections in file frame.py:

```bash
nano "$CONDA_PREFIX/lib/python3.14/site-packages/pandas/core/frame.py"
```
Find the current line:
```python
if isinstance(index, set):
	raise ValueError("index cannot be a set")
```
And replace it to:
```python
if isinstance(index, set):
    index = sorted(index)
```

### 4. Run the script
```python
python pain.py
```

### Evidence of rest
In my free time I enjoy playing video games. Today it's Warcraft 3
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/df513ed9-aa3b-4705-a686-472dd0d5874a" />
