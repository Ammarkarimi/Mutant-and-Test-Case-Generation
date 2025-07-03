prompt = """
    You are a test case assistant. You need to write the test cases below the given test function. 
    
    ###EXAMPLE###
    def any_int(x, y, z):
        if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
            if (x+y==z) or (x+z==y) or (y+z==x):
                return True
            return False
        return False

    def test():
        You have to write you code here

    Strictly give only test case with one indentation block only and inside test() function"""