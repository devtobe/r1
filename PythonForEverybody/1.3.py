def computepay(hrs,rate):
    if hrs <= 40:
        pay = hrs * rate
        return pay
    else:
        pay = 40 * rate + (hrs - 40) * rate * 1.5
        return pay

user_hours = float(input("Enter Hours: "))
user_rate = float(input("Enter Rate: "))

pay = computepay(user_hours,user_rate)

print(pay)