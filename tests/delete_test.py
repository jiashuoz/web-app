import requests 
import time
import multiprocessing as mp
import matplotlib.pyplot as plt
import json

URL = "https://i8f5v6eer8.execute-api.us-east-2.amazonaws.com/dev/product_catalog-delete/"

def interval_test_create(sleep_time, n):
    run_times = []
    data = {'id': 'id1'}

    requests.delete(URL, params=data)
    # send request n times with sleep_time interval
    # for i in range(n):
    #     data['id'] = 'id' + str(i)
    #     each_start_t = time.time()
    #     r = requests.post(url = URL, json = data)
    #     each_end_t = time.time()
    #     run_times.append(each_end_t - each_start_t)
    #     time.sleep(sleep_time)
    
    # plot_name = 'create_interval_' + str(sleep_time) + '-seconds_' + str(n) + '-trials'
    # easy_plot(plot_name, list(range(n)), run_times)

def easy_plot(plot_name, x, run_times):
    plt.figure()
    plt.title(plot_name)
    plt.xlabel('Trials')
    plt.ylabel('Runtimes - seconds')
    plt.plot(x, run_times)
    # plt.show()
    plt.savefig(plot_name + '.png')

def main():
    for i in range(50):
        response = requests.delete(URL + "id" + str(i))
        print(response)
    # Setup a list of processes that we want to run
    


if __name__ == "__main__":
    main()
