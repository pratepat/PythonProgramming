# John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# For example, there are  socks with colors . There is one pair of color  and one of color .
# There are three odd socks left, one of each color. The number of pairs is .

def sockMerchant(n, ar):
    ar = sorted(ar)
    print(ar)
    i=j=k=0
    num = ar[i]
    while(i<n-1):
        if(ar[i] == ar[i+1]):
            j = j + 1
            #print('i = '+str(i) +' ar1 = ' +str(ar[i]) +' ar2 = '+str(ar[i+1]) +' j = '+str(j))
            i = i + 2
        else:
            i = i + 1
    return j
# TC 1
n = 9
ar = [10 ,20 ,20 ,10 ,10 ,30 ,50 ,10 ,20]
print(sockMerchant(n, ar))
#3

# TC 2
n = 10
ar = [1 ,1 ,3 ,1 ,2 ,1 ,3 ,3 ,3 ,3]
print(sockMerchant(n, ar))
#4

# TC 3
n = 15
ar = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
print(sockMerchant(n, ar))
#6
