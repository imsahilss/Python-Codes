class Items:
    def __init__(self,fv,sv):
        self.first = fv
        self.second = sv
        self.total = fv+sv

def main():
    n = int(input())
    itemArr = []
    for i in range(n):
        fv,sv = map(int,input().split())
        itemArr.append(Items(fv,sv))
    itemArr = sorted(itemArr, key = lambda item:(item.total,item.first))
    for i in range(n):
        print('{} + {} = {}'.format(itemArr[i].first,itemArr[i].second,itemArr[i].total))

if __name__ == '__main__':
    main()