< your solution here >
1) Create new python env:
mamba create -n myenv python=3.14

2) Install all libraries needed for the code:
mamba activate myenv
mamba install pandas pyarrow opencv biopython google-api-core

3) Make new env with old biopython
mamba create -n biopython177 biopython=1.77 

4) Copy files required from biopython177 to myenv - into the library biopython
mkdir ~/anaconda3/envs/myenv/lib/python3.14/site-packages/Bio/SubsMat

cp ~/anaconda3/envs/biopython177/lib/python3.9/site-packages/Bio/SubsMat/MatrixInfo.py ~/anaconda3/envs/myenv/lib/python3.14/site-packages/Bio/SubsMat

touch ~/anaconda3/envs/myenv/lib/python3.14/site-packages/Bio/SubsMat/__init__.py

5) Edit pandas library - make so it can take index as a set:
cd ~/anaconda3/envs/myenv/lib/python3.14/site-packages/pandas/core

grep -n "cannot be a set" frame.py

sed -i 's/raise ValueError("index cannot be a set")/index = list(index)/' frame.py
sed -i 's/raise ValueError("columns cannot be a set")/columns = list(columns)/' frame.py

6) Go to HW folder and execute pain.py:
python pain.py


