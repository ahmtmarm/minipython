expression = input("Expression:")

x,y,z = expression.split(" ")
#kullanıcının girdiği değeri sırasıyla değişkinlere atar

new_x = float(x)
new_z = float(z)

if y == "+":
    result = new_x + new_z
if y == "-":
    result = new_x - new_z
if y == "*":
    result = new_x * new_z
if y == "/":
    result = new_x / new_z
print(result)