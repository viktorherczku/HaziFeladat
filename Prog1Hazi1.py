import math as m

def feladat_1(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

def feladat_2():

    a=int(input("elso:"))
    b=int(input("masodik:"))
    c=int(input("harmadik:"))

    if a>b and a>c and b>c:
        return c,b,a

    elif a>b and a>c and b<c:
        return b,c,a

    elif a>b and a<c and b<c:
        return b,a,c

    elif a<b and a<c and b<c:
        return a,b,c

    elif a<b and a<c and b>c:
        return a,c,b

    elif a<b and a>c and b>c:
        return c,a,b

def feladat_3(x):

    if x>-2 and x<0:
        return 2*x

    elif x>=0 and x<2:
        return x*x

    elif x>2:
        return 10
    else:
        print("Hibas ertek")

def feladat_4(a,b,c):

    minimum=0

    if a<b:
        if b<c or (b>c and a<c):
            minimum=a
        else:
            minimum=c
    elif a>b and b<c:
        minimum=b
    else:
        minimum=c

    if a==b and b==c:
        minimum=a
    print("minimum:",minimum)

    maximum=0

    a=abs(a)
    b=abs(b)
    c=abs(c)

    if a > b and b>c or (b<c and a>c):
        maximum = a
    else:
        maximum = c

    if a < b and b>c:
        maximum = b
    else:
        maximum = c

    if a == b and b == c:
        maximum= a
    print("abszolut ertek maximuma: ",maximum)
def feladat_5(a,b,c,d):
    print(a,b,c,d)

    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

def feladat_6():

    while True:

        a=float(input("elso: "))
        b=float(input("masodik: "))
        c=float(input("harmadik: "))

        if a<=0 or b<=0 or c<=0:
            print("Hiba")

        else:
            break

    if a+b>c and a+c>b and b+c>a:

        p=(a+b+c)/2
        T=m.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=a*b*c/(4*T)
        print("R=%.2f és r=%.2f"%(R,r))


def feladat_7(hossz,szel,drot):

    ker=hossz*2+szel*2

    if drot>ker:

        return drot-ker," maradt"

    elif drot<ker:

        return ker-drot," kell még"

    else:
        return 0

def feladat_8(x,a,b,c,d):

    if x<5:

        print(3*x-5)

    elif 5<=x<=10:

        print(10)

    elif x>10:

        print(9*x+1)

    if a+c>2*d and b>0:

        print(d-3*b)

    elif a+c<2*d and b<0:

        print(d+3*b)

    else:

        print(4)
def feladat_9(a,b,c):

    delta=b**2-4*a*c

    if delta<0:

        return None

    elif delta==0:

        return -b/(2*a)

    elif delta>0:

        return (-b+m.sqrt(delta))/(2*a),(-b-m.sqrt(delta))/(2*a)

def feladat_10(a,b):
    db = 0
    for i in range(a, b + 1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            db += 1
    print(db, "db")
#def feladat_11(a):

def feladat_12(max_pont,elert_pont):
    minimum=max_pont*0.60
    if elert_pont>minimum:
        return "Sikeres"
    else:
        return "Sikertelen"

def feladat_13(jegy):
    if jegy==1:
        return "Elégtelen"
    elif jegy==2:
        return "Elégséges"
    elif jegy==3:
        return "Közepes"
    elif jegy==4:
        return "Jó"
    elif jegy==5:
        return "Jeles"
    else:
        return "Hiba"

def feladat_14(szam):
    if szam == 1:
        return "Január"
    elif szam == 2:
        return "Február"
    elif szam == 3:
        return "Március"
    elif szam == 4:
        return "Április"
    elif szam == 5:
        return "Május"
    elif szam == 6:
        return "Június"
    elif szam == 7:
        return "Július"
    elif szam == 8:
        return "Augusztus"
    elif szam == 9:
        return "Szeptember"
    elif szam == 10:
        return "Oktober"
    elif szam == 11:
        return "November"
    elif szam == 12:
        return "December"
    else:
        return "Hiba"

def feladat_15(a,b):
    h=0
    while a>=b:
        h=h+1
        a=a-b
    return h

def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a

def feladat_17(n):
    a=n
    uj=0
    while n!=0:
        b=n%10
        uj=uj*10+b
        n=n//10
    return uj==a

def feladat_18(a,b):
    x=a
    y=b
    p=0
    while x>0:
        if x%2!=0:
            p=p+y
        x=x/2
        y=y+y
    return p

def feladat_19(n):
    p=True
    if n==1:
        p=False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            p=False
            break
    return p

def feladat_20A(n):
    a=1
    b=1
    if n==1:
        print(a, end=" ")
    elif n==2:
        print(a,b,end=" ")
    else:
        c=a+b
        print(a,b,c,end=" ")
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c,end=" ")
            k=k+1

def feladat_20B(n):
    a=1
    b=1
    k=1
    while k<=n:
        print("%.4f"%b,end=" ")
        a=a+b
        b=a-b
        k=k+1

def feladat_21(n):
    ujszam=0
    while n!=0:
        ujszam=ujszam*10+n%10
        n=n//10
    return ujszam

def feladat_22(alap,kitevo):
    eredmeny=1
    while kitevo>0:
        if kitevo%2!=0:
            eredmeny=eredmeny*alap
            kitevo=kitevo-1
        alap=alap*alap
        kitevo=kitevo//2
    return eredmeny

def feladat_23(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def feladat_24():
    asd=True
    db1=0
    db2=0
    while asd==True:
        a=int(input("input: "))

        if a==0:
            asd=False
        else:
            if a%7==5:
                db1+=1
            if a%13==7:
                db2+=1
    return ("7el osztva 5 a maradek: "),db1,("13mal osztva 7 a maradek: "),db2

def feladat_25():
    fo=int(input("fo: "))
    km2=int(input("km^2: "))
    nepsuruseg=fo//km2
    if nepsuruseg>0:
        if nepsuruseg<50:
            print("Ritkan lakott nepsuruseg")
        elif nepsuruseg>50 and nepsuruseg<300:
            print("Atlagos nepsuruseg")
        else:
            print("Surun lakott")
    else:
        print("Hiba")

def feladat_26():
    osszeg=0
    negativ=0
    pozitiv=0
    asd=True
    while asd is True:
        szam=int(input("szam: "))
        if szam==0:
            asd=False
        else:
            osszeg=osszeg + szam
            print(osszeg)
            if szam>0:
                pozitiv+=1
            elif szam<0:
                negativ+=1
    print("pozitiv szamok: ")
    print(pozitiv)
    print("negativ szamok: ")
    print(negativ)

def feladat_27():
    asd=True
    poz=1
    pozitiv=0
    neg=1
    negativ=0
    while asd is True:
        szam=int(input("szam: "))
        if szam>0:
            poz+=1
            pozitiv+=1
        elif szam<0:
            neg+=1
            negativ+=1

        if poz-neg==2 or poz-neg==-2:
            asd=False
    print("Pozitiv szamok: ")
    print(pozitiv)
    print("Negativ szamok: ")
    print(negativ)

def feladat_28(szam):
    for i in range(1,szam):
        if i*i<szam:
            print(i)

def feladat_29(szam):
    num = 1
    while szam >= 1 and szam<=11:
        num = num * szam
        szam = szam - 1
    return num

def feladat_30():
    ev=int(input("ev: "))
    ho=int(input("ho: "))
    nap=int(input("nap: "))
    if ev>0 and ho>0 and nap>0 and ho<13 and nap<32:

        if ho==1:
            print(31,". napja a", ev, "évnek")
        elif ho==2:
            print(31+nap,". napja a",ev,"évnek")
        elif ho==3:
            print(31+28+nap, ". napja a", ev, "évnek")
        elif ho==4:
            print(31 + 28 +31 +nap, ". napja a", ev, "évnek")
        elif ho==5:
            print(31 + 28 + 31 +30+ nap, ". napja a", ev, "évnek")
        elif ho==6:
            print(31+28+31+30+31+nap, ". napja a", ev, "évnek")
        elif ho==7:
            print(31+28+31+30+31+30+nap, ". napja a", ev, "évnek")
        elif ho==8:
            print(31+28+31+30+31+30+31+nap, ". napja a", ev, "évnek")
        elif ho==9:
            print(31 + 28 + 31 + 30 + 31 + 30 + 31 +31+ nap, ". napja a", ev, "évnek")
        elif ho==10:
            print(31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 +30+ nap, ". napja a", ev, "évnek")
        elif ho==11:
            print(31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 +30+31+ nap, ". napja a", ev, "évnek")
        elif ho==12:
            print(31 + 28 + 31 + 30 + 31 + 30 + 31 + 31+30 + nap, ". napja a", ev, "évnek")
    else:
        print("Hiba")

def feladat_31(szam):
    a=szam//2
    for i in range(1,a):
        if szam%i==0:
            print(i)
    print(szam)
def feladat_32(n1,n2):
    szam = int(input("szam: "))
    for i in range(n1 + 1, n2):
        if i % szam == 0:
            print(i)

def feladat_34(szam):
    if szam>6 and szam%2==0:
        tomb=[]
        for i in range(1,szam):
            if feladat_19(i):
                tomb.append(i)
        for j in tomb:
            for x in tomb:
                if j+x==szam:
                    return j,x
    else:
        return "Hiba"


def feladat_36(szam):
    a=1
    b=1
    k=1
    db=0
    for i in range(szam):
        if b<szam:
            a=a+b
            b=a-b
            k=k+1
            db=db+1
        if i==b:
            break

    return db
def feladat_37(szam):
    a = 1
    b = 1
    k = 1
    db = 0
    for i in range(szam):
        a = a + b
        b = a - b
        k = k + 1
        db = db + 1
        if b>szam:
            return b













def main():
    print("Feladat 1:")
    print(feladat_1(10,5))

    print("Feladat 2:")
    print(feladat_2())

    print("Feladat 3:")
    print(feladat_3(1.7))

    print("Feladat 4:")
    feladat_4(-1,-2,-3)

    print("Feladat 5:")
    feladat_5(6,35,-43,10)

    print("Feladat 6:")
    feladat_6()

    print("Feladat 7:")
    print(feladat_7(3,5,10))

    print("Feladat 8:")
    feladat_8(4,10,3,20,7)

    print("Feladat 9:")
    print(feladat_9(1,1,1))
    print(feladat_9(1,2,1))
    print(feladat_9(1,-4,3))

    print("Feladat 10:")
    feladat_10(1952, 1996)

    print("Feladat 12:")
    print(feladat_12(100,61))

    print("Feladat 13:")
    print(feladat_13(5))

    print("Feladat 14:")
    print(feladat_14(2))

    print("Feladat 15:")
    print(feladat_15(15,3))

    print("Feladat 16:")
    print(feladat_16(360,225))

    print("Feladat 17:")
    print(feladat_17(131))

    print("Feladat 18:")
    print(feladat_18(11,68))

    print("Feladat 19:")
    print(feladat_19(11))

    print("Feladat 20 Elso resze:")
    feladat_20A(5)
    print("Feladat 20 Masodik resze:")
    feladat_20B(5)
    print()

    print("Feladat 21:")
    print(feladat_21(321))

    print("Feladat 22:")
    print(feladat_22(2,3))

    print("Feladat 23:")
    print(feladat_23(6))

    print("Feladat 24:")
    print(feladat_24())

    print("Feladat 25:")
    feladat_25()

    print("Feladat 26:")
    feladat_26()

    print("Feladat 27:")
    feladat_27()

    print("Feladat 28:")
    feladat_28(10)

    print("Feladat 29:")
    print(feladat_29(5))

    print("Feladat 30:")
    feladat_30()

    print("Feladat 31:")
    feladat_31(100)

    print("Feladat 32:")
    feladat_32(5,55)

    print("Feladat 34:")
    print(feladat_34(10))



    print("Feladat 36:")
    print(feladat_36(8))

    print("Feladat 37:")
    print(feladat_37(8))




if __name__ == '__main__':
    main()

