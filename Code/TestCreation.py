import random
Lower_Limit = 1
Upper_Limit = 2
Total_Copy  = 5

file = open("reference.fasta","r")
seq = file.read()
Test_Seq = ""
Seq_Length = len(seq)
Segment_Length = Seq_Length//Total_Copy
for i in range(Total_Copy):
    x = random.randint(Lower_Limit,Upper_Limit)
    index = random.randint(i*Segment_Length,(i+1)*Segment_Length-x)
    print("("+str(index)+","+str(index+x-1)+")", end = '')
    # print(seq[index:index+x])
    if(i <Total_Copy-1):
        Test_Seq += seq[i*Segment_Length:index]+seq[index:index+x]+seq[index:index+x]+ seq[index+x:(i+1)*Segment_Length]
    else:
        Test_Seq += seq[i * Segment_Length:index] + seq[index:index + x] + seq[index:index + x] + seq[index + x:Seq_Length]

print("")
print(seq)
print(Test_Seq)
file.close()