[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/p5qkc4i3)
## Create Tuple/Dictionary 
จงเขียนโปรแกรมสำหรับการเก็บข้อมูลนักเรียนจำนวน `num` คน 
โดยโปรแกรมจะรับจำนวนเต็ม `num` จากนั้น โปรแกรมจะต้องใช้ **loop** ในการรับข้อมูลนักเรียนในแต่ละรอบ ได้แก่

1) `firstname` ชื่อ
2) `lastname` นามสกุล
3) `score` คะแนนของนักเรียน 

โปรแกรมจะเก็บ `(firstname, lastname)` เป็น tuple จากนั้น สร้าง dictionary `student_dict` โดยจะใช้ tuple `(firstname, lastname)`
เป็น key และ `score` คะแนนของนักเรียนเป็น value  

เมื่อเก็บข้อมูลทั้งหมดแล้ว โปรแกรมจะคำนวณและแสดงผลลัพธ์เป็นรายชื่อของนักเรียนที่ได้คะแนนมากที่สุดดังนี้ 

```
Firstname: xxx, Last name: xxx
```

**หมายเหตุ:** 
* สามารถสมมติได้ว่าผู้ใช้จะ input `score` คะแนนของนักเรียนเป็นจำนวนที่มากกว่าหรือเท่ากับ 0 เท่านั้น
* สามารถสมมติได้ว่ามีนักเรียนที่ได้คะแนนมากที่สุดแค่ 1 คน

<hr>

**ตัวอย่างที่ 1:**
**Input:** `num = 3` 
```
3
Kitty
Tang
10.0
Mickey
Mouse
20.0
Bad
Boy
5.0
```
**Expected output:** โปรแกรมจะแสดงค่าต่อไปนี้
```
Firstname: Mickey, Last name: Mouse
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `num = 2` 
```
2
Liga
Kick
50.0
Tiger
Sugar
20.0
```
**Expected output:** โปรแกรมจะแสดงค่าต่อไปนี้
```
Firstname: Liga, Last name: Kick
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `num = 5` 
```
5
Davika
Hoorne
100
Mario
Maurer
70
Araya
Hargate
80
Ton
Arch
90
Fern
Fern
50
```
**Expected output:** โปรแกรมจะแสดงค่าต่อไปนี้
```
Firstname: Davika, Last name: Hoorne
```
<hr>
