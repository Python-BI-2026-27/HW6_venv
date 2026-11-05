pushd %TEMP%
pip download biopython==1.79 --no-deps --no-binary :all: -d bp179
tar -xzf bp179\biopython-1.79.tar.gz -C bp179
python -c "import Bio, os, shutil; dst=os.path.join(os.path.dirname(Bio.__file__),'SubsMat'); shutil.copytree(r'bp179\biopython-1.79\Bio\SubsMat', dst, dirs_exist_ok=True); print('OK ->', dst)"
popd