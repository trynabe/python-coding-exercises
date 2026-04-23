def shopping_basket(*items): 
    # 'items' จะรวบของทุกอย่างที่ส่งมาเป็น Tuple (วงเล็บ) [cite: 681, 708]
    print(f"You put {len(items)} items in the basket:")
    print(items) 

# 1. ใส่ 3 อย่าง
print("--- เคสที่ 1: ใส่ 3 อย่าง ---")
shopping_basket("Milk", "Eggs", "Bread")

# 2. ใส่ 1 อย่าง
print("\n--- เคสที่ 2: ใส่ 1 อย่าง ---")
shopping_basket("Water")

# 3. ไม่ใส่อะไรเลย
print("\n--- เคสที่ 3: ไม่ใส่อะไรเลย ---")
shopping_basket()