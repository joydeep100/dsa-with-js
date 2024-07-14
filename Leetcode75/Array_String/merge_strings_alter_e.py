class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ''
        i = 0
        j = 0

        while (i < len(word1) and j < len(word2)):
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1

        while (i < len(word1)):
            res += word1[i]
            i += 1

        while (j < len(word2)):
            res += word2[j]
            j += 1

        return res


res = Solution()
print(res.mergeAlternately('abc', 'pqrdd'))
# apbqcrdd
