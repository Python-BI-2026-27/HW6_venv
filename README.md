# Painfully running pain.py

## Tested on
WSL, Ubuntu 26.04 LTS, conda 26.7.2 (x86_64).\
Tested package versions:\
Python 3.14.10,\
pandas 2.3.3,\
pyarrow 26.0.0,\
opencv 5.0.0,\
protobuf 7.35.1,\
biopython 1.88

## Steps
1. Create the environment:

`conda env create -f environment.yaml`

2. Activate your environment:

`conda activate pain_env`

3. Restore the **SubsMat** folder from Biopython 1.79 in the new Biopython 1.88 package. Download the 1.79 sources and copy only the pure-Python **SubsMat** folder into the installed Biopython:

`mkdir -p biopython_src`

`pip download biopython==1.79 --no-deps --no-binary :all: -d biopython_src`

`tar -xzf biopython_src/biopython-1.79.tar.gz -C biopython_src`

`cp -r biopython_src/biopython-1.79/Bio/SubsMat "$CONDA_PREFIX/lib/python3.14/site-packages/Bio/"`

  Optional cleanup (the downloaded sources are no longer needed):

`rm -r biopython_src`

4. Pain.py uses `index={1, 2, 3, 4}`, which is rejected by pandas with "index cannot be a set". Replace that check in the installed pandas with `pass`:

`sed -i.bak 's/raise ValueError("index cannot be a set")/pass/' "$CONDA_PREFIX/lib/python3.14/site-packages/pandas/core/frame.py"`


5. Run the script:

`python pain.py`

## Time to relax after this painful journey...
![Relaxation proof](rest.jpg)
