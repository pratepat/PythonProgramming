# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps.
# For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:
#
# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
#
# For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high.
# Finally, he returns to sea level and ends his hike.

def countingValleys(n, s):
    level = valleys = 0
    v = False
    up = dwn = 0
    for i in range(0, n):
        #print(s[i])
        if(s[i] == 'U'):
            level = level + 1
            up = up + 1
        else:
            level = level - 1
            dwn = dwn + 1
            if(dwn > up):
                v = True

        #print(str(up) +' ' +str(dwn) +' '+str(v)+' '+str(valleys)+' '+str(level))
        if(level == 0 and v == True):
            valleys = valleys + 1
            v = False

    return valleys

# TC1
n = 8
s = 'UDDDUDUU'
print(countingValleys(n, s))
#1

#TC2
n = 8
s = 'DDUUUUDD'
print(countingValleys(n, s))
#1

#TC3
n = 16
s = 'DDUUUUDDUDDDUDUU'
print(countingValleys(n, s))
#2
