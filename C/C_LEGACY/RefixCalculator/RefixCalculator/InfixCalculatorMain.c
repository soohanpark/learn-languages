#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include "InfixCalculator.h"

int main(void)
{
	int testCase;
	char exp[50][100];

	printf("총 테스트 케이스 수 : ");
	scanf("%d", &testCase);
	
	for (int i = 0; i < testCase; i++) {
		printf("중위표기법 입력 >> ");
		scanf("%s", exp[i]);
	}

	for (int i = 0; i < testCase; i++) {
		printf("%s = %d \n", exp[i], EvalInfixExp(exp[i]));
	}

	return 0;
}