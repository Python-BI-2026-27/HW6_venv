< your solution here >
Steps for tracibility:
1. conda hw6: python3.14, pip
2. python -m pip install pandas opencv-python biopython google-api-core
	- issue - Bio.SubsMat requires Biopython==1.76 or earlier
3. python -m pip install "biopython==1.76"
	- issue - error for this version pip installation
	- mistake - 1.76 is not the last version of biopython with Bio.SubsMat
