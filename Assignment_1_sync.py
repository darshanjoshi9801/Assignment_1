import string
import random
import time

fnames = ['file1.txt', 'file2.txt']


def maruti_generator():
    word = random.choice(['MARUTI', 'NOT_MARUTI'])
    if word == "NOT_MARUTI":
        return f"{''.join(random.sample(string.ascii_uppercase,k=random.randint(1,10)))}\n"
    else:
        return f'{word}\n'


def file_maker():
    while True:
        with open('file1.txt','a') as file1, open('file2.txt','a') as file2:
            file1.write(maruti_generator())
            time.sleep(1)
            file2.write(maruti_generator())


def count_func():
    counter_dic = {fname: 0 for fname in fnames}
    for fname in fnames:
        with open(fname, 'r') as file:
            for line in file:
                if line.strip( ) == 'MARUTI':
                    counter_dic[fname] += 1
    with open('counts.log', 'w') as file:
        for fname, count in counter_dic.items():
            file.write(f"The word MARUTI in {fname} has occured {count} times\n")

if __name__=='__main__':
    try:
        file_maker()
    except KeyboardInterrupt:
        count_func()