l = [1,3,7,1,5,9,21,3,12,1,12,18,1,12,100,120,13]
n = 120# max_no in fedwick tree

print(l)
print("")
output = []

f_arr = [0]*(n+1) # fedwick_arr

for _, v in enumerate(l):
    x = v + (v & (-v))
    ans = 0

    while x < n:
        ans += f_arr[x]
        x = x + (x & (-x))
        
    output.append(ans)

    x = v
    while(x > 0):
        f_arr[x] = f_arr[x]+1
        x = x - (x & (-x))
        
    # print("index:", i, "total numbers greater than the", v, " are ", ans)

print(output)
