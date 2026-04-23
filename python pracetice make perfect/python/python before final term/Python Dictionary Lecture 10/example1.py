donations = dict(sam=25.0,
lena=88.99,
chuck=13.0,
linus=99.5,
stan=150.0,
lisa=50.25,
harrison=10.0)

min_value = min(donations.values())
max_value = max(donations.values())
print("minvalue : "+str(min_value))
print("maxvalue : "+str(max_value))

for key,value in donations.items():
    if value == min_value:
        print("name (min) : "+ key)
    if value == max_value:
        print("name (max) : "+ key)