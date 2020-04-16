import turtle
import random

# สร้างหน้าพร้อมกับกำหนดคำสั่งที่ใช้ในการเข้าถึงพื้นหลังโดยมีการกำหนดสีพื้นหลัง
gui = turtle.Turtle()
turtle.Screen().bgcolor("black")
# สร้างตัวแปรที่ใช้ในการเก็บสี
colors = ["red","yellow","orange","pink"]
# กำหนดให้เส้นของส่วนแรกวาดเป็นสีขาว
gui.color("white")
# กำหนดเงื่อนไขในการวาดภาพ
for i in range(10):
    for i in range(2):
        # วาดเส้นไปด้านหน้า 100
        gui.forward(100)
        # เมื่อวาดเส้นไปด้านหน้าเสร็จทำมุม 60 องศาแล้วกำหนดให้หัวปากกาวาดไปขวา
        gui.right(60)
        gui.forward(100)
        gui.right(120)
    # ทำมุม 36 องศาพร้อมกับกำหนดหัวปากกาวาดไปทางขวา
    gui.right(36)
    # เริ่มต้นโดยการวาดเส้นที่เป็นสีขาวพร้อมกับสุ่มสีที่อยู่ในตัวแปร colors
    gui.color(random.choice(colors))
# แสดงผลลัพธ์ค้างไว้
turtle.done()