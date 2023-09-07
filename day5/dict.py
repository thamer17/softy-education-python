fruit = {
    "name": "Orange", 
    "weight": "3 Kg", 
    "rate": 5
    } #pair
print(fruit)
print("The fruit name is ", fruit["name"], ".")
print("The fruit weight is ", fruit["weight"], ".")
print("The fruit rate is ", fruit["rate"], ".")
print("The size of the fruit: ", len(fruit))
fruit["name"] = "Apple"
fruit["quality"] = "Good"
# delete
del fruit["rate"]
#fruit.clear()# empty the dictionnary
fruit.pop("name")
fruit.update({"rate": "5", "price": "5 Dt"})
fruit.update({"weight": "5 Kg"})
print("All keys! ", fruit.keys())
print("All values! ", fruit.values())
print(fruit.get("quality"))
