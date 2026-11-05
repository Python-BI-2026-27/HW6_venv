# HW6 — Virtual Environments
## Environment
The script was successfully executed on:

- **Operating system:** macOS 15.7.4
- **Architecture:** ARM64 (Apple Silicon)
- **Python:** 3.14.3
- **pip:** 26.2.2
- **Environment manager:** Conda

## Installation
### 1. Create a Conda environment
Create a new environment with Python 3.14.3:

```bash
conda create -n hw6_py314 -c conda-forge --override-channels python=3.14.3
conda activate hw6_py314
```

### 2. Install dependencies
From the repository directory, run:

```bash
python -m pip install -r requirements.txt
```

### 3. Install Biopython 1.79
The script uses `Bio.SubsMat`, which is available in Biopython 1.79 but was removed in later versions.
Biopython 1.79 cannot be built normally with Python 3.14 because its C extensions are incompatible with this Python version.
First, install the required build tools:

```bash
python -m pip install setuptools==84.2.1 wheel==0.48.0
```

Download and extract the Biopython source distribution:

```bash
python -m pip download biopython==1.79 --no-deps --no-binary=:all: -d /tmp
cd /tmp
tar -xzf biopython-1.79.tar.gz
cd biopython-1.79
```

Open `setup.py`:

```bash
nano setup.py
```

Find:

```python
ext_modules=EXTENSIONS,
```

Replace it with:

```python
ext_modules=[],
```

This disables compilation of the incompatible C extensions.
Save the file and install the modified package:

```bash
python -m pip install . --no-build-isolation
```

Verify the installation:

```bash
python -c "from Bio.SubsMat import MatrixInfo; print('Biopython OK')"
```

### 4. Fix pandas compatibility
The script passes a Python `set` as the DataFrame index. Pandas 3.1.1 explicitly rejects this input.
Locate the installed `frame.py` file:

```bash
python -c "import pandas.core.frame as f; print(f.__file__)"
```

Open the file in a text editor and find:

```python
if isinstance(index, set):
    raise ValueError("index cannot be a set")
```

Replace it with:

```python
if isinstance(index, set):
    index = list(index)
```

This converts the set into a supported index format.
**Note:** Sets do not guarantee element ordering. This modification is intended only for reproducing the provided educational script.

### 5. Run the script
Return to the repository directory containing `pain.py`.
Run:

```bash
python pain.py
```

Expected output:

```text
✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
```

The original `pain.py` file was not modified.

## Part 2 — Rest
This week, I took some time to relax by walking in the park and collecting acorns.
I also had fun creating memes featuring my hamster.

### Photos

**Walking in the park and collecting acorns:**

![Acorns collected during my walk](images/acorn.jpeg)

**Creating memes with my hamster:**

![MY KURDUK](images/hamster_kurduk.png)
