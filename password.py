
#print(True and False)
#print(True and False)
password=input()
alpha_count=0
special_count=0
numeric_count=0
for each_char in password:
    if((each_char>='A' and each_char<='Z') or (each_char>='a' and each_char<='z')):
        alpha_count=alpha_count+1
    elif(each_char>='0' and each_char<='9'):
        numeric_count=numeric_count+1
    else:
        special_count=special_count+1
if(alpha_count==5 and numeric_count==3 and special_count==1):
    print("password valid")
else:
    print("password invaid")