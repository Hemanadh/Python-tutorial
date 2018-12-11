#working with lists
a=[45,78,34,56,12]

print(len(a))
print(min(a))
print(max(a))
print(sum(a))

#indexing
print(a[0])
print(a[-1])

#slicing

print(a[1:3])
print(sum(a[1:3]))
print(sum(a[-2:]))

# methods
print(a)
a.append(1000)      #add to the list
print(a)
a.insert(2,120)     # insert 120 in position 2
print(a)

a.remove(78)        # remove value
print(a)
a.pop()             # pop all index
print(a)


a.sort()
print(a)
a.reverse()
print(a)

print(a.count(12))  # occurance
print(a.index(12))  # index of the value










