#!/usr/bin/env python 
import mysql.connector
import argparse
import pprint

from datetime import date, timedelta
from utility.helpers import readAuthConfig

parser = argparse.ArgumentParser(description='Hack stuff.')
parser.add_argument('--credentials', '-C', default="credentials.ini", help='Location of credential file')
parser.add_argument('--profile', '-P', default="db0", help='Profile to use')
options = parser.parse_args()

credentials = options.credentials
profile = options.profile
authConfig = readAuthConfig(credentials, profile)

my_user = authConfig['user']
my_password = authConfig['password']
my_host = authConfig['host']
my_database = authConfig['database']

cnx = mysql.connector.connect(user=my_user, password=my_password,
                              host=my_host,
                              database=my_database)
cursor = cnx.cursor()

query = ("SELECT cust_id, cust_name FROM klltest")

cursor.execute(query)

for (cust_id, cust_name) in cursor:
  print( cust_id, cust_name )

cnx.close()
