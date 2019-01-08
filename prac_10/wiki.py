import wikipedia

get_search = wikipedia.search(input("What would you like to search for? "))
while get_search != "":
    print(wikipedia.summary(get_search))
    get_search = wikipedia.search(input("What would you like to search for? "))
