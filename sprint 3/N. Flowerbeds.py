n = int(input())
m_arr = []
for i in range(n):
    arr = [list(map(int, input().split()))]
    m_arr += arr
m_arr.sort()
first = m_arr[0][0]
second = m_arr[0][1]
for j in range(len(m_arr) - 1):
    if second >= m_arr[j + 1][0]:
        if second <= m_arr[j + 1][1]:
            second = m_arr[j + 1][1]
    else:
        print(first, second)
        first = m_arr[j + 1][0]
        second = m_arr[j + 1][1]
print(first, second)
