# HW6 — Virtual Environments

## Requirements:
macOS
Mamba

### 1. Python environment and libraries

The project was tested on macOS using Miniforge and Mamba.

The main environment uses Python 3.14 and the following packages:

    pandas

    pyarrow

    biopython

    opencv

    google-api-core

### 2. Biopython compatibility

The original script imports Bio.SubsMat, which is not available in recent versions of Biopython.

To obtain this legacy module, a temporary Python 3.11 virtual environment was created. Biopython 1.79 was installed in that environment because it still contains Bio.SubsMat.

The required files were copied from the temporary environment into the project's compat/Bio/SubsMat directory:

__init__.py

FreqTable.py

MatrixInfo.py

The compatibility module can then be copied into the installed Biopython package in the main environment.

First, create the destination directory:
mkdir -p "$(python -c 'import Bio; print(Bio.__path__[0])')/SubsMat"

Then copy the files:
cp compat/Bio/SubsMat/*.py "$(python -c 'import Bio; print(Bio.__path__[0])')/SubsMat/"

### 3. Pandas compatibility fix

The script passes a Python set as a DataFrame index. The installed Pandas version does not accept a set directly.

The installed pandas/core/frame.py file was modified. The following code:
if isinstance(index, set):
    raise ValueError("index cannot be a set")

was replaced with:
if isinstance(index, set):
    index = sorted(index)

### 4. Run the program
python pain.py


## Дополнительное звадание:
Расскажу историю своего отдыха. Так как у меня сгорел балкон, то мои выходные были потрачены на переезд в другую квартиру, ведь пока не пройдет экспертиза мне нельзя жить в своей. Однако это не помешало мне провести хорошо время, ведь мои друзья помогли мне переехать и обжиться в новом месте, поэтому в конце трудного выходного дня, мы все вместе поиграли в настолки (Манчкин и Монополия, других увы нет). Ну, и после такого мне удалось вернуться бегать, считаю, что бег - это лучший отдых:)