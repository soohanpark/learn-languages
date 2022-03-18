#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <Windows.h>
#include <math.h>

#define PI 3.141592

void main() {
	int menu;

	double r = 0;

	double ans1, ans2, ans3;

	while (1) {
		
		printf("<<선택>>\n");
		printf("1. (원의) 둘레\t2. (원의) 넓이\t3. (구의) 부피\n");
		scanf("%d", &menu);

		switch (menu)
		{
		case 1:
			printf("반지름의 길이 >> ");	scanf("%lf", &r);
			printf("-----------------------계산중-------------------------\n");
			Sleep(800);
			ans1 = 2 * PI * r;
			printf("둘레는 %6.2lf 입니다.", &ans1);
			break;

		case 2:
			printf("반지름의 길이 >> ");	scanf("%lf", &r);
			printf("-----------------------계산중-------------------------\n");
			Sleep(800);
			ans2 = PI * pow(r,2);
			printf("넓이는 %6.2lf 입니다.", &ans2);
			break;

		case 3:
			printf("반지름의 길이 >> ");	scanf("%lf", &r);

			printf("-----------------------계산중-------------------------\n");
			Sleep(800);
			ans3 = (4 / 3)*PI*pow(r,3);
			printf("부피는 %lf 입니다.", &ans3);
			break;
		default:
			break;
		}
		if (menu == 4)
			break;
	}
}


