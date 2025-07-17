#  sets are unordered, mutable, no duplications
# create set in two ways
set1 = {1, 2, 3, 4}
# or 
set2 = set()
# or create from iterable, 
set4 = set([1, 2, 4, 5, 6, 7, 8, 9, 0])
setNAME = set("Thread Miller")

print(type(set1))
print(type(set2))

# set operations
set1.add(5)
set2.clear() # removes all item from the set
set1.pop() # set works with FIFO
print(set1)

prime = {1, 2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}

# intersections, union
print(prime.intersection(odds))
print(prime.union(evens))
print(prime.difference(odds))
print(prime.symmetric_difference(evens)) #return a new set excluding elements that are not common to both

# updates
prime.intersection_update(evens) # this will update set prime with only the elements common to both sets
print(prime)


# Super and Sub Sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
setB = {1, 3, 5, 7, 9}

print(setA.issuperset(setB)) #if setA contains element if set B
print(setB.issubset(setA)) # if element of B are found in A
print(setA.isdisjoint(setB)) #if there is no intersection btw both sets

# copying sets
setI = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
setJ = {1, 3, 5, 7, 9}

setY = setI # these points to the same place in memory, i.e if Y is modified, I is also modified

# the proper way to copy os 
setK =setI.copy() # not K is not the same as I

# frozen sets are immutable
setF = frozenset([1, 2, 3, 4])
#  we cannot add or remove from the above set