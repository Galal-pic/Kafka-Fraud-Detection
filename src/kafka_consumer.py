from config.kafka_config import get_kafka_consumer
from config.db_config import get_db_connection
from config.model_config import load_model
from src.message_processor import process_message
from src.db_handler import insert_to_db

def main():
    consumer = get_kafka_consumer()
    connection = get_db_connection()
    model = load_model()

    try:
        with connection.cursor() as cursor:
            consumer.subscribe(["fraudulent_data"])
            i = 0

            while True:
                msg = consumer.poll(1)
                if msg:
                    value, prediction = process_message(msg, model)
                    insert_query = """
                    INSERT INTO fraud_data (step, type, amount, nameOrig, oldbalanceOrg, 
                                            newbalanceOrig, nameDest, oldbalanceDest, 
                                            newbalanceDest, isFraud, isFlaggedFraud, Prediction)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """
                    insert_to_db(cursor, insert_query, (value["step"], value["type"], 
                        value["amount"], value["nameOrig"], value["oldbalanceOrg"], 
                        value["newbalanceOrig"], value["nameDest"], value["oldbalanceDest"], 
                        value["newbalanceDest"], value["isFraud"], value["isFlaggedFraud"], prediction))
                    connection.commit()
                    print(f"pushed message number {i}")
                    i += 1
    finally:
        connection.close()

if __name__ == "__main__":
    main()
