print("โปรแกรมคำนวณพื้นที่รูปสี่เหลี่ยม")
def area_square(a):
    return a ** 2

def area_rectangle(w, h):
    return w * h

def area_rhombus(d1, d2):
    return (d1 * d2) / 2

def area_parallelogram(b, h):
    return b * h

def area_trapezoid(a, b, h):
    return ((a + b) / 2) * h

def area_kite(d1, d2):
    return (d1 * d2) / 2

shape = input("เลือกรูป (square/rectangle/rhombus/parallelogram/trapezoid/kite): ")

if shape == "square":
    a = float(input("ด้าน: "))
    print(f"พื้นที่ = {area_square(a)}")

elif shape == "rectangle":
    w = float(input("กว้าง: "))
    h = float(input("สูง: "))
    print(f"พื้นที่ = {area_rectangle(w, h)}")

elif shape == "rhombus" or shape == "kite":
    d1 = float(input("เส้นทแยง d1: "))
    d2 = float(input("เส้นทแยง d2: "))
    print(f"พื้นที่ = {area_rhombus(d1, d2)}")

elif shape == "parallelogram":
    b = float(input("ฐาน: "))
    h = float(input("สูง: "))
    print(f"พื้นที่ = {area_parallelogram(b, h)}")

elif shape == "trapezoid":
    a = float(input("ด้านบน: "))
    b = float(input("ด้านล่าง: "))
    h = float(input("สูง: "))
    print(f"พื้นที่ = {area_trapezoid(a, b, h)}")
    
