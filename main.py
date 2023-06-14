from datetime import datetime

# Linearni kongruentni metod
# Nk = a*Nk-1 + b  mod c
a = 3124325343
b = 5075434327
c = 2^24


def LKM(k: int):
    if k < 1: return 0
    N = 0.67542
    for i in range(0, k):
        N = (a * N + b) % c
    #print(N/c)
    return N/c

#dodatak za vecu nasumicnost
rand = 0

#naci jednu promenljivu
def findX(rand: int):
    return LKM(datetime.now().microsecond+rand)

#da li je sabiranje vece od 1
def isGT1(rand: int):
    x1 = findX(rand)
    x2 = findX(rand)
    result = pow(x1,2) + pow(x2,2)
    if result > 1:
        return 1
        #print(1, "(" + str(x1) + ")^2 + (" + str(x2) + ")^2 = ", result)
    return 0
    #else: print(0, "(" + str(x1) + ")^2 + (" + str(x2) + ")^2 = ", result)

#MAIN
#spisak n-ova
nlst = []
print("(Uneti 0 za kraj unosa)")
while(1):
    n = int(input("Uneti n: "))
    if n <= 0: break
    nlst.append(n)
if nlst.__len__() == 0: exit()

for i in nlst:
    #novo racunanje
    Pn = 0
    for j in range(0,i):
        rand += 1
        Pn += isGT1(rand)
    print("Rezultat za "+str(i)+" sabiranja:", Pn/i)
#END OF MAIN