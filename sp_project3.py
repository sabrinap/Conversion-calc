# ==============================================================================
# PROGRAM Conversion Calculator
# PROJECT NUMBER: 3 
# DUE DATE: Tuesday 10/08/2019
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# Write a menu-driven program which allows a person to type in a command and an
# English unit of measurement, and convert the measurment to its equivalent
# in Metric units.
#
# INPUT
#
# All input will be interactive. Ask user to enter a command, and a numeric
# value for the measurement they want to convert. The program must allow the
# user to enter menu commands and numbers to convert, until they choose to stop.
#
# INPUT ERROR CHECKING
#
# Program must check for invalid command and negative numbers, and ask user to
# re-enter a value when necessary, until a valid data item is entered.
#
# OUTPUT
#
# The program prints an output menu, echoprints the user's input in
# a readable fashion, and then prints out the calculated results.
#
# ASSUMPTIONS
#
# We assume that input data is valid and correctly entered by the user.
# The program is guaranteed to warn user from invalid data entered and
# end program.
# ==============================================================================

# Constant Variable
CENTIMETERS = 2.5400
METERS = 0.3048
KILOMETERS = 1.6094
KILOGRAMS = 0.4536
LITERS = 3.7853
USERINPUT_1 = 1
USERINPUT_2 = 2
USERINPUT_3 = 3
USERINPUT_4 = 4
USERINPUT_5 = 5
USERINPUT_6 = 6
NEGATIVE = -1
# quit is initialized to False
quit = False

# print introductory program output heading
print ('Welcome to the Amazing Conversion Program!\n')
print ('Please choose an option from the menu below for the type of')
print ('conversion you wish to perform. Then enter a non-negative')
print ('menu number and it will be converted for you. Choose the last')
print ('option (6) to quit.')
print ('\nChoose a number from the menu.')
print ('1. Inches to centimeters')
print ('2. Feet to meters')
print ('3. Miles to kilometers')
print ('4. Pounds to kilograms')
print ('5. Gallons to liters')
print ('6. Quit the program ')

# quit = false which means while not False, means True. which means the loop will be while True:
# this loop will run until the user enters 6.
while not quit:

    # getting user input
    userInput = int(input('\nEnter your choice: '))

    # While loop for error checking with users input
    while userInput < USERINPUT_1 or userInput > USERINPUT_6:
        userInput = int(input('\nPlease enter a choice from the menu above: '))

    # Inches to Centimeters
    # need to figure out how to loop the menu
    if userInput == USERINPUT_1:
        Inches = int(input('\nPlease enter the length in inches: '))

        # Error checking user input
        while Inches <= NEGATIVE:
            Inches = int(input('This program does not convert negative values.\nPlease enter the length in inches: '))

        # if else to make sure output is correct
        if Inches == 1:
            total_Cent = Inches * CENTIMETERS
            print(Inches, 'Inch is equivalent to', total_Cent, 'centimeters.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')
        else:
            total_Cent = Inches * CENTIMETERS
            print(Inches, 'Inches is equivalent to', total_Cent, 'centimeters.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')

    # Feet to Meters
    # need to figure out how to loop menu
    elif userInput == USERINPUT_2:
        Feet = int(input('\nPlease enter the height in feet: '))

        # Error checking user input
        while Feet <= NEGATIVE:
            Feet = int(input('This program does not convert negative values.\nPlease enter the height in feet: '))

        # if else to make sure output is correct
        if Feet == 1:
            total_Meters = Feet * METERS
            print("%.3f" % Feet, 'Foot is equivalent to', "%.3f" % total_Meters, 'meters.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')
        else:
            total_Meters = Feet * METERS
            print("%.3f" % Feet, 'Feet is equivalent to', "%.3f" % total_Meters, 'meters.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')

        # Miles to Kilometers
        # need to figure out how to loop the menu
    elif userInput == USERINPUT_3:
        Miles = int(input('\nPlease enter the distance in Miles: '))

        # Error checking user input
        while Miles <= NEGATIVE:
            Miles = int(input('This program does not convert negative values.\nPlease enter the distance in miles: '))

        # if else to make sure output is correct
        if Miles == 1:
            total_Kilom = Miles * KILOMETERS
            print("%.3f" % Miles, 'Mile is equivalent to', "%.3f" % total_Kilom, 'kilometers.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')
        else:
            total_Kilom = Miles * KILOMETERS
            print("%.3f" % Miles, 'Miles is equivalent to', "%.3f" % total_Kilom, 'kilometers.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')

        # Pounds to Kilograms
        # need to figure out how to loop the menu
    elif userInput == USERINPUT_4:
        Pounds = int(input('\nPlease enter the weight in Pounds: '))

        # Error checking user input
        while Pounds <= NEGATIVE:
            Pounds = int(input('This program does not convert negative values.\nPlease enter the weight in Pounds: '))

        # if else to make sure output is correct
        if Pounds == 1:
            total_Kilog = Pounds * KILOGRAMS
            print("%.3f" % Pounds, 'Pound is equivalent to', "%.3f" % total_Kilog, 'kilograms.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')
        else:
            total_Kilog = Pounds * KILOGRAMS
            print("%.3f" % Pounds, 'Pounds is equivalent to', "%.3f" % total_Kilog, 'kilograms.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')

        # Gallons to Literes
        # need to figure out how to loop the menu
    elif userInput == USERINPUT_5:
        Gallons = int(input('\nPlease enter the quantity in Gallons: '))

        # Error checking user input
        while Gallons <= NEGATIVE:
            Gallons = int(input('This program does not convert negative values.\nPlease enter the quantity in Gallons: '))

        # if else to make sure output is correct
        if Gallons == 1:
            total_Liters = Gallons * LITERS
            print("%.3f" % Gallons, 'Gallon is equivalent to', "%.3f" % total_Liters, 'liters.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')
        else:
            total_Liters = Gallons * LITERS
            print("%.3f" % Gallons, 'Gallons is equivalent to', "%.3f" % total_Liters, 'liters.')
            #prints menu
            print('\nChoose a number from the menu.')
            print('1. Inches to centimeters')
            print('2. Feet to meters')
            print('3. Miles to kilometers')
            print('4. Pounds to kilograms')
            print('5. Gallons to liters')
            print('6. Quit the program ')

    # exit program
    # userInput == 6: when user enters 6 we make quit True.
    # Therefore not True is False and we will break out of the loop
    else:
        print('Thank you for using the Amazing Conversion Program!')
        quit = True
