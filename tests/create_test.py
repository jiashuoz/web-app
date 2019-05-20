# import requests 
import time
import multiprocessing as mp
import matplotlib.pyplot as plt
import json
import requests 
import numpy as np

URL = "https://i8f5v6eer8.execute-api.us-east-2.amazonaws.com/dev/product_catalog-create"

def interval_test_create(sleep_time, n):
    request_times = []
    lambda_times = []
    db_init_times = []
    db_put_times = []
    data = {'id': 'id1',
	    'description': "description",
        'price': 1}
    # send request n times with sleep_time interval
    for i in range(n):
        data['id'] = 'id' + str(i)
        each_start_t = time.time()
        
        response = requests.post(url = URL, json = data)
        each_end_t = time.time()

        request_times.append(each_end_t - each_start_t)
        lambda_times.append(response.json()['lambda_time'])
        db_init_times.append(response.json()['db_init_time'])
        db_put_times.append(response.json()['db_put_time'])

        time.sleep(sleep_time)
    
    plot_name = 'create_interval_' + str(sleep_time) + 'seconds_' + str(n) + 'trials'
    request_times = list(map(lambda x: x * 1000, request_times))
    lambda_times = list(map(lambda x: x * 1000, lambda_times))
    db_init_times = list(map(lambda x: x * 1000, db_init_times))
    db_put_times = list(map(lambda x: x * 1000, db_put_times))
    
    bar_plot(plot_name, n, request_times, lambda_times, db_init_times, db_put_times)
    easy_plot(plot_name, n, request_times, lambda_times, db_init_times, db_put_times)
    plt.show()

def easy_plot(plot_name, n, run_times, lambda_times, db_init_times, db_put_times):
    plt.figure(0)
    plt.title(plot_name)
    plt.xlabel('Trials')
    plt.ylabel('Runtimes - microseconds')

    x = list(range(n))

    plt.plot(x, run_times, label='total request runtime', linewidth=0.5)
    plt.legend()
    plt.plot(x, lambda_times, "g--", label='lambda function runtime', linewidth=0.5)
    plt.legend()
    plt.plot(x, db_init_times, "r--", label='database init runtime', linewidth=0.5)
    plt.legend()
    plt.plot(x, db_put_times, "m--", label='database init runtime', linewidth=0.5)
    plt.legend()
    ##plt.savefig(plot_name + '.png')
    

def bar_plot(plot_name, n, run_times, lambda_times, db_init_times, db_put_times):
    # data to plot
    
    # create plot
    plt.figure(1)
    fig, ax = plt.subplots()
    index = np.arange(n)
    bar_width = 0.2
    opacity = 0.8
    
    rects1 = plt.bar(index, run_times, bar_width,
    alpha=opacity,
    color='b',
    label='total_run_times')
    
    rects2 = plt.bar(index + bar_width, lambda_times, bar_width,
    alpha=opacity,
    color='g',
    label='lambda_times')

    rects3 = plt.bar(index + 2 * bar_width, db_init_times, bar_width,
    alpha=opacity,
    color='r',
    label='db_init_times')

    rects4 = plt.bar(index + 3 * bar_width, db_put_times, bar_width,
    alpha=opacity,
    color='m',
    label='db_put_times')
    
    plt.xlabel('Trails')
    plt.ylabel('Runtime in ms')
    plt.title(plot_name)
    ## plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
    plt.legend()
    
    plt.tight_layout()
    

def main():
    # Setup a list of processes that we want to run
    # sequential_test_list()
    # interval_test_create(1, 10)
    interval_test_create(920, 5)
    


if __name__ == "__main__":
    main()
