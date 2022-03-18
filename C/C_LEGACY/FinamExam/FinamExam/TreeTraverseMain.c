#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include "BinaryTree2.h"

int nodeNum;
BTreeNode * bt[26];
char nodeChar[26];

void setNodes();
void linkNodes();
void ShowCharData(char data);

void main() {
	
	scanf("%d", &nodeNum);
	setNodes();
	
	for (int i = 0; i < nodeNum; i++) {
		linkNodes();
	}

	printf("\n");
	PreorderTraverse(bt[0], ShowCharData); //bt[0](A)은 항상 루트노드이다. 
	printf("\n");
	InorderTraverse(bt[0], ShowCharData);
	printf("\n");
	PostorderTraverse(bt[0], ShowCharData);
}

void setNodes() {
	for (int i = 0; i < nodeNum; i++) {
		nodeChar[i] = 65 + i;
	}

	for (int i = 0; i < nodeNum; i++) {
		bt[i] = MakeBTreeNode();
		SetData(bt[i], nodeChar[i]);
	}
}

void linkNodes() {
	char temp_nodes[3];
	int temp_root_idx, left_node_idx, right_node_idx;
	
	scanf(" %c %c %c", &temp_nodes[0], &temp_nodes[1], &temp_nodes[2]);

	for (int i = 0; i < nodeNum; i++) {
		if (temp_nodes[0] == bt[i]->data) {
			temp_root_idx = i;
		}
		if (temp_nodes[1] == bt[i]->data) {
			left_node_idx = i;
		}
		if (temp_nodes[2] == bt[i]->data) {
			right_node_idx = i;
		}
	}

	if (temp_nodes[1] != '.') {
		MakeLeftSubTree(bt[temp_root_idx], bt[left_node_idx]);
	}
	if (temp_nodes[2] != '.') {
		MakeRightSubTree(bt[temp_root_idx], bt[right_node_idx]);
	}
}

void ShowCharData(char data)
{
	printf(" %c ", data);
}