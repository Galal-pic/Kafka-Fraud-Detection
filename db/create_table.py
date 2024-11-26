from config.db_config import get_db_connection
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS fraud_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        step INT NOT NULL,
        type VARCHAR(50) NOT NULL,
        amount FLOAT NOT NULL,
        nameOrig VARCHAR(255) NOT NULL,
        oldbalanceOrg FLOAT NOT NULL,
        newbalanceOrig FLOAT NOT NULL,
        nameDest VARCHAR(255) NOT NULL,
        oldbalanceDest FLOAT NOT NULL,
        newbalanceDest FLOAT NOT NULL,
        isFraud TINYINT NOT NULL,
        isFlaggedFraud TINYINT NOT NULL,
        Prediction TINYINT NOT NULL
    );
    """
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            print("Table 'fraud_data' created successfully.")
    finally:
        connection.close()

if __name__ == "__main__":
    create_table()