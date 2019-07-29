def mergeSort(arr):
    #Split
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        #set index to 0
        i=j=k=0

        #Compare
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] =  lefthalf[i]
                i = i+1
            else:
                arr[k] = righthalf[j]
                j=j+1

            k=k+1

        # Assign the rest of array
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k] = righthalf[j]
            j=j+1
            k=k+1

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)
