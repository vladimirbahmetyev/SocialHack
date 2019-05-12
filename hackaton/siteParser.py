import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import codecs


def getPosts(url: str, query: str, spq: int = 0, spu: int = 0):
    browser = webdriver.Chrome()

    browser.get(url + query)
    body = browser.find_element_by_tag_name("body")
    for i in range(spq):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
    tweets = browser.find_elements_by_class_name("tweet-text")
    tweets_txt = [tweet.text for tweet in tweets if tweet.text != '']

    users = browser.find_elements_by_class_name("username")
    users_txt = [user.text[1:] for user in users if user.text != '']
    users_txt = users_txt[2:]

    posts = dict(zip(users_txt, tweets_txt))
    posts_out = {}

    for user, tweet in posts.items():
        url = "https://twitter.com/" + user
        browser.get(url)
        body = browser.find_element_by_tag_name("body")
        for i in range(spu):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
        tweetsU = browser.find_elements_by_class_name("tweet-text")
        tweetsU_txt = [tweetU.text for tweetU in tweetsU if tweetU.text != '']

        postsU = [tweet]
        postsU.extend(tweetsU_txt)
        postsU = list(set(postsU))
        posts_out[user] = postsU

    return posts_out


def gencsv(posts, filename):
    with codecs.open(filename, 'w', 'utf-8') as file:
        for user, tweet in posts.items():
            file.write("%s,%s\n" % (user, tweet))