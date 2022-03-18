#include <stdio.h>
#include <stdlib.h>
#include "stacker.h"

void StackInit(Stack * pstack)
{
	pstack->topIndex = -1;
}

int SIsEmpty(Stack * pstack) //스택이 비어있으면 1, 아니면 0 출력
{
	if (pstack->topIndex == -1)
		return TRUE;
	else
		return FALSE;
}

void SPush(Stack * pstack, Data data) //정수 x 를 스택에 쌓는다.
{
	pstack->topIndex += 1;
	pstack->stackArr[pstack->topIndex] = data;
}

Data SPop(Stack * pstack) //스택에서 가장 위에 있는 정수를 빼고 반환, 스택에 정수가 없다면 -1 출력
{
	int rIdx;

	if (SIsEmpty(pstack))
	{
		return -1;
	}

	rIdx = pstack->topIndex;
	pstack->topIndex -= 1;

	return pstack->stackArr[rIdx];
}

Data SPeek(Stack * pstack) //스택의 가장 위에 있는 정수 반환. 없을경우 -1 반환.
{
	if (SIsEmpty(pstack))
	{
		return -1;
	}

	return pstack->stackArr[pstack->topIndex];
}

int SSize(Stack * pstack) { //스택의 사이즈 반환.
	return pstack->topIndex+1; //스택의 갯수는 인덱스보다 1 만큼 크다.
}


