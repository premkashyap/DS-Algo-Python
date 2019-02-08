class propsdemo:

    def __init__(self, x):
        self.x =x
    
    @property
    def x(self):
        return self.__x 
    
    @x.setter
    def x(self ,value):
        if value<0:
            self.__x = 0
        else:
            self.__x=value
    
if __name__ == '__main__':
    p = propsdemo(-1)
    print(p.x)