import string
import random
import asyncio


async def maruti_generator(fname):
    while True:
        word = random.choice(['MARUTI', 'NOT_MARUTI'])
        with open(fname,'a') as file:
            if word == "NOT_MARUTI":
                file.write(f"{''.join(random.sample(string.ascii_uppercase,k=random.randint(1,10)))}\n")
            else:
                file.write(f'{word}\n')
        await asyncio.sleep(1)


async def maruti_counter(fname, counts_dic):
    while True:
        with open(fname) as file:
            str_list = file.readlines()
            counts_dic[fname] = str_list.count('MARUTI\n')
        await asyncio.sleep(1)


async def count_file_writer(counts_dic):
    while True:
        with open('counts.log','w') as count_file:
            for fname,count in counts_dic.items():
                count_file.write(f"Count in {fname}: {count}\n")
        await asyncio.sleep(1)


if __name__ == '__main__':
    counts = {}
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(maruti_generator('file1.txt'))
    task2 = loop.create_task(maruti_generator('file2.txt'))
    task3 = loop.create_task(maruti_counter('file1.txt',counts))
    task4 = loop.create_task(maruti_counter('file2.txt',counts))
    task5 = loop.create_task(count_file_writer(counts))

    #task_list = [task1, task2, task3, task4, task5]
    #final_task = loop.gather(*task_list)
    loop.run_forever()
