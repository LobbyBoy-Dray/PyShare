# ========== 2.5 财务应用程序: 计算小费==========
subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate: "))
gratuity = subtotal * gratuityRate / 100
total = subtotal + gratuity
print("The gratuity is", gratuity, "and the total is", total)