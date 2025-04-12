def read_single_digit(d) :
    digit_kor = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구" ]
    print(digit_kor[d], end = ' ')

def read_number(n):
    if n < 0 or n >999:
        print("0 이상 999 이하의 숫자만 입력하세요.")
        return

    for digit in str(n):
        read_single_digit(int(digit))

num = int(input("세자리 정수 입력: "))
read_number(num)
