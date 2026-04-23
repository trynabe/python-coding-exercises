## Count Multiple Letters

จงเขียนโปรแกรมที่มีการเรียกใช้ function ที่ชื่อว่า `multiple_letter_count` ที่รับ 1 parameter คือ `text` และ return dictionary ที่มี key เป็นตัวอักษร และมี value เป็นจำนวนตัวอักษรใน `text` นั้น ๆ
**หมายเหตุ** สามารถสมมติได้ว่าตัวอักษรใน `text` จะเป็นตัวอักษร a-z ตัวพิมพ์เล็กเท่านั้น

**ตัวอย่างที่ 1:**
**Input:** 
```
awesome
```
**Expected output:** 
```
{'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}
```
<hr>

**ตัวอย่างที่ 2:**
**Input:** 
```
hi
```
**Expected output:** 
```
{'h': 1, 'i': 1}
```
<hr>

**ตัวอย่างที่ 3:**
**Input:** 
```
hello how are you
```
**Expected output:** 
```
{'h': 2, 'e': 2, 'l': 2, 'o': 3, ' ': 3, 'w': 1, 'a': 1, 'r': 1, 'y': 1, 'u': 1}
```
<hr>
