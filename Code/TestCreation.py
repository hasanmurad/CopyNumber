import random
Lower_Limit = 1
Upper_Limit = 2
Total_Copy = 5
Lower_Number_of_Copy_Limit = 2
Upper_Number_of_Copy_Limit = 3

Reference_File = open("reference.fasta","r")
Test_File = open("test.fasta","w")
Level_File = open("level.txt","w")
seq = Reference_File.read()
Test_Seq = ""
Seq_Length = len(seq)
Segment_Length = Seq_Length//Total_Copy
for i in range(Total_Copy):
    x = random.randint(Lower_Limit,Upper_Limit)
    index = random.randint(i*Segment_Length,(i+1)*Segment_Length-x)
    Level_File.write("("+str(index)+","+str(index+x-1)+")")
    number_of_copy = random.randint(Lower_Number_of_Copy_Limit,Upper_Number_of_Copy_Limit)
    if(i <Total_Copy-1):
        Test_Seq += seq[i*Segment_Length:index];
        for j in range(number_of_copy):
            Test_Seq +=seq[index:index+x]
        Test_Seq +=seq[index+x:(i+1)*Segment_Length]
    else:
        Test_Seq += seq[i * Segment_Length:index];
        for j in range(number_of_copy):
            Test_Seq += seq[index:index + x]
        Test_Seq +=seq[index + x:Seq_Length]
Test_File.write(Test_Seq)
Reference_File.close()
Test_File.close()
Level_File.close()