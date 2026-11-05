# HW6 Virtual environments

Tested on Ubuntu 24.04.5 LTS (WSL2 on Windows), x86_64, Miniconda + mamba 2.5.0.
You also need internet and curl.

`pain.py` is not changed.

## 1. Clone

Everything is in the `HW6` branch.

```bash
git clone -b HW6 https://github.com/shmetterling-va/HW6_venv.git
cd HW6_venv
```

## 2. Environment

The script needs Python 3.14 (`annotationlib` is only in 3.14). Python comes from conda-forge, the rest is installed with pip from `requirements.txt`. All versions there are pinned, the pandas fix in step 4 is for pandas 2.3.3.

```bash
mamba env create -f environment.yaml
conda activate pain
```

The pip part is slow and doesn't print anything, just wait.
`mamba activate pain` didn't work for me (`Shell not initialized`), so I used `conda activate`.

## 3. Bio.SubsMat

The first run failed with `No module named 'Bio.SubsMat'`. It was removed in biopython 1.80, and 1.79 doesn't install on Python 3.14. SubsMat is just 3 python files, so I copied them from biopython 1.79 on GitHub into the installed biopython.

```bash
SITE=$(pip show biopython | grep Location | cut -d' ' -f2)
mkdir -p $SITE/Bio/SubsMat
curl -o $SITE/Bio/SubsMat/__init__.py https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/__init__.py
curl -o $SITE/Bio/SubsMat/FreqTable.py https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/FreqTable.py
curl -o $SITE/Bio/SubsMat/MatrixInfo.py https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/MatrixInfo.py
```

`SITE` is the folder where pip installed the packages (`pip show biopython` prints it as `Location`).

## 4. pandas

Next error was `ValueError: index cannot be a set` on `pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})`. New pandas doesn't allow a set as index, and old pandas doesn't work on 3.14. So I changed this one line in pandas to turn the set into a list:

```bash
sed -i 's/raise ValueError("index cannot be a set")/index = list(index)/' $SITE/pandas/core/frame.py
```

## 5. Run

```bash
python pain.py
```

Should print:

```
✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
```

Other packages: pyarrow is for the `float32[pyarrow]` dtype, protobuf gives `import google`, and opencv-python-headless gives `cv2` (the headless version does not need libGL).

## Part 2. Rest

This week I went to the Bund (Waitan) in Shanghai for the first time. It was a nice break from code :)

![rest](images/rest.jpg)
