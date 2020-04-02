#Apple 兰博洋
#March 21
#汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)# 子目标1
        move(1, a, b, c)# 子目标2	
        move(n-1, b, a, c)# 子目标3