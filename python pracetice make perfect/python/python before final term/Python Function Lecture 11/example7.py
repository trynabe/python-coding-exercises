def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"
print(speak())
print(speak("pig"))
print(speak("duck"))
print(speak("cat"))
print(speak("lion"))