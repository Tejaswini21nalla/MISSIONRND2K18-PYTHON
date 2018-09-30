def min_max(list):
    list1 = []
    for item in list:
        n=len(item)
        list1.append(n)
    x=min(list1)
    y=list1.index(x)
    z=max(list1)
    w=list1.index(z)
    return (list[y],list[w])

def get_min_max_words(input):
    """
    returns the words with the least and maximum length.
    Use min and max and pass another function as argument
    """
    return (min_max(input))# replace this calls to min and max
s=get_min_max_words(["fork", "engine", "fly"])
print(s)
