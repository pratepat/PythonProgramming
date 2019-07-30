def repeatedString(s, n):

    i = num_a = num_rest = tot = 0
    reps = 0

    while(i<len(s)):
        if(s[i] == 'a'):
            num_a = num_a + 1
        else:
            num_rest = num_rest + 1
        i = i + 1

    tot = num_a + num_rest
    #print('num_a = '+str(num_a)+' num_rest = '+str(num_rest)+' tot = '+str(tot))

    num_a = num_a * (n // tot)
    #print('num_a = '+str(num_a)+' '+str(n % tot))

    i = 0
    while(i < (n % tot)):
        if(s[i] == 'a'):
            num_a = num_a + 1
        i = i + 1
    #print('num_a = '+str(num_a))

    return num_a

# TC1
s1 = 'aba'
n1 = 10
print(repeatedString(s1,n1))

# TC2
s2 = 'a'
n2 = 1000000000000
print(repeatedString(s2,n2))

# TC3
s3 = 'abcac'
n3 = 10
print(repeatedString(s3,n3))
