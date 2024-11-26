# Kafka-MySQL-ML Project

## Overview
This project demonstrates a real-time pipeline using Kafka for message streaming, MySQL for data storage, and a pre-trained ML model for predictions.

### Components
1. **Producer**: Reads data from a CSV file and streams it to a Kafka topic.
2. **Consumer**: Consumes messages, applies predictions, and inserts them into a MySQL database.
3. **Database**: MySQL stores the processed data.
4. **Machine Learning**: Pre-trained model predicts fraud likelihood.

---

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
