#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef __AB_STACK_H__
#define __AB_STACK_H__

#define TRUE	1
#define FALSE	0
#define STACK_LEN	10000

typedef int Data;

typedef struct _arrayStack
{
	Data stackArr[STACK_LEN];
	int topIndex;
} ArrayStack;

typedef ArrayStack Stack;

#endif

void StackInit(Stack * pstack)
{
	pstack->topIndex = -1;
}

int empty(Stack * pstack) //스택이 비어있으면 1, 아니면 0 출력
{
	if (pstack->topIndex == -1)
		return TRUE;
	else
		return FALSE;
}

void push(Stack * pstack, Data data) //정수 x 를 스택에 쌓는다.
{
	pstack->topIndex += 1;
	pstack->stackArr[pstack->topIndex] = data;
}

Data pop(Stack * pstack) //스택에서 가장 위에 있는 정수를 빼고 반환, 스택에 정수가 없다면 -1 출력
{
	int rIdx;

	if (empty(pstack))
	{
		return -1;
	}

	rIdx = pstack->topIndex;
	pstack->topIndex -= 1;

	return pstack->stackArr[rIdx];
}

Data top(Stack * pstack) //스택의 가장 위에 있는 정수 반환. 없을경우 -1 반환.
{
	if (empty(pstack))
	{
		return -1;
	}

	return pstack->stackArr[pstack->topIndex];
}

int size(Stack * pstack) { //스택의 사이즈 반환.
	return pstack->topIndex + 1; //스택의 갯수는 인덱스보다 1 만큼 크다.
}


int main() {
	Stack stack;
	StackInit(&stack);
	int instNum;


	scanf("%d", &instNum);

	char inst[10];
	int inst_temp;
	int inst_int;

	int printAns[100];
	int j = 0;


	for (int i = 0; i < instNum; i++) {


		scanf("%s%[^\n]", inst, &inst_temp);
		inst_int = atoi(&inst_temp);

		if (strcmp(inst, "push") == 0) {
			push(&stack, inst_int);
		}
		else if (strcmp(inst, "pop") == 0) {
			int temp = pop(&stack);
			printAns[j] = temp;
			j++;
		}
		else if (strcmp(inst, "size") == 0) {
			int temp = size(&stack);
			printAns[j] = temp;
			j++;
		}
		else if (strcmp(inst, "empty") == 0) {
			int temp = empty(&stack);
			printAns[j] = temp;
			j++;
		}
		else if (strcmp(inst, "top") == 0) {
			int temp = top(&stack);
			printAns[j] = temp;
			j++;
		}
	}

	for (int i = 0; i < j; i++) {
		printf("%d\n", printAns[i]);
	}

	return 0;
}