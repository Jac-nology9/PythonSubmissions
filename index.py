#1. first line 
print ('Hello best coder')


#2. arithmetic operations addd and divide
    #addit0n
num1 = float(input('Enter the first number 2 be added:'))
num2 = float(input('Enter the sek0nd number 2 be added:'))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")
    #divisi0n
num3 = float(input('Enter the first number 2 be divided:'))
num4 = float(input('Enter the sek0nd number 2 be divided:'))
if num4 == 0:
    print("Err0r: Divisi0n by zer0 is n0t all0wed.")
else:
    div_result = num3/num4
    print(f"Division: {num3} / {num4} = {div_result}")


#3. Area 0f a triangle
base = float(input('Enter the length 0f the base 0f the triangle:'))
hgt = float(input('Enter the sheight 0f the triangle:'))
area = 0.5 * base * hgt
print(f"The area 0f the triangle is: {area}")


#4. Swap two variables

    #input tw0 variables 
j = input('Enter the value 0f the first variable(j):')
w = input('Enter the value 0f the sek0nd variable(w):')
    #Display the 0riginal values 
print(f"Original values: j = {j}, w = {w}")
    #swap the values using temporary variable
temp = j
j = w
w = temp
    #Display the swapped values
print(f"Swapped values: j = {j},w = {w}")


#5. Generating a rand0m number 
import random
print(f"Rand0m NUmber: {random.randint(1,100000000)}")


#6. k0nvert kil0metres t0 miles 
kilometres = float(input("Enter distance in km: "))
    #C0nversi0n fact0r: 1km = 0.621371 miles
Conversion_factor = 0.621371
miles = kilometres * Conversion_factor
print(f'{kilometres} km is equal t0 {miles} miles')


#7. Celsuius t0 Fahrenheit



