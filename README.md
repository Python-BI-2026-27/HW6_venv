# HW 6. Virtual environments
## Tested on:
- macOS 26.5.2 (Apple Silicon, arm64)
- mamba 2.9.0 (Miniforge)

## 1. Installing mamba
Check if mamba is already installed:

```bash
mamba --version
```
If it prints version number, skip the first step

Otherwise, download the Miniforge installer, which includes mamba
The link: https://github.com/conda-forge/miniforge

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
```
Run the script with

```bash
bash Miniforge3-$(uname)-$(uname -m).sh
```
During installation:
- scroll through the license with `Enter` and type `yes` to accept it;
- press `Enter` to accept default install location;
- type `yes` when asked to initialize Miniforge3 or update your shell profile.

Next step is to restart the terminal and check the installation:

```bash
mamba --version
```
It should print the mamba version.

## 2. Clone the repository

```bash
git clone https://github.com/bombilidae/HW6_venv_Posazhennikova.git
cd HW6_venv_Posazhennikova
```
All following commands maust be run from this folder.

## 3. Create and activate the environment
```bash
mamba env create -f environment.yaml
mamba activate pain
```
Notes on `environment.yaml`:

- Python 3.14 is required. The script uses `annotationlib` (introduced in version 3.14), `typing.TypeIs` and `glob.translate` (version 3.13), also `typing.override` and nested f-strings that use the same quotation marks (version 3.12).
- Some package names differ from the names of the modules imported from them: `cv2` is part of `opencv`, `Bio` belongs to `biopython`, and `google` is a namespace package provided by the `protobuf` library.
- `pyarrow` is necessary for using the `float32[pyarrow]` data type in pandas.

## 4. Restore the removed `Bio.SubsMat`
The script needs `Bio.SubsMat`, but this module was was deprecated in Biopython 1.78 and removed in Biopython 1.80. Biopython 1.79 is last release that includes `Bio.SubsMat`, cannot be installed on Python 3.14 because it doesn't support this Python version.
The solution is to borrow the original, unmodified `SubsMat` module from the Biopython 1.79 source archive and place it into the installed Biopython:

```bash
pip download biopython==1.79 --no-deps --no-binary biopython -d /tmp/biopython_old
tar -zxf /tmp/biopython_old/biopython-1.79.tar.gz -C /tmp/biopython_old
cp -r /tmp/biopython_old/biopython-1.79/Bio/SubsMat "$(python -c 'import Bio, os; print(os.path.dirname(Bio.__file__))')"
```

What these commands do:
1. `pip download` downloads the Biopython 1.79 source code into a temporary folder `/tmp` (without installing it).
2. `tar` unpacks the downloaded archive.
3. `cp` copies the `SubsMat` folder into the installed Biopython. The `python -c` command inside finds where Biopython is installed

## 5. Fix pandas
Since pandas 1.5, set cannot be used as  DataFrame index: `ValueError: index cannot be a set` (pandas issue GH47215).
Older pandas versions don’t support Python 3.14, so this check need to be commented out in the installed pandas.

```bash
pandas_file=$(python -c "import pandas.core.frame as f; print(f.__file__)")
sed -i '' '/isinstance(index, set)/,/index cannot be a set/s/^/#/' "$pandas_file"
```

1. The first command finds the pandas file `frame.py` and saves its path to the variable `pandas_file`.
2. `sed` adds `#` at the beginning of the two lines of the check.
On Linux, use `sed -i` instead of `sed -i ''`.

## 6. Run the script 

```bash
python pain.py
```

Exprcted output:

```
✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
```

## Part 2. Rest

This week I went glamping with a view of a misty lake to catch the *Twilight* "hoa hoa" vibes and rode on the swings.

![glamping](glamping.png)



