#include "CLinkedList.h"
#include "stdio.h"


int C, N, K;
int data;

void setInput() {
	printf("N 입력 >> ");
	scanf_s("%d", &N);
	printf("K 입력 >> ");
	scanf_s("%d", &K);
}

void main(){
    List list;
    ListInit(&list);

	printf("C 입력 >> ");
	scanf_s("%d", &C);

	setInput();

	// for --- C
	for (int z = 0; z < C; z++) {

		// 두번째 케이스 이상 시작시, 초기화
		if (z != 0) {
			printf("\n");
			setInput();
			ListInit(&list);
		}

		//N명 세우기
		for (int i = 0; i < N; i++) {
			LInsert(&list, i + 1);
		}


		LFirst(&list, &data);

		//자살
		while (LCount(&list) != 2) {

			LRemove(&list);

			for (int x = 0; x < K; x++) {
				LNext(&list, &data);
			}
		}

		//출력
		printf("\n\n생존자는\n");
		for (int y = 0; y < LCount(&list); y++) {
			printf("%d\t", data);
			LNext(&list, &data);
		}
		printf("\n");
	}
}