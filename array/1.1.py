class solution(object):
    def containsDuplicate(self, num):
        for x in range(len(num)):
            for a in range(len(num)):
                if num[a] == num[x] and a != x:
                    return True
        return False


sol = [1, 2, 3, 4]
A = solution()
print(A.containsDuplicate(sol))
