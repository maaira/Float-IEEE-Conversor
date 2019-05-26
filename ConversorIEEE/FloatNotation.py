from numpy import float32 

class FloatNotationConversor:
#self.N recebe uma lista contendo a notação, tamanho do expoente, tamanho da mantissa e o valor do BIAS
    def __init__(self):
        self.N8  = [8 ,3 ,4 ,3   ]
        self.N32 = [32,8 ,23,127 ]
        self.N64 = [64,11,52,1023]
        pass
#initial function that get the value to convert e set the apropriate notation
    def InsertNumber(self, decimal: float, notation : int): 
    
        print(' ')
    
        if notation == 8 and abs(decimal)< 8 : self.ConvertToBin(abs(decimal), self.N8, self.GetSinal(decimal)) 
        if notation == 32 and abs(decimal)< pow(2,32) : self.ConvertToBin(float32(abs(decimal)), self.N32, self.GetSinal(decimal)) 
        if notation == 64 and abs(decimal)< pow(2,64) : self.ConvertToBin(abs(decimal), self.N64, self.GetSinal(decimal))
        else : print('Number is bigger than the notation')
        input()

#function that separer the integer from de fractional part and convert each other
    def ConvertToBin(self,num , notation:list , sinal : int): 
        integer = int(num)
        fl_num = num - int(num)
        binary = format(integer, 'b')
        fl_binary = self.ConvertFractionToBin(fl_num, notation)
    
        if notation[0] == 8:
            exp = self.ConvertBin(binary , 3)
            mant = self.ConvertBin(fl_binary, 4)
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
    
    def GetSinal(self, decimal: float):
        if decimal < 0: return 1
        else : return 0

    def CompleteStrBin(self, tam: int):
        cont = 0
        st = ''
        while cont < tam:
            st = '0' + st
            cont += 1
        return st


    def Concatenar(self, str1: str, str2: str):
        return str1 + str2

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
        while num != 1 | cont < notation[0]:
            num = num*2
            if num >= 1 : 
                num -= 1
                str_bin += '1'
            else : str_bin += '0'
            cont += 1
            
        return str_bin

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


    def Expoente( self, bin : str):
        index = bin[0]+'.'+bin.replace('.','')[1:]
        return ((bin.index('.') - index.index('.')), index[2:])

    def GetExpoente( self, exp : int, notation : list):
        bin = format(exp + notation[3], 'b')
        while len(str(bin))<  notation[1]:
            bin+='0'
        return bin
        

