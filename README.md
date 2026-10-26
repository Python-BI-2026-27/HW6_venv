# HW6: Virtual Environment

## What I did

The goal of this assignment was to run pain.py without changing the original script.
I used Ubuntu WSL and Conda to create a separate environment with Python 3.14.9. I chose this version because the script uses several features introduced in recent Python versions.
I started by running pain.py and installing the missing dependencies. I installed pandas, pyarrow, google-auth, OpenCV, and Biopython.
During this process, I encountered several compatibility problems.

## Biopython

The script uses Bio.SubsMat.MatrixInfo, which was removed from newer versions of Biopython.
I first tried installing Biopython 1.79, but it failed to build with Python 3.14. Even after installing GCC, compilation failed because the old Biopython source code uses an API that is no longer available.
I decided to use Biopython 1.88 and restore the original MatrixInfo.py file from Biopython 1.79. I saved this file in the legacy directory.

## Pandas

After fixing Biopython, I encountered another error:
ValueError: index cannot be a set
The script passes a set as the index of a DataFrame, but pandas 3.1.0 does not allow this.
I changed the corresponding check in pandas so that a set is converted into a sorted list.

## Other dependencies

I also found that installing the google package did not resolve import google. Installing google-auth solved this problem.
The remaining libraries were installed without additional changes.

## Making the solution reproducible

After getting pain.py to work, I created apply_patches.py to automate the Biopython and pandas modifications.
I also saved the required package versions in environment.yaml.

Finally, I created a new Conda environment called hw6-test and repeated the installation and setup from scratch. The script ran successfully, so I confirmed that the solution was reproducible.

## How to run

Clone my repository and switch to the homework branch:
git clone https://github.com/YugayYulia/HW6_venv.git
cd HW6_venv
git switch hw6-venv

Create and activate the Conda environment:
conda env create -f environment.yaml
conda activate hw6-venv

Apply the compatibility fixes:
python apply_patches.py

Run the script:
python pain.py

## My rest

After sorting out all the Python dependencies and compatibility issues, I’ve started checking my gear for the upcoming season! Unfortunately, it turns out my boots and bindings need replacing—much like those old software versions. I need to come up with a way to treat myself...
![My rest](images/Board.jpg)
