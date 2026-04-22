"""
*
**
***
****
*****
******
*******
********
*******
******
*****
****
***
**
*
"""

asteriscos = int( input ('Dime el número máximo de asteriscos: '))
#parte que baja
for i in range (1, asteriscos + 1):
    print('*' *i)
    
#parte que baja
for i in range(asteriscos + 1, 0, -1):
    print("*" * i)

