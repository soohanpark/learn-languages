#define _CRT_SECURE_NO_WARNINGS

#include "stacker.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	Stack stack;
	StackInit(&stack);

	int instNum;

	printf("총 명령의 수 >> "); //총 명령의 수 입력.
	scanf("%d", &instNum);

	char inst[10]; 
	int inst_temp; 
	int inst_int; 

	for (int i = 0; i < instNum; i++) {
		
		printf("명령 : ");
		scanf("%s%[^\n]", inst, &inst_temp); //명령어 저장, 데이터(정수) scanf로 받을 때, 사용할 임시 저장.
		inst_int = atoi(&inst_temp); //atoi를 통해 임시로 받은 정수 변환.
		
		if (strcmp(inst, "push") == 0) { //정수 x 를 스택에 쌓는 연산.
			SPush(&stack, inst_int);
		}
		else if (strcmp(inst, "pop") == 0) { //스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 만약 스택에 정수가 없는 경우 -1 출력.
			int temp = SPop(&stack);
			printf("\t\t\t%d\n", temp);
		}
		else if (strcmp(inst, "size") == 0) { //스택에 들어가 있는 정수의 갯수를 반환. (index+1 이 스택에 들어가 있는 갯수)
			int temp = SSize(&stack);
			printf("\t\t\t%d\n", temp);
		}
		else if (strcmp(inst, "empty") == 0) { //스택이 비어 있으면 1, 아니면 0을 출력.
			int temp = SIsEmpty(&stack);
			printf("\t\t\t%d\n", temp);
		}
		else if (strcmp(inst, "top") == 0) { //스택의 가장 위에 있는 정수를 출력. 만약 스택에 정수가 없는 경우 -1 출력.
			int temp = SPeek(&stack);
			printf("\t\t\t%d\n", temp);
		}
	}

	return 0; 
}