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

#def feladat_10(a,b):

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

# def feladat_18(a,b): #nincs kesz
#     x=a
#     y=b
#     p=0
#     while x>0:
#         if x%2!=0:
#             p=p+y
#             print(p)
#         x=x/2
#         print(x)
#         y=y+y
#         print(y)
#     return p

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

    #print(feladat_10(1985,2020))

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

    # print(feladat_18(11,68))

    print("Feladat 19:")
    print(feladat_19(11))

    print("Feladat 20 Elso resze:")
    feladat_20A(5)
    print("Feladat 20 Masodik resze:")
    feladat_20B(5)




if __name__ == '__main__':
    main()