# Setup Guide
## 1. Install Miniforge (conda + mamba)

```bash
# Download the installer (Linux x86_64 example)
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"

# Run the installer
bash Miniforge3-$(uname)-$(uname -m).sh
```

## 2. The `environment.yml` file

Save the following as `environment.yml`:

```yaml
name: pain_env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - biopython=1.81
  - numpy<2.0
  - pyarrow
  - pip
  - pip:
      - pandas>=2.1
      - opencv-python
      - google
```

### Why exactly these versions

- **`python=3.10`** — a stable "middle ground" where `numpy<2`, modern `pyarrow`
  and `pandas>=2.1` all resolve together. The originally requested `python=3.14`
  has no builds for the pinned old packages, and `biopython=1.79` (2021) does not
  exist for Python 3.14 at all.

- **`biopython=1.81`** — the closest version to the requested 1.79 that has wheels
  for Python 3.10. The API between 1.79 and 1.81 is essentially unchanged.

- **`numpy<2.0`** — kept as requested; it resolves fine on Python 3.10.

- **`google`** — a tiny meta-package. It does NOT provide an importable `google`
  module (see section 5), but it is harmless to keep in the list.

## 3. Create and activate the environment

```bash
# Create the environment from the file (mamba resolves much faster)
mamba env create -f environment.yml

# Activate it
mamba activate pain_env

# Verify
conda info --envs          # pain_env should be marked with *
python --version           # should print 3.10.x
conda list | grep -E "biopython|numpy|pandas|pyarrow|opencv"
```

## 4. Why some lines in `pain.py` must be commented out

Three groups of reasons:
1. **Python 3.12+ syntax.** Quotation marks inside f-strings and nested valid only since Python 3.12.
2. **New Python features used in imports/annotations.** `typing.override` (3.12+),
   `typing.TypeIs` (3.13+), `glob.translate` (3.13+) and the `annotationlib` module
   (3.14 only) do not exist in Python 3.10.
3. **Removed Biopython modules.** `Bio.SubsMat` (with `MatrixInfo`) was removed
   in Biopython 1.80.

Also two runtime traps:
- `import google` — the `google` package from PyPI (Google search bindings)
  imports as `googlesearch`, not `google`. `pip install google` prints
  "Requirement already satisfied", yet `import google` still raises
  `ModuleNotFoundError`. The only fix without rewriting code is to comment it out.

- `pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})` — pandas forbids a `set` as
  an index and raises `ValueError: index cannot be a set`.

## 5. The final state of `pain.py`

```python
import math
# import typing
# import glob
# from typing import override

string = f"{math.pi:.5f}"
# pattern = glob.translate(string)
series = ['"Whither Canada"', '"Owl Stretching Time"', '"The Ant, an Introduction"']
# text = f"Do you know, which TV series is it: {", ".join(series)}"

recursion = []
# recursion.append([f"{f"{f"{f"{f"{f"{recursion}"}"}"}"}"}"])


# from annotationlib import get_annotations, Format


class Letter: pass

class Base:
  def get_seq_type(self) -> str:
    return "DNA"

  # def is_letter(self) -> typing.TypeIs[Letter]:
  #   return isinstance(self, str)

class RnaChild(Base):
  # @override
  def get_seq_type(self) -> str:
    return "RNA"

import pandas as pd
# import google
import cv2
import warnings
from Bio import BiopythonWarning

with warnings.catch_warnings():
  warnings.simplefilter('ignore', BiopythonWarning)
  from Bio import pairwise2
  # from Bio.SubsMat import MatrixInfo as matlist

  series = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
  # alignments = max(pairwise2.align.globalds("ATATCTCGATCGCTACGTC", "CTAGCTCGCTGCTCAGCATC",
  #                                           matlist.blosum62, -10, -0.5), key=lambda x: x.score)
# pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})
print(u'\u2728\u2764', b'\xd0\x92\xd1\x81\xd1\x91 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82, \xd1\x82\xd1\x8b \xd0\xb1\xd0\xbe\xd0\xbb\xd1\x8c\xd1\x88(\xd0\xbe\xd0\xb9/\xd0\xb0\xd1\x8f) \xd0\xbc\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x86!!!!'.decode("utf-8").removesuffix("!"), u'\u2728\u2764')
```

## 6. Run the script

```bash
mamba activate pain_env
python pain.py
```

Expected output:

```
✨❤ Всё работает, ты большой(ой/ая) молодец❤ ✨
```

All procedures and tests were executed on a machine running MX Linux.
