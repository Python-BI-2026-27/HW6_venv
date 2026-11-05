# HW6
**How to run *pain.py* without changing the script itself.**
Tested on Arch Linux x86_64, with Miniforge(Mamba and Python 3.14) and zsh.
The steps also require *wget* and a text editor.

## 1. Create the environment
Install *Miniforge* if needed, and initialize Conda for your shell. Open a terminal in the directory containing *pain.py* and *environment.yaml* and run:
```bash
mamba env create -f environment.yaml
conda activate hw6_venv
```
The *environment.yaml* file contains the dependencies. 
Mamba may display a security warning about packages. Enter "y" to confirm the installation.

## 2. Restore the old Biopython module
Biopython 1.88 no longer includes Bio.SubsMat, which is required by *pain.py*. 

Download the three original files from Biopython 1.79:
```bash
mkdir -p "$CONDA_PREFIX/lib/python3.14/site-packages/Bio/SubsMat"
cd "$CONDA_PREFIX/lib/python3.14/site-packages/Bio/SubsMat"

wget https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/__init__.py
wget https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/MatrixInfo.py
wget https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/FreqTable.py

cd -
```

## 3. Modify pandas
The script uses a set as a DataFrame index, which pandas does not allow. Since *pain.py* can't be changed, we need edit pandas module.

Open the file:
```bash
cd "$CONDA_PREFIX/lib/python3.14/site-packages/pandas/core"
cp frame.py frame.py.bak
nvim frame.py
```
Find:
```
if isinstance(index, set):
    raise ValueError("index cannot be a set")
```
And replace with:
```
if isinstance(index, set):
    index = list(index)
```
Save the file and return to the project directory:
```bash
cd -
```

## 4. Run the script
```bash
python pain.py
```

___
## No rest, no life
![First rest](rest1.jpg)
![second rest](rest2.jpg)