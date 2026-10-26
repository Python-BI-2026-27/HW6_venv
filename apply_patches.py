from pathlib import Path
import shutil

import Bio
import pandas


# Restore the original MatrixInfo module from Biopython 1.79
project_dir = Path(__file__).resolve().parent
source = project_dir / "legacy" / "MatrixInfo.py"

bio_dir = Path(Bio.__file__).resolve().parent
target_dir = bio_dir / "SubsMat"
target_dir.mkdir(exist_ok=True)

shutil.copy2(source, target_dir / "MatrixInfo.py")
print("Biopython MatrixInfo restored")


# Patch pandas to accept a set as a DataFrame index
pandas_dir = Path(pandas.__file__).resolve().parent
frame_file = pandas_dir / "core" / "frame.py"

original = """if isinstance(index, set):
            raise ValueError("index cannot be a set")"""

replacement = """if isinstance(index, set):
            index = sorted(index)"""

content = frame_file.read_text()

if original in content:
    content = content.replace(original, replacement, 1)
    frame_file.write_text(content)
    print("Pandas patch applied")
elif replacement in content:
    print("Pandas patch already applied")
else:
    raise RuntimeError("Expected pandas code was not found")
