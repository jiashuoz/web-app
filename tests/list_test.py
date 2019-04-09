# importing the requests library 
import requests 
import time
  
# api-endpoint 
URL = "https://i8f5v6eer8.execute-api.us-east-2.amazonaws.com/dev/product_catalog-list"
  
# # location given here 
# location = "delhi technological university"
  
# # defining a params dict for the parameters to be sent to the API 
# PARAMS = {'address':location} 
  
# sending get request and saving the response as response object

n = 100
t0 = time.time()
for i in range(n): r = requests.get(url = URL) 
t1 = time.time()

# t0: 1554742852.484355
# t1: 1554742862.537465
print("t0: " + str(t0))
print("t1: " + str(t1))
  
# extracting data in json format 
records = r.json() 

  
# extracting latitude, longitude and formatted address  
# of the first matching location 
  
# printing the output 
for record in records:
    print(record['id'] + ": " + record['description'])