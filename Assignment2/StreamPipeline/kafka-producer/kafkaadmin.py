from kafka.admin import KafkaAdminClient, NewTopic

def delete_topics(admin):
    admin.delete_topics(topics=['game', 'avg_score'])


def create_topics(admin, topic_list):
    admin.create_topics(new_topics=topic_list, validate_only=False)


if __name__ == '__main__':
    admin_client = KafkaAdminClient(bootstrap_servers="34.133.77.8:9092",
                                    client_id='ipek')  # use your VM's external IP Here!
    topic_list = [NewTopic(name="game", num_partitions=1, replication_factor=1),
                  NewTopic(name="avg_score", num_partitions=1, replication_factor=1),
                  NewTopic(name="reddit", num_partitions=1, replication_factor=1)]
    create_topics(admin_client, topic_list)
