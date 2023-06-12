import subprocess
import time 
import datetime

increase = [0.1125]
decrease_4to6 = [0.1]
decrease_2to3 = [0.07]
decrease_10to20 = [5.0]
type1 = ["T1"]
type2 = ["T2"]
type3 = ["T3"]
type4 = ["T4"]
type5 = ["T5"]
type6 = ["T6"]
type7 = ["T7"]
type8 = ["T8"]

def run_processes(a, inc_or_dec1, b, inc_or_dec2, c, inc_or_dec3, d, inc_or_dec4, e, inc_or_dec5, f, inc_or_dec6, g, inc_or_dec7, h, inc_or_dec8, sec):
    num_processes = a+b+c+d+e+f+g+h
    processes = []
    for i in range(num_processes):
        processes.append(None)
    
    # Start all processes
    idx = 0
    i = 0
    while(i < a):
        processes[idx] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type1)
        i = i + 1
        idx = idx + 1
    i = 0
    while(i < b):
        processes[idx] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type2)
        i = i + 1
        idx = idx + 1
    i = 0
    while(i < c):
        processes[idx] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type3)
        i = i + 1
        idx = idx + 1
    i = 0
    while(i < d):
        processes[idx] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type4)
        i = i + 1
        idx = idx + 1
    i = 0
    while(i < e):
        processes[idx] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type5)
        i = i + 1
        idx = idx + 1
    i = 0
    while(i < f):
        processes[idx] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type6)
        i = i + 1
        idx = idx + 1
    i = 0
    while(i < g):
        processes[idx] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type7)
        i = i + 1
        idx = idx + 1
    i = 0
    while(i < h):
        processes[idx] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type8)
        i = i + 1
        idx = idx + 1

    # Wait for the specified duration
    t_end = time.time() + sec
    while time.time() < t_end:
        continue

    # Terminate all processes
    # for process in processes:
    #     process.terminate()
    for i in range(0, len(processes)):
        processes[i].terminate()

while(datetime.datetime.now().minute%2 == 0):
    continue

run_processes(4, increase, 4, increase, 4, increase, 5, increase, 5, increase, 4, increase, 4, increase, 5, increase, 60)
for i in range(0, 1):

    if(i != 0):
        #Hour1
        run_processes(4, increase, 4, increase, 4, increase, 5, increase, 5, increase, 4, increase, 4, increase, 5, increase, 120)

    #Hour2
    run_processes(1, decrease_2to3, 1, decrease_2to3, 1, decrease_2to3, 5, increase, 5, increase, 1, decrease_2to3, 1, decrease_2to3, 5, increase, 120)

    #Hour3
    run_processes(1, decrease_4to6, 1, decrease_4to6, 1, decrease_4to6, 5, increase, 5, increase, 1, decrease_4to6, 1, decrease_4to6, 5, increase, 120)

    #Hour4
    run_processes(4, increase, 4, increase, 4, increase, 5, increase, 2, increase, 4, increase, 4, increase, 2, increase, 120)

    #Hour5
    run_processes(5, increase, 5, increase, 5, increase, 1, decrease_4to6, 5, increase, 5, increase, 5, increase, 2, increase, 120)

    #Hour6
    run_processes(1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_4to6, 3, increase, 5, increase, 1, decrease_10to20, 4, increase, 120)

    #Hour7
    run_processes(4, increase, 4, increase, 4, increase, 1, decrease_2to3, 1, decrease_10to20, 3, increase, 4, increase, 1, decrease_2to3, 120)

    #Hour8
    run_processes(5, increase, 4, increase, 4, increase, 1, decrease_4to6, 1, decrease_4to6, 1, decrease_4to6, 4, increase, 1, decrease_4to6, 120)

    #Hour9
    run_processes(3, increase, 2, increase, 2, increase, 1, decrease_4to6, 1, decrease_4to6, 1, decrease_4to6, 2, increase, 3, increase, 120)

    #Hour10
    run_processes(1, decrease_4to6, 4, increase, 2, increase, 1, decrease_4to6, 1, decrease_4to6, 1, decrease_4to6, 4, increase, 1, decrease_10to20, 120)

    #Hour11
    run_processes(1, decrease_10to20, 1, decrease_4to6, 3, increase, 2, increase, 1, decrease_2to3, 1, decrease_4to6, 1, decrease_4to6, 1, decrease_4to6, 120)

    #Hour12
    run_processes(1, decrease_10to20, 3, increase, 1, decrease_2to3, 1, decrease_10to20, 1, decrease_2to3, 1, decrease_4to6, 1, decrease_4to6, 5, increase, 120)

    #Hour13
    run_processes(1, decrease_10to20, 1, decrease_10to20, 3, increase, 3, increase, 3, increase, 1, decrease_4to6, 4, increase, 1, decrease_2to3, 120)

    #Hour14
    run_processes(2, increase, 4, increase, 1, decrease_2to3, 3, increase, 1, decrease_10to20, 1, decrease_4to6, 1, decrease_10to20, 1, decrease_4to6, 120)

    #Hour15
    run_processes(5, increase, 1, decrease_2to3, 1, decrease_2to3, 4, increase, 5, increase, 1, decrease_4to6, 5, increase, 1, decrease_4to6, 120)

    #Hour16
    run_processes(1, decrease_2to3, 2, increase, 1, decrease_4to6, 1, decrease_4to6, 2, increase, 1, decrease_4to6, 1, decrease_4to6, 1, decrease_4to6, 120)

    #Hour17
    run_processes(5, increase, 1, decrease_2to3, 1, decrease_10to20, 1, decrease_4to6, 1, decrease_2to3, 5, increase, 1, decrease_4to6, 1, decrease_10to20, 120)

    #Hour18
    run_processes(1, decrease_10to20, 2, increase, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 3, increase, 1, decrease_10to20, 1, decrease_10to20, 120)

    #Hour19
    run_processes(1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 120)

    #Hour20
    run_processes(1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 120)

    #Hour21
    run_processes(1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 120)

    #Hour22
    run_processes(1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 120)

    #Hour23
    run_processes(1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 120)

    #Hour24
    run_processes(1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 120)

run_processes(1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 1, decrease_10to20, 5)










# run_processes(4, increase, 0, increase, 0, increase, 0, increase, 0, increase, 0, increase, 0, increase, 0, increase, 61)
# processes = [None, None, None, None]

# for i in range(4):
#     processes[i] = subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type1)
#     # processes.append(p)
# # processes =  [subprocess.Popen(["python", "src.py"] + [str(p) for p in increase] + type1)]
# # for process in processes:
# #     process.start()

# # Wait for the specified duration
# t_end = time.time() + 70
# while time.time() < t_end:
#     continue

# # Terminate all processes
# # for process in processes:
# #     process.terminate()
# # for i in processes:
# #     p.terminate()
# for i in range(0, len(processes)):
#     processes[i].terminate()