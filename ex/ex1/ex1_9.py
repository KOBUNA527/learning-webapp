num = int(input("四桁の整数？"))

keta = num // 1000
print(f"千の桁は{keta}です")

keta = (num % 1000) // 100
print(f"百の桁は{keta}です")

keta = (num % 100) // 10
print(f"十の桁は{keta}です")

keta = num % 10
print(f"一の桁は{keta}です")
