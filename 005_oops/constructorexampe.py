class Person:
  def __init__(self,n,o):
    self.name=n
    self.occ=o
    print(f'{self.name} is {self.occ}')
    
  def info(self):
    print(f'{self.name} is {self.occ}')
    
a=Person("vishal","python developer")   
# a.info()