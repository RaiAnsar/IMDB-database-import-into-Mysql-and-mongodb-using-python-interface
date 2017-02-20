# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys;
sys.path.append("F:\Big_data_programming\py_lib\imdb\parser\http");
sys.path.append("F:\Big_data_programming\py_lib\imdb\parser");
sys.path.append("F:\Big_data_programming\py_lib");
sys.path.append("F:\Big_data_programming\py_lib\imdb\locale");
sys.path.append("F:\Big_data_programming\py_lib\imdb");
sys.path.append("F:\Big_data_programming\py_lib\imdb\parser\http\bsouplxml");
sys.path.append("C:\Python27\Lib\site-packages");

from imdb import IMDb
import mysql.connector
ia = IMDb()


cnx = mysql.connector.connect(user='root', password='mysql', database='imdb')
cursor = cnx.cursor()


mov_id=[]
for movs in range(110111,111111):
    try:
        m= ia.get_movie(movs)
        rating= m['rating']
        name= str(m)
        IMDBid= m.movieID
        mov_id.append(IMDBid)
        year= m['year']
        add_movies= ("INSERT INTO imdb "
               "(ID, title, rating, Year) "
               "VALUES (%s, %s, %s, %s)")
        data_movies= (IMDBid, name, rating, year)
        cursor.execute (add_movies, data_movies)
        print movs
    except:
        continue

cnx.commit()


for i in range(750,805):
    try:
        print i, ia.get_movie(mov_id[i])['cast']
        for person in ia.get_movie(mov_id[i])['cast']:
            movie_id= mov_id[i]
            id= person.personID
            name= person['name']
            add_people = ("INSERT INTO imdb_people "
               "(ID, movie_id, name) "
               "VALUES (%s, %s, %s)")
            data_people = (id,movie_id,name)
            cursor.execute(add_people, data_people)
        cnx.commit()
    except:
        continue    
    
cursor.close()
cnx.close()


	




