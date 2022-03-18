#include "stdio.h"

void main() {
	int arr[] = { 1,2,3,4,5 };
	int *ptr = arr;

	printf("%d\n", *ptr);
	printf("%d\n", *(ptr + 1)); //int형도 실제 +4 가 된다는 것이지, 실사용시 "*변수명+1" 해주면 된다!
	printf("%d\n", *(ptr + 4));
	printf("%d\n", *(ptr + 3));
}