num=int(input())
lcd_not_inv=['3','4','7']
def possible(num):
    for i in str(num):
        if i in lcd_not_inv:
            return False
    return True
def rev(n):
    rn=0
    while n!=0:
        d=n%10
        rn=rn*10+d
        n//=10
    return rn
if(num>0):
    count=0
    temp=1
    while(count!=num):
        if possible(temp):
            count+=1
        temp+=1
    if((temp-1)==6):
        print(9)
    elif((temp-1)==9):
        print(6)