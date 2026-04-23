cart = {
    "p001":2,
    "p005":1,
    "p012":5
}

cart["p001"] = cart["p001"] + 1
print(f"อัปเดตน้ำดื่ม: {cart['p001']} ชิ้น")

cart["p020"] = 1
print(f"ตะกร้าทั้งหมด: {cart}")

print("--- IN THE FUCKING CART ---")
for product_id, quantity in cart.items():
    print(f"รหัส {product_id} มีจำนวน {quantity} ชิ้น")