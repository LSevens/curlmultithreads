from multiprocessing import Process
import requests
import time
import random

url = 'http://exmaple.ru/pathtoendpoint'
children = 2  # number of child processes to spawn, more processes = more tokens in params
timeout = random.randint(5, 15)  # random timeout between requests in seconds
retry = 2  # number of retries
delay = 0  # time for trigger delay in seconds
params = [(('param', 'key'),),
          (('param', 'key'),)
          ]   # tokens


def child(num):
    x = 0
    while x < retry:
        x += 1
        response = requests.post(url, params=params[num])
        if (response.elapsed.total_seconds()) > delay:
            file = open("triggerDelays.txt", "a")
            file.write(str(response.elapsed.total_seconds()) + '\n')
            file.close()
        print(response.elapsed.total_seconds())
        time.sleep(timeout)


if __name__ == '__main__':
    for i in range(children):
        proc = Process(target=child, args=(i,))
        proc.start()