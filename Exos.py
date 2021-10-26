#Itératif
#Exo 2

def factiterative(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    return fact


#Exo3

def tableau0(n):
    liste=[]
    for i in range(1,n+1):
        liste.append(0)
    tableau=liste*n
    return(tableau)


#Exo 5

def moyenne(L) :
    somme=0
    for i in L :
        somme+=i
    moy=somme/len(L)
    return moy


#Exo 6

def contient(liste1,n):
    for i in liste1:
        if i==n:
            return (True)
    return (False)


#Exo 9

def fusionListes(liste2,liste3):
    i=0
    res=[]
    while not liste2==[] and not liste3==[]:
        if liste2[i]<liste3[i]:
            res.append(liste2[i])
            del liste2[i]
        elif liste2[i]>liste3[i] :
            res.append(liste3[i])
            del liste3[i]
        else :
            res.append(liste2[i])
            res.append(liste3[i])
            del liste2[i]
            del liste3[i]
    if liste2==[]:
        res.extend(liste3)
    else :
        res.extend(liste2)
    return(res)



#Récursif
#Exo2

def rechMax(liste4):
    res=liste4[0]
    if len(liste4) > 1:
        max=rechMax(liste4[1:])
        if res>max:
            return res
        else : 
            return max
    else:
        return liste4[0]

print(rechMax([7,5,9,4]))