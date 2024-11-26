def insert_to_db(cursor, query, data):
    cursor.execute(query, data)
