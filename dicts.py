def mufun2(x, y):
    myBroths = {
        "bro1": x,
        "bro2": y,
    }
    return myBroths


def mufun():
    bro1 = {
        "Name": input("Name: "),
        "Surname": input("Surname: "),
        "Year": input("Year: ")
    }
    bro2 = {
        "Name": input("Name2: "),
        "Surname": input("Surname2: "),
        "Year": input("Year2: ")
    }
    return bro1, bro2


a, b = mufun()

print(mufun2(a, b))
