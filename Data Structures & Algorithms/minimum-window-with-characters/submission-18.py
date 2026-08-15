class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        from collections import Counter
        benchmark = Counter(t)
        required = len(benchmark)  # number of distinct chars that must be satisfied

        rcount = {}
        formed = 0  # number of distinct chars currently satisfied

        minlen = float("inf")
        output = ""
        i = 0

        for j, char in enumerate(s):
            if char in benchmark:
                rcount[char] = rcount.get(char, 0) + 1
                if rcount[char] == benchmark[char]:
                    formed += 1

            while formed == required:
                if j - i + 1 < minlen:
                    minlen = j - i + 1
                    output = s[i:j + 1]

                left_char = s[i]
                if left_char in benchmark:
                    rcount[left_char] -= 1
                    if rcount[left_char] < benchmark[left_char]:
                        formed -= 1
                i += 1

            # j advances automatically via the for loop

        return output




