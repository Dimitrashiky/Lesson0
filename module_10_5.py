from datetime import datetime
from multiprocessing import Pool
def read_info(name):
    all_data = []
    with open(name, "r") as file:
        while True:
            if not file.readline():
                break
            all_data.append(file.readline())

file_name = ["file 1.txt", "file 2.txt", "file 3.txt", "file 4.txt"]
#start_1 = datetime.now()
#for file in file_name:
    #read_info(file)
#stop_1 = datetime.now()
#print(stop_1 - start_1)
start_2 = datetime.now()
if __name__ == '__main__':
    with Pool(1) as p:
      p.map(read_info, file_name)
stop_2 = datetime.now()
print(stop_2 - start_2)

