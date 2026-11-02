# Python Homework 6 "Virtual Environments"

## System launch information:

- Operating system: Windows 11
- Shell: PowerShell
- Environment manager: Conda
- Python version: 3.14

## Steps:
### 1. Create the environment:

Install [`Miniconda`](https://www.anaconda.com/docs/getting-started/miniconda/install/windows-cli-install) (if still not installed).

Create `coda environment` from the provided `environment.yml` file:

```
conda env create -f environment.yml
conda activate hw6_env
```

If `conda activate` is unavailable, initialize `Conda` first:

```powershell
conda init powershell
```

### 2. Resolve the incompatibility of Biopython version:

The script uses `Bio.SubsMat`(v1.79), which was removed and switched to “Bio.Align.substitution_matrices” module in `Biopython` v1.8. `Biopython` v1.79 do not support `Python 3.14`. Thus, edit installed module of `Biopython` and restore the original module files.

Release the following commands in terminal:

```
$bioDir = python -c "import Bio; print(Bio.__path__[0])"
$subsDir = Join-Path $bioDir "SubsMat"
New-Item -ItemType Directory -Path $subsDir -Force

$source = "https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat"

Invoke-WebRequest "$source/__init__.py" -OutFile "$subsDir/__init__.py"
Invoke-WebRequest "$source/MatrixInfo.py" -OutFile "$subsDir/MatrixInfo.py"
Invoke-WebRequest "$source/FreqTable.py" -OutFile "$subsDir/FreqTable.py"
```

Commands interpretation:
1) Find path to the `Biopython` and save as variable;
2) Form path to `SubsMat` module;
3) Create directory for module;
4) Write to variable the path to module files in Biopython repository;
5) 5-7 commands to download module scripts.  

### 3. Resolve pandas index handling: 

The script uses a `Python set` as a DataFrame `index`. The installed `pandas` version rejects this type. Convert the `set` to an ordered `list` inside the installed `pandas` module.

Run the following commands:

```
$frame = python -c "import pandas.core.frame as f; print(f.__file__)"

$code = [System.IO.File]::ReadAllText($frame)
$old = 'raise ValueError("index cannot be a set")'

$code = $code.Replace($old, 'index = sorted(index)')
[System.IO.File]::WriteAllText(
    $frame,
    $code,
    [System.Text.UTF8Encoding]::new($false)
)
```

Commands interpretation:
1) Find and write to variable path to `frame.py` file of pandas;
2) Read file content; 
3) Set code string of error call, which should be edited;
4) Replace the error call with a conversion of the set into a list;
5) Sav echanges to `frame.py`.

These modification allows the `integer set` used in `pain.py` to be converted into a `sorted list`.

### 4. Run the whole script:

Execute the script from the repository directory:

```
python pain.py
```

Relevant output is: `✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤`

###################################################

## Part 2: Chilling in October

![Доказательство](image.png)
