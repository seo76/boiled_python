def lst():
    global mano, nom

    mano = []
    nom = 0

    while nom <= 100:
        nom = nom + 1
        mano.append(nom)


def ltpls():
    lst()
    nom2 = 1
    for nom2 in range (100):
        mano[nom2]

def lst2():
    if (mano[1] == 2):
        print("1")
    else:
        print("d")

n=0
lst()
lst2()
print(mano[0])
