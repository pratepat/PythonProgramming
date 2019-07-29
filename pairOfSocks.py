# John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# For example, there are  socks with colors . There is one pair of color  and one of color .
# There are three odd socks left, one of each color. The number of pairs is .

def sockMerchant(n, ar):
    ar = sorted(ar)

    i=j=k=0
    for i in range(0,n-1):
        if(ar[i] == ar[i+1]):
            j = j+1 #3
        else:
            j = 0


# Driver
n = 9
ar = [10 ,20 ,20 ,10 ,10 ,30 ,50 ,10 ,20]

print(sockMerchant(n, ar))
