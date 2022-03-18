#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

void main() {
	int age, test;
	char gender;
	double height;

	printf("나이는? \t");
	scanf_s("%d", &age);
	printf("키는? \t");
	scanf_s("%lf", &height);
	printf("성별은? \t");
	scanf_s(" %c", &gender);

	printf("\n--------------------------------------\n");
	printf("젠더에 들어가있는 문자열은 %c 이다.", &gender);

	
}