
import numpy as np
import time

f = open("file.txt","w+")

f.write("data_1\tdata_2\tdata_3\n")

for i in range(10):
	f.write("%d\t%d\t%d\n" %(i, i+1, i+2))

f.close()
