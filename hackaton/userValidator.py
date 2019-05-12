#TODO rework metric
from delfunc import prepr
from ML import CalcTone
import numpy as np

def getUsersWeight(usersDict):
    usersWeight = {}
    for user in usersDict:
        usersPosts = usersDict[user]

        postTones = [-CalcTone(prepr(post)) + 2 for post in usersPosts]

        # tones may be
        # 1 - positive
        # 0 - neutral
        # -1 - negative

        averageAbsScore = abs(sum(postTones) / len(postTones))

        usersWeight[user] = 1 - averageAbsScore

        lengthOfAllPosts = 0

        for record in usersDict[user]:
            lengthOfAllPosts += len(record)

        averageRecordLengthInChar = lengthOfAllPosts / len(usersDict[user])

        usersWeight[user] *= gaussian(averageRecordLengthInChar, 110, 50)
    out = [value for value in usersWeight.values()]
    return out

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
