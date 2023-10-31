try:
    x = int(input('x'))
except ValueError:
    print ('please input a number')
y= int (input('y'))


def num_func(x, y):
    
    total=x + y
          
    return total

z=num_func(x,y)
print(z)
    
