#!/usr/bin/env python 
import mysql.connector
import pprint

from utility.helpers import readAuthConfig
from utility.helpers import getArgs

options = getArgs()
conf = readAuthConfig(options.credentials, options.profile)

cnx = mysql.connector.connect(
      user=conf['user'], 
      password=conf['password'],
      host=conf['host'],
      database=conf['database'])

cursor = cnx.cursor()

query = ("SELECT cust_id, cust_name FROM klltest")

cursor.execute(query)

for (cust_id, cust_name) in cursor:
  print( cust_id, cust_name )

cnx.close()
