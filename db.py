import pymysql

def get_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="HotelDB",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
