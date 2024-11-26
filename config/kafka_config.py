from quixstreams import Application

def get_kafka_consumer():
    return Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        auto_offset_reset="earliest"
    ).get_consumer()

def get_kafka_producer():
    return Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
        auto_offset_reset="latest"
    ).get_producer()
