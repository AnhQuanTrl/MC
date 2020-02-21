import re
out = open("CodeGenSuite2.py", "wt")
inf = open("CodeGenSuite.py","rt")
l = [line for line in inf if "def" in line] 
print(set(x for x in l if l.count(x) > 1))  