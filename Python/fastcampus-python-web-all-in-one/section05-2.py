# Section05-2
# 반복문

# 기본 반복문 : for, while


# for-else문
numbers = [1,2,3,4,5,6]
for num in numbers:
    if num == 3:
        print("found: {}!".format(num))
        break
    else:
        print("not found: {}!".format(num))
# for 구문에서 `break`를 만나지 않는다면, else에 해당하는 것을 실행! (만약, break를 만난다면 실행하지 않음)
else:
    print("Not found 33.....")