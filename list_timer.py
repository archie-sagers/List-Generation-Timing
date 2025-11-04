import random
import numpy as np
import matplotlib.pyplot as plt
import time

startno = 0
endno = 100

ys = []
yssd = []

ys_concl = []
ys_conclsd = []

ys_concr = []
ys_concrsd = []

ys_comp = []
ys_compsd = []

xs = []

# list variables

list_length = 0
startno = 0
endno = 0
list1 = []

def timeitsd(somefunc,*args,repeats=100,**kwargs):
    """Times how long a defined function takes"""
    times=[]
    for i in range(repeats):
        starttime=time.perf_counter()
        ans=somefunc(*args,**kwargs)
        endtime=time.perf_counter()
        timetaken=endtime-starttime
        times.append(timetaken)
    
    mean=np.mean(times) # compute the mean time taken
    stdev=np.std(times) # compute the standard deviation of times taken (how variable is the time taken)
 
    return (mean, stdev)   #The first output will be the mean time taken and 
                          #the second output will be the standard deviation of times taken

def create_random_list(length, startnumber, endnumber):
    """Creates a random list using the append method"""
    for x in range(length):
        a=random.randint(startnumber, endnumber)
        list1.append(a)
    return list1

def create_random_list_concl(length, startnumber, endnumber):
    """Creates a random list concatenating from the left"""
    list1 = []
    for x in range(length):
        a=[random.randint(startnumber, endnumber)]
        list1 = a + list1
    return list1

def create_random_list_concr(length, startnumber, endnumber):
    """Creates a random list concatenating from the right"""
    list1 = []
    for x in range(length):
        a=[random.randint(startnumber, endnumber)]
        list1 = list1 + a
    return list1

def create_random_list_comp(length, startnumber, endnumber):
    """Creates a random list using list comprehension"""
    list1 = []
    list1 = [random.randint(startnumber, endnumber) for x in range(length)]
    return list1

for n in range(0, 1000, 10):
    """Calls the different list functions and returns the times"""
    xs.append(n)
    
    result = timeitsd(create_random_list, 0, 100, n)
    ys.append(result[0]) # Adds the 
    yssd.append(result[1] / np.sqrt(100))
    
    result_concl = timeitsd(create_random_list_concl, 0, 100, n)
    ys_concl.append(result_concl[0])
    ys_conclsd.append(result_concl[1] / np.sqrt(100))
    
    result_concr = timeitsd(create_random_list_concr, 0, 100, n)
    ys_concr.append(result_concr[0])
    ys_concrsd.append(result_concr[1] / np.sqrt(100))
    
    result_comp = timeitsd(create_random_list_comp, 0, 100, n)
    ys_comp.append(result_comp[0])
    ys_compsd.append(result_comp[1] / np.sqrt(100))
    

plt.figure(figsize=(10, 6))
plt.scatter(xs, ys, label='Append')
plt.scatter(xs, ys_concl, label='Concatenate Left')
plt.scatter(xs, ys_concr, label='Concatenate Right')
plt.scatter(xs, ys_comp, label='Comprehension')
plt.legend(loc='upper left')
plt.xlabel('Length of list')
plt.ylabel('Time (s)')
plt.title('Average length of time to generate lists of different lengths')
plt.grid(True)

plt.figure(figsize=(10, 6))
plt.errorbar(xs, yssd, label='Append EE')
plt.errorbar(xs, ys_conclsd, label='Concatenate Left EE')
plt.errorbar(xs, ys_concrsd, label='Concatenate Right EE')
plt.errorbar(xs, ys_compsd, label='Comprehension EE')
plt.legend(loc='upper left')
plt.xlabel('Length of list')
plt.ylabel('Time (s)')
plt.title('Expected Error of time to generate lists of different lengths')
plt.grid(True)
