arr1=[1,2,3,4,5,6,7]
k1=3
#OUTPUT: [5, 6, 7, 1, 2, 3, 4]
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]

arr2=[-1,-100,3,99]
k2=2

def rotateArr(nums,k):
    for i in range(k):
        a=nums.pop()
        nums.insert(0,a)
    return nums

print(rotateArr(arr1,k1))
print(rotateArr(arr2,k2))

#NOTES:
# create a list of vowels
#vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3 (4th position)
#vowel.insert(3, 'o')