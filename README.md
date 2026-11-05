Russian
Инструкция по запуску pain.py (Windows, PowerShell)

1. Подготовка системы и установка Python 3.14

Откройте PowerShell от имени администратора.
Установите Python 3.14 (или новее) командой:

winget install Python.Python.3.14 --override "PrependPath=1 InstallAllUsers=1"
Если откроется дополнительное окно, поставьте две галочки: "Use admin privilages when installing py.exe" и "Add python.exe to PATH", после этого нажмите "Install Now"

После завершения установки перезапустите окно PowerShell, чтобы обновились системные пути.

Проверка:

py -3.14 --version
(Должно вывестись Python 3.14.x)

2. Создание и активация виртуального окружения

В командной строке перейдите в папку с вашим скриптом:

cd C:\Users\user\path\to\script

Создайте новое окружение с названием, например, .venv:

py -3.14 -m venv .venv

Активируйте новое окружение:

.\.venv\Scripts\Activate.ps1
Проверка: В начале строки приглашения в консоли должно появиться название окружения в скобках: (.venv).

3. Установка основных зависимостей

Убедившись, что окружение активировано, выполните:

python -m pip install --upgrade pip setuptools wheel
pip install "pandas>=2.2.3,<3.0.0" pyarrow opencv-python-headless protobuf
Проверка: Установка должна завершиться сообщением Successfully installed... без красного текста ошибок.

4. Установка Biopython (с обходом компиляции C-расширений)

Скачайте исходники и распакуйте их:

python -m pip download --no-deps --no-binary :all: biopython==1.77
tar -xf biopython-1.77.tar.gz
cd biopython-1.77
python setup.py build_py
python setup.py install --skip-build
cd ..
Проверка:

python -c "from Bio import pairwise2; from Bio.SubsMat import MatrixInfo; print('Biopython OK')"

5. Патч библиотеки Pandas

Укажите путь к файлу из библиотеки pandas:

$frame_path = ".\.venv\Lib\site-packages\pandas\core\frame.py"
Выполните команду для замены строки с ошибкой на приведение множества к списку:

(Get-Content $frame_path) -replace 'raise ValueError\("index cannot be a set"\)', 'index = list(index)' | Set-Content $frame_path

6. Запуск скрипта

Запустите скрипт:

python pain.py

На экране должно появиться сообщение: ✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤



English
Instructions for running pain.py (Windows, PowerShell)

1. System preparation and Python 3.14 installation

Open PowerShell as an administrator.
Install Python 3.14 (or newer) using the command:


winget install Python.Python.3.14 --override "PrependPath=1 InstallAllUsers=1"
If an additional window opens, check the two boxes: "Use admin privileges when installing py.exe" and "Add python.exe to PATH", then click "Install Now".

After the installation is complete, restart the PowerShell window to update the system paths.

Verification:


py -3.14 --version
(It should output Python 3.14.x)

2. Creating and activating a virtual environment

In the command line, navigate to the folder containing your script:


cd C:\Users\user\path\to\script
Create a new environment named, for example, .venv:


py -3.14 -m venv .venv
Activate the new environment:


.\.venv\Scripts\Activate.ps1
Verification: The environment name should appear in parentheses at the beginning of the console prompt: (.venv).

3. Installing main dependencies

Ensuring the environment is activated, run:


python -m pip install --upgrade pip setuptools wheel
pip install "pandas>=2.2.3,<3.0.0" pyarrow opencv-python-headless protobuf
Verification: The installation should finish with the message Successfully installed... without any red error text.

4. Installing Biopython (bypassing C extension compilation)

Download the source files and extract them:


python -m pip download --no-deps --no-binary :all: biopython==1.77
tar -xf biopython-1.77.tar.gz
cd biopython-1.77
python setup.py build_py
python setup.py install --skip-build
cd ..
Verification:


python -c "from Bio import pairwise2; from Bio.SubsMat import MatrixInfo; print('Biopython OK')"
Patching the Pandas library

5. Specify the path to the file from the pandas library:


$frame_path = ".\.venv\Lib\site-packages\pandas\core\frame.py"
Execute the command to replace the error line with casting the set to a list:


(Get-Content $frame_path) -replace 'raise ValueError\("index cannot be a set"\)', 'index = list(index)' | Set-Content $frame_path
Running the script

6. Run the script:


python pain.py
The following message should appear on the screen: ✨❤ Всё работает, ты больш(ой/ая) молодец!!! ✨❤
