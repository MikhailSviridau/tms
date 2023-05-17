line = 'aaaaaBccBddBeeBffBggB'
a = line[5::3]
print(a)
line_2 = 'AAAABBBBCCCCDDDDFFFF'
b = line_2[:4] + line_2[4:8] + line_2[8:16] + line_2[-4:-8]
print(b)
line_3 = "PYTHON"
c = line_3[::-1]
print(c)