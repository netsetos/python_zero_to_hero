# username = "use12345"
# password = "pass1"
#
# if len(username) >= 5:
#     if len(password) >= 8:
#         print("Registration successful!")
#     else:
#         print("Password must be at least 8 characters long.")
# else:
#     print("Username must be at least 5 characters long.")


score = 99
level = 1

if score >= 100:
    level += 1
    print(f"Congratulations! You've leveled up to Level {level}.")
else:
    print("Keep playing to level up!")


data = [12, None, 15, 10, None]  #--> [12,15,10]

cleaned_data = []
for value in data:
    if value is None:
        cleaned_data.append(0)  # Replace missing value with 0
    else:
        cleaned_data.append(value)

print("Cleaned Data:", sum(cleaned_data))


cart_total = 500
membership = ""

if membership == "Gold":
    discount = 0.2  # 20% discount
elif membership == "Silver":
    discount = 0.1  # 10% discount
else:
    discount = 0  # No discount

final_price = cart_total - (cart_total * discount)
print(f"Final Price: {final_price}")


stock_price = 120

if stock_price > 150:
    print("Alert: Stock price is too high. Consider selling!")
elif stock_price < 100:
    print("Alert: Stock price is too low. Consider buying!")
else:
    print("Stock price is stable. Hold your position.")


heart_rate = 101

if heart_rate < 60:
    print("Alert: Low heart rate. Immediate attention needed!")
elif 60 <= heart_rate <= 100:
    print("Heart rate is normal.")
else:
    print("Alert: High heart rate. Consult a doctor!")

temperature = 28

if temperature < 18:
    print("Turning on the heater.")
elif temperature > 25:
    print("Turning on the air conditioner.")
else:
    print("Temperature is optimal. No adjustment needed.")


server_load = 25  # Load in percentage

if server_load < 50:
    print("Server is running optimally.")
elif 50 <= server_load <= 80:
    print("Warning: Server load is moderate.")
else:
    print("Critical Alert: Server is overloaded!")






