# python-kafka-sample

#### Start Kafka

> docker-compose up -d

#### Create topic

> docker exec -it kafka-python-demo-kafka-1 kafka-topics --create --topic test-topic --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

#### List topics using the correct container name
docker exec python-kafka-sample-kafka-1 kafka-topics --bootstrap-server localhost:9092 --list

#### Or check if Kafka is ready
docker exec python-kafka-sample-kafka-1 kafka-topics --bootstrap-server kafka:29092 --list

#### Install package

> pip install confluent-kafka

#### Run consumer

> python consumer.py

#### Run producer

> python producer.py