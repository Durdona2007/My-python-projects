
def converter():
    print("Valyuta Konvertorga xush kelibsiz!")
    print("1: So‘m → Dollar")
    print("2: Dollar → So‘m")

    kurs = 12300  # 1 USD = 12,300 so'm

    while True:
        choice = input("Yo‘nalishni tanlang (1 yoki 2, chiqish uchun 'exit'): ")
        if choice.lower() == 'exit':
            print("Dastur tugatildi.")
            break

        if choice == '1':
            uzs = float(input("So‘m miqdorini kiriting: "))
            usd = uzs / kurs
            print(f"{uzs} so‘m ≈ {round(usd, 2)} dollar")
        elif choice == '2':
            usd = float(input("Dollar miqdorini kiriting: "))
            uzs = usd * kurs
            print(f"{usd} dollar ≈ {round(uzs, 2)} so‘m")
        else:
            print("Noto‘g‘ri tanlov! 1 yoki 2 ni tanlang.")

converter()
