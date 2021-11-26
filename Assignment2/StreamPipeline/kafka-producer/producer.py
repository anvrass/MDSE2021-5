from kafka import KafkaProducer


def kafka_python_producer_sync(producer, msg, topic):
    s_msg = str(msg)
    producer.send(topic, bytes(s_msg, encoding='utf-8'))
    print("Sending " + s_msg)
    producer.flush(timeout=60)


def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)


def kafka_python_producer_async(producer, msg, topic):
    producer.send(topic, bytes(msg, encoding='utf-8')).add_callback(success).add_errback(error)
    producer.flush()

def read_reddit_data():
    import praw
    import pandas as pd
    reddit = praw.Reddit(client_id='ZFCLJ7BZHGrUJFPMQ89sCw', client_secret='DZFIupQh5UlFoYGaz18wEewRexex7A',
                         user_agent='Streaming Scraper')

    # get 1000 hot posts from subreddit : Conservative
    new_posts = reddit.subreddit('Conservative').new(limit=1000)

    posts = []
    ml_subreddit = reddit.subreddit('Conservative')
    for post in ml_subreddit.new(limit=1000):
        posts.append(
            [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
    posts = pd.DataFrame(posts, columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

    #to save the data locally
    #posts.to_csv("reddit.csv")
    lines = posts.values.tolist()
    return lines

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='34.133.77.8:9092')  # use your VM's external IP Here!
    lines = read_reddit_data()

    #If the above code does not work, download the data to your computer and use the commented code.
    #with open('C:/Users/ipeku/Downloads/Streaming_Pipeline/db_container/reddit.csv', encoding="utf8") as f:
    #    lines = f.readlines()
    
    for line in lines:
        kafka_python_producer_sync(producer, line, 'reddit')


