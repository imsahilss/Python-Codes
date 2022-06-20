T = int(input(''))
print(T)
for i in range(1, T+1):
    h, m = input().split()
    h = int(h)
    m = int(m)
    h_id = int(h*30 + m*0.5)
    m_id = int(m*6)
    a = abs(h_id-m_id)

    if a > 180:
        a = 360-a

    print(a)






