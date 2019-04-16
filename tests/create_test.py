import requests 
import time
import multiprocessing as mp
import matplotlib.pyplot as plt
import json

URL = "https://i8f5v6eer8.execute-api.us-east-2.amazonaws.com/dev/product_catalog-create"

def interval_test_create(sleep_time, n):
    request_run_times = []
    lambda_run_times = []
    dynamo_run_times = []
    data = {'id': 'id1',
	    'description': "description",
        'price': 1}
    # send request n times with sleep_time interval
    for i in range(n):
        data['id'] = 'id' + str(i)
        each_start_t = time.time()
        response = requests.post(url = URL, json = data)
        each_end_t = time.time()
        request_run_times.append(each_end_t - each_start_t)
        
        lambda_run_times.append(response.json()['lambda_time'])
        dynamo_run_times.append(response.json()['db_time'])
        time.sleep(sleep_time)
    
    plot_name = 'create_interval_' + str(sleep_time) + '-seconds_' + str(n) + '-trials'
    request_run_times = list(map(lambda x: x * 100, request_run_times))
    lambda_run_times = list(map(lambda x: x * 100, lambda_run_times))
    dynamo_run_times = list(map(lambda x: x * 100, dynamo_run_times))
    print(lambda_run_times)
    print(dynamo_run_times)
    easy_plot(plot_name, list(range(n)), request_run_times, lambda_run_times, dynamo_run_times)

def easy_plot(plot_name, x, run_times, lambda_times, db_times):
    plt.figure()
    plt.title(plot_name)
    plt.xlabel('Trials')
    plt.ylabel('Runtimes - seconds')
    plt.plot(x, run_times)
    plt.plot(x, lambda_times)
    plt.plot(x, db_times)
    plt.show()
    plt.savefig(plot_name + '.png')

def main():
    # Setup a list of processes that we want to run
    # sequential_test_list()
    # interval_test_create(1, 10)
    interval_test_create(0, 10)
    


if __name__ == "__main__":
    main()
