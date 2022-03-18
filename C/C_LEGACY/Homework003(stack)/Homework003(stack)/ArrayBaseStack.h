#ifndef __AB_STACK_H__
#define __AB_STACK_H__

#define TRUE	1
#define FALSE	0
#define STACK_LEN	100

typedef int Data;

typedef struct _arrayStack
{
	Data stackArr[STACK_LEN];
	int topIndex;
} ArrayStack;

typedef ArrayStack Stack;

void StackInit(Stack * pstack);	//스택초기화.
int SIsEmpty(Stack * pstack);	//스택이 빈경우 true, 아니면 false 

void SPush(Stack * pstack, Data data); //스택에 데이터 저장.
Data SPop(Stack * pstack);	//스택의 마지막 데이터 반환 및 제거
Data SPeek(Stack * pstack);	//스택의 마지막 데이터 엿보기

#endif