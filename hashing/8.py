class Solution:
    def encode(self, strs):
        a = ""
        for i in strs:
            encoded = str(len(i)) + '#' + i
            a += encoded
        return a

    def decode(self, str):
        a = []
        for i in (len([x for x in (str.split())])):
            j = i
            while str[j] != '#':
                j += 1
            int(str[i-1])
            for k in range(i+1, i+j+1, 1):
                a.append(k)
        return (a)


A = Solution()
nums = ["we", "say", ":", "yes"]
print(A.decode(A.encode(nums)))
