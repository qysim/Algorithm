# import sys
# sys.stdin = open("input.txt", "r")

# 0과 1의 비율을 키 값으로 암호코드 숫자 딕셔너리 만들기
code_dic = {
    (3,2,1,1): 0,
    (2,2,2,1): 1,
    (2,1,2,2): 2,
    (1,4,1,1): 3,
    (1,1,3,2): 4,
    (1,2,3,1): 5,
    (1,1,1,4): 6,
    (1,3,1,2): 7,
    (1,2,1,3): 8,
    (3,1,1,2): 9,
}


# 16진수를 2진수로 변환하는 함수
def h_to_b(h):
    # 16진수를 10진수로 변환하기
    dec_n = int(h, base=16)
    # 10진수를 2진수로 변환
    bin_n = ''
    # 10진수 숫자가 0이 아니면 반복
    while dec_n:
        result = dec_n % 2
        dec_n //= 2
        if result:  # 10진수를 2로 나눈 나머지가 0이 아니면
            bin_n = '1' + bin_n
        else:       # 10진수를 2로 나눈 나머지가 0이면
            bin_n = '0' + bin_n

    while len(bin_n) < 4:
        bin_n = '0' + bin_n

    return bin_n


def solve(code_line):
    # 2. 암호코드 후보 찾기
    tmp_code = []
    for i in range(N):
        start = M * 4 - 1
        while start:
            if code_line[i][start] == '1':
                code = []
                for _ in range(8):
                    w1 = w2 = w3 = w4 = 0
                    while code_line[i][start] == '1':
                        w4 += 1
                        start -= 1
                    while code_line[i][start] == '0':
                        w3 += 1
                        start -= 1
                    while code_line[i][start] == '1':
                        w2 += 1
                        start -= 1

                    multi_num = w2
                    if w3 < multi_num:
                        multi_num = w3
                    if w4 < multi_num:
                        multi_num = w4
                    w1 = 7 * multi_num - w2 - w3 - w4
                    start -= w1

                    w1 //= multi_num
                    w2 //= multi_num
                    w3 //= multi_num
                    w4 //= multi_num

                    code.insert(0, code_dic[(w1,w2,w3,w4)])
                if code not in tmp_code:
                    tmp_code.append(code)
                    # tmp_code.append(''.join(map(str, code)))
            start -= 1
    # print(tmp_code)
    # 3. 정상적인 암호코드인지 확인
    total = 0
    for code in tmp_code:
        odd_sum = code[0] + code[2] + code[4] + code[6]
        even_sum = code[1] + code[3] + code[5]
        if (odd_sum*3 + even_sum + code[7]) % 10 == 0:
            total += odd_sum + even_sum + code[7]

    return total


T = int(input())
for tc in range(1, T+1):
    # N: 배열의 세로크기, M: 배열의 가로크기
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    # 1. 배열을 16진수에서 2진수로 변환
    code_line = []
    for i in range(N):
        tmp = ''
        for j in range(M):
            tmp += h_to_b(data[i][j])
        code_line.append(tmp)

    print(f'#{tc} {solve(code_line)}')
