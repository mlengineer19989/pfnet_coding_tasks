from typing import List

class Solution_first():
    def __init__(self, N:int, X:int) -> None:
        self.N:int = N
        self.X:int = X
        self.a:List[int] = [0]*self.N

    def solution(self) -> int:
        while self.X != 0:
            self.search()
        return sum(self.a)


    def search(self):
        for i in range(self.N)[::-1]:
            if self.X >= 2**i:
                self.a[i] += 1
                self.X =self.X - 2**i
                break

#動的計画法による再帰的な解法
def func(n, X):
    if n==1:
        return X
    else:
        an:int = 0
        while X >= (an+1) * 2**(n-1):
            an += 1
        return func(n-1, X-an * 2**(n-1)) + an

if __name__ == "__main__":
    L = input().split()
    N = int(L[0])
    X = int(L[1])

    print(func(N, X))

    # sl = Solution_first(N, X)
    # print(sl.solution())