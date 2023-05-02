LLP = [1,2,3,4,-1]
LL = [None,None,None,None,None]
hp = 0
sp = -1

def Stats():
    global hp, sp, LLP, LL
    print(LL)
    print(LLP)
    print(f"hp : {hp}, sp : {sp}")
    print("------------------------------")

def Add(x):
    global hp, sp, LLP, LL
    if hp == -1:
        print("List is full")
    else:
        temp = sp
        sp = hp
        LL[sp] = x
        hp = LLP[hp]
        LLP[sp] = temp

def Search(x):
    found = False
    i = sp
    while not(found) and (i != -1):
        if LL[i] == x:
            found = True
            print(i)
        else:
            i = LLP[i]
    if not(found):
        print("Item not found")

def Delete(x):
    global hp, sp, LLP, LL
    if sp != -1:
        found = False
        i = sp
        j = i
        while not(found) and (i != -1):
            if LL[i] == x:
                found = True
            else:
                j = i
                i = LLP[i]
        if not(found):
            print("Item not found")
        else:
            if i == sp:
                sp = LLP[i]
            LLP[j] = LLP[i]
            LLP[i] = hp
            LL[i] = None
            hp = i

    else:
        print("List is empty")