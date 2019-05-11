import re
from string import punctuation
from string import digits
import pymorphy2
import codecs

def prepr(input: str):
    input = input.lower()
    input = re.sub(':', '', input)
    input = re.sub("#", '', input)
    delreg = "(\S+(\.|\/)+\S+)+"
    input = re.sub(delreg, '', input)
    stop = punctuation + digits + '»«'
    ru = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ '
    input = ''.join([s for s in input if s not in stop and s in ru])
    stopwords = []
    morph = pymorphy2.MorphAnalyzer()
    input =  [morph.parse(word)[0].normal_form for word in input.split()]
    with codecs.open("stopwords.txt", 'r', 'utf-8') as file:
        for line in file:
            print(line)
            stopwords += line
    input = [word for word in input if word not in stopwords]

    return input