f=open('data.txt','r')      #by default file open in read mode  
# r for read and w for write

#print(f.readline()) #file ki first line read ho jae gi
#print(f.readline()) #file ki second line read ho jae gi
#print(f.readline())  #file ki third line read ho jae gi

# or use for loop instead of using   
for opening in f:
    print(opening)

f.close()  #make sure to close the file


