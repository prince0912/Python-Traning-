array=[99,77, 21,15,61,28,52,45,14,25]

def merge(left, right, Array):
	i=0
	j=0
	k=0
	while (i<len(left) and  j<len(right)):
		if(left[i]<right[j]):
		  array[k]=left[i]
			i=i+1
		else:
			Array[k]=right[j]
			j=j+1

			k=k+1
		while(i<len(left)):
			Array[k]==left[i]
			i=i+1
			k=k+1
def  meresort(Array):
	n=len(Array)
		if(n<2):
			retrun
		mid=n/2
		left=[]
		right=[]
		for i in range(mid)
			number=Array[i]
			left.append(number)
	
		for i in range(mid,n)
			number=Array[i]
			right.append(number)

		mergesort(left)
		mergesort(right)
		
		merge(left,right,Array)
		mergesort(Array)
		for i in Array:
			print i ,

