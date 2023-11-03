E = set(map(int,input().split(",")))
N = set(map(int,input().split(",")))

union_set = E.union(N)
print("Union:", union_set)

intersection_set = E.intersection(N)
print("Intersection:", intersection_set)


difference_set = E.difference(N)
print("E - N:", difference_set)

symm_diff_set = E.symmetric_difference(N)
print("Symmetric Difference:", symm_diff_set)





