**README.md**

This repository helps fix the `pain.py`, bringing it to an useful state.

This code was tested on Ubuntu-24-04 via WSL2.

Just do some easy steps:

1. Create a conda environment using 

```bash
conda create -n pain python=3.14
```

and activate it:

```bash
conda activate pain
```

2. Install required pakages:

```bash
conda install -c conda-forge pandas biopython "pyarrow>=13"
python -m pip install opencv-python google google-auth
```

3. Fix Biopython using this code: 

```bash
SCRIPT_DIR="$(dirname "$(realpath "$0")")"
DATA_DIR="$SCRIPT_DIR/data"

BIO_URL="https://files.pythonhosted.org/packages/28/73/4d61169ce1f15c65ea49af89e534b2089375a44b608cb65062b58ff414de/biopython-1.79.tar.gz"

mkdir -p "$DATA_DIR"
curl -L "$BIO_URL" -o "$DATA_DIR/biopython-1.79.tar.gz"

tar -xzf "$DATA_DIR/biopython-1.79.tar.gz" -C "$DATA_DIR"

SITE_PACKAGES="$(python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"

cp -r "$DATA_DIR/biopython-1.79/Bio/SubsMat" "$SITE_PACKAGES/Bio/"
```

4. Fix pandas using this code: 

```bash
PANDAS_DIR="$(python -c 'import pandas; print(pandas.__path__[0])')"
sed -i 's/raise ValueError("index cannot be a set")/index = list(index)/' "$PANDAS_DIR/core/frame.py"
```

5. Congratulations! Now you can run pain.py and enjoy it! Thank you, Joe from Texas!

```bash
python3 pain.py
```

p.s.

As my boss says, the best way to rest is to busy yourself with other things.

So, I finally have annotated CD4+ cells in our cell atlas - it was my rest)

![отдых-что может быть прекраснее?](img/img1.png)



