#pandas
import pandas as pd
iris =  pd.read_csv("irisplant.txt")
print(iris)
#numpy
from numpy import genfromtxt
my_data = genfromtxt('irisplant.txt', delimiter=',')

print(type(my_data))
