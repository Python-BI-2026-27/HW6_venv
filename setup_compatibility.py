import os
import Bio
import pandas

folder = os.path.join(os.path.dirname(Bio.__file__), "SubsMat")
os.makedirs(folder, exist_ok=True)

with open(os.path.join(folder, "MatrixInfo.py"), "w") as file:
    file.write('from Bio.Align import substitution_matrices\n'
               'blosum62 = substitution_matrices.load("BLOSUM62")\n')


path = os.path.join(os.path.dirname(pandas.__file__), "core", "frame.py")

with open(path, "r") as file:
    text = file.read()
text = text.replace('raise ValueError("index cannot be a set")', 'index = sorted(index)', 1)

with open(path, "w") as file:
    file.write(text)
