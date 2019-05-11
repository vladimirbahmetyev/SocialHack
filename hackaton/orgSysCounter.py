from siteParser import getPosts
from siteParser import gencsv


def calcOrgRait(theme: str, socialNetwork: str):
    posts = getPosts(url=socialNetwork, query=theme)
    tonesList = [CalcTone(gencsv(post, "defaultName")) for post in posts]


