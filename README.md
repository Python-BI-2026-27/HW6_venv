# Instructions for relieving pain

## Tested on 
- Windows 11 (25H2)
- mamba 2.9.0 (Miniforge3)
- All commands are run in PowerShell

## Pain relief steps

### 1. Create and activate the environment in terminal 
```powershell
mamba env create -f environment.yaml
conda activate pain_env
```

### 2. Restore the deleted module Bio.SubsMat
The Bio.SubsMat module was removed from biopython version 1.80 and later. Therefore, we need to download version 1.79 of biopython and copy the Bio.SubsMat module from version 1.79 to our version 1.88.

Download directory biopython-179 to the working directory.
```powershell
git clone --depth 1 --branch biopython-179 https://github.com/biopython/biopython.git biopython-179
cd biopython-179\Bio
Copy-Item -Recurse SubsMat (python -c "import Bio; print(Bio.__path__[0])")
```
Return to the working directory: 
```powershell
cd ../..
```
You can delete the copied directory biopython-179

### 3. Fix pandas so that it accepts a set as an index
Pandas version 3.1.0 prohibits passing a set as an index and raises a ValueError: index cannot be a set. The check in the code of the installed pandas should be changed: instead of an error, the set is converted into a list.

The command prints the path to frame.py. Open this file in a text editor
```powershell
python -c "import pandas.core.frame; print(pandas.core.frame.__file__)"
```
Go to line 507 or search for "index cannot be a set" in the frame.py file and make the replacement from:
```python
# GH47215
if isinstance(index, set):
    raise ValueError("index cannot be a set")
```
To:
```python
# GH47215
if isinstance(index, set):
    index = list(index)
```
Save the changes in the frame.py file.

### 4. Pain launch
```powershell
python pain.py
```

# Работа - не волк. Работа - это ворк, а волк - это ходить (It cannot be translated into English)
![Me and the fox (on the right)](сonfirmation_of_rest\chilling_out.jpg)