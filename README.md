HW 6. Virtual Environments

System information

The script was tested in the following environment:

- Operating system: Ubuntu 24.04.3 LTS
- Linux environment: WSL (Windows Subsystem for Linux)
- Architecture: x86_64
- Python: 3.14.10
- Environment manager: Miniconda
- Conda environment: "pain"

1. Create the environment

Create the Conda environment using the provided "environment.yaml" file:

conda env create -f environment.yaml

Activate it:

conda activate pain

2. Compatibility modifications

Two compatibility modifications were required to run the original "pain.py" script without changing its source code.

2.1. Biopython compatibility

The script imports:

from Bio.SubsMat import MatrixInfo as matlist

The "Bio.SubsMat" module is no longer available in Biopython 1.88.

A compatibility module was therefore added to the installed Biopython package.

Find the Biopython installation directory:

BIO_DIR=$(python -c "import Bio; print(Bio.__path__[0])")

Create the compatibility package:

mkdir -p "$BIO_DIR/SubsMat"

Create "__init__.py":

cat > "$BIO_DIR/SubsMat/__init__.py" <<'EOF'
from . import MatrixInfo
EOF

Create "MatrixInfo.py":

cat > "$BIO_DIR/SubsMat/MatrixInfo.py" <<'EOF'
from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")
EOF

2.2. pandas compatibility

The original script passes a Python set as the DataFrame index:

pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})

The installed pandas version raises a "ValueError" when a set is passed as an index.

To retain the original script unchanged, the corresponding check in "pandas/core/frame.py" was modified to convert sets into sorted lists.

Locate the file:

PANDAS_FRAME=$(python -c "import pandas.core.frame as f; print(f.__file__)")

Back up the original file:

cp "$PANDAS_FRAME" "$PANDAS_FRAME.bak"

Replace the original check with:

# Local compatibility modification for this exercise
if isinstance(index, set):
    index = sorted(index)
if isinstance(columns, set):
    columns = sorted(columns)

This modification is specific to the exercise and is not part of the standard pandas implementation.

3. Run the script

Make sure that "pain.py" is in the current working directory.

Run:

python pain.py

Expected output:

✨ ❤ Всё работает, ты больш(ой/ая) молодец!!! ✨ ❤

Notes

- The original "pain.py" file was not modified.
- The environment was created using Conda.
- "google-api-core" was installed using pip.
- The Biopython and pandas compatibility modifications were made in the installed packages.
- The script was successfully executed in the described environment.s
