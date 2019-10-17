class Solution(object):

    def combination_sum(self, k, n):
        ret = []
        input = range(1, 10)
        self.helper(input, k, n, [], ret)
        return ret

    def helper(self, input, k, n, tmp, ret):
        s = sum(tmp) if tmp else 0
        if s > n or k < 0:
            return
        elif s == n and k==0:
            ret.append(tmp)
            return
        else:
            for i, v in enumerate(input):
                self.helper(input[i + 1:], k - 1, n, tmp + [v], ret)


if __name__ == '__main__':
    print(Solution().combination_sum(3, 7))
