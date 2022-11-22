
import random

#Question 1
print("Question 1")

myTable = []

for i in range(0, 5):
    myTable.append(random.randint(0,20))


print(myTable)

stockage = myTable[0]
myTable[0] = myTable[len(myTable)-1]
myTable[len(myTable)-1] = stockage

print(myTable)


#Question 2
print("Question 2")

myTable = []

for i in range(0, 5):
    myTable.append(random.randint(0,20))


print(myTable)

for i in range (0, len(myTable)-1):
    if(myTable[i] > myTable[i+1]):
        stockage = myTable[i]
        myTable[i] = myTable[i+1]
        myTable[i+1] = stockage

print(myTable)


#Question 3
print("Question 3")

myTable = []

for i in range(0, 10):
    myTable.append(random.randint(0,20))


print(myTable)

triage = False
while(not triage):
    triage = True
    for i in range (0, len(myTable)-1):
        if(myTable[i] > myTable[i+1]):
            stockage = myTable[i]
            myTable[i] = myTable[i+1]
            myTable[i+1] = stockage
            triage = False

print("tri à bulle terminé!")
print(myTable)


#Question 4
# Le tri à bulles est très lent car si il est en train de remonter la plus grande valeur du tableau par exemple, il ne fera remonter que celle ci pendant une itération entière
# ce qui va demander de faire beaucoup plus d'itérations qu'un autre style de tri. 
# Pour ce qui est de son ordre de grandeur, on peut estimer que dans un tableau de 100 valeurs, 80 ne seront pas à la bonne place, et donc la machine devra 
# effectuer au moins une quarantaine d'itérations. 


