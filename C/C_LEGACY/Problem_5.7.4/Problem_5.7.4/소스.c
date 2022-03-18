#include <stdio.h>
#include <windows.h>

int main() {

	char wanna;
	char ans;
	int DIFF = 32;

	while (100) {
		
		printf("대->소 또는 소->대 로 변환하고 싶은 문자를 입력하시오\n>>");
		wanna = getchar();

		if (wanna > 'Z') {
			printf("<<<<<변환중>>>>>\n");
			Sleep(800);
			ans = wanna - DIFF;
			printf("결과 값은 %c 입니다.\n", ans);
		}
		
		// printf의 변수로 &ans 를 했을때, 계속해서 같은 더미 문자만 출력되었음.
		// 하지만, printf 에서는 주소가 아닌 변수의 값을 가져와야 하므로 변수의 주소를 가져와주는 & 가 필요없음.
		// 따라서 같은 더미 문자(주소를 char 형태로 출력)가 반복해서 나오는(변수의 내용이 변해도 변수의 주소는 일정) 현상 해결.

		else {
			printf("<<<<<변환중>>>>>\n");
			Sleep(800);
			ans = wanna + DIFF;
			printf("결과 값은 %c 입니다.\n", ans); 
		}

		getchar();
	}
	return 0;
}