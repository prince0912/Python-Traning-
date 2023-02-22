list=[]
N=int(input("Enter the range of list:"))
for i in range(1,N):
  list.append(i)
print("Max element in list",max(list))
print("Min element in list",min(list))
