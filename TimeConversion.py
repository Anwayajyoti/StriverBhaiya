s1='12:00:00AM'
s2='01:00:00AM'
s3='12:00:00PM'
s4='11:59:59PM'
def timeConversion(s):
    if s[-2:]=='AM' and s[:2]=='12':
        return('00'+s[2:-2])
    elif s[-2:]=='AM':
        return(s[0:-2])
    elif s[-2:]=='PM' and s[:2]=='12':
        return('12'+s[2:-2])
    else:
        return(str(12+int(s[:2]))+s[2:-2])
print(timeConversion(s1))
print(timeConversion(s2))
print(timeConversion(s3))
print(timeConversion(s4))


