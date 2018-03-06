import redis
import sys
import time

r = redis.Redis(
    host='127.0.0.1')

i = 0

start = time.time()

while i  < 1000000:
    r.set("key"+str(i),"val"+str(i))
    i += 1

end = time.time()

print end-start


