HW6 — Virtual Environments

Environment

The script was successfully executed on:

* Operating system: macOS 15.7.4
* Architecture: ARM64 (Apple Silicon)
* Python: 3.14.3
* pip: 26.2.2
* Environment manager: Conda

Installation

1. Create a Conda environment

conda create -n hw6_py314 -c conda-forge --override-channels python=3.14.3
conda activate hw6_py314

2. Install dependencies

From the repository directory, run:

python -m pip install -r requirements.txt

3. Install Biopython 1.79

The script uses Bio.SubsMat, which is available in Biopython 1.79 but was removed in later versions.

Biopython 1.79 cannot be built normally with Python 3.14 because its C extensions are incompatible with this Python version.

Download the source distribution:

python -m pip download biopython==1.79 --no-deps --no-binary=:all: -d /tmp
cd /tmp
tar -xzf biopython-1.79.tar.gz
cd biopython-1.79

Open setup.py and replace:

ext_modules=EXTENSIONS,

with:

ext_modules=[],

This disables compilation of the incompatible C extensions.

Install the modified package:

python -m pip install setuptools wheel
python -m pip install . --no-build-isolation

4. Fix pandas compatibility

The script passes a Python set as the DataFrame index. Pandas 3.1.1 explicitly rejects this input.

Locate the installed frame.py file:

python -c "import pandas.core.frame as f; print(f.__file__)"

Open this file and find:

if isinstance(index, set):
    raise ValueError("index cannot be a set")

Replace it with:

if isinstance(index, set):
    index = list(index)

This converts the set into a supported index format.

Note: Sets do not guarantee element ordering. This modification is intended only for reproducing the provided educational script.

5. Run the script

Return to the repository directory and execute:

python pain.py

Expected output:

✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤

The original pain.py file was not modified.

Part 2 — Rest

### Photos

**Walking in the park and collecting acorns:**

![Acorns collected during my walk](images/acorn.jpeg)

**Creating memes with my hamster:**

![My hamster meme](images/hamster_kurduk.png)
