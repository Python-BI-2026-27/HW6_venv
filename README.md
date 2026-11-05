# Homework 6 Runner (`pain.py`)

## 💻 Prerequisites

Ensure your local system matches one of the following specifications:
* **Operating System:** macOS 14.0+ (Sonoma or newer) OR Linux (Ubuntu 20.04+, Debian, Fedora, etc.).
* **Architecture:** Apple Silicon (`osx-arm64`), Intel/AMD (`x86_64`), or ARM64 Linux (`linux-aarch64`).
* **Environment Manager:** Anaconda / Miniconda.

---

## 🚀 Step-by-Step Installation

### 1. Provision the Conda Environment
Initialize the isolated deployment environment and configure core packages using the bundled configuration file:

```bash
conda env create -f environment.yaml
conda activate hw6_working
```

### 2. Install Legacy Biopython Component
Since legacy components fail compiler checks under modern Python runtimes on specific architectures, map the module tree directly:

1. Download the reference archive: **[Biopython 1.77 (ZIP)](https://biopython.org/wiki/Download)**.
2. Unpack the ZIP archive on your local machine.
3. Locate the core folder named **`Bio`** and copy it.
4. Paste the **`Bio`** folder directly into your active Conda environment's `site-packages` directory:

   * **On macOS:** Open Finder, press `Cmd + Shift + G`, and navigate to:
     ```text
     /opt/miniconda3/envs/hw6_working/lib/python3.14/site-packages/
     ```
   * **On Linux:** Copy the folder using your terminal:
     ```bash
     cp -R /path/to/extracted/biopython-177/Bio ~/miniconda3/envs/hw6_working/lib/python3.14/site-packages/
     ```
     *(Note: If you use Anaconda instead of Miniconda, change 'miniconda3' to 'anaconda3' in the path).*

### 3. Manual Pandas Validation Adjustment
To prevent Pandas from throwing a fatal validation error when encountering a Python `set` structure, follow these steps to adjust the global type validator:

1. Open the core Pandas data types file in your text editor (VS Code, Vim, Nano, etc.):
   * **On macOS:** `/opt/miniconda3/envs/hw6_working/lib/python3.14/site-packages/pandas/core/dtypes/common.py`
   * **On Linux:** `~/miniconda3/envs/hw6_working/lib/python3.14/site-packages/pandas/core/dtypes/common.py`
2. Search for the main validator function using `Ctrl + F` (or `Cmd + F`):
   ```text
   def pandas_dtype
   ```
3. Insert the type-casting override snippet at the very beginning of the function body:

   **Before:**
   ```python
   def pandas_dtype(dtype) -> Dtype:
       # ... existing internal pandas code ...
   ```

   **After (Add these three lines with a 4-space indent):**
   ```python
   def pandas_dtype(dtype) -> Dtype:
       if isinstance(dtype, set):
           dtype = list(dtype)
       # ... rest of the existing internal pandas code ...
   ```
4. Save the file and close the editor.

---

## 🏃 Execution

Activate the target environment, navigate to the root directory of your assignment, and execute the core module:

```bash
python pain.py
```

---

## 🛠️ Troubleshooting

### `ModuleNotFoundError: No module named 'Bio'`
* **Cause:** The `Bio` directory was pasted into an incorrect destination or your Conda installation uses a custom root folder.
* **Fix:** Print your exact active package route by running `python -c "import site; print(site.getsitepackages())"` in your terminal and relocate the `Bio` folder to that specific destination.

### `IndentationError: expected an indented block...`
* **Cause:** Corrupted whitespaces or misaligned indents introduced during manual edits.
* **Fix:** Ensure you used exactly **4 spaces** for the lines added inside `common.py`. Do not use the `Tab` key. If the file is broken, restore it via `conda install --force-reinstall pandas` and try again.

  -------------------------------------------------------
Ждал четверга чтобы сдать дз, так как новый WOW вышел сегодня
![](photo_2026-11-05 13.51.14.jpeg)
