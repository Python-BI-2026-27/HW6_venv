# HW6: making `pain.py` run

Tested on: macOS (Apple Silicon, arm64), zsh, `mamba` 2.9.0 (Miniforge installed via `brew install --cask miniforge`).

`pain.py` itself is not modified. The recipe below creates an environment and applies two small manual fixes to installed packages.

## Recipe

### 1. Create and activate the environment

Run from the repository root (where `environment.yaml` lives):

```bash
mamba env create -f environment.yaml
mamba activate pain
```

This installs Python 3.14 (required by `annotationlib`, `glob.translate` and `typing.override`), pandas, pyarrow (needed for `float32[pyarrow]`), OpenCV (`cv2`), protobuf (provides the `google` namespace), Biopython 1.88 and pip.

### 2. Restore `Bio.SubsMat`

The `Bio.SubsMat` module was removed in Biopython 1.80, but `pain.py` imports it. Biopython 1.79 cannot be installed on Python 3.14, so copy the pure-Python `SubsMat` package from the 1.79 sources into the installed `Bio` package:

```bash
pip download biopython==1.79 --no-deps --no-binary :all: -d bio179
tar -xzf bio179/biopython-1.79.tar.gz -C bio179
cp -r bio179/biopython-1.79/Bio/SubsMat "$(python -c "import Bio, os; print(os.path.dirname(Bio.__file__))")"
```

`bio179/` is only a temporary download folder and can be deleted afterwards.

### 3. Allow a `set` as a DataFrame index in pandas

The last statement of `pain.py` calls `pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})`. Every pandas version compatible with this script rejects a `set` index with `ValueError: index cannot be a set`, so the check has to be disabled by hand.

1. Print the pandas directory:
   ```bash
   python -c "import pandas, os; print(os.path.dirname(pandas.__file__))"
   ```
2. Open `core/frame.py` inside that directory in a text editor.
3. Search for `cannot be a set`. You will find two checks next to each other:
   ```python
   if isinstance(index, set):
       raise ValueError("index cannot be a set")
   if isinstance(columns, set):
       raise ValueError("columns cannot be a set")
   ```
4. Comment out **only the first two lines** (the `index` check):
   ```python
   # if isinstance(index, set):
   #     raise ValueError("index cannot be a set")
   if isinstance(columns, set):
       raise ValueError("columns cannot be a set")
   ```
   Leave the `columns` check untouched.
5. Save the file.

### 4. Run

```bash
python pain.py
```

Expected output (a single line):

```
✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
```

## Part 2: rest

This week I repotted my plants into bigger pots and watched The Haunting of Hill House. Highly recommended! Carla Gugino is mesmerizing in it, as in all of Mike Flanagan's work.
