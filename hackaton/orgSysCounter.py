from siteParser import getPosts
from siteParser import gencsv
from userValidator import getUsersWeight
from ML import CalcTone

def calcOrgRait(socialNetwork: str, theme: str):
    posts = getPosts(url=socialNetwork, query=theme)
    n = len(posts)
    usersWeight = getUsersWeight(posts)
    tonesList = [CalcTone(post[0]) for user, post in posts.items()]
    return sum([tonesList[i]*usersWeight[i] for i in range(n)])/n

# print(calcOrgRait("https://twitter.com/search?q=", "мтс"))

