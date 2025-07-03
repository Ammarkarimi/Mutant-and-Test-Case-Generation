def any_int(x, y, z):
       if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
           if (x+y==z) or (x+z==2*y) or (y+z==x):  # Scaled 'z' by 2
               return True
           return False
       return False
