class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for char in strs:
            s += str(len(char)) + "#" + char

        return s
            


    def decode(self, s: str) -> List[str]:
        num_read = 0
        reading_num = True
        ss = ""
        answer = []

        for char in s:
            if reading_num:
                if char != "#":
                    num_read = num_read * 10 + int(char)
                else:
                    reading_num = False

                    if num_read == 0:
                        answer.append("")
                        reading_num = True

            else:
                ss += char
                num_read -= 1

                if num_read == 0:
                    answer.append(ss)
                    ss = ""
                    reading_num = True

        return answer
