from pathlib import Path
from urllib.request import urlretrieve
import re

import Bio
import pandas


# Restore the removed Biopython module
subs_dir = Path(Bio.__file__).parent / "SubsMat"
subs_dir.mkdir(exist_ok=True)

urlretrieve(
    "https://raw.githubusercontent.com/biopython/biopython/"
    "biopython-179/Bio/SubsMat/MatrixInfo.py",
    subs_dir / "MatrixInfo.py",
)

# Modify the pandas code to allow a set to be used as a DataFrame index

frame_path = Path(pandas.__file__).parent / "core" / "frame.py"

source = frame_path.read_text(encoding="utf-8")

pattern = r'raise ValueError\("index cannot be a set"\)'
replacement = "index = sorted(index)"

modified_source, n = re.subn(pattern, replacement, source)

if n == 1:
    frame_path.write_text(modified_source, encoding="utf-8")
elif n == 0 and source.count(replacement) == 1:
    print("Pandas is already patched")
else:
    raise RuntimeError("Unexpected pandas source code")

print("Compatibility fixes applied")
