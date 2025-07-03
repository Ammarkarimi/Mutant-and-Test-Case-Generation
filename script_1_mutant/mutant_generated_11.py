def any_int(x, y, z):
       if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
           if (x+y==z) or (x+z==y) and (y-z==x):  # Changed 'or' to 'and', added subtraction
               return True
           return False
       return False
