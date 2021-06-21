a = int(input("Введите время в секундах: "))
print(f"{str(a // 3600).zfill(2)}:{str(a % 3600 // 60).zfill(2)}:{str(a % 3600 % 60).zfill(2)}")
