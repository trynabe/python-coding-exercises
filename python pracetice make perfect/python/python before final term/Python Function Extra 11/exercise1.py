# เขียนฟังก์ชัน say_hello()
# เพื่อพิมพ์ข้อความ "Hello World" และเรียกใช้ 3 คร้ัง
number = int(input())
word = input()

def say_word_multiple_times(number, word):
    for _ in range(number):
        print(f"Say : {word}")

say_word_multiple_times(number, word)