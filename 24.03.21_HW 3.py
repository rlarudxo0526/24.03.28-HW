## 1-11 ##
inStr, outStr = "파이썬###COOKBOOK$$$@@@열공중1234", ""

for i in range(0, len(inStr)) :
    if inStr[i].isalpha() == True :
        outStr += inStr[i]

print("한글/영문자만 남김 --> %s" %outStr)
