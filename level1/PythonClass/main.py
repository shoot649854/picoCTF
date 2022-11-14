infile = open("/Users/shotomorisaki/programming/picoCTF/level1/PythonClass/input.txt","r")
outfile = open("/Users/shotomorisaki/programming/picoCTF/level1/PythonClass/output.txt", "w")

line = ""
sum = 0
count = 0

# line = infile.readline()
# print(line)
# print(line[-5:])


for i in range(4):
    line = infile.readline()
    value = float(line[-5:])
    sum += value
    count += 1


    outfile.write(line)
    line = infile.readline()

outfile.write("--------/n")
average = sum / count

print(average)
outfile.write("The average is: %.0f"%(average))

infile.close()
outfile.close()