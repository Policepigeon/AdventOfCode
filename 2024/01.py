#the first day of coding
list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]
totaldiff = 0
list1 = sorted(list1)
list2 = sorted(list2)
print(list1,list2)
for i in range(1,len(list1)):
  diff = abs(list1[i]-list2[i])
  totaldiff = totaldiff + diff 
  print("diff = ",diff)
  print("tdiff =",totaldiff)
print(totaldiff)