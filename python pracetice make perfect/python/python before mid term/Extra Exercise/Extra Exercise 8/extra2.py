number = int(input())

for i in range(2,number+1,2):
    a = 1500*(1+(0.04/i))**(i*5)
    print(i,a)
