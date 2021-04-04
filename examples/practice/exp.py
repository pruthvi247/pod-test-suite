
class employee2:
        '''description of your class- doc string'''
        def __init__(self,enam,eno):
                self.ename=enam
                self.eno=eno
        def info(self):
                eno = 888
                print(eno)
                print(self.eno)

if __name__ == "__main__":
    ee = employee2("acv","123")
    ee.info()