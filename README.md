# Installation guide
- Fork repo and clone it by any comfortable for you method
- In terminal move to `HW6_venv` directory
- Create new virtual environment by mamba/conda/micromamba
```bash
 mamba create -n <name_of_your_virtual_environment>
```
- Activate it
```bash
mamba activate -n <name_of_your_virtual_environment>
```
- Download packages
```bash
mamba env update -f environment.yml
```
- Run `problems_resolver.sh`
```bash
bash problems_resolver.sh
```
- Enjoy, Dude

# How it works
## `environment.yml`
Download and install packages from conda-forge and pypi - nothing interesting
## `problems_resolver.sh`
`ENV_PATH="${CONDA_PREFIX}"` - path to actual activated virtual envirnonment

`PACKAGES_DIR="${ENV_PATH}/lib/python3.14/site-packages"` - path to directory with downloaded packages

Tried to make all changes with 'if-condition'

### Edit module in pandas
`FRAME_PY="${PACKAGES_DIR}/pandas/core/frame.py"` - file with `DataFrameClass`

`STRING_TO_REPLACE='raise ValueError("index cannot be a set")'` - our problem for run 'pain.py' with incorrect arguments

`REPLACE_WITH="index = list(index)"` - our bugfix (no)


Use `sed` for file editing
```bash 
if grep -Fq "$STRING_TO_REPLACE" "$FRAME_PY"; then
    echo "Редактируем класс DataFrame библиотеки pandas"
    sed -i "" "s/${STRING_TO_REPLACE}/${REPLACE_WITH}/" $FRAME_PY
fi
```

So, congrats, you broke the pandas lib but resolve the homework).

### Install SubsMat from old version of Biopython
`BIOPYTHON_178_LINK="https://github.com/biopython/biopython/archive/refs/tags/biopython-178.tar.gz"` - link fpr download from GitHub project repo

`BIO_DIR="${PACKAGES_DIR}/Bio"` - directory of already downloaded actual Biopython package

`ARCHIVE_SUBDIR="biopython-biopython-178/Bio/SubsMat"` - name of dowloaded archive

Download via `curl` and unarchive by `tar`

```bash
if [[ ! -d "${BIO_DIR}/SubsMat" ]]; then
    echo "Скачиваем и устанавливем SubsMat модуль"
    curl -fsSL "${BIOPYTHON_178_LINK}" \
    | tar -xz -C "${BIO_DIR}" \
    --strip-components=2 \
    "${ARCHIVE_SUBDIR}"    
fi
```

---
Author - Kolesnik Yan
\
Github - [KolesnikYI](https://github.com/KolesnikYI)
\
telegram - [@YanKolesnik](https://t.me/YanKolesnik) 