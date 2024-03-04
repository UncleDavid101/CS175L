def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Kelvin
    kelvin = ((fahrenheit - 32) / 1.79999999) + 273.15
    return kelvin
    

def convertToCentigrade(fahrenheit):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Centigrade
    centigrade = (fahrenheit - 32) / 1.8
    return centigrade
    

def doConversion():
    #getFahrenheit(), get back Fahrenheit
    fahrenheit = int(input('Enter Fahrenheit temperature (must be -50 to 130):'))
    #convertToKelvin(), send Fahrenheit get back Kelvin
    convertToKelvin(fahrenheit)
    #ConvertToCentigrade, sends Fahrenheit gets back Centigrade
    convertToCentigrade(fahrenheit)
    #prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'
    print('Fahrenheit: ', fahrenheit,  ' Kelvin: ', convertToKelvin(fahrenheit), ' Centigrade: ', convertToCentigrade(fahrenheit))
    

def repeat():
    #Inputs How many conversions would you like to do this time?
    validation = int(input('How many conversions would you like to do this time?'))
    #for x in range how many
    for x in range(validation):
        #doConversion()
        doConversion()
    

def controlLoop():
    #Inputs 'Do you want to do some conversions(Yes or No)?'
    conversions = input('Do you want to do some conversions(Yes or No)? ')
    #if 'yes' repeat()
    if conversions == 'Yes':
        repeat()
    else:
        print('Goodbye')
    

def getFahrenheit():
    #Inputs 'Enter Fahrenheit temperature (must be -50 to 130):'
    fahrenheit = int(input('Enter Fahrenheit temperature (must be -50 to 130):'))
    #(validation loop)'Please re-enter'
    while fahrenheit < -50 or fahrenheit > 130:
        fahrenheit = int(input('Please re-enter: '))
    #return Fahrenheit
    return fahrenheit
    

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
