import string
import random
import asyncio
import time
import aiofiles


class FileMonitoringSys:
    async def __maruti_generator(self, fname):
        while True:
            word = random.choice(['MARUTI', 'NOT_MARUTI'])
            async with aiofiles.open(fname,'a') as file:
                if word == "NOT_MARUTI":
                    await file.write(f"{''.join(random.sample(string.ascii_uppercase,k=random.randint(1,10)))}\n")
                else:
                    await file.write(f'{word}\n')
            await asyncio.sleep(1)

    async def __maruti_counter(self, fname, counts_dic):
        while True:
            async with aiofiles.open(fname) as file:
                str_list = await file.readlines()
                counts_dic[fname] = str_list.count('MARUTI\n')
            await asyncio.sleep(1)

    async def __count_file_writer(self, counts_dic):
        while True:
            async with aiofiles.open('counts.log','w') as count_file:
                for fname, count in counts_dic.items():
                    await count_file.write(f"Count in {fname}: {count}\n")
            await asyncio.sleep(1)

    def code_runner(self):
        counts = {}
        loop = asyncio.get_event_loop()
        loop.create_task(self.__maruti_generator('file1.txt'))
        loop.create_task(self.__maruti_generator('file2.txt'))
        loop.create_task(self.__maruti_counter('file1.txt', counts))
        loop.create_task(self.__maruti_counter('file2.txt', counts))
        loop.create_task(self.__count_file_writer(counts))
        loop.run_forever()


if __name__ == '__main__':
    try:
        start = time.time()
        obj = FileMonitoringSys()
        obj.code_runner()
    except KeyboardInterrupt:
        print(f"Script has run successfully in {time.time()-start} ")


