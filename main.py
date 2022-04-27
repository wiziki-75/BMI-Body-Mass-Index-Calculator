size = input('Enter your size in meters : ')

weigth = input('\nEnter your weigth in kg : ')

IMC = float(weigth) / (float(size) * float(size))

print('\nYour BMI is : \n' + str(round(IMC, 1)) + '\n')

if IMC < 18.5:
    for i in range(0, 999):
        weigth2 = float(weigth) + i
        IMC = float(weigth2) / (float(size) * float(size))
        if IMC >= 18.5:
            print('You must gain ' + str(i) + 'kg.')
            break
elif IMC > 25:
    for i in range(0, 999):
        weigth2 = float(weigth) - i
        IMC = float(weigth2) / (float(size) * float(size))
        if IMC < 25:
            print('You must lose ' + str(i) + 'kg.')
            break
else:
    print('Your BMI is fine.')