day = 7

list_n = []
for i in range(day):
    temperature = int(input(f"Day {i+1} Temperature : "))
    list_n.append(temperature)

average = 0
average = sum(list_n) / day

print(f"Average = {average:.2f}")
# INPUT
#    30 32 31 29 28 33 35 
# OUTPUT
#    Average = 31.14
