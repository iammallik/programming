import bisect as bs

def update(bit: List[int], x: int):

    while x > 0:
        print(3)
        x -= 1



def search(bit: List[int], x: int) -> int:


def start():
    inputs = [2, 4, 5, 1, 3]
    sorted_input = [i for i in inputs]
    sorted_input.sort()

    bit = [0]*(len(inputs)+1)
    ans = 0


    for idx, val in enumerate(inputs):
        ans += search(bit, index(sorted_input, 2*val+1))
        update(bit, index(val))


def index(arr: List[int], x: int) -> int:
    y = bs.bisect_left(arr, x) + 1
    return y


if __name__ == '__main__':
    start()