import ast  # for converting str to list
import nltk
from nltk.stem import PorterStemmer

# handle genres
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L


# Here keeping top 3 cast
def convert_cast(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter += 1
    return L


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L


# now removing space like that
'Anna Kendrick'
'AnnaKendrick'


def remove_space(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


ps = PorterStemmer()


def stems(text):
    T = []

    for i in text.split():
        T.append(ps.stem(i))

    return " ".join(T)


