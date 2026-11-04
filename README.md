# HW6: Virtual environments

## What is it

A recipe for setting up an environment in which Joe's script `pain.py` runs

Tested on Ubuntu 24.04.4 (x86_64)

## Getting Started

### Requirements

 Installed [Miniforge](https://github.com/conda-forge/miniforge), which provides `conda` and `mamba`

### Run

1. Clone the repository
    ```bash
    git clone git@github.com:KamilaS1/HW6_venv_Sagitdinova.git
    ```

2. Go to the project directory
    ```bash
    cd HW6_venv_Sagitdinova
    ```

3. Create an environment with Python 3.14 (the script needs `glob.translate` and `annotationlib`, which are not available in older versions)
    ```bash
    mamba create -n hw6 python=3.14
    ```

4. Activate the environment (all of the following steps must be run inside it)
    ```bash
    conda activate hw6
    ```

5. Install the dependencies
    ```bash
    pip install -r requirements.txt
    ```

6. Restore the `Bio.SubsMat` module, which was removed in Biopython 1.80, by copying it from the Biopython 1.79 source code
    ```bash
    pip download --no-deps --no-binary :all: biopython==1.79
    tar xzf biopython-1.79.tar.gz
    cp -r biopython-1.79/Bio/SubsMat "$CONDA_PREFIX/lib/python3.14/site-packages/Bio/"
    rm -r biopython-1.79 biopython-1.79.tar.gz
    ```

7. Comment out the pandas check that forbids using a `set` as a `DataFrame` index. Open `frame.py` in any text editor (for example, VS Code):
    ```bash
    code "$CONDA_PREFIX/lib/python3.14/site-packages/pandas/core/frame.py"
    ```
    Find lines 506–507:
    ```python
            if isinstance(index, set):
                raise ValueError("index cannot be a set")
    ```
    Add `#` at the beginning of both lines and save the file:
    ```python
    #        if isinstance(index, set):
    #            raise ValueError("index cannot be a set")
    ```
8. Run the script
    ```bash
    python pain.py
    ```
    Expected output:
    ```
    ✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
    ```
## Rest
My friends and I celebrated Halloween, I was dressed as Fiona from Shrek when she turned into an ogre:

   ![We celebrated Halloween with friends](images/halloween.png)