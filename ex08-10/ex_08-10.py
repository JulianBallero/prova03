n=1
def funcao81(n):
    n=n*3
    print(n)
    return(funcao81(n))
##funcao81(n)

m=4
def funcao82(m):
    m=m/2
    print(m)
    return(funcao82(m))
##funcao82(m)

x=1
y=1
z=1
def funcao83(x,y,z):
    if z%2==1:
        x=x+1
        print(str(x)+"a"+"-"+str(y)+"b")

    if z%2==1:
        y=y+1
        print(str(x)+"a"+"-"+str(y)+"b")

    z+=1

    return funcao83(x,y,z)
##funcao83(x,y,z)


q=2
p=0
contarepet=0
def funcao84(p,q,contarepet):
    p=(p -(q*contarepet))
    p=(p +(q*contarepet))
    contarepet= contarepet+1
    print(p)
    return(funcao84(p,q,contarepet))
##funcao84(p,q,contarepet)


soma=0
o=0
def funcao9(o,soma):
    o += 1
    soma=soma+o
    print (soma)
    return(funcao9(o,soma))
##funcao9(o,soma)

bacpor15min=25000
contaminutos=15
total=75000
def funcao10(bacpor15min,total,contaminutos):
    print("minuto"+str(contaminutos)+"="+str(total))
    total=total+ bacpor15min
    contaminutos= contaminutos+15
    return funcao10(bacpor15min,total,contaminutos)
##funcao10(bacpor15min,total,contaminutos)