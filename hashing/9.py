class Solution:
    def encode(self, strs):
        a = ""
        for i in strs:
            encoded = str(len(i)) + '#' + i
            a += encoded
        return a

    def decode(self, s):
        a = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            a.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return a


A = Solution()
strs = ["we", "say", ":", "yes"]
encoded_str = A.encode(strs)
decoded_strs = A.decode(encoded_str)
print(decoded_strs)
