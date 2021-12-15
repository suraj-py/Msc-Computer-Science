def indentity(seq_1, seq_2):

    insert_gap(seq_1, seq_2)

    score = []
    val = 0

    for i in range(len(seq_1)):
        for j in range(len(seq_1)):

            if seq_1[i] == seq_2[j]:
                score.append('1')
                val += 1
            else:
                score.append('0')

    total_element = len(seq_1) * len(seq_2)
    indentity_value = (val/total_element) * 100

    print(f'Sequence 1: {seq_1}')
    print(f'Sequence 2: {seq_2}')
    print(f'Identity : {indentity_value}')

def insert_gap(seq_1, seq_2):
    if len(seq_1) == len(seq_2):
        print()
    else:
        gap_position = int(input('Enter gap positin: '))
        if len(seq_1) < len(seq_2):
            seq_1.insert(gap_position, ' - ')
        else:
            seq_2.insert(gap_position, ' - ')


s1 = input('Enter Sequence 1: ')
s2 = input('Enter Sequence 2: ')
seq1, seq2 = list(s1), list(s2)
indentity(seq1, seq2)
