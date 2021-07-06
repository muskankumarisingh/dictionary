values=["eight","one","six","seven","two"]
key=[8,1,7,6,2]
d={}
i=0
attempt=0
for i in range(0,len(key)):
    for j in range(0,len(key)):
        if key[i]<key[j]:
            attempt=key[j]
            key[j]=key[i]
            key[i]=attempt
a=dict(zip(key,values))
print(a)
        
