d={"1":["a","b"],"2":["c","d"]}
list1=d.get("1")
list2=d.get("2")
for i in range(2):
    for j in range(2):
        print(list1[i]+list2[j])

#second method using while loop
# d={"1":["a","b"],"2":["c","d"]}
# i=0
# while i<len(list1):
#     j=0
#     while j<len(list2):
#         new=list1[i]+list2[j]
#         print(new)
#         j=j+1
#     i=i+1