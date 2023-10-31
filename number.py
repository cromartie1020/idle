
def input_number():
    # This function checks that the value you enter is a number.
    # Input must be a number to exit function
    
    numb=True
    while(numb):
        try:
            x=input('Please enter a number. ')
            x=int(x)
            x=x+0
            numb=False
            return x
        except ValueError:
            print('You did not enter a number. ',end='')
            
            
x=input_number()
print(x)

        