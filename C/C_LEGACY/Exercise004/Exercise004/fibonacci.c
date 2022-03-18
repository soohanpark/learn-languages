#include "fibonacci.h"


int fibonacci(int n) {
	Enqueue(&q, 0);	Enqueue(&q, 1);

	int temp;

	for (int i = 2; i <= n; i++) {
		temp = Dequeue(&q) + QPeek(&q);
		//temp = QPeek(&q) + Dequeue(&q); <----이렇게 하면 에러!! Qpeek는 맨 아래에 깔린 데이터를 엿본다. 그러므로 먼저 데이터를 빼내고 엿보기!
		Enqueue(&q, temp);
		//Enqueue(&q, Dequeue(&q) + QPeek(&q));
	}

	return temp;
}