# HW6: Virtual environments
This solution runs pain.py without modifying the script.

**Platform compatibility**: The environment file avoids platform-specific packages and build identifiers and is intended for Linux and macOS. The setup was tested on Ubuntu under WSL2. On Windows, run the commands through WSL2; on Linux and macOS, use Bash/Zsh.

**System used**: Ubuntu under WSL2

## 1. Prepare the repository 
Install Conda or Mamba before starting. Run the commands below from the repository root in a Bash/Zsh terminal.

The repository should contain `pain.py`, `environment.yaml`, and `legacy_dir/SubsMat/`. 
The `SubsMat` directory must be copied from Bio/SubsMat in the original Biopython 1.79 source distribution.

Source: [Biopython 1.79 release files.](https://pypi.org/project/biopython/1.79/#files)

## 2. Create the environment 
Use the following contents for `environment.yaml`:

```YAML
name: pain
channels:
  - conda-forge
dependencies:
  - python=3.14
  - pip=26.2.2
  - pandas=3.1.1
  - pyarrow=26.0.1
  - pip:
      - biopython==1.88
      - opencv-python==5.0.0.93
      - google-api-python-client==2.201.0
```
Create and activate the environment:
```Bash
conda env create -f environment.yaml
conda activate pain 
```
Alternatively, use `mamba env create -f environment.yaml` to create it.

The file lists the main dependencies without Linux-specific system packages or build identifiers. Installation on other platforms depends on the availability of these versions. The original setup was run on WSL2 Ubuntu.

## 3. Restore Bio.SubsMat
The script imports `Bio.SubsMat.MatrixInfo`, which is restored from Biopython 1.79. Copy the bundled folder into the installed Biopython package:

```Bash
cp -R legacy_dir/SubsMat "$CONDA_PREFIX/lib/python3.14/site-packages/Bio/"
```
Keep Biopython 1.88 installed. Only the missing `Subsmat` directory is added.

## 4. Fix pandas indexing 
Open the installed `frame.py` in a text editor. For example, with Nano:

```Bash
nano "$CONDA_PREFIX/lib/python3.14/site-packages/pandas/core/frame.py"
```

Inside `DataFrame.__init__`, find:

```python
if isinstance(index, set):
    raise ValueError("index cannot be a set")
```
Replace it with:
```python
if isinstance(index, set):
    index = list(index)
```
Keep the indentation and save the file. In Nano, press `Ctrl+O`, then `Enter`, then `Ctrl+X`.
This converts the set used as an index in `pain.py` into a list before pandas processes it.

## 5. Run the script
```bash
python pain.py
```
Expected final output:
```text
✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
```
