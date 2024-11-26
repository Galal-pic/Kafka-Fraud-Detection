import pymysql

DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "Galal_Ewida",
    "password": "1234",
    "database": "frud_database"
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)
