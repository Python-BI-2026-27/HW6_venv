#SubsMat fix
import sys
import types
import Bio

from Bio.Align import substitution_matrices

matrix_info = types.ModuleType("MatrixInfo")
matrix_info.blosum62 = substitution_matrices.load("BLOSUM62")

subs_mat = types.ModuleType("Bio.SubsMat")
subs_mat.MatrixInfo = matrix_info

sys.modules["Bio.SubsMat"] = subs_mat
Bio.SubsMat = subs_mat

#pandas set fix

import pandas as pd

original_dataframe = pd.DataFrame

def patched_dataframe(*args, **kwargs):
    if isinstance(kwargs.get("index"), set):
        kwargs["index"] = sorted(kwargs["index"])

    return original_dataframe(*args, **kwargs)

pd.DataFrame = patched_dataframe