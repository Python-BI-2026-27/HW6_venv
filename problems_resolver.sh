#!/usr/bin/env bash
set -euo pipefail

ENV_PATH="${CONDA_PREFIX}"
PACKAGES_DIR="${ENV_PATH}/lib/python3.14/site-packages"

# Изменяем frame.py
FRAME_PY="${PACKAGES_DIR}/pandas/core/frame.py"
STRING_TO_REPLACE='raise ValueError("index cannot be a set")'
REPLACE_WITH="index = list(index)"

if grep -Fq "$STRING_TO_REPLACE" "$FRAME_PY"; then
    echo "Редактируем класс DataFrame библиотеки pandas"
    sed -i "" "s/${STRING_TO_REPLACE}/${REPLACE_WITH}/" $FRAME_PY
fi

# Добавляем SubsMat пакет
BIOPYTHON_178_LINK="https://github.com/biopython/biopython/archive/refs/tags/biopython-178.tar.gz"
BIO_DIR="${PACKAGES_DIR}/Bio"
ARCHIVE_SUBDIR="biopython-biopython-178/Bio/SubsMat"

if [[ ! -d "${BIO_DIR}/SubsMat" ]]; then
    echo "Скачиваем и устанавливем SubsMat модуль"
    curl -fsSL --progress-bar "${BIOPYTHON_178_LINK}" \
    | tar -xz -C "${BIO_DIR}" \
    --strip-components=2 \
    "${ARCHIVE_SUBDIR}"    
fi

echo "Все проблемки решены, можно и поспать!"
