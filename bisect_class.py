import bisect
from collections import defaultdict
import heapq

'''
maxTravelDist = 10,000
forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

Output:
[[2,4],[3,2]]

https://leetcode.com/discuss/interview-question/318918
'''

class Pair(object):
    def __init__(self, val, index):
        self.val = val
        self.i = index
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __repr__(self):
        return "Pair(val:{}, index:{})".format(self.val, self.i)

# print("Enter Max distance:")
max_distance = 10000 # int(input())

# print("Enter forward routes list:")
# f_len = int(input())
fls = [3000, 5000, 7000, 10000] #input().split()
fl = [int(i) for i in fls]

# print("Enter return routes list:")
# r_len = int(input())
rls = [2000, 3000, 4000, 5000] #input().split()
rl = [int(i) for i in rls]

flo = [] # Forward list as object
rlo = [] # Return list as objects

for i, val in enumerate(fl):
    flo.append(Pair(val, i+1))

for j, val in enumerate(rl):
    rlo.append(Pair(val, j+1))

res_map = defaultdict(list)
rlo.sort()

print(flo)
print(rlo)

for o in flo:
    rval = max_distance - o.val
    needed = bisect.bisect(rlo, Pair(rval, 0)) -1
    # print("--> val:", o, "req_val:",rval, "returned_index:", needed, )
    if needed >= 0:
        ro = rlo[needed]
        total = o.val + ro.val
        res_map[total].append((o.i, ro.i))

total_values = res_map.keys()
total_values = [-i for i in total_values]
heapq.heapify(total_values)
ans = abs(heapq.heappop(total_values))

# print(res_map)
print(res_map[ans])

if __name__ == '__main__':
    print("hello from main")
















