from delfunc import prepr


def getUsersWeight(usersDict, usersList: list):
    usersWeight = []
    for user in usersList:
        usersPosts = usersDict[user]

        postTones = [-CalcTone(prepr(post)) + 2 for post in usersPosts]

        # tones may be
        # 1 - positive
        # 0 - neutral
        # -1 - negative

        averageAbsScore = abs(sum(postTones) / postTones.__len__())

        if averageAbsScore < 0.5:
            continue

        usersWeight[user] = 1 - averageAbsScore

        lengthOfAllPosts = 0

        for record in usersDict[user]:
            lengthOfAllPosts += record.__len__()

        averageRecordLengthInChar = lengthOfAllPosts / sum(usersDict[user].__len__())

        if averageRecordLengthInChar < 60 or averageRecordLengthInChar > 140:
            continue

        usersWeight[user] *= 1 - averageRecordLengthInChar / 100
    return usersWeight
