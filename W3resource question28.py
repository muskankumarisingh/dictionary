num={"n1":[2,3,1],"n2":[5,1,2],"n3":[3,2,4]}
for keys,values in num.items():
    sorted_num={keys,sorted(values)}
print(sorted_num)