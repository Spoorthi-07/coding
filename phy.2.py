
condition=True
while(condition):
    full_name=input()
    for each_char in full_name:
        if(each_char==' '):
            condition=False
last_index=full_name.index(' ')
first_name=full_name[:last_index]

condition=True
digit=False
upper_letter=False
while(condition):
    password=input()
    len_password=len(password)
    for each_char in password:
        if(each_char.isdigit()):
            digit=True
            break
    for each_char in password:
        if(each_char.isupper()):
            upper_letter=True
            break
    if(len_password>=8 and digit==1 and upper_letter==1):
        print("first_name is: ", first_name)
        condition=False
