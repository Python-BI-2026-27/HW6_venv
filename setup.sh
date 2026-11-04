#!/bin/bash

SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")

cp sitecustomize.py "$SITE_PACKAGES/"

echo "Compatibility fix module installed"