str=input("enter the string")
dic={}
for x in str:
    if x in dic:
        dic[x]=dic[x]+1
    else:
        dic[x]=1
for key in dic:
    print(key,":",dic[key])