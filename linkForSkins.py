def mergeSort(arry):
	if len(arry) <= 1:
		return arry
	left_hand , right_hand = splitter(arry)
	left = mergeSort(left_hand)
	right = mergeSort(right_hand)
	return merge(left,right)
def splitter(arry):
	mid = len(arry)//2
	left_value = arry[:mid]
	right_value = arry[mid:]
	return left_value,right_value
def merge(leftend,rightend):
	lis = []
	i = 0
	j = 0 
	while i < len(leftend) and j < len(rightend):
		if leftend[i] > rightend[j]:
			lis.append(rightend[j])
			j+= 1
		else:
			lis.append(leftend[i])
			i += 1
	while i < len(leftend):
		lis.append(leftend[i])
		i += 1
	while j < len(rightend):
		lis.append(rightend[j])
		j += 1
	return lis

hy = [9,8,7,6,5,4,3,2,1]
print(mergeSort(hy))

