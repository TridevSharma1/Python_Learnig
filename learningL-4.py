Info = {
    'name' : 'Tridev Sharma',
    'Age' : 17,
    'Marks' : [20,30,20,19,30],
    'percent' : 98.9,
    'pass' : True
}

Info['name']= 'Tridev'
Info['Gender'] = 'Male'
print(Info)
print(Info['name'],Info['Age'])

Student = {
    'name' :' Tridev Sharma',
    "subject" :{
    'Geo' :  30,
    'Eco' : 20,
    'Hindi' : 20
 }
}

print(Student)

print(Info.keys())
print(Info.values())
print(Info.items())
print(Info.get('name'))
Info.update({"Gender" : "MAle"})

print(Info)
 
#set

Collection = {1,2,2,2,3,3,3,4,4,9,8,4,5}
Hay = set()

print(type(Hay))
print(Collection)

Bio_Data = set()

Bio_Data.add(9)
Bio_Data.add(7)
Bio_Data.add(8)
Bio_Data.add(10)

print(Bio_Data)
Bio_Data.remove(7)

print(Bio_Data)
print(Bio_Data.pop())

#set union

print(Collection.union(Bio_Data))
print(Collection.intersection(Bio_Data))

print(Collection.difference(Bio_Data))
print(Bio_Data.symmetric_difference(Collection))
print(Collection.issubset(Bio_Data))
print(Bio_Data.issuperset(Collection))
