# Reproducing `pain.py`

## System

- OS: Windows 11 (x86_64)
- Shell: PowerShell
- Package manager: micromamba
- Python: 3.8

## Why Python 3.8

`pain.py` uses `Bio.SubsMat` from Biopython. This module was removed in Biopython >= 1.80, and the last version that ships it as a ready-to-use binary for Windows + Python 3.8 is `biopython 1.76` (channel `main`, build `py38he774522_0`). Therefore the environment is pinned to Python 3.8 and `biopython 1.76`.

Some lines of `pain.py` use features that only exist in newer Python versions (3.12+). Those lines are commented out (see the list below), because Python 3.8 and Python 3.12+ are mutually exclusive for this script.

## Setup

1. Install micromamba (or Miniforge), then open a new terminal and check:

   ```powershell
   micromamba --version
   ```

2. Create the environment from `environment.yaml`:

   ```powershell
   micromamba env create -f environment.yaml
   ```

   Or create it manually:

   ```powershell
   micromamba create -n bioenv -c main python=3.8 "biopython=1.76=py38he774522_0" -y
   micromamba activate bioenv
   python -m pip install pandas==2.0.3 pyarrow==17.0.0 opencv-python==5.0.0.93 "google-api-python-client<2"
   ```

3. Important: make sure the user-level `site-packages` does not shadow the packages from `bioenv`. If any of the following exist, remove them:

   ```powershell
   Remove-Item -Recurse -Force "$env:APPDATA\Python\Python38\site-packages\Bio" -ErrorAction SilentlyContinue
   Remove-Item -Recurse -Force "$env:APPDATA\Python\Python38\site-packages\pandas" -ErrorAction SilentlyContinue
   Remove-Item -Recurse -Force "$env:APPDATA\Python\Python38\site-packages\pyarrow" -ErrorAction SilentlyContinue
   ```

   Otherwise Python may import a different `Bio` / `pandas` version and fail.

4. Run the script:

   ```powershell
   python pain.py
   ```

   The script is expected to finish with no output and no errors.

## Commented-out lines in `pain.py`

The original file was not modified except for commenting out the lines below. Each line is incompatible with Python 3.8 or with the pinned `biopython 1.76`.

| Line | Commented-out code | Reason |
|------|--------------------|--------|
| 5 | `from typing import override` | `typing.override` was introduced in Python 3.12. |
| 8 | `pattern = glob.translate(string)` | `glob.translate` was added in Python 3.13. |
| 10 | `text = f"Do you know, which TV series is it: {", ".join(series)}"` | Reusing the same quote character inside an f-string requires Python 3.12+ (PEP 701). |
| 14 | `recursion.append([f"{f"{...}"}"}"])` | Nested f-strings with reused quotes require Python 3.12+ (PEP 701). |
| 18 | `from annotationlib import get_annotations, Format` | `annotationlib` was added in Python 3.14. |
| 22-34 | `class Letter`, `class Base`, `class RnaChild` | They use `typing.TypeIs` (Python 3.13) and `typing.override` (Python 3.12). |
| 52 | `key=lambda x: x.score` inside `max(...)` | In the available `biopython 1.76` build, `pairwise2.align.globalds` returns a plain tuple without `.score`. The alignment itself still runs. |
| 54 | `pd.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})` | pandas 2.x rejects a `set` as `index` (`ValueError: index cannot be a set`). |
| 55 | `print(..., .decode("utf-8").removesuffix("!"), ...)` | `str.    removesuffix` was added in Python 3.9. |

## What still works

- `math`, `typing` (basic), `glob` (except `translate`)
- `pandas` + `pyarrow` (`pd.Series(..., dtype="float32[pyarrow]")`)
- `google` (`import google`, via `google-api-python-client`)
- `cv2` (`opencv-python`)
- Biopython: `Bio.SubsMat.MatrixInfo` and `pairwise2.align.globalds(..., matlist.blosum62, -10, -0.5)` — the bioinformatics part of the script runs correctly.

## Versions used

- Python 3.8.20
- biopython 1.76 (`py38he774522_0`, channel `main`)
- pandas 2.0.3
- pyarrow 17.0.0
- opencv-python 5.0.0.93
- google-api-python-client 1.12.11
