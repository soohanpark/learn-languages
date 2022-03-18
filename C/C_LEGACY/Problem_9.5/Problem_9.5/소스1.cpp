
//			 __________		|			天天天	|				今        |
//		    |          |	|		  /       |	|			   /  |       |
//          |		   |	|		  ----|---	凶---	      /    |   ---|
//			| 	       |	|		  ____|____	|                   ____  |
//			|__________|	|			|						   /    |
//							|			|_________				   /____|

#include "stdio.h"
#include "stdlib.h"
#include "windows.h"
#include "conio.h"

#define N 5

void purchaseItem();
int mainMenu();
void checkBill();
void exitProgram();
void printProduct();
void chooseProduct();
void addList(int product_num, int product_count);


char unit_name[N][10] = { "note","pencil","eraser","ruler","pen" };
int unit_cost[N] = { 1000,500,300,800,1500 };



static int listCounter=0;

int list_quantity[50];
int list_cost[50];
char list_name[50][10];


void main() {
	while (100)
	{
		listCounter = 0;

		int menu = mainMenu();

		switch (menu)
		{
		case 1:
			purchaseItem();
			break;
		case 2:
			checkBill();
			break;
		case 3:
			exitProgram();
			break;
		default:
			printf("Wrong Input !");
			continue;
			break;
		}
	}
}



int mainMenu() {
	int menu;
	system("cls");
	printf(">>Welcome!\n");
	printf("=========================\n");
	printf("=== 1. Purchase Items ===\n");
	printf("=== 2. Check the Bill ===\n");
	printf("=== 3. Bye-bye!       ===\n");
	printf("=========================\n");
	printf("Choose menu >> ");
	scanf_s("%d", &menu);
	return menu;
}

void purchaseItem() {
	while (100) {
		system("cls");
		printProduct();
		chooseProduct();
		printf("Don't you need anything else? (Y/N)  ");
		char chooseYN;
		scanf_s(" %c", &chooseYN);
		if (chooseYN == 'N' || chooseYN == 'n')
			break;
	}

	printf("\n\nNow, inside your bag...\n");
	int z=0;
	while (100) {
		printf(" %s is\t %dpcs\t %dwon\n", list_name[z], list_quantity, list_cost);
		z++;
		if (list_cost[z] == 0)
			break;
	}

	printf("\nPress any key to continue!");
	_getche();
}

void printProduct() {
	printf(">>Purchase Item\n");
	printf("=========================\n");
	printf("=== 1. NOTE	     1000 ===\n");
	printf("=== 2. PENCIL	  500 ===\n");
	printf("=== 3. ERASER	  300 ===\n");
	printf("=== 4. RULER	  800 ===\n");
	printf("=== 5. PEN  	 1500 ===\n");
	printf("=========================\n");
}

void chooseProduct() {
	int product_num, product_count;
	printf("Choose Item >> "); scanf_s("%d", &product_num);
	printf("Quantity >> "); scanf_s("%d", &product_count);
	addList(product_num, product_count);
}

void addList(int product_num, int product_count) {
	list_name[listCounter][10] = unit_name[product_num - 1][10];
	list_quantity[listCounter] = product_count;
	list_cost[listCounter] = product_count * unit_cost[product_num - 1];
	listCounter++;
}

void checkBill() {

}

void exitProgram() {
	system("cls");
	printf("shutdown the programing");
	for (int i = 0; i < 3; i++) {
		Sleep(300);
		printf(".");
	}
	Sleep(300);
	system("exit");
}

