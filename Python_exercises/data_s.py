"""Given a two list. Create a third list by picking an odd-index 
 element from the first list and even index elements from second"""

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
list3 = list()

odd=listOne[1::2]
even=listTwo[0::2]
list3.extend(odd)
list3.extend(even)

print(list3)










