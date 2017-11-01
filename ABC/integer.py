total = int(input("Enter days:"))
months = total // 30
days = total % 30
print("Month={},days={}".format(months, days))
print("Month={},days={}".format(*divmod(total, 30)))