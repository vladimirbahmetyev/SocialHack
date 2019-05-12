from delfunc import prepr
from ML import CalcTone


def getAdvAndDis(tonesList, usersWeight, posts):
    advantages = []
    disAdvantages = []
    n = len(tonesList)
    for i in range(n):
        if tonesList[i] > 2.4 and usersWeight[i] > 0.6:
            advantages.extend(prepr(posts[i]))
        if CalcTone(posts[i]) < 1.5 and usersWeight[i] > 0.6:

            disAdvantages.extend(prepr(posts[i]))
    cleanAdvantages = advantages.copy()
    cleanAdvantages = list(set(cleanAdvantages))
    top = [(advantages.count(adv), adv) for adv in cleanAdvantages]
    top = sorted(top)[::-1][:10]
    top = [x[1] for x in top]

    cleanDisAdvantages = disAdvantages.copy()
    cleanDisAdvantages = list(set(cleanDisAdvantages))
    bot = [(disAdvantages.count(adv), adv) for adv in cleanDisAdvantages]
    bot = sorted(bot)[::-1][:10]
    bot = [x[1] for x in bot]
    return top, bot