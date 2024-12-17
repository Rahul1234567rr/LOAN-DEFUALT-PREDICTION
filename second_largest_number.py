arr=[2,5,6,7,1]
sl=0
l=0
for i in range(len(arr)):
    if arr[i]>l:
        l=arr[i]

for i in range(len(arr)):
    if arr[i]>sl and arr[i]!=l:
        sl=arr[i]
print(sl)
        
