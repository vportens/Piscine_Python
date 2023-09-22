## Create your own library

### Step 1 : Create the distribuable package
in ft_package 
```
python setup.py sdist bdist_wheel
```

### Step 2 : Create a executable env to not polluate our production env
```
python3 -m venv your_env_name
```
```
source your_env_name/bin/activate
```

### Step 3 : Install package
```
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
``` 
or
```
pip install ./dist/ft_package-0.0.1.tar.gz
```

### Step 4 : Verification
```
pip list
```
if youb don't see your **ft-package** in the package list there is a probleme

### Step 5 : Test 
```
python3 test.py
```

### Step 6 : Quit and destroy your test environnement
```sh
deactivate
```