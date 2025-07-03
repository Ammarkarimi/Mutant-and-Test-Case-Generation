def any_int(x, y, z):
       if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
           if (x-y==z) or (x+z!=y) and (y+z==x):  # Changed '==' to '!=' and 'or' to 'and'
               return True
           return False
       return False
