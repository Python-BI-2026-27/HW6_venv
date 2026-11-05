# Running Joe's analysis script (`pain.py`)

## System

- macOS 11.6.1 (Big Sur, build 20G224)
- Architecture: x86_64 (Intel)
- Package manager: micromamba 2.10.0
- Python 3.14.10 (conda-forge)

## Files in this repository

- `environment.yaml`: conda-forge packages (Python, pandas, pyarrow, protobuf, OpenCV, pip).
- `README.md`.
- `pain.py`: the script.

## Steps

### 1. Create the environment

From the repository folder:

```bash
micromamba env create -n pain-env -f environment.yaml -y
```

Activate the environment. Run the shell hook in each new terminal before activating:

```bash
eval "$(micromamba shell hook --shell zsh)"
micromamba activate pain-env
```

### 3. Install Biopython 1.79 from source, without C extensions

Biopython 1.79 is required because it still contains `Bio.SubsMat`, which was removed in later versions. No conda-forge build of 1.79 exists for Python 3.14. The C extensions of 1.79 do not compile on Python 3.14, so they are disabled. The script only uses pure-Python modules (`Bio.pairwise2`, `Bio.SubsMat`).

```bash
mkdir -p ~/src && cd ~/src
python -m pip download "biopython==1.79" --no-binary :all: --no-deps -d .
tar -xzf biopython-1.79.tar.gz
cd biopython-1.79
sed -i '' 's/^EXTENSIONS = \[$/EXTENSIONS = []  # disabled for Python 3.14\n_UNUSED_EXTENSIONS = [/' setup.py
grep -n "EXTENSIONS" setup.py
python -m pip install .
cd ~
```

Expected output: the `grep` shows the line `EXTENSIONS = []  # disabled for Python 3.14`.


### 4. Patch pandas: accept `set` as index and columns

`pain.py` line 46 calls `pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})`. pandas 3.1.1 raises `ValueError: index cannot be a set` on this call. The script cannot be changed, so the check in the installed pandas is replaced with a conversion to `list`.

Back up the file first, then patch it:

```bash
PANDAS_FRAME="$(python -c 'import pandas, os; print(os.path.join(os.path.dirname(pandas.__file__), "core", "frame.py"))')"
cp "$PANDAS_FRAME" "$PANDAS_FRAME.bak"

python - "$PANDAS_FRAME" <<'EOF'
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
old = '''        if isinstance(index, set):
            raise ValueError("index cannot be a set")
        if isinstance(columns, set):
            raise ValueError("columns cannot be a set")
'''
new = '''        if isinstance(index, set):
            index = list(index)
        if isinstance(columns, set):
            columns = list(columns)
'''
assert s.count(old) == 1, "anchor not found or not unique"
open(p, "w", encoding="utf-8").write(s.replace(old, new))
print("patched")
EOF
```

Expected output: `patched`.

To revert the change:

```bash
cp "$PANDAS_FRAME.bak" "$PANDAS_FRAME"
```

### 5. Run the script

```bash
cd /path/to/repository
python pain.py
```

The script runs to the end and prints a greeting line with ✨❤ symbols.

### 6. Relax

![Love reading](reading.png)
