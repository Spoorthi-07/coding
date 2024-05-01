
secret_num=33
condition=True
while(condition):
    n=int(input())
    if(n==secret_num):
        print("Congratulations you guessed it right")
        condition=False
    elif(n>secret_num):
        print("Number is too large")
    elif(n<secret_num and n>0):
        print("Number too small")
    elif(n<=0):
        condition=False
        print("Quit the game")
		