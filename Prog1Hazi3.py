import numpy as np
def lnko(a,b):
    maradek=a%b
    if maradek==0:
        return b
    else:
        return lnko(b,maradek)
def osztok(n):
    db=2
    for i in range(2,n//2+1):
        if n%i==0:
            db+=1
    return db

def feladat_1():
    t=[]
    n=int(input("n="))
    for x in range(n):
       t.append(int(input()))
    for i in range(len(t)-1):
        for j in range(i+1,len(t)):
            if t[i]==t[j]:
                print("egyenlo sorszamok:",i,j)

def feladat_2(n):
    paros=0
    paratlan=0
    for i in range(1,n+1):
        if i%2==0:
            paros+=1
        if i%2!=0:
            paratlan+=1
    print("Arány:",paros/paratlan)

def feladat_3(t):
    x=0
    db=0
    for i in t:
        db+=1
        i=abs(i)
        x+=i
    return x/db

def feladat_4(n):
    pozitiv=1
    negativ=0
    db=0
    for i in range(n):
        asd=int(input("szam: "))
        if asd>0:
            pozitiv*=asd
        if asd<0:
            db+=1
            negativ+=asd
    print(pozitiv,negativ/db)

def feladat_5(t):
    x=1
    y=0
    for i in t:
        if i<7:
            x*=i
        elif i>10:
            y+=i
    print("kisebbek:",x)
    print("nagyobbak:",y)

def feladat_6():
    db=0
    elso=0
    masodik=0
    while True:
        db += 1
        asd=int(input("szam: "))

        if elso + masodik == asd and masodik!=0:
            print(asd)
        if db%2==0:
            masodik=asd

        if db%2!=0:
            elso=asd

        if asd==0:
            break

def feladat_7():
    lista=[]
    max=0
    elso=0
    masodik=0
    harmadik=0
    while True:
        asd=int(input("szam: "))
        if asd!=0:
            lista.append(asd)
        if asd==0:
            break
    for i in range(0,len(lista)-2):
        for j in range(i+1,len(lista)-1):
            for a in range(i+2,len(lista)):
                if ((lista[i]+lista[j]+lista[a])/3)>max and lista[i]!=lista[j] and lista[i]!=lista[a] and lista[j]!=lista[a]:
                    max=((lista[i]+lista[j]+lista[a])/3)
                    elso=lista[i]
                    masodik=lista[j]
                    harmadik=lista[a]
    print(elso,masodik,harmadik)

def feladat_8(t,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if t[i]>t[j]:
                return False
    return True


def feladat_9(t,meret):
    for i in range(meret-1):
        for j in range(i+1,meret):
            if lnko(t[i],t[j])!=1:
                return 0
            else:
                return 1

def feladat_10(t,k):
    l=[]
    meret=len(t)
    for i in range(meret-1):
        for j in range(i+1,meret):
            if t[i]>t[j]:
                tmp=t[i]
                t[i]=t[j]
                t[j]=tmp

    for i in range(meret):
        l.append(osztok(t[i]))

    also=0
    felso=meret-1
    while also<=felso:
        kozep=(felso+also)//2
        if k<l[kozep]:
            felso=kozep-1
            if k<l[kozep]:
                return kozep

        elif k>l[kozep]:
            also=kozep+1
            if k<l[kozep]:
                return kozep








def main():
    print("feladat 1:")
    feladat_1()

    print("feladat 2:")
    feladat_2(69)

    print("feladat 3:")
    n = int(input("n="))
    tomb=np.empty(n,dtype='int')
    for i in range(n):
        tomb[i]=int(input())
    print(feladat_3(tomb))

    print("feladat 4:")
    feladat_4(5)

    print("feladat 5:")
    feladat_5(tomb)

    print("feladat 6:")
    feladat_6()

    print("feladat 7:")
    feladat_7()

    print("feladat 8:")
    n=int(input("n: "))
    tomb=np.empty(n,dtype='d')
    for i in range(n):
        tomb[i]=float(input())
    print(feladat_8(tomb,len(tomb)))

    print("feladat 9:")
    n=int(input("n: "))
    tomb=np.empty(n,dtype='int')
    for i in range(n):
        tomb[i]=int(input())
    print(feladat_9(tomb,len(tomb)))

    print("feladat 10:")
    n=int(input("n: "))
    k=int(input("k: "))
    tomb=np.empty(n,dtype='int')
    for i in range(n):
        tomb[i]=int(input())
    print(feladat_10(tomb,k))

if __name__ == '__main__':
    main()