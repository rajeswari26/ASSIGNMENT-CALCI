#clear()	
student_1= {
     'name':'kimtae',
     'age':24,
     'phone number':9846583392,
     'email-id':'kimtae12@bts.com',
     }
student_1.clear()
print(student_1)


#copy()
student_1= {
     'name':'kimtae',
     'age':24,
     'phone number':9846583392,
     'email-id':'kimtae12@bts.com',
     }
student_2=student_1.copy()
print(student_2)


#fromkeys()
y=student_1.fromkeys('age',24)
print(y)


#get()
y=student_1.get("email-id")
print(y)


#items()
y=student_1.items()
print(y)


#keys()	
y=student_1.keys()
print(y)


#pop()
y=student_1.pop('age')
print(y)	


#popitem()
y=student_1.popitem()
print(y)


#setdefault(	)
y=student_1.setdefault('age',26)
print(y)


#update()	
y=student_1.update({'hobby':'singer'})
print(student_1)


#values()
y=student_1.values()
print(y)
