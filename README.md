# HW 6

## Part 1
- Check the Python version (version 3.14 was used). 
- Install `pandas` (`python3.14 -m pip install`) and `google-api-python-client` (`python3.14 -m pip install`). Rename the local `google-api-python-client` directory to `google`.
- Install `opencv-python` (as `cv2`).
- Install `biopython`.
- #Rename `substitution_matrices` (located within `Bio.Align`) to `Bio.SubsMat` locally.
- Update `pyarrow` (version >= 23) using `pip install -U pyarrow`.
- In `Python314\Lib\site-packages\pandas\core\frame.py`, at line 507 (within the `__init__` method), comment out the following condition:
    - #if isinstance(index, set):
          #raise ValueError("index cannot be a set")


  The code still fails at lines 41 and 44–45.

## Part 2

Does a change count?
!['rest'](img/num1.jpg)
