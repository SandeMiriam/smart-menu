from ast import While


food=("Burger","Drink","Fries","Apple Pie")
prices=[5,1,3,2]

myorderFood=[]
myorderCost=[]

print("Welcome to Miss Oyuga's Hotel.")


order = input("Can I take your order?")
if order=="No":
  exit()
else:
    print("Thank You")

nextOrder=True

While 

nextOrder == True

foodOrder = input("Please enter item")
if foodOrder == "Burger":
    myorderFood.append(food[0])
    myorderCost.append(prices[0])

elif foodOrder=="Drink":
    myorderFood.append(food[1])
    myorderCost.append(prices[1])

elif foodOrder =="Fries":
    myorderFood.append(food[2])
    myorderCost.append(prices[2])

elif foodOrder=="Apple":
    myorderFood.append(food[3])
    myorderCost.append(prices[3])

else:
    print("Not on menu")
    print(myorderFood)
    print(myorderCost)