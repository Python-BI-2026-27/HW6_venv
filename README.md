# HOMEWORK 6 - VENV

Instructions on how to run the unchanged `pain.py` script by installing dependencies and modifying the installed packages.

## Requirements and setup

Tested on:

- macOS 26.7.1
- Python 3.14.10
- clean `conda` environment (`conda 26.9.4`)

`Conda` must already be installed! Use `conda 26.9.4` or later versions. Python packages are installed using `pip`.

Run the commands below in a `bash` or `zsh` terminal. Keep the homework environment activated during the setup.

### 1. Create a new conda environment

- Run the following commands in terminal:

```bash
conda create -n hw6 python=3.14.10 pip
conda activate hw6
```

You can use another environment name instead of `hw6`.

### 2. Install the required packages

- Navigate to the homework repository folder (`HW6_venv/`) containing `pain.py` and `requirements.txt`.

- Install the package versions listed in `requirements.txt` by running the following command in terminal:

```bash
python -m pip install -r requirements.txt
```

This installs `pandas`, `OpenCV`, `Biopython`, `google-api-core`, `pyarrow` and their dependencies.

### 3. Restore `Bio.SubsMat`

The script uses `Bio.SubsMat`, which is missing from the installed `Biopython` version. Restore this module from the official `Biopython 1.79` archive.

- Download and extract the `Biopython 1.79` files by running the following command in terminal:

```bash
curl -fL https://biopython.org/DIST/biopython-1.79.tar.gz -o biopython-1.79.tar.gz
tar -xzf biopython-1.79.tar.gz
```

- Copy the entire `SubsMat` directory into the installed `Bio` package by running the following command in terminal:

```bash
cp -R biopython-1.79/Bio/SubsMat "$CONDA_PREFIX/lib/python3.14/site-packages/Bio/"
```

`$CONDA_PREFIX` is the path to the active conda environment. In case of any issues with copying, insert the path to conda environment manually instead of `$CONDA_PREFIX`.

- After copying succeeds, remove the downloaded archive and extracted files:

```bash
rm -rf biopython-1.79/ biopython-1.79.tar.gz
```

### 4. Modify `pandas` to handle the `set` used as an index

The script uses a `set` as the `pandas` dataframe index, as `set` is unordered, `pandas` rejects this input with exception `ValueError: index cannot be a set`.

Since `pain.py` must be unchanged, modify the installed `pandas` code to convert the set into a sorted `list`.

- Open `frame.py`:

```bash
nano +507 "$CONDA_PREFIX/lib/python3.14/site-packages/pandas/core/frame.py"
```

You can also use another text editor, the code above uses `nano`.

- Find the following code chunk:

```python
        if isinstance(index, set):
            raise ValueError("index cannot be a set")
```

Replace it with:

```python
        if isinstance(index, set):
            index = sorted(index)
```

It's important to keep the original indentation.

If line 507 does not point to the expected code, find `index cannot be a set` in the code and replace it.

Save changes and exit the editor. In case of using `nano`, you can do it by the following actions:

- Press `Ctrl+O`
- Press Enter
- Press `Ctrl+X`

If nano opens an empty file, exit without saving and check the path to `pandas` folder in active environment.

### 5. Run the script

From the homework repository folder (`HW6_venv` by default), run in terminal:

```bash
python pain.py
```

Expected output in case of correct setup:

```text
✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
```