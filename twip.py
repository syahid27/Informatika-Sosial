import tweepy
import csv

api_key = 'yTMJW8fir7nMIFCtdJJ5aOctM'
api_key_secret = 'y7BymnLQsmrTofwjfH5LjXUZlEnP0j6jd7VrwOI8zG1EYfrXDr'
access_token = '854637856446218241-Zny9BH2VP7keNeB3gD1v5hkJc5YWd38'
access_token_secret = 'BGD9Aq2pWlAyrTaJgCJYnldaljxUYHkvuhdxmuF6YlZfm'
tweetsPerQry = 1000
maxTweets = 1000000
search_key = "#mudikdilarang"
maxId = -1
tweetCount = 0

authentication = tweepy.OAuthHandler(api_key, api_key_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

while tweetCount < maxTweets:
    if maxId <= 0 :
        newTweets = api.search(q=search_key, count=tweetsPerQry, result_type="recent", tweet_mode = "extended")
    
    newTweets = api.search(q=search_key, count=tweetsPerQry, result_type="recent", tweet_mode = "extended", max_id=str(maxId-1))

    if not newTweets :
        print("Tweet Habis")
        break

    for tweet in newTweets:
        dictTweet = {
            "username" : tweet.user.name,
            "tweet" : tweet.full_text.encode('utf-8')
        }
        print("Username {username} : {tweet}".format(username=dictTweet["username"], tweet=dictTweet["tweet"]))
        with open(search_key+".csv", 'a+', newline='') as csv_file:
            fieldNames = ["username", "tweet"]
            writer = csv.DictWriter(csv_file, fieldnames = fieldNames, delimiter=";",)
            writer.writerow(dictTweet)

    tweetCount += len(newTweets)	
    maxId = newTweets[-1].id