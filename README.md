# HW 6. Virtual environments

## Part 1.

Tested on: Windows 10, WSL2 Ubuntu 24.04.3 LTS, mamba 2.5.0.

Installing mamba and cloning the repository are left to the reviewer. Start with the Ubuntu terminal open in the root folder of the repository. Every separate code block below is a single command: copy it, paste it into the terminal (Ctrl+Shift+V), press Enter, wait until it finishes, and only then move on to the next block. Use one terminal window for all commands.

```bash
mamba env create -y -f environment.yaml
```

```bash
mamba activate pain
```

```bash
SITE=$(python -c "import sysconfig; print(sysconfig.get_paths()['purelib'])")
```

```bash
mkdir -p "$SITE/Bio/SubsMat"
```

```bash
for f in __init__.py FreqTable.py MatrixInfo.py; do curl -fsSL "https://raw.githubusercontent.com/biopython/biopython/biopython-179/Bio/SubsMat/$f" -o "$SITE/Bio/SubsMat/$f"; done
```

```bash
sed -i '/if isinstance(index, set):/,+1d' "$SITE/pandas/core/frame.py"
```

```bash
python pain.py
```

## Part 2.

I played competitive Mafia with my friends.