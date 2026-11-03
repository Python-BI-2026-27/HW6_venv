> Script checked on macOS Tahoe 26.6.2, using Python 3.14.10.

## How to work with `pain.py`

You can quickly set up the environment for this script using `environment.yaml` that can be found in the root of this repository instead of intalling pkgs one after the other as described in **Step 2**. However, you still need to do manual changes from **Step 2** in order for the script to run.

```bash
mamba env create -f environment.yaml --copy
mamba activate environment
```
The `--copy` option is required because you will be changing files within installed libraries. This helps restrict those changes only to your virtual environment, because hardlinks to cache won't be used.

### Step 1.

Make sure your version of Python is at least 3.14. This is required for `annotationlib` to work. 

You should create a `mamba` / `conda` environment for this script:

```bash
mamba create -n environment --copy python=3.14.10 pip
mamba activate environment
```

### Step 2. 

Install these packages. Use `mamba` / `conda` first and `pip` for pkgs that cannot be installed using `mamba` / `conda`, or only `pip`. Use *one* of the following commands:

- **pandas**:

```bash
mamba install pandas==3.1.0
pip install pandas==3.1.0
```

You will then have to "debug" a file in the latest **pandas** version in order to use it like Joe. Thing is, he uses a set as an index, which was doable in v1.4.4 but then got removed in v1.5.0 of **pandas**. We cannot use v1.4.4, because **a)** it works only with [Python](https://pypi.org/project/pandas/1.4.4/#files) 3.8-3.10 and **b)** `pyarrow.DataType` (which Joe uses in his script) [works](https://pandas.pydata.org/pandas-docs/stable/whatsnew/v1.5.0.html) only starting from v1.5.0 of **pandas**. Thus, with the latest version of **pandas** the script will raise this error:

```
"ValueError: index cannot be a set"
```

which comes from file `frame.py` in `/pandas/core`, line 507. To find it, use

```bash
python -c "import pandas.core.frame as f; print(f.__file__)"
```

To "fix" the error, you need to comment out these lines (506-507 in file) in `frame.py`:

```python
        if isinstance(index, set):
            raise ValueError("index cannot be a set")
```

- **google**:

```bash
pip install google-api-python-client==2.201.0
```
This is needed for Python to correctly read Joe's import (according to [this](https://stackoverflow.com/questions/36183486/importerror-no-module-named-google)).

- **cv2**:

```bash
pip install opencv-python==5.0.0.93
```

Found this way of installation [here](https://stackoverflow.com/questions/51853018/how-do-i-install-opencv-using-pip). 

- **Biopython**:

```bash
mamba install Biopython==1.88
pip install Biopython==1.88
```

You will then have to visit this [page](https://github.com/biopython/biopython/tree/biopython-179/Bio/SubsMat) (the official GitHub repo for **Biopython** 1.79) and download all files from folder `/SubsMat`, then create the folder manually. (You can also find the folder in the root of this repo.)

This is because in v1.80 the authors removed this folder containing `Bio.SubsMat` and replaced it with `Bio.Align.substitution_matrices` (can be found in folder `/Align` now). However, Joe uses `Bio.SubsMat` in his script. 

Since the folder itself doesn't contain anything that conflicts with Python 3.14+ (`MatrixInfo.py`, for instance, only contains dictionaries, and `__init__.py` imports modules from standard libraries) and all the dependencies are present in the latest version of Biopython, you can simply *put your manually created `/SubsMat` library inside the `/Bio` folder* (**Note**: *do it within your environment for this script*).

To find the `/Bio` folder, use:

```bash
python -c "import Bio; print(Bio.__path__[0])"
```

- **pyarrow**:

```bash
mamba install pyarrow==26.0.0
pip install pyarrow==26.0.0
```

### Step 3.

Launch the script within your active environment from the root of this repository:

```bash
python pain.py
```

### How I relaxed during the week

I have bought a new computer, which allowed me to enjoy the new DLC for Cyberpunk 2077.

![As proof, here is my V.](images/screenshot.png)