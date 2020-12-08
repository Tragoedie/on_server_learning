from on_server_learning.concurrency.functions_for_concurrency import create_list
from on_server_learning.concurrency.functions_for_concurrency import counter


amount_of_numbers = int(input('Enter the length of the list of numbers:'))
massive = create_list(amount_of_numbers)
number_of_threads = int(input('Enter the number of threads:'))
results = []
counter(massive, number_of_threads, results)

total_sum_conc = 0
total_sum_massive = 0
for x in range(len(results)):
    total_sum_conc += results[x]
for y in range(len(massive)):
    total_sum_massive += massive[y]
print('List total = ', total_sum_conc)
print('Sum calculated by summing the array with a loop = ', total_sum_massive)
