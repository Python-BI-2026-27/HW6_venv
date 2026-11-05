## Tested on:
- macOS 26.6.2
- Python 3.14.10
- Conda 25.11.0
- VS Code 

## Files

- `pain.py` - the original script 
- `environment.yaml` - the Python environment and required libraries
- `setup_compatibility.py` - fixes compatibility problems in installed libraries
- `README.md` — instructions for running the script

## How to run

1. Create the environment:
bash conda env create -f environment.yaml

2. Activate the environment:
bash conda activate pain-repro
 
3. Run the compatibility setup:
python setup_compatibility.py

4. Run script:
bash python pain.py
 

If everything works, the script prints: "✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤"

## Notes
- The environment installs the libraries needed by the script.
- The compatibility setup is necessary because the script uses an old Biopython module and a pandas operation that does not work with the installed version.

## Proof I took a break
Walked around a bit
![Evidence](autumn.png)