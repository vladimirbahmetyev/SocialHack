#TODO rework metric
from delfunc import prepr
from ML import CalcTone

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

        if averageAbsScore < 0.8:
            continue

        usersWeight[user] = 1 - averageAbsScore

        lengthOfAllPosts = 0

        for record in usersDict[user]:
            lengthOfAllPosts += len(record)

        averageRecordLengthInChar = lengthOfAllPosts / len(usersDict[user])

        if averageRecordLengthInChar < 60 or averageRecordLengthInChar > 140:
            continue

        usersWeight[user] *= 1 - averageRecordLengthInChar / 100
    out = [value for value in usersWeight.values()]
    return out
