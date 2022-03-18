#include "stdio.h"
#include "헤더.h"
#include "stdlib.h"

void main() {

	srand(time(NULL));
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			PAPER[i][j] = rand()%5+1;
		}
		PAPER[i][10] = 0;
	}
	//PAPER 데이터 입력.

	

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if (PAPER[i][j] == ANS[j]) {
				RES[i][j] = 'O';
				PAPER[i][10]++;
			}
			else
				RES[i][j] = '-';
		}
	}
	//채점 후,PAPER[][10]에 점수 입력 



	printf("\t***문항별 채점 결과***\n");
	printf("================================================================================================\n");
	printf("문항\t0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t점수\n");
	printf("================================================================================================\n");
	
	for (int a = 0; a < 10; a++) {
		printf("%d번\t", a);
		for (int b = 0; b < 10; b++) {
			printf(" %c\t",RES[a][b]);
		}
		printf("%d점\n", PAPER[a][10]);
	}

	//출력
}

