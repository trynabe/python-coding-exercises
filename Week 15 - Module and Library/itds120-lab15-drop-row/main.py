'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab15-drop-row
**/
'''
# TODO#1 - รับข้อมูล 2D Array
# คำใบ้:
#   1. อ่านค่าจาก input() แถวแรกเพื่อรับขนาดของ array (row, col)
#   2. ใช้ลูป for เพื่ออ่านข้อมูลแต่ละแถว
#   3. แปลงข้อมูลเป็น int และเก็บใน list
#   4. สร้าง numpy array จาก list ที่ได้
# Your Python code goes here

# TODO#2 - หาตำแหน่งแถวที่ผลรวมต่ำสุด
# คำใบ้:
#   1. ใช้ np.sum() ที่ระบุ axis เพื่อหาผลรวมของแต่ละแถว
#   2. ใช้ np.argmin() เพื่อหาตำแหน่งของแถวที่มีผลรวมต่ำสุด
# Your Python code goes here

# TODO#3 - ทำการสร้าง 2D array ใหม่ ที่ไม่มีแถวที่ผลรวมต่ำสุด
# คำใบ้:
#   1. สร้าง array เปล่าขนาด (row-1, col) ด้วย np.zeros()
#   2. คัดลอกข้อมูลจาก input_mat ไปยัง output_mat โดยข้ามแถวที่มีผลรวมต่ำสุด
# Your Python code goes here

# TODO$4 - แสดงผลลัพธ์ด้วย output_mat
# Your Python code goes here
import numpy as np

row, col = map(int, input().split())
data = []
for _ in range(row):
    data.append(list(map(float, input().split())))
input_mat = np.array(data)

row_sum = np.sum(input_mat, axis=1)
min_index = np.argmin(row_sum)

output_mat = np.zeros((row - 1, col))
output_mat = np.delete(input_mat, min_index, axis=0)

print(output_mat)