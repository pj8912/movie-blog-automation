import wikipedia

# wiki = wikipediaapi.Wikipedia(
#         language='en',
#         extract_format=wikipediaapi.ExtractFormat.WIKI
# )

# search_term = "Python programming language"
search_term = input("Search: ")
result = wikipedia.search(search_term, 1000)
print(result)
print()
print('Their urls')
print()


# This works******
# for i in result:
#     base_url = "https://en.wikipedia.org/wiki/"
#     url = base_url+i
#     print(url)


def add_underscore(a):
    a1 = ""
    for i in range(len(a)):
        if a[i] == ' ':
            a1 = a1 + '_'
        else:
            a1 = a1 + a[i]
    return a1

title_list = []

for i in result:
    title = add_underscore(i)
    title_list.append(title)
    print(title)

print('\n title list: \n ')
print(title_list)



print('\n-----------------\n')

for i in result:
    res = add_underscore(i)
    base_url = "https://en.wikipedia.org/wiki/"
    url = base_url+res
    print(url)


# for result in search_results.results:
#     print(result.fullurl)
