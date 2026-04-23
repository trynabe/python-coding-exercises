temps_c = [0,20,37,100]
temps_f = list(map(lambda x: (x * 9/5) + 32, temps_c))
print(temps_f)

temps_c = [0,20,37,100]
def analyze_weather(temps_c):
    print(f"highest : {max(temps_c)}")
    print(f"lowest : {min(temps_c)}")
    print(f"average : {sum(temps_c)/len(temps_c)}")
    print(f"biggest : {max(temps_c, key=abs)}")
analyze_weather(temps_c)