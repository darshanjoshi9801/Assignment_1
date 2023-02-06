import string
import random
import time
import asyncio
fnames = ['file1.txt', 'file2.txt']


async def maruti_generator(fname):
    word = random.choice(['MARUTI', 'NOT_MARUTI'])
    with open(fname,'a') as file:
        if word == "NOT_MARUTI":
            file.write(f"{''.join(random.sample(string.ascii_uppercase,k=random.randint(1,10)))}\n")
            await asyncio.sleep(0.5)
        else:
            file.write(f'{word}\n')
            await asyncio.sleep(0.5)


async def file_maker():
    while True:
        for fname in fnames:
            await maruti_generator(fname)
            #await asyncio.sleep(0.5)


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
        asyncio.run(file_maker())
    except KeyboardInterrupt:
        count_func()

# file_maker()
# count_func()
# adding a comment to check the git revert