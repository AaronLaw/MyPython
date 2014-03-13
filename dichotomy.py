#coding:utf-8
'''二分法'''

def dichotomy(arr,m,n):
    def findlow(arr,m):
        if arr[0]>m:
            return 0
        low = 0
        high = len(arr)-1
        while low<high:
        	mid = (low+high)/2
        	if arr[mid]>m:
        		high -= 1
        	elif arr[mid]<m:
        		low += 1
        	else:
        		return mid
        return mid+1

    def findhigh(arr,n):
        if arr[-1]<n:
            return len(arr)
        low = 0
        high = len(arr)-1
        while low<high:
            mid = (low+high)/2
            if arr[mid]>n:
                high -= 1
            elif arr[mid]<n:
                low += 1
            else:
                return mid+1
        return mid+1
    return arr[findlow(arr,m):findhigh(arr,n)]


arr = [1,3,5,7,9,11]

print dichotomy(arr,2,7)
print dichotomy(arr,4,9)
print dichotomy(arr,9,15)