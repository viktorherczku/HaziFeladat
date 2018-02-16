import codecs as cod
def fibo1(n):
    a=1
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        c=a+b
        print(a,b,c)
        k=3
        while k<n:
            a=b
            b=c
            c=a+b
            print(c)
            k+=1

def fibo2(n):
    a=1
    b=1
    k=1
    fajl=open("ki1.txt",mode="w")
    while k<n:
        #print("%.4f" % (a/b))
        fajl.write("%.4f " % (a/b))
        a=a+b
        b=a-b
        k=k+1
    fajl.close()

def feladat1(fajl_nev):
    #fajl=open(fajl_nev,mode="r")
    fajl = cod.open(fajl_nev,encoding='utf-8', mode="r")
    max=0
    max_sor=""
    for sor in fajl:
        sor=sor.strip()
        if(sor[0].isupper() and len(sor.strip())>max):
            max=len(sor)
            max_sor=sor
    print(max,max_sor)
    fajl.close()

def feladat2():
    fajl=open("be1.txt",mode="r")
    for sor in fajl:
        if("   " in sor):
            fajl=open("ki1.txt",mode="w")
            fajl.write(sor)
            fajl.close()
            break

def fel7(lista,betu):
    li=[]
    fajl=open("ki2.txt",mode="w")
    for i in lista:
        if i[0]==betu:
            li.append(i)
    fajl.write(str(li))
    fajl.close()



#def valtozonelkulicsere(a,b):
    #ez csak pythonban mukodik
    #print(a,b)
    #a,b=b,a
    #print(a,b)

def main():
    #fibo1(10)
    #valtozonelkulicsere(5,3)
    #a=10
    #b=-7
    #a=a+b
    #b=a-b
    #a=a-b
    #print(a,b)
    #fibo2(10)
    #feladat1("be1.txt")
    #feladat2()
    fel7(["alma","ananasz","narancs"],'a')
if __name__ == '__main__':
    main()