
def calculator():
    print("Python Kalkulyatorga xush kelibsiz!")
    print("Amallar: +  -  *  /")

    while True:
        num1 = input("1-sonni kiriting (yoki 'exit' yozing): ")
        if num1.lower() == 'exit':
            break
        num2 = input("2-sonni kiriting: ")
        op = input("Amalni tanlang (+ - * /): ")

        try:
            num1 = float(num1)
            num2 = float(num2)

            if op == '+':
                print("Natija:", num1 + num2)
            elif op == '-':
                print("Natija:", num1 - num2)
            elif op == '*':
                print("Natija:", num1 * num2)
            elif op == '/':
                print("Natija:", num1 / num2)
            else:
                print("Noto‘g‘ri amal tanlandi.")
        except:
            print("Xatolik! Raqam yoki amal noto‘g‘ri.")

calculator()
