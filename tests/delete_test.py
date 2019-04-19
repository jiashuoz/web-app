import requests 
import time
import multiprocessing as mp
import matplotlib.pyplot as plt
import json

URL = "https://i8f5v6eer8.execute-api.us-east-2.amazonaws.com/dev/product_catalog-delete/"

def interval_test_delete(sleep_time, n):
    request_times = []
    lambda_times = []
    dynamo_times = []

    for i in range(n):
        each_start_t = time.time()
        response = requests.delete(URL + "id" + str(i))
        each_end_t = time.time()

        request_times.append(each_end_t - each_start_t)
        lambda_times.append(response.json()['lambda_time'])
        dynamo_times.append(response.json()['db_time'])

        time.sleep(sleep_time)

    request_times = list(map(lambda x: x * 1000, request_times))
    lambda_times = list(map(lambda x: x * 1000, lambda_times))
    dynamo_times = list(map(lambda x: x * 1000, dynamo_times))

    plot_name = 'delete_interval_' + str(sleep_time) + 'seconds_' + str(n) + 'trials'
    # easy_plot(plot_name, list(range(n)), request_times, lambda_times, dynamo_times)

def easy_plot(plot_name, x, run_times, lambda_times, db_times):
    plt.figure()
    plt.title(plot_name)
    plt.xlabel('Trials')
    plt.ylabel('Runtimes - microseconds')
    plt.plot(x, run_times, label='total request runtime', linewidth=0.5)
    plt.legend()
    plt.plot(x, lambda_times, "r--", label='lambda function runtime', linewidth=0.5)
    plt.legend()
    plt.plot(x, db_times, "y--", label='database runtime', linewidth=0.5)
    plt.legend()
    plt.savefig(plot_name + '.png')
    plt.show()
    
def main():
    interval_test_delete(0, 5)
    # Setup a list of processes that we want to run
    


if __name__ == "__main__":
    main()
