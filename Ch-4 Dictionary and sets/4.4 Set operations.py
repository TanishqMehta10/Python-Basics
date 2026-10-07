# 1. add() - adds an element to the set
s1 = {1, 2, 3, 4}
s1.add(5)
print(s1)

# 2. remove() - removes an element from the set
s1 = {1, 2, 3, 4, 5}
s1.remove(3)
print(s1)

# 3. discard() - removes an element if it exists
s1 = {1, 2, 3, 4, 5}
s1.discard(3)
print(s1)
# remove() gives an error if the element doesn't exist, while discard() does nothing without giving an error.

# 4. union() - combines two sets
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}

print(s1.union(s2))

# 5. intersection() - finds common elements between two sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.intersection(s2))

# 6. difference() - finds elements present in first set but not in second set
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.difference(s2))
print(s2.difference(s1))

# 7. symmetric_difference() - finds elements that are not common between two sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.symmetric_difference(s2))

# 8. copy() - creates a copy of the set
s1 = {1, 2, 3, 4}
s2 = s1.copy()

print(s2)

# 9. clear() - removes all elements from the set
s1 = {1, 2, 3, 4}
s1.clear()
print(s1)

# 10. issubset() - checks whether one set is a subset of another set
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}

print(s1.issubset(s2))

# 11. issuperset() - checks whether one set contains another set
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
print(s1.issuperset(s2))

# 12. isdisjoint() - checks whether two sets have no common elements
s1 = {1, 2, 3}
s2 = {4, 5, 6}

print(s1.isdisjoint(s2))