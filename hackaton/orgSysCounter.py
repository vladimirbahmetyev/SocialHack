import matplotlib.pyplot as plt
import numpy as np

from ML import CalcTone
from siteParser import getPosts
from userValidator import getUsersWeight


def calcOrgRait(socialNetwork: str, theme: str):
    posts = getPosts(url=socialNetwork, query=theme)
    n = len(posts)
    usersWeight = getUsersWeight(posts)
    tonesList = [CalcTone(post[0]) for user, post in posts.items()]
    return sum([tonesList[i]*usersWeight[i] for i in range(n)])/n, usersWeight, tonesList

def frontend(url, query):
    rating, uW, tL = calcOrgRait(url, query) #uW -- список весов юзеров
                                             #tL -- список тональностей комментариев
    print(rating)                            #rating -- рейтинг поискового запроса
    plt.hist(tL)
    plt.show()
    sup = []
    n = len(uW)
    for i in range(n):
        count = 0
        for j in range(n):
            if uW[j] >= i / n and uW[j] <  (i + 1) / n:
                count += 1
        sup.append(count)
    x = np.arange(0, 1, 1 / n)
    plt.plot(x, sup)
    plt.show()

#frontend("https://twitter.com/search?q=", "мтс")




