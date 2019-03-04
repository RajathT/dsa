def quick(left,right,l):
    part = sort(left,right,l)
    if left < part-1:
        quick(left,part-1,l)
    if part < right:
        quick(part,right,l)
    return l

def sort(s, e, l):
    pivot = l[(s+e)//2]
    i = s
    j = e
    while i<=j:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        if i<=j:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1
            j -= 1
    return i
    
    
l = [9,8,1,0,7,6,5,4,3,2,1,0,-1]

l = quick(0,len(l)-1,l)
print(l)
        
