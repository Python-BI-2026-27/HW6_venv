# 🧬 HW6

A step-by-step guide to preparing the Python environment, installing the required libraries, restoring a legacy Biopython module, applying a pandas compatibility change, and running the project.

> **Environment manager:** Anaconda3 + Mamba
> **Main environment:** `myenv`
> **Python version:** `3.14`

---

## 1. Create the Main Python Environment

Create a new environment named `myenv` with Python 3.14:

```bash
mamba create -n myenv python=3.14
```

## 2. Install the Required Libraries

Activate the environment, then install the packages needed by the code:

```bash
mamba activate myenv
mamba install pandas pyarrow opencv biopython google-api-core
```

## 3. Create a Separate Environment with Legacy Biopython

Create a second environment containing Biopython 1.77:

```bash
mamba create -n biopython177 biopython=1.77
```

## 4. Copy the Required Biopython File into `myenv`

Create the `Bio/SubsMat` directory in the main environment:

```bash
mkdir -p ~/anaconda3/envs/myenv/lib/python3.14/site-packages/Bio/SubsMat
```

Copy `MatrixInfo.py` from the legacy environment:

```bash
cp ~/anaconda3/envs/biopython177/lib/python3.9/site-packages/Bio/SubsMat/MatrixInfo.py \
   ~/anaconda3/envs/myenv/lib/python3.14/site-packages/Bio/SubsMat/
```

Create the package initializer:

```bash
touch ~/anaconda3/envs/myenv/lib/python3.14/site-packages/Bio/SubsMat/__init__.py
```

## 5. Apply the pandas Compatibility Change

These changes allow pandas to accept sets for the `index` and `columns` arguments by converting them to lists.

Navigate to the pandas core directory:

```bash
cd ~/anaconda3/envs/myenv/lib/python3.14/site-packages/pandas/core
```

Locate the relevant validation message in `frame.py`:

```bash
grep -n "cannot be a set" frame.py
```

Replace the `index` and `columns` errors with list conversions:

```bash
sed -i 's/raise ValueError("index cannot be a set")/index = list(index)/' frame.py
sed -i 's/raise ValueError("columns cannot be a set")/columns = list(columns)/' frame.py
```


## 6. Run the Project

Navigate to the `HW` folder, make sure the `myenv` environment is active, and run the script:

```bash
python pain.py
```

---

