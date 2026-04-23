# 12 multiple

start = int(input("Number : "))
end = int(input("Number : "))

for i in range(start,end+1):
    print(" ")
    print(f"Formula : {i}")
    for j in range(1,13):
        print(f"{i} x {j} = {i*j}")