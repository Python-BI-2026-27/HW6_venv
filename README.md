# HW6 — Virtual Environments

## Part 1. Running pain.py

Tested on Ubuntu 26.04 LTS (WSL2) with Python 3.14.4.

The original pain.py file was not modified.

### 1. Create and activate a virtual environment

Run the following commands from the repository directory:

    python3 -m venv .venv
    source .venv/bin/activate

### 2. Install dependencies

    python -m pip install -r requirements.txt

The requirements.txt file lists the exact package versions used.

### 3. Restore the legacy Biopython module

Biopython 1.88 no longer includes Bio.SubsMat.
The script requires its original MatrixInfo module.

Restore MatrixInfo.py from the official Biopython 1.79 source:

    mkdir -p .venv/lib/python3.14/site-packages/Bio/SubsMat

    curl -fL https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/MatrixInfo.py -o .venv/lib/python3.14/site-packages/Bio/SubsMat/MatrixInfo.py

### 4. Fix pandas index compatibility

Pandas 3.1.1 rejects a set used as a DataFrame index.
Convert that set into a sorted list inside the installed library:

    sed -i 's/raise ValueError("index cannot be a set")/index = sorted(index)/' .venv/lib/python3.14/site-packages/pandas/core/frame.py

This modification affects only pandas inside the virtual environment.

### 5. Run the script

    python pain.py

Expected output:

    ✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤

### Notes

The google-auth package provides the google namespace.
The opencv-python-headless package provides the cv2 module.

The script was successfully executed with these dependencies and modifications. Neither pain.py nor the Python interpreter was modified.


## Part 2. Rest and Recovery

Apparently, my idea of relaxation is spending my days off in a laboratory!

This week, I set up two laboratories at the Grozny branch of Lomonosov Moscow State University: one for biochemistry and another for molecular biology and genetics. Watching my ideas come to life was incredibly satisfying.

The week was full of surprises. After being disappointed by some microscopes in the microscopy lab, I discovered **21 excellent microscopes** in storage! But nothing prepared me for seeing **28 double-beam spectrophotometers in a single room!**

"I'll spectrophotometrize everything you own," I thought to myself. "Strictly for scientific purposes, of course. Pending approval from the ethics committee."

And just when I thought things couldn't get more exciting, I discovered that one of the professors had requested **two Oxford Nanopore sequencers** for future purchase!

Some people relax by going on holiday. Apparently, I relax by discovering scientific equipment and setting up laboratories. And I wouldn't have it any other way!
