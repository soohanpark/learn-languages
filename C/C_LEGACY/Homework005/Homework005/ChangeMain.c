#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include "BinaryTree2.h"

void ShowIntData(int data);
void dataInit(int testCase, int nodeNum, int temp_preOrder[], int temp_inOrder[]);
void inputData();
void printData(int nodeNum, int data[]);
void noding(int x, int * preOrder[], int * inOrder[], int superIdx, int nodeNu);
int findNodeIndex(BTreeNode * Nodes[], int temp_arr[]);
int getIdx(BTreeNode * Nodes, int * inOrder[]);

int testCase, nodeNum;
int preOrder[100], inOrder[100];
BTreeNode * Nodes[100];

void main() {
	scanf("%d", &testCase);	//테스트 케이스 수 입력.

	for (int i = 0; i < testCase; i++) {
		dataInit(testCase, nodeNum, preOrder, inOrder);	//변수 초기화.

		inputData();	//데이터 입력.

		int x = getIdx(Nodes[0], inOrder);	//루트의 인덱스 구하기.

		noding(x, preOrder, inOrder, 0, nodeNum);	//트리 재구성.

		PostorderTraverse(Nodes[0], ShowIntData);	//후위 순회 결과 출력.
		printf("\n");
	}
}

int getIdx(BTreeNode * Nodes, int * inOrder[]) {
	int x;
	int rootData = GetData(Nodes);
	for (int i = 0; ; i++) {
		if (rootData == inOrder[i]) {
			x = i;
			break;
		}
	}
	return x;
}

void ShowIntData(int data)
{
	printf("%d ", data);
}

void dataInit(int testCase, int nodeNum, int temp_preOrder[], int temp_inOrder[]) {
	testCase = 0;
	nodeNum = 0;
	for (int i = 0; i < 100; i++) {
		temp_preOrder[i] = 0;
		temp_inOrder[i] = 0;
	}
}

void printData(int nodeNum, int data[]) {
	for (int i = 0; i < nodeNum; i++) {
		printf("%d ", data[i]);
	}
	printf("\n");
}

void inputData() {
	//노드 수 입력.
	scanf("%d", &nodeNum);


	//preOrder, inOrder 입력.
	for (int i = 0; i < nodeNum; i++) {
		scanf("%d", &preOrder[i]);
	}
	for (int i = 0; i < nodeNum; i++) {
		scanf("%d", &inOrder[i]);
	}

	//노드 수 만큼 생성.
	for (int i = 0; i < nodeNum; i++) {
		Nodes[i] = MakeBTreeNode();
		SetData(Nodes[i], preOrder[i]);	//루트노드도 자동적으로 설정됨 Nodes[0]은 항상 최상위 루트노드.(전위)
	}
}

int findNodeIndex(BTreeNode * Nodes[], int temp_arr[]) { //몇번째 노드인지 찾는것
	int ans;
	for (int i = 0; ; i++) {
		if (temp_arr[0] == GetData(Nodes[i])) {
			ans = i;
			break;
		}
	}

	return ans;
}

void noding(int x, int * preOrder[], int * inOrder[], int superIdx, int nodeNu) {
	int temp_leftTree[100], temp_rightTree[100];
	int temp_inorder_leftTree[100], temp_inorder_rightTree[100];
	int left_idx = -1;
	int right_idx = -1;
	int new_left_idx = -1;
	int new_right_idx = -1;
	int temp_left_length = 0, temp_right_length = 0;


	if (x != 0) {	//왼쪽 서브트리 존재 (x==0 이면 존재X)

		for (int i = 0; i <= x - 1; i++) {
			temp_leftTree[i] = preOrder[i + 1];
			temp_inorder_leftTree[i] = inOrder[i];
			temp_left_length++;
		}

		left_idx = findNodeIndex(Nodes, temp_leftTree);
		MakeLeftSubTree(Nodes[superIdx], Nodes[left_idx]);
		new_left_idx = getIdx(Nodes[left_idx], temp_inorder_leftTree);
	}

	if (x != nodeNu - 1) { //오른쪽 서브트리 존재 (x == nodeNum-1 이면 존재X)

		for (int i = x + 1, j = 0; i <= nodeNu - 1; i++, j++) {
			temp_rightTree[j] = preOrder[i];
			temp_inorder_rightTree[j] = inOrder[i];
			temp_right_length++;
		}

		right_idx = findNodeIndex(Nodes, temp_rightTree);
		MakeRightSubTree(Nodes[superIdx], Nodes[right_idx]);
		new_right_idx = getIdx(Nodes[right_idx], temp_inorder_rightTree);
	}

	if (new_left_idx != -1) {
		noding(new_left_idx, temp_leftTree, temp_inorder_leftTree, left_idx, temp_left_length);
	}
	if (new_right_idx != -1) {
		noding(new_right_idx, temp_rightTree, temp_inorder_rightTree, right_idx, temp_right_length);
	}

}