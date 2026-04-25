import requests, time

times = []
for i in range(100):
    start = time.time()
    requests.get('http://127.0.0.1:5000')
    end = time.time()
    times.append(end - start)
    print(f'Request {i+1}: {end-start:.2f}s')

times.sort()
print('---RESULTS---')
print(f'Fastest: {times[0]:.2f}s')
print(f'Average: {sum(times)/len(times):.2f}s')
print(f'Slowest (tail): {times[-1]:.2f}s')
print(f'90th percentile: {times[int(len(times)*0.9)]:.2f}s')