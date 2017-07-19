import csv



fp = open('number.csv')
a = csv.reader(fp)
list2 = []
list3 = []
for row in a:
    list = row
for i in range(0,len(list)):
    if list[i] == '' and i%2!=0:
        list[i] = i
for i in range (0,len(list)) :
    if list[i] == '':
        list2.append(i)
    if list [i]!='':
       list3.append(list [i])



fp = open('fruits.csv')
a = csv.reader(fp)
fruit2 = []
for row in a:
    fruit = row
for i in range(0,len(fruit)):
    if i not in list2:
        fruit2.append(fruit[i])
for i in range (0,len(fruit2)):
    if fruit2[i]=='' :
        fruit2[i] = fruit2[i-10]



fp = open('rotten.csv')
a = csv.reader(fp)
rotten2 = []
rotten3 = []
for row in a:
    rotten = row
for i in range(0,len(rotten)):
    if rotten[i]=='1':
        rotten[i]='t'
    elif rotten[i]== '0':
        rotten[i]='f'
    if i not in list2:
        rotten2.append(rotten[i])
for i in range(0,len(rotten2)):
    if rotten2[i]=='t':
        rotten3.append(i)



fp = open('price.csv')
a = csv.reader(fp)
price2 = []
for row in a:
    price = row
for i in range(0,len(price)):
    if price[i]!='':
        price[i]=float(price[i])
    if i not in list2:
        price2.append(price[i])
for i in range(0,len(price2)):
    if i in rotten3:
        price2[i]='0.0'
    # if the id is present ,price is not given and fruit is not rotten then -1.0 value is given to it.
    if price2[i]=='':
        price2[i]='-1.0'



fp = open("Data.csv","wb")
fieldnames = ["Id","Name","Price","Rotten"]
write = csv.DictWriter(fp,fieldnames=fieldnames)
for i in range (0, len(list3)):
    write.writerow({"Id":list3[i],"Name":fruit2[i],"Price":price2[i],"Rotten":rotten2[i]})
fp.close()


