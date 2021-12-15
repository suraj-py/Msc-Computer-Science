file = open('Variola.txt', 'r')
data = file.read()

n = len(data)

data_dic = dict()

for i in 'ACTG':
    data_dic[i] = data.count(i)

# print(data_dic)

for i in 'ACTG':
    print(f'{i} : {data_dic[i]}')
