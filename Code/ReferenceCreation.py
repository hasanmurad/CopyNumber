reference_file =open("reference.fasta","w")
file = open("chr22.fa","r")
print(file.readline()[0:-1],end="")
while(True):
    str = file.readline()
    if str== "":
         break
    for ch in str[0:-1]:
        if ch != 'N' and ch != 'n':
            reference_file.write(ch)

file.close()
reference_file.close()