# Section 10
# 파이썬 예외 처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요!

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시, 예외 처리 코딩 권장 (EAFP 코딩 스타일)

# 예외 발생 시키기 : raise
try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError  # 예외 발생 시키기
except ValueError:
    print('문제 발생!')
else:  # 예외 발생 안할 경우 실행됨.
    print('OK')