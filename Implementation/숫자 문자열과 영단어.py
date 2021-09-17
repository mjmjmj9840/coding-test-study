def solution(s):
    answer = ""
    words_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                  "eight": "8", "nine": "9"}

    words = ""
    for i in range(len(s)):
        if s[i].isalpha():  # 알파벳일 경우
            words += s[i]
            if words in words_dict.keys():
                answer += words_dict[words]
                words = ""
        else:  # 숫자일 경우
            answer += s[i]

    return int(answer)
