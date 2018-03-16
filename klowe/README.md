# Setup
```
mkdir bin && cd bin
virtualenv hackathon_venv
source hackathon_venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install mysql-connector-python-rf
pip install configparser argparse
```

## Installing Kairos Face API in PyCharm (Windows)

* Create a new Python 3.6 virtual environment 
* Make a note of the path to the new virtual environment
* Launch Git Bash
* Change to the top of your source directory
* git clone https://github.com/ffmmjj/kairos-face-sdk-python.git
* cd kairos-face-sdk-python
* Run <path to virtual environment>\python" -m pip install -e .
** E.g. "C:\Users\108752\src\p36_venv\Scripts\python" -m pip install -e .
* Verify that the module is visible from the Project Settings page in PyCharm


# Credentials file
Create the following:
```
[default]
user=mysql_user1
password=<replace me>
host=10.81.20.67
database=db1
```

# Test
```
(hackathon_venv) [108752@rhldakll075 klowe]$ ./klltest1.py
1 Harcourt Fenton Mudd
2 William P. Riker
3 Jean-Luc Picard
4 Tasha Yar
```

