# sorting algorithms:
# bubbule
# selection

# insertion sort:
l=[4,3,2,10,12,1,5,6,8] 

for i in range(1,len(l)):
    k=l[i]
    j=i-1
    while j>=0 and k<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=k
print("After completion of Insertion Sort:",l)

