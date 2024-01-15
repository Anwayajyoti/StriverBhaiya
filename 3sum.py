# Approach

# Sort the given array in non-decreasing order.
# Loop through the array from index 0 to n-1.
# For each iteration, set the target as -nums[i].
# Set two pointers, j=i+1 and k=n-1.
# While j<k, check if nums[j]+nums[k]==target.
# If yes, add the triplet {nums[i], nums[j], nums[k]} to the result and move j to the right and k to the left.
# If no, move either j or k based on the comparison of nums[j]+num[k] with target.
# To avoid duplicate triplets, use set and then change it to list
                    
nums=[-1,0,1,2,-1,-4]
nums.sort()
hash=set()
for i in range(len(nums)):
    target=-1*nums[i]
    j=i+1
    k=len(nums)-1
    while j<k:
        if nums[j]+nums[k]<target:
            j+=1
        elif nums[j]+nums[k]>target:
            k-=1
        elif nums[j]+nums[k]==target:
            hash.add((nums[i],nums[j],nums[k]))
            j+=1
            k-=1
print(hash)

