def caesarCipher(s, k):
    # Write your code here
    res=[]
    for i in s:
        res.append(ord(i))
    for i in range(len(res)):
        if 65<=res[i]<=90:
            res[i]=(65+(res[i]-65+k)%26)
        elif 97<=res[i]<=122:
            res[i]=(97+(res[i]-97+k)%26)
    return (''.join(map(chr,res)))
        
