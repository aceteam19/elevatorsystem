#!C:\Users\Administrator\AppData\Local\Programs\Python\Python38\python.exe

import mysql.connector

host = "192.168.1.201"

port = "3306"

cnx = mysql.connector.connect(user='root', password='aceteam19',
                                   host=host, port=port,
                                   database='elevatorcontrols')


def get_all_items():
    myc = cnx.cursor(dictionary=True)
    myc.execute("""

    SELECT
        *
    FROM `items`
    
    """)
    return myc.fetchall()
