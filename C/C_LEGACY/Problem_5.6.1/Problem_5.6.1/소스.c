#include "헤더.h"
#include "stdio.h"

void main() {
	printf("입력 >> ");
	int ans;
	scanf_s("%d", &ans);
	printf("%d 의 제곱은 %d\n%d의 세제곱은 %d\n", ans, SQUARE(ans), ans, CUBE(ans));
}