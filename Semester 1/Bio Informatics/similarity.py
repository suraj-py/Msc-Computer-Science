def similarity():

    seq_1 = list(input('Enter Sequence 1: '))
    seq_2 = list(input('Enter Sequence 2: '))

    similarity = []

    n = int(input('How many elements you want similar: '))

    for i in range(n):
        ele = input('Enter an element: ')
        m = int(input('How many elements are similar to: '))

        similarity.append([])
        similarity[i].append(ele)

        for j in range(m):
            ele2 = input('What is it similar to: ')
            similarity[i].append(ele2)

    print(f'Sequence 1: {seq_1}')
    print(f'Sequence 2: {seq_2}')
    print(f'Similar elements: {similarity}')

    score = 0
    for i in range(len(seq_1)):
        for j in range(len(similarity)):

            if seq_1[i] in similarity[j] and seq_2[i] in similarity[j] and seq_1[i] != seq_2[i]:
                score += 1

    sim = (score/n) * 100

    print(f'Simirarity is {sim} %')


similarity()
