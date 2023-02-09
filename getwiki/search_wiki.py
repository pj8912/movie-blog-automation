import wikipedia

title_list = []

def add_underscore(a):
    a1 = ""
    for i in range(len(a)):
        if a[i] == ' ':
            a1 = a1 + '_'
        else:
            a1 = a1 + a[i]
    return a1


def search_wikipedia(search_term):
    result = wikipedia.search(search_term, 1000)
    for i in result:
            title = add_underscore(i)
            title_list.append(title)