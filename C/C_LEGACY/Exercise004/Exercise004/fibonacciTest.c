#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include "CircularQueue.h"
#include "fibonacci.h"

void main() {
	int num;

	printf("INPUT N : ");
	scanf("%d", &num);

	printf("\n The answer is %d", fibonacci(num));
}