## How to relief pain?
Below you can find the instruction to run pain.py. You need to use sitecustomize.py, --init--.py and MatrixInfo.py
from this repo.
(Instruction was written for MacOS)

1. Open Terminal and check if MAMBA is already installed on your computer 
```bash 
mamba --version
```
2. If you see the answer like `command not found` , download and install MAMBA by following the 
instructions at the [link](https://github.com/conda-forge/miniforge).
3. Create virtual environment: 
``` bash 
mamba create -n your_name_of_venv python=3.14
```
4. Activate venv 
``` bash
mamba activate your_name_of_venv
 ```
5. Add libraries 
``` bash 
mamba install -c conda-forge pandas opencv biopython 
pip install google-genai
pip install pyarrow
```
6. Find the path to the Bio folder (remove /__init__.py from the output): 
``` bash
python -c "import importlib.util; spec = importlib.util.find_spec('Bio'); print(spec.origin)"
```
7. Create a folder with name - `SubsMat` in the folder Bio
8. Add an empty __init__.py and MatrixInfo.py in SubsMat folder
9. Add sitecustomize.py in site-packages (in envs, command for full path is below)
``` bash
python -c "import site; print(site.getsitepackages()[0])"
```
10. I hope that after that you can only type `python pain.py` in commandline to run the script. (You need to do in from the folder, where your 'pain' located OR to write the full path. 
For example: `python ~/bioinf/Python/HW_6_venv). If everything OK, you will see that you are cool =)

P.S: After all I realised that it also works without __init__.py in SubsMat=))

Phew, now for the whole point of all this: REST.
I had a long break last week (so it’s a huge relief that you moved the deadline!). I was in Canada, 
looking at mountains, rivers, and deer. I bought a new Starbucks mug for my collection 
(though it’s a shame the collections change so often now and my shelf has started to look rather garish).


![1](photos/1.JPG)  
![2](photos/2.JPG)  
![3](photos/3.JPG)  
![4](photos/4.JPG)


