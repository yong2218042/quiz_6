def validate_resident_number(resident_number):
    if len(resident_number) != 13:
        return False

    digits = [int(char) for char in resident_number[:12]] # 주민등록번호의 앞 12자리를 숫자로 변환
    weights = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    result = sum(a * b for a, b in zip(digits, weights)) # 각 자리에 가중치를 곱하고 합산
    remainder = result % 11
    checksum = 11 - remainder if remainder != 0 else 1 # 나머지를 계산하고 0이면 1로 설정
    last_digit = int(resident_number[-1])
    return checksum == last_digit # 계산된 결과와 주민등록번호의 마지막 자리 비교

while True:
    resident_number = input("주민등록번호를 입력하세요 (숫자만, 나가려면 'exit' 입력): ")

    if resident_number.lower() == 'exit':
        break

    if validate_resident_number(resident_number):
        print("유효한 주민등록번호입니다.")
    else:
        print("유효하지 않은 주민등록번호입니다.")

