# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:32:36 2017

@author: Akshayaa
"""

import sys
sys.path.append("C:\Python27\Lib\site-packages")

from pymongo import MongoClient
import mysql.connector


cnx = mysql.connector.connect(user='root', password='mysql', database='imdb')
cursor = cnx.cursor()

client = MongoClient()
db = client.test_database
imdb_db1= db.imdb_db1
query= ("select * from imdb")
cursor.execute(query)
dic= {}
di=[]
mov_id_l=[]
for (ID, title, rating, Year) in cursor:
	dic= {"_id": ID, "rating": rating, "Year": Year}
	mov_id_l.append(ID)
	di.append(dic)

imdb_id1 = imdb_db1.insert(di)


	
cursor.execute("SELECT movie_id, GROUP_CONCAT(name SEPARATOR ', ') Actors FROM imdb_people GROUP BY movie_id")


for movie_id,Actors in cursor:
    post = imdb_db1.find_one({'_id': movie_id})
    if post is not None:
        post['Actors'] = Actors
        imdb_db1.save(post)
        
        
cursor.close()
cnx.close()
    
	