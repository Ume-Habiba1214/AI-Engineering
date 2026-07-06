print("*"*40)
print("BMI Calculator".center(40))
print("*"*40)
Weight=float(input("Enter the weight in Kgs: "))
Height_cm=float(input("Enter the Height in CM: "))
Height_meters = Height_cm / 100
BMI=Weight/(Height_meters**2)
if BMI < 18.5:
    print("UnderWeight")
elif BMI>18.5 and BMI< 24.9:
    print("Normal Weight") 
elif BMI>25 and BMI< 29.9:
    print("OverWeight")
else:
    print("Obese")


print("*"*40)
print(f"Your BMI: {BMI:.2f}")
print("*"*40)