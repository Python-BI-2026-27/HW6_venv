# HW6: Virtual Environments

## System

Tested on Ubuntu 26.04.1 LTS (Linux x86_64).

## Requirements

- Miniconda (installed and initialized)
- `wget`, `tar`, `cp` and `sed`

## Installation and usage

**1. Create and activate the Conda environment.**

Run the following commands from the repository directory:

```bash
conda env create -f environment.yaml
conda activate hw6_venv
```

**2. Restore the `Bio.SubsMat` module.**

Biopython 1.88 no longer contains `Bio.SubsMat`, which is required by `pain.py`. Restore the original module from Biopython 1.79:

```bash
mkdir -p "$HOME/Downloads"

wget https://github.com/biopython/biopython/archive/refs/tags/biopython-179.tar.gz -O "$HOME/Downloads/biopython-1.79.tar.gz"

tar -xzf "$HOME/Downloads/biopython-1.79.tar.gz" -C "$HOME/Downloads" biopython-biopython-179/Bio/SubsMat

cp -r "$HOME/Downloads/biopython-biopython-179/Bio/SubsMat" "$CONDA_PREFIX/lib/python3.14/site-packages/Bio/"
```

**3. Adjust pandas to accept the set used as a DataFrame index in `pain.py`.**

Pandas 3.1.1 rejects sets passed as the `index` argument. For the integer set used in this script, converting it into a sorted list provides a valid index.

```bash
sed -i 's/raise ValueError("index cannot be a set")/index = sorted(index)/' "$CONDA_PREFIX/lib/python3.14/site-packages/pandas/core/frame.py"
```

This modification affects pandas in the active Conda environment. The original `pain.py` remains unchanged.

**4. Run the script.**

```bash
python pain.py
```

The script should finish successfully and display a congratulatory message.

## Rest

Here I was, just a few days ago, in a perfectly peaceful and warm little corner of the world, watching my dudes celebrate Wednesday.

<img src="rest.JPG" alt="My vacation" width="400"> <img src="wednesdaydude.JPG" alt="It's Wednesday, my dudes!" width="400">


And here I am now, back from vacation, like a fox with long tails of homework assignments waiting to be done.

<img src="final.JPG" alt="Me after vacation" width="400">
