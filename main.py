import keys
import tweepy
import json
import requests
import time
from functions import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def check_id_in_file(id):
    with open('replied_tweets.txt' , 'r') as read_obj:
        for line in read_obj:
            if(id in line):
                return True
    return False


def main():
    mentions = api.mentions_timeline()
    myFile = open('replied_tweets.txt' , 'a')
    for mention in mentions:
        mention_id = str(mention.id)
        if(('#whatpokemonami' in mention.text) and (check_id_in_file(mention_id) == False)):
            myFile.write(str(mention.id))
            myFile.write("\n")
            pokemon = get_pokemon(mention.text)
            tweet_status = ("@" + mention.user.screen_name + " " + "Based on your birthday you are: \n" + "NAME: "
            + pokemon['name'] + "\nPOKEDEX ENTRY: " + str(pokemon['index']) + "\nTYPES: " + pokemon['type'])
            file = "pokemon.png"
            status = api.update_with_media(file, tweet_status)
            print("Replied to @" + mention.user.screen_name + "\n")




while True:
    main()
    print("Waiting for Tweet")
    time.sleep(5)
