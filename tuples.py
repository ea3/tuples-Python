t = (1,2,3)
mylist = [1,2,3]
print(type(t))
print(type(mylist))
print(len(t))
print(len(mylist))   # length
t = ('one', 2, 3)
print(t[0])
print(t[-1])
t = ('a', 'a', 'b')
print(t.count('a'))   # count items
print(t.index('a'))   # locations. 
print(t)
mylist[0] = 'NEW ITEM'
print(mylist)
#t[0] = 'NEW ITEM'     Can't reassign.
print(t)