
import sys,os
sys.path.insert(0, os.path.abspath(os.path.abspath('')))

from examples.sharing_variable import a2
from examples.sharing_variable import a1


a1.init()
a2.stuff()

print(a1.myList)