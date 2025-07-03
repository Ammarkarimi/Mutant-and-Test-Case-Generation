def any_int(x, y, z):
       if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
           if (x+y==z) or (x+z==y) or (y+z!=x):  # Changed '==' to '!=' in the last condition
               return True
           return False
       return False
