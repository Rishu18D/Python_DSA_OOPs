def abc(str1,str2):
    a=len(str1)
    b=len(str2)
    result=""
    if str1==str2:
        result=str1
    else:
        for i in range(0,a):
            for j in range(0,b):
                if str1[i]==str2[j]:
                    result+=str1
        return result
str1="Rishu"
str2="Singh"
result=abc(str1,str2)
print(result)
