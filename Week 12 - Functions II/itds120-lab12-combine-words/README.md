[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/6FpxjEbT)
## Combine Words
จงเติมชุดคำสั่งใน function `combine_words` เพื่อให้โปรแกรมสามารถเติมคำต่าง ๆ ตามตำแหน่งที่กำหนด

โดยโปรแกรมจะรับ 3 inputs ดังต่อไปนี้
'''
input_text = input()
position_text = input()
extra_text = input()
'''
จากนั้น โปรแกรมจะเรียก function `combine_words` ซึ่งมี parameter `word` และ `**kwargs` โดยรับ `input_text` 
และ dictionary ที่มี key-value pairs ดังนี้ `position=position_text, extra=extra_text`
โดย function `combine_words` จะตรวจสอบประเภทใน `position` และเติมข้อความ `extra` ตามตำแหน่ง คือ
* ถ้า `position` มีค่าเป็น `prefix`, จะ return ข้อความใน `extra` ต่อด้วยข้อความใน `word`
* ถ้า `position` มีค่าเป็น `suffix`, จะ return ข้อความใน `word` ต่อด้วยข้อความใน `extra` 
* ในกรณีอื่น ๆ ที่ค่า `position` ไม่ใช่ `prefix` และ `suffix`, จะ return ข้อความใน `word` โดยไม่มีการแก้ไขใด ๆ

**หมายเหตุ:**  สามารถสมมติได้ว่าข้อความ input จะเป็นประเภท string เท่านั้น

<hr>

**ตัวอย่างที่ 1:**
**Input:**   `input_text='child'`, `position_text='prefix'` และ `extra_text='man'`
```
child
prefix
man
```
**Expected output:** เนื่องจาก `position_text='prefix'` จึงเติมข้อความใน `extra` ต่อด้วยข้อความใน `word`
```
manchild
```
<hr>

**ตัวอย่างที่ 2:**

**Input:**   `input_text='child'`, `position_text='suffix'` และ `extra_text='ish'`
```
child
suffix
ish
```
**Expected output:** เนื่องจาก `position_text='suffix'` จึงเติมข้อความใน `word` ต่อด้วยข้อความใน `extra` 
```
childish
```
<hr>

**ตัวอย่างที่ 3:**
**Input:**   `input_text='child'`, `position_text='no'` และ `extra_text='no'`
```
child
no
no
```
**Expected output:** เนื่องจาก `position_text='no'` จึงไม่มีการเติมข้อความใน `word` ใด ๆ
```
child
```
<hr>

**ตัวอย่างที่ 4:**
**Input:**   `input_text='work'`, `position_text='prefix'` และ `extra_text='home'`
```
work
prefix
home
```
**Expected output:** เนื่องจาก `position_text='prefix'` จึงเติมข้อความใน `extra` ต่อด้วยข้อความใน `word`
```
homework
```
<hr>
