def times10(x):
    return 10 * x

print(times10(2))


def firstA(w):

    if w[0] == "a":
        return True
    
    return False

print(firstA("android"))



def sizer(n):

    if n < 10:
        return "small"
    if n < 100:
        return "medium"
    if n > 100:
        return "large"

print(sizer(2))


def doubleword(w):

    word = w

    for i in range(1,len(w)):
        word = word + word

    return word

print(doubleword("go"))


