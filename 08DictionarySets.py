#========================DICTIONARY=======================

marks = {
    "harry": 100,
    "kksingh": 99,
    "mukesh": 91
}
# print(marks, type(marks))
# print(marks["harry"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"kksingh": 100})
print(marks)


# ===================SETS=========================
d = {}                #empty dictionary
s = {1, 2, 3, 4, 5}   #its a set with values
e = set()             #its an example of empty set

#SET DOES NOT CONTAINS DUPLICATE VALUES AND YE UNORDERED HOTA HAI AND DOES NOT HAVE INDEX
#====================SETS METHODS===================

set1 = {2, 3, 4, 5}
set2 = {4, 5,2, 9,8}
print(set1.union(set2))
print(set1.intersection(set2))

