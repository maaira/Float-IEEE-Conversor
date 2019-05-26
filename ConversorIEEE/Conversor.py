from FloatNotation import FloatNotationConversor
import os

clear = lambda: os.system('cls')

convert = FloatNotationConversor()
while True:
    
    print('1 - 8 bits\n2 - 32 bits\n3 - 64 bits\n0- Exit')
    i = int(input('Insert the index of the notation of the number to convert: \n'))
    if i == 0:
        break
    clear()
    
    num = float(input('Inser the number:\n'))

    if i == 1 :
        convert.InsertNumber(num, 8)
    if i == 2 :
        convert.InsertNumber(num, 32)
    if i == 3 :
        convert.InsertNumber(num, 64)
    

    clear()