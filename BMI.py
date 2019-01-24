#計算BMI
height = int(input('請輸入您的身高(公分) = '))
height_m = (height) / 100
weight = int(input('請輸入您的體重(公斤) = '))
bmi = float(weight / (height_m * height_m))
if bmi < 18.5:
	print('您的體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('您的體重正常!')
elif bmi >= 24 and bmi < 27:
	print('您的體重過胖!')
elif bmi >= 27 and bmi < 30:
	print('您的體重輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('您的體重中度肥胖')
else:
	print('您的體重重度肥胖!!!!')