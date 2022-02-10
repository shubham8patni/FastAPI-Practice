li = [9,6,2,4,3,1,5,8,7]

#save list to new variable after sorting
s_li = sorted(li)
print(s_li)

#sorting the list within itself, original list sorted
li.sort()
print(li)

#descending order 
s_li = sorted(li, reverse=True)
li.sort(reverse=True )