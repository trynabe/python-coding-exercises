[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MbzXfX7P)
## Print Email with the Count

จงเขียนโปรแกรมที่สร้าง dictionary ชื่อว่า `mail_dict` โดยโปรแกรมจะรับ **ตัวเลขจำนวนเต็ม**  `n` ซึ่งเป็นจำนวนข้อมูลหรือ key-value pairs ใน `mail_dict`
และจะวน **loop** เพื่อรับข้อมูลแต่ละรายการ ดัังนี้
1) email ซึ่งจะเป็น `key` ใน dictionary `mail_dict`
2) จำนวนข้อความที่ถูกส่งโดย email นั้น ซึ่งจะถูกใช้เป็น `value` ใน dictionary `mail_dict`

จากนั้นโปรแกรมจะคำนวณและแสดงผลลัพธ์ดังต่อไปนี้
* แสดงเฉพาะชื่อ email ที่มีจำนวนข้อความเป็นเลขคู่
* ถ้าไม่มี email ที่มีจำนวนข้อความเป็นเลขคู่ ให้แสดงข้อความว่า `'Not Found'`

**ตัวอย่างที่ 1:**
**Input:** `n = 5`  
```
5
helloworld@gmail.com
3
nadach@gmail.com
2
yaya@gmail.com
4
mark@gmail.com
1
khimberry@gmail.com
6
```
**Expected output:** โปรแกรมจะแสดงค่า email ที่มีจำนวนข้อความเป็นเลขคู่ใน dictionary ดังต่อไปนี้
```
nadach@gmail.com
yaya@gmail.com
khimberry@gmail.com
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n = 3`  
```
3
jame@gmail.com
1
mint@gmail.com
1
top@gmail.com
8
```
**Expected output:** โปรแกรมจะแสดงค่า email ที่มีจำนวนข้อความเป็นเลขคู่ใน dictionary ดังต่อไปนี้
```
top@gmail.com
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `n = 2`  
```
2
mark@gmail.com
3
khimberry@gmail.com
5
```
**Expected output:** โปรแกรมจะแสดงข้อความว่า Not Found
```
Not Found
```
<hr>
