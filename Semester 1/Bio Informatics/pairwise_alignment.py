def pairwise_alignment(seq_1, seq_2):
    insert_gap(seq_1, seq_2)
    score = []

    for i in range(len(seq_1)):
        if seq_1[i] == seq_2[i]:
            score.append('1')
        else:
            score.append('0')

    print(f'Sequence 1: {seq_1}')
    print(f'Sequence 2: {seq_2}')

    print(f'Score: {score}')

def insert_gap(seq_1, seq_2):
    l1 = len(seq_1)
    l2 = len(seq_2)

    if l1 == l2:
        print()
    else:
        gap_position = int(input('Enter the positin you want to insert the gap: '))
        if l1 < l2:
            seq_1.insert(gap_position, ' - ')
        else:
            seq_2.insert(gap_position, ' - ')


s1 = input('Enter Sequence 1: ')
s2 = input('Enter Sequence 2: ')

seq1, seq2 = list(s1), list(s2)
pairwise_alignment(seq1, seq2)
