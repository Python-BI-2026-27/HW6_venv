
< your solution here >
1.0. sudo apt update
1. sudo apt install python==3.14.4
1.1. sudo apt install pip
2. in project folder: python3 -m venv <env_name>
3. activate env: python3 -m venv pain_venv
4. install pandas: pip install pandas
5. run command in terminal python -c "import sys; f = '<env_name>/lib/python3.14/site-packages/pandas/core/frame.py'; lines = open(f).readlines(); open (f, 'w').writelines([('#' + l if 506 <= i <= 509 else l) for i,l in enumerate(lines)])"
6. create google module filler: mkdir <env_name>/lib/python3.14/site-packages/google
7. install opencv: pip install opencv-python
8. pip install Biopython
9. modify Biopython with old functions: 
    cd <env_name>/lib/python3.14/site-packages/Bio
    curl -sL "https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/pairwise2.py" -o "pairwise2.py"
    mkdir SubsMat
    cd SubsMat/
    curl -sL "https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/__init__.py" -o "__init__.py"
    curl -sL "https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/MatrixInfo.py" -o "MatrixInfo.py"
    curl -sL "https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/FreqTable.py" -o "FreqTable.py"
10. Go back to project folder: cd ./../../../../../..
11. install pyarrow: pip install pyarrow
12. Run pain.py: python pain.py

    
