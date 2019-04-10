# importing the requests library 
import requests 
import time
import multiprocessing as mp
import matplotlib.pyplot as plt
  
# list all products
URL = "https://i8f5v6eer8.execute-api.us-east-2.amazonaws.com/dev/product_catalog-list"
  
# # location given here 
# location = "delhi technological university"
  
# # defining a params dict for the parameters to be sent to the API 
# PARAMS = {'address':location} 
  
# sending get request and saving the response as response object

def sequential_test_list():
    n = 100
    run_times = []
    # send request 100 times
    for i in range(n):
        each_start_t = time.time()
        r = requests.get(url = URL) 
        each_end_t = time.time()
        run_times.append(each_end_t - each_start_t)
    
    easy_plot('list_sequential_' + str(n) + '-trials', list(range(n)), run_times)

def interval_test_list(sleep_time, n):
    run_times = []
    # send request n times with sleep_time interval
    for i in range(n):
        each_start_t = time.time()
        r = requests.get(url = URL) 
        each_end_t = time.time()
        run_times.append(each_end_t - each_start_t)
        time.sleep(sleep_time)
    
    plot_name = 'list_interval_' + str(sleep_time) + '-seconds_' + str(n) + '-trials'
    easy_plot(plot_name, list(range(n)), run_times)

def easy_plot(plot_name, x, run_times):
    plt.figure()
    plt.title(plot_name)
    plt.xlabel('Trials')
    plt.ylabel('Runtimes - seconds')
    plt.plot(x, run_times)
    # plt.show()
    plt.savefig(plot_name + '.png')

def main():
    # Setup a list of processes that we want to run
    # sequential_test_list()
    interval_test_list(1, 10)

# t0: 1554742852.484355
# t1: 1554742862.537465
# print("t0: " + str(t0))
# print("t1: " + str(t1))
  
# # extracting data in json format 
# records = r.json() 

  
# # extracting latitude, longitude and formatted address  
# # of the first matching location 
  
# # printing the output 
# for record in records:
#     print(record['id'] + ": " + record['description'])

if __name__ == "__main__":
    main()