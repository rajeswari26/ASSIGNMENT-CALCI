#APPEND 
basket = [1,3,4,2,5,6]
print("append function!!")
print(basket)
basket.append(40)
new_basket = basket
print(new_basket)

#CLEAR
print("clear function!!")
print(basket)
basket.clear()
print(basket)

#COPY
bucket = ['apple','orange','mango','kiwi','lichi']
print("copy function!!")
print(bucket)
bucket.copy()
print(bucket)

#COUNT
bag =['book','pen','pencil','bottle','file','lunch','pen']
print("count function!!")
x=bag.count('pen')
print(x)

#EXTEND
print("extend function!!")
bag =['book','pen','pencil','bottle','file','lunch','pen']
extra =(1,2,3,4)
bag.extend(extra)
print(bag)

#INDEX
print("index function!!")
print(bag.index('bottle'))

#INSERT 
print("insert function!!")
bag =['book','pen','pencil','bottle','file','lunch','pen']
bag.insert(2,'chalk')
print(bag)

#POP 
print("pop function!!")
bag =['book','pen','pencil','bottle','file','lunch','pen']
bag.pop()
print(bag)

#REMOVE
print("remove function!!")
bag =['book','pen','pencil','bottle','file','lunch','pen']
bag.remove('pen')
print(bag)

#REVERSE
print("reverse function!!")
bag =['book','pen','pencil','bottle','file','lunch','pen']
bag.reverse()
print(bag)

#SORT
print("sort function!!")
bag =['book','pen','pencil','bottle','file','lunch','pen']
bag.sort()
print(bag)
