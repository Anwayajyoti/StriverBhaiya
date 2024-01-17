def maxLen(self, n, arr):
        #Code here
        sum=0
        length=0
        d={}
        d[0]=-1
        for i in range(n):
            sum+=arr[i]
            if sum in d:
                length=max(length,i-d[sum])
            else:
                d[sum]=i
        return length
