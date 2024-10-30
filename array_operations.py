arr=[1,10,15,19,10,32,27,7,11]
arr.index(15)               #Returns the index of the first occurrence of x in the list
arr.count(10)               #Returns the number of times x appears in the list
arr.sort()                  #Sorts the list in ascending order by default (or descending if reverse=True)
arr.reverse()               #Reverses the elements in place.
b=len(arr)                  #Returns number of elements in array
c=sum(arr)                  #Returns sum of elements in array
d=min(arr)                  #Returns minimum element in array
e=max(arr)                  #returns maximum element in array
arrt = [1, 2, 3]
squares = [x**2 for x in arrt]  # [1, 4, 9]

#Here’s an overview of these methods:
#Add: append(), insert(), extend()
#Remove: pop(), remove(), clear()
#Search: index(), count()
#Sort & Reverse: sort(), reverse()
#Copy: copy()
#Utilities: len(), sum(), min(), max()
