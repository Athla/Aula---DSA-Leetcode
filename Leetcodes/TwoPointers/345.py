class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s_list = list(s)
        l, r = 0, len(s_list) - 1

        while l < r:
            while l < r and vowels.find(s_list[l]) == -1:
                l += 1
            while l < r and vowels.find(s_list[r]) == -1:
                r -= 1

            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1

        return "".join(s_list)
