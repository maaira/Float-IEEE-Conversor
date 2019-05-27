from numpy import float32 

class FloatNotationConversor:
#self.N receives a list containing the notation, exponent size, mantissa size and BIAS value
#N[0] = notation, N[1] = size of expoent, N[2] = size of mantissa, N[3] = BIAS
    def __init__(self):
        self.N8  = [8 ,3 ,4 ,3   ]
        self.N32 = [32,8 ,23,127 ]
        self.N64 = [64,11,52,1023]
        pass
    
#initial function that get the value to convert e set the apropriate notation
#Alert: The 8 bits notation is the fixed point notationand the 64 e 32 bits uses the IEEE standard
    def InsertNumber(self, decimal: float, notation : int): 
    
        print(' ')
    
        if notation == 8 and abs(decimal)< 8 : self.ConvertToBin(abs(decimal), self.N8, self.GetSinal(decimal)) 
        elif notation == 32 and abs(decimal)< pow(2,32) : self.ConvertToBin(float32(abs(decimal)), self.N32, self.GetSinal(decimal)) 
        elif notation == 64 and abs(decimal)< pow(2,64) : self.ConvertToBin(abs(decimal), self.N64, self.GetSinal(decimal))
        else : print('Number is bigger than the notation')
        input()

#function that separer the integer from de fractional part and convert each other
    def ConvertToBin(self,num , notation:list , sinal : int): 
        integer = int(num)
        fl_num = num - int(num)
        binary = format(integer, 'b')
        fl_binary = self.ConvertFractionToBin(fl_num, notation)
    
        if notation[0] == 8:
            
            exp = self.ConvertBin(binary , notation[1])
            mant = self.ConvertBin(fl_binary, notation[2])
            binary = str(sinal) + exp + mant        
            hexadecimal = hex(int(binary, base=2))
            self.PrintNotation(notation, sinal, exp, mant, hexadecimal)
            
        else:
            
            int_exp, str_fl = self.Expoente(binary + '.' + fl_binary)
            exp = self.GetExpoente(int_exp, notation) 
            mant = self.Mantissa(str_fl, notation)
            binary = str(sinal) + exp + mant        
            hexadecimal = hex(int(binary, base=2))
            self.PrintNotation(notation, sinal, exp, mant, hexadecimal)

    def ConvertBin(self,num : str, tam: int):
        return self.CompleteStrBin(tam-len(num))+num
    
#Define the valor of the signal, if smaller than 0 the signal is equal a 1, if bigger than -1 the signal is equal a 0    
    def GetSinal(self, decimal: float):
        if decimal < 0: return 1
        else : return 0
        
#Complete the bit with 0
    def CompleteStrBin(self, tam: int):
        cont = 0
        st = ''
        while cont < tam:
            st = '0' + st
            cont += 1
        return st

#Concatena two strings
    def Concatenar(self, str1: str, str2: str):
        return str1 + str2
    
#Write the number converted
    def PrintNotation(self, notation: list, sinal : int, exp : str, mantissa : str, hexa: str):
        print ('Notation:' , notation[0])
        print ('Sinal:   ' , sinal)
        print ('Expoente:' , exp )
        print ('Mantissa:' , mantissa)
        print (' ')
        print('Hexadecimal : ', hexa)

#function that convert the frational part using successive multiplications for 2
    def ConvertFractionToBin(self, num, notation : list):   
        str_bin = ''
        cont = 0
        while num != 1 | cont < notation[2]:
            num = num*2
            if num >= 1 : 
                num -= 1
                str_bin += '1'
            else : str_bin += '0'
            cont += 1
            
        return str_bin
    
#Adjust the mantissa size according to the notation
    def Mantissa(self, fl_str : str, notation: list):
     
        if len(fl_str) == notation[2]:
            return fl_str
        elif len(fl_str) > notation[2]:
            return fl_str[:notation[2]]
        else:
            cont = 0
            st = ''
            while cont < len(fl_str)- notation[2] :
                st+='0'
            return fl_str+st

#takes the converted string to binary and calculates through the address of the character '.' the exponent. 
#The method return the exponent and the binary number after the point(mantissa)
    def Expoente( self, bin : str):
        index = bin[0]+'.'+bin.replace('.','')[1:]
        return ((bin.index('.') - index.index('.')), index[2:])
    
#Sum the expoent with the BIAS and add '0' to complete
    def GetExpoente( self, exp : int, notation : list):
        bin = format(exp + notation[3], 'b')
        while len(str(bin))<  notation[1]:
            bin+='0'
        return bin
        

