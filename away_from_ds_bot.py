import pickle
import random
import tweepy as tw
import time

# Get the titles
my_file = open("titles.txt", "r")
content = my_file.read()
title_list = content.split(",")
my_file.close()

# Get the hashtags
with open('hashtags', 'rb') as fp:
    hashtags = pickle.load(fp)

# Get the names
my_file = open("names.txt", "r")
content = my_file.read()
name_list = content.split(",")
my_file.close()

# Log keys, tokens and secrets
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authorize access
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

for line in title_list:
    # Get numbers for randomness
    name_number = random.randint(0, 49)
    hash_sample = random.sample(hashtags, 3)
    image_number = random.randint(1, 30)

    # Build final post
    post = [line, "by", name_list[name_number], f"#{hash_sample[0]}", f"#{hash_sample[1]}", f"#{hash_sample[2]}"]
    final_post = " ".join([elem for elem in post])

    # Upload image randomly from folder
    image = str(f"./pictures/{image_number}.jpeg")
    media_obj = api.media_upload(filename=image)

    # Make the post
    api.update_status(status=final_post, media_ids=[media_obj.media_id])

    # Print something in the terminal
    print("Post made, going to sleep for half an hour")
    
    # Sleep for an hour
    time.sleep(1800)
