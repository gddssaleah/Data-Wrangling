import pandas as pd

a = {'Student':['Ice Bear','Panda','Grizzly'], 'Math':[80,95,79]}
b = {'Student':['Ice Bear','Panda','Grizzly'], 'Electronics':[85,81,83]}
c = {'Student':['Ice Bear','Panda','Grizzly'], 'GEAS':[90,79,93]}
d = {'Student':['Ice Bear','Panda','Grizzly'], 'ESAT':[93,89,88]}

A = pd.DataFrame(a, columns = ['Student','Math'])
B = pd.DataFrame(b, columns = ['Student','Electronics'])
C = pd.DataFrame(c, columns = ['Student','GEAS'])
D = pd.DataFrame(d, columns = ['Student','ESAT'])

merged = A.merge(B).merge(C).merge(D)
long = pd.melt(merged, id_vars = 'Student', value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT'], var_name = 'Subject', value_name= 'Grades').sort_values('Student')
