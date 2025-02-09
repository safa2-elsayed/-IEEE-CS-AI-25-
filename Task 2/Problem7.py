def common_elements(set1, set2):
    return set1.intersection(set2)  


set1 = set(map(int, input("Enter The Elements of The First Set : ").split()))
set2 = set(map(int, input("Enter The Elements of The Second  Set : ").split()))

result = common_elements(set1, set2)
print("The Common Elements : ", result)
