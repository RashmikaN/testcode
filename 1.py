num = int(input())
def Base3(num):
    if (num==0):
        return
    x=num%3
    num//=3
    if (x<0):
        num+=1
    Base3(num);
    if (x<0):
        print(x+(3*(-1)))
    else:
        print(x,end='')
def convertBase3(num):
    if (num==0):
        print(0)
    else:
        Base3(num)
convertBase3(num);