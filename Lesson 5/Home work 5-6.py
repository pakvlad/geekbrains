subj = {}
with open('lessons.txt', 'r') as my_file:
    for line in my_file:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0'<= i <='9')]).split()))
        subj[name] = name_sum
    print(f'{subj}')