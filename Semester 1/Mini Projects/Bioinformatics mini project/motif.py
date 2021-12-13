import random
def motif_finding(file_name):

    l = int(input('Enter length of Motif: '))
    try:
       file = open(file_name, mode='r', encoding = 'utf-8')
       r = file.read()
       # print(f'Sequence: {r}')

       size = len(r)
       print(f'Size of the sequence - {size}')

       pos = random.randint(0,len(r)-5)
       print(f'Position - {pos}')

       motif = r[pos:pos+l]
       print(f'Motif - {motif}')
       i = pos + 1

       while(i <= size-1):
           if(motif == r[i:i+1]):
               str1 = r[i:i+1]
               print(f'Match motif - {str1}')
               file1=open("motoutput.txt","a")
               file1.write(str1 + " ")
           i += 1
    finally:
       file.close()

file_name = input('Enter file name: ')
motif_finding(file_name)
