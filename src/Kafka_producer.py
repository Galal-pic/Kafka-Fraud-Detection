import time
import json
import logging
from config.kafka_config import get_kafka_producer
from src.data_generator import fraudulent_data_generator

def main():
    producer = get_kafka_producer()
    file_path = "data/fraud_0.1origbase.csv"
    fraudulent_dataset_generator = fraudulent_data_generator(file_path)
    i = 0

    try:
        for fraud_data in fraudulent_dataset_generator:
            producer.produce(
                topic="fraudulent_data",
                key=f"{i}",
                value=json.dumps(fraud_data)
            )
            logging.info("Produced record #%d", i)
            time.sleep(4)
            i += 1
    finally:
        producer.flush()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
