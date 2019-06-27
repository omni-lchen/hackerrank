if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    x = max(arr)
    l = list()
    for i in range(len(arr)):
        if arr[i] < x:
            l.append(arr[i])
    r = max(l)
    print r
