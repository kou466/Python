height = float(input("키(cm): "))
weight = float(input("몸무게(kg): "))
height = height*0.01
BMI = weight/(height*height)
if(BMI < 18.5):
    print("저체중")
elif(BMI >= 18.5 and BMI < 23):
    print("정상")
elif(BMI >= 23 and BMI < 25):
    print("과체중")
elif(BMI >= 25 and BMI < 30):
    print("경도비만")
elif(BMI >= 30 and BMI < 35):
    print("중등도비만")
else:
    print("고도비만")