def any_int(x, y, z):
       if isinstance(x,int) or isinstance(y,int) and isinstance(z,int):  # Changed 'and' to 'or' in the first condition
           if (x+y!=z) or (x+z==y) or (y+z==x):
               return True
           return False
       return False
