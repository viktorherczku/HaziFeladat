import math as m
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

def main():
    print("feladat 1:")
    print(feladat_1(8))

    print("feladat 2:")
    print(feladat_2(10))

    print("feladat 4:")
    feladat_4()

    print("feladat 6:")
    print(feladat_6(123,300))


if __name__ == '__main__':
    main()