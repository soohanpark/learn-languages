#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include "ArrayBaseStack.h"


char inputString[10000];


void main() {
	Stack stack;
	Stack temp_stack;

	//반복수행할 테스트 케이스 입력
	int testcase;
	printf("수행할 테스트 케이스 수를 입력하세요\n>>");
	scanf("%d", &testcase);

	//테스트케이스 수대로 반복
	for (int i = 0; i < testcase; i++) {
		
		StackInit(&stack);
		StackInit(&temp_stack);

		int flag = TRUE;

		printf("문자열을 입력하세요\n>>");
		scanf("%s", inputString);

		for (int i = 0; i < strlen(inputString); i++) {
			SPush(&stack, inputString[i]);
		}

		Data temp_data_pop;
		Data temp_data_peek;
		Data temp_data_pair;

		//짝 매칭 알고리즘
		while (SIsEmpty(&stack) != TRUE) {
			temp_data_pop = SPop(&stack);
			if (SIsEmpty(&stack) != TRUE) {
				temp_data_peek = SPeek(&stack);
			}

			switch (temp_data_pop)
			{
			case ')':
				if (temp_data_peek == '{' || temp_data_peek == '[') {
					flag = FALSE;
					break;
				}
				SPush(&temp_stack, temp_data_pop);
				break;
			case '}':
				if (temp_data_peek == '(' || temp_data_peek == '[') {
					flag = FALSE;
					break;
				}
				SPush(&temp_stack, temp_data_pop);
				break;
			case ']':
				if (temp_data_peek == '{' || temp_data_peek == '(') {
					flag = FALSE;
					break;
				}
				SPush(&temp_stack, temp_data_pop);
				break;

			case '(':
				if (SIsEmpty(&temp_stack) != TRUE)
					temp_data_pair = SPeek(&temp_stack);
				else {
					flag = FALSE;
					break;
				}

				if (temp_data_pair != ')') {
					flag = FALSE;
					break;
				}
				SPop(&temp_stack);

				break;
			case '{':
				if (SIsEmpty(&temp_stack) != TRUE)
					temp_data_pair = SPeek(&temp_stack);
				else {
					flag = FALSE;
					break;
				}
				
				if (temp_data_pair != '}') {
					flag = FALSE;
					break;
				}
				SPop(&temp_stack);
				break;
			case '[':
				if (SIsEmpty(&temp_stack) != TRUE)
					temp_data_pair = SPeek(&temp_stack);
				else {
					flag = FALSE;
					break;
				}

				if (temp_data_pair != ']') {
					flag = FALSE;
					break;
				}
				SPop(&temp_stack);
				break;
			default:
				printf("ERROR!");
				break;
			}
		}

		//temp_stack에 데이터가 남아있는 경우, 짝이 안맞음으로 flag = FALSE;
		if (SIsEmpty(&temp_stack) != TRUE)
			flag = FALSE;

		if (flag == FALSE)
			printf("NO\n");
		else
			printf("YES\n");
	}
}