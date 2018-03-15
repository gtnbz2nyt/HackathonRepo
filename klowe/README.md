# Setup
```
mkdir bin && cd bin
virtualenv hackathon_venv
source hackathon_venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install mysql-connector-python-rf
pip install configparser argparse
```

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

