nums = [100,4,200,1,3,2]
longest=0
numsSet=set(nums) #SET to check if left number is preent
for i in nums:
    #To check if i is the first number or starting number
    if (i-1) not in numsSet:
        length=0
        while i+length in numsSet:
            length+=1
        longest=max(length,longest)
print(longest)
        
