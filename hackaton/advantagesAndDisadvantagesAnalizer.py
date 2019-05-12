from delfunc import prepr
from ML import CalcTone


def getAdvAndDis(tonesList, usersWeight, posts):
    advantages = []
    disAdvantages = []
    n = len(tonesList)
    for i in range(n):
        if tonesList[i] > 2.4 and usersWeight[i] > 0.6:
            advantages.append(prepr(posts[i]))
        if CalcTone(posts[i]) < 1.5 and usersWeight[i] > 0.6:
            disAdvantages.append(prepr(posts[i]))

    cleanAdvantages = advantages.copy()
    cleanAdvantages = list(set(cleanAdvantages))
    top = [advantages.count(cleanAdvantages[i]) for i in range(len(cleanAdvantages))]
    top.sort()

    cleanDisAdvantages = disAdvantages.copy()
    cleanDisAdvantages = list(set(cleanDisAdvantages))
    bot = [advantages.count(cleanDisAdvantages[i]) for i in range(len(cleanDisAdvantages))]
    bot.sort()

    return top, bot