name = input("Name: ")
age = int(input("Age: "))
major = input("Major: ")
def show_info(**kwargs):
    print(f"name: {kwargs["name"]} | age: {kwargs["age"]} | major: {kwargs["major"]}")
show_info(name=name, age=age, major=major)