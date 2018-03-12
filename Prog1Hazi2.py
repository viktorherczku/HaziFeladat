import math as m
import sys
import codecs as cod
def prim_e(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def feladat_1(szam):
    db=0
    for i in range(1,szam+1):
        if szam%i==0:
            db+=1
    if db==4:
        return True
    return False

def feladat_2(n):
    prim=[2,3,5]
    szam=6
    while len(prim)<n:
        if prim_e(szam):
            prim.append(szam)
        szam+=1
    return prim[n-1]

def feladat_3(szam):
    asd=1
    while 2*asd<szam:
        asd=asd*2
    return 2*asd

def feladat_4():
    elso=0
    masodik=-1
    harmadik=-1
    for i in  range(1,10):
        elso=elso+1
        masodik=0
        harmadik=0
        db=0
        for j in range(1,10):
            masodik+=1
            harmadik=0
            for k in range(1,10):
                harmadik+=1
                if elso!=masodik and elso!=harmadik and masodik!=harmadik:
                    print(elso,masodik,harmadik)

def osztok_szama(szam):
    db=2
    for i in range(2,szam//2+1):
        if szam%i==0:
            db+=1
    return db
def feladat_5(n):
    max=1
    for i in range(2,n+1):
        if max<osztok_szama(i):
            max=osztok_szama(i)
            print(i)

def feladat_6(a,b):
    p=True
    db=0
    a=str(a)
    b=str(b)
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                db=db+1
    if db>=2:
        return p
    else:
        p=False
        return p

def feladat_7(elso,masodik):
    elso=abs(elso)
    masodik=abs(masodik)
    elso=str(elso)
    masodik=str(masodik)
    for i in range(len(elso)):
        for j in range(len(masodik)):
            if elso[i]==masodik[j]:
                return True
    return False

def feladat_8(szam):
    db=0
    asd=0
    for i in range(1,szam):
        if asd<szam:
            asd+=i
            print(asd)
            db+=1
    return db

def feladat_9():
    perc = 0
    aktualismagassag = 1
    asd=2
    while aktualismagassag<300:
        aktualismagassag += aktualismagassag/asd
        asd+=1
        perc+=1
    return perc

def feladat_10():
    try:
        txt=open("be.txt",mode="r")
        meret=0
        for sor in txt:
            sor=sor.strip()
            if (sor[0].isupper()) and len(sor)>meret:
                meret=len(sor)
        print(meret)
        txt.close()
    except OSError:
        print("hiba")
    except Exception as a:
        print(a)

def feladat_11():
    try:
        txt=open("be.txt",mode="r")
        meret=9999
        for sor in txt:
            sor = sor.strip()
            for i in range(len(sor)):
                if (sor[i] == ".") or (sor[i] == "!") or (sor[i] == "?"):
                    if (len(sor) < meret):
                        meret = len(sor)
        print(meret)
        txt.close()
    except OSError:
        print("hiba")
    except Exception as a:
        print(a)

def feladat_12():
    try:
     file=open("be.txt",mode="r")
     file1=open("ki.txt",mode="w")
     db=0
     for sor in file:
         sor = sor.split(" ")
         a=sor[len(sor)-1]
         a=int(a)
         for i in range(len(sor)-1):
             if sor[i]==sor[i+1]:
                 db=db+1
         if db+1>=a:
             return True
         else:
             return False
    except OSError:
        print("hiba")
    except Exception as a:
        print(a)
def feladat_13():
    try:
        file=open("be.txt",mode="r")
        db=0
        for sor in file:
            sor=sor.split(" ")
            a=sor[len(sor)-1]
            a=int(a)

            for i in range(len(sor)-1):
                x=int(sor[i])
                y=int(sor[i+1])
                z=abs(x-y)
                if z<=a:
                    db=db+1
            print(db)
    except OSError:
        print("hiba")
    except Exception as a:
        print(a)
# def feladat_14(): #nem jó
#     file=open("fel12.txt",mode="r")
#     a=[]
#     db=0
    # for sor in file:
    #     for i in range(len(sor)):
    #         print(i)
    #         a=sor[i]
    #     for j in range(len(sor)-1,-1,-1):
    #         print(j)
    #         b=sor[j]
    #     for i in range(len(sor)):
    #             if a==b:
    #                 db=db+1
    #     print(db)
    # for sor in file:
    #     for i in range(len(sor)):
    #         for j in range(len(sor) - 1, -1, -1):
    #             if sor[i]==sor[j]:
    #                 a.append(sor[i])
    # print(a)


def feladat_15():
    try:
        file=open("be.txt",mode="r")
        file1=open("ki.txt",mode="w")
        lista=[]

        for sor in file:
            sor=sor.strip()

            if sor!=" ":

                lista.append(sor)
                if sor=="":
                    break
        for x in lista:
            if x=="":
                lista.remove(x)
        a=str(lista)
        file1.write(a)
        file.close()
        file1.close()
    except OSError:
        print("hiba")
    except Exception as a:
        print(a)

def feladat_16():
    try:
        file=cod.open("be.txt",encoding='utf-8',mode="r")
        file1=open("ki.txt",mode="w")
        nagy=True
        for sor in file:
            sor=sor.strip()
            li=sor.split(" ")
            for szo in li:
                if (szo[0].isupper()):
                    nagy=False
                    break
                if nagy:
                    sor = str(sor)
                    file1.write(sor)
                    file1.write("\n")
                    break

                else:
                    nagy=True
        file.close()
        file1.close()
    except FileExistsError:
        print("nem letezik a file!")
    except Exception:
        print("valamilyen kivetelt dobott!")

def feladat_17():
    try:
        file=cod.open("be.txt",encoding='utf-8',mode="r")
        file1=open("ki.txt",mode="w")
        nagy=True
        for sor in file:
            sor=sor.strip()
            li=sor.split(" ")
            for szo in li:
                if (szo[0].islower()):
                    nagy=False
                    break
            if nagy:
                    sor = str(sor)
                    file1.write(sor)
                    file1.write("\n")
                    break
            else:
                    nagy=True
        file.close()
        file1.close()
    except FileExistsError:
        print("nem letezik a file!")
    except Exception:
        print("valamilyen kivetelt dobott!")


def feladat_18():
    try:
        lista=[]
        lista2=[]
        file=open("be.txt",mode="r")
        for sor in file:
            sor=sor.strip()
            lista=sor.split(" ")


            asd=lista[len(lista)-1]
            lista2=asd.split(":")
            lista2[0] = int(lista2[0])
            lista2[1] = int(lista2[1])


            if lista2[0]>lista2[1]:
                print(lista[0])
            else:
                print(lista[2])

        print(lista)
    except OSError:
        print("hiba")
    except Exception as a:
        print(a)


def feladat_19():
    try:
        max=0

        lista=[]
        file=open("be.txt",mode="r")
        for sor in file:
            sor=sor.strip()
            lista=sor.split(" ")
            for i in lista:

                if int(lista[1])>max:
                    max=int(lista[1])
                    p=i
        print(p)
    except OSError:
        print("hiba")
    except Exception as a:
        print(a)







def main():
    print("feladat 1:")
    print(feladat_1(8))

    print("feladat 2:")
    print(feladat_2(10))

    print("feladat 3:")
    print(feladat_3(513))

    print("feladat 4:")
    feladat_4()

    print("feladat 5:")
    feladat_5(10)

    print("feladat 6:")
    print(feladat_6(123,300))

    print("feladat 7:")
    print(feladat_7(11,12))

    print("feladat 8:")
    print(feladat_8(5))

    print("feladat 9:")
    print(feladat_9())

    print("feladat 10:")
    feladat_10()

    print("feladat 11:")
    feladat_11()

    print("feladat 12:")
    print(feladat_12())

    print("feladat 13:")
    feladat_13()


    print("feladat 15:")
    feladat_15()

    print("feladat 16:")
    feladat_16()

    print("feladat 17:")
    feladat_17()

    print("feladat 18:")
    feladat_18()

    print("feladat 19:")
    feladat_19()



if __name__ == '__main__':
    main()