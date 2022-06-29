weight= float(input("enter your weight in (kg) :"))
height= float(input("enter your height in (m) :"))
bmi=weight/(height*height)
print(bmi," :")
if bmi<18.5 : print("underweight")
elif bmi>=18.5 and bmi<=24.5 : print("normal")
elif bmi>=25 and bmi<=29.5 : print("overweight")
else : print("obese")



