import random
list= ['A','T','C','G']
length = 10
seq = ""
for i in range(length):
     seq += list[random.randint(0,3)]
file = open("reference.fasta","w")
file.write(seq)
file.close()