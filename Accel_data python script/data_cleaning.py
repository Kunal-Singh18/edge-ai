num=[]
a=[0,0]
Bytes_to_read = 11
seq=[]
No_of_samples=0
timeStampBytes=[0, 0, 0, 0]
x=-0
y=-0
z=-0
xg=0
yg=0
zg=0
index=0

seq1=[]
seq2=[]

#function to convert bytes to integer
def bytes_to_int(bytes):
    result=0

    for i in bytes:
        result = result*256 + int(i)
    
    return result

#open the binary file .. there are 4 files for different types of faulty motors this code is for one such file data processing
f = open("RawAcceleroDataFile2","r+b") 

#read data from the file and add in the seq list
for i in f.read():
    seq.append(i)

#print lengtt of the list
lenghtOfList = len(seq) - 11 #we discarded last 11 bytes
print("lenght")
print(lenghtOfList)


#run loop

while index < lenghtOfList:
    num= seq
    a[0] = num[Bytes_to_read - 11] + num [Bytes_to_read - 10] + num [Bytes_to_read - 9] + num [Bytes_to_read - 8] + num [Bytes_to_read - 7] + num[Bytes_to_read- 6] + num [Bytes_to_read - 5] + num [Bytes_to_read - 4] + num [Bytes_to_read - 3] + num [Bytes_to_read - 2]
    a[0]= a[0] & 0x00ff # mark the lsb
    
    if num[Bytes_to_read - 1]==a[0]:

        #extract the timestamp bytes
        timeStampBytes[0]=num[Bytes_to_read - 11]
        timeStampBytes[1]=num[Bytes_to_read - 10]
        timeStampBytes[2]=num[Bytes_to_read - 9]
        timeStampBytes[3]=num[Bytes_to_read - 8]

        #convert time stamp to int
        timestamp=bytes_to_int(timeStampBytes)

        #convert to UTC format
        timestamp =  1560000000000 + timestamp

        #convert received hexadecimal data of x,y,x to the numeric format
                
        x= ((num[Bytes_to_read- 6]<<8 ) |(num[Bytes_to_read- 7]) ) & 0x0000ffff
        y= ((num[Bytes_to_read- 4]<<8 ) |(num[Bytes_to_read- 5]) ) & 0x0000ffff
        z= ((num[Bytes_to_read- 2]<<8 ) |(num[Bytes_to_read- 3]) ) & 0x0000ffff

        if x > 32767:
            x = x-65535
        if y > 32767:
            y = y-65535
        if z > 32767:    
            z = z-65535
        
        #Get the x ,y ,z value in g 
        xg = (x * .039)
        yg = (y * .039)
        zg = (z * .039)
                
         #append the pattern id 
        seq1.append('1')       # Pattern id
        seq1.append(',')
        
        #Append pattern name
        seq1.append("Fault2")  # Pattern name
        seq1.append(',')
        seq1.append(timestamp)
        seq1.append(',')
        seq1.append(xg)
        seq1.append(',')
        seq1.append(yg)
        seq1.append(',')
        seq1.append(zg)
        seq1.append('\r')
        seq1.append('\n')
        joined_seq = ''.join( str(v)for v in seq1)

    else:
        print(No_of_samples)
        print("data discarded")    
    
    Bytes_to_read = Bytes_to_read + 11
    No_of_samples=No_of_samples+1
    index = index + 11


file = open("AccelerometerLabeledData2.txt" ,"a") 
print("Data saved to file")
print(joined_seq)
file.write(joined_seq)
file.close()







    
