class Solution(object):

    def phone_number_to_letters(self, numbers):
        if not numbers:
            return None

        ret = list()
        self.helper(numbers, ret, '')
        return ret

    def helper(self, numbers, ret, tmp):
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi"
        }
        if not numbers:
            ret.append(tmp)
            return

        for char in mapping[numbers[0]]:
            self.helper(numbers[1:], ret, tmp + char)


if __name__ == "__main__":
    print(Solution().phone_number_to_letters('234'))
