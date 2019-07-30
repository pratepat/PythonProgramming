3//2
3%2
4//2
4%3

def jumpingOnClouds(c):
    n = len(c)
    cnt = jump = 0
    for i in range(0, n):
        if(c[i] == 0):
            cnt = cnt + 1
        else:
            #print('cnt = '+str(cnt))
            if(cnt%3 == 0 or cnt%2 == 0):
                jump =  jump + cnt//2
                cnt = 2
            elif(cnt == 1):
                cnt = cnt + 1
            #print('jump = '+str(jump))
    #print('cnt last = '+str(cnt))
    jump = jump + cnt//2
    return jump

#TC1
n = 6
c1 = [0, 0, 0, 0, 1, 0]
print(jumpingOnClouds(c1))

n = 7
c2 = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(c2))


n = 6
c3 = [0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c3))


c4 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
print(jumpingOnClouds(c4))
