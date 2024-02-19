class solution(object):
    def containsDuplicate(self, num):
        num.sort()
        for x in range(len(num)-1):
            if num[x] == num[x+1]:
                return True
            return False


A = solution()
B = [1, 2, 3, 1]
print(A.containsDuplicate(B))
