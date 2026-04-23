[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/NFLzNIay)
## Create a Shopping Cart List of Dictionaries

จงเขียนโปรแกรมเพื่อเก็บข้อมูลสินค้าที่ผู้บริโภคกดเพิ่มลงในตะกร้าสินค้า โดยมีลักษณะโครงสร้างดังต่อไปนี้

```
Shopping Cart [List]
    Item {Dictionary}
        name
        quantity
        price
    Item {Dictionary}
        name
        quantity
        price
```

ซึ่งโปรแกรมจะมี list ที่ชื่อ `shopping_list` ไว้เก็บข้อมูลสินค้าจำนวน `n` รายการ 
โดยสินค้าแต่ละตัวจะมีโครงสร้างเป็น dictionary ประกอบไปด้วย 3 keys ได้แก่  `name` , `quantity`, และ `price` 

โปรแกรมจะรับจำนวนสินค้า `n` ชนิด จากนั้นใช้ **loop** ในการรับข้อมูลของสินค้าแต่ละรายการ (`name` , `quantity`, `price`) 
เพื่อสร้าง dictionary `item` ของสินค้าชนิดนั้น ๆ จากนั้น dictionary `item` ที่ถูกสร้าง จะถูกเก็บเข้าไปใน `shopping_list` list ทีละรายการ

เมื่อได้ `shopping_list` list ที่เก็บ dictionary ของสินค้าทั้งหมด `n` รายการแล้ว โปรแกรมจะคำนวณและแสดงผลลัพธ์ ดังต่อไปนี้
* แสดง `shopping_list` 
* แสดงยอดรวมของสินค้าใน `shopping_list` โดยคำนวณจาก `quantity` * `price` ของทุกสินค้าด้วยทศนิยม 1 ตำแหน่ง
<hr>

**ตัวอย่างที่ 1:**
**Input:** `n=3` 
```
3
a
1
2
b
3
4
c
5
6
```
**Expected output:** โปรแกรมจะแสดงค่าใน dictionary และผมรวม ดังต่อไปนี้
```
[{'name': 'a', 'quantity': 1, 'price': 2.0}, {'name': 'b', 'quantity': 3, 'price': 4.0}, {'name': 'c', 'quantity': 5, 'price': 6.0}]
44.0
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** `n=2` 
```
2
a
1
2
b
3
4
```
**Expected output:** โปรแกรมจะแสดงค่าใน dictionary และผมรวม ดังต่อไปนี้
```
[{'name': 'a', 'quantity': 1, 'price': 2.0}, {'name': 'b', 'quantity': 3, 'price': 4.0}]
14.0
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** `n=1` 
```
1
a
5
5
```
**Expected output:** โปรแกรมจะแสดงค่าใน dictionary และผมรวม ดังต่อไปนี้
```
[{'name': 'a', 'quantity': 5, 'price': 5.0}]
25.0
```
<hr>

