< your solution here >
Steps for tracibility:
1. conda hw6: python3.14, pip
2. python -m pip install pandas opencv-python biopython google-api-core
	- issue - Bio.SubsMat requires Biopython==1.76 or earlier
3. python -m pip install "biopython==1.76"
	- issue - error for this version pip installation
	- mistake - 1.76 is not the last version of biopython with Bio.SubsMat, use 1.79
4. Download raw Biopython 1.79 files, copy Bio.SubsMat to existing Biopython 1.88 folder
5. Install pyarrow
6. 	-issue - pandas index cannot be a set, need to customize pandas index
	- /opt/miniconda3/envs/hw6/lib/python3.14/site-packages/pandas/core/frame.py:
	if isinstance(index, set):
		raise ValueError("index cannot be a set")
	change to
	if isinstance(index, set):
		index = sorted(index)
7. Done, all works
