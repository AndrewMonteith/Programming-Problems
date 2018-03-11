#include <iostream>
#include <memory>

using namespace std;

// A solution to part A can be done using a Circular Linked link style data structure.
// I wanted to make my own because I was bored
struct Node {
	int payload;
	Node* next;

	Node(int p, Node* n) : payload(p), next(n) {}
};

void moveForward(Node** curPos, int n) {
	for (auto i = 0; i < n; i++) {
		(*curPos) = (*curPos)->next;
	}
}

void insert(Node* curPos, int n) {
	Node* newNode = new Node(n, curPos->next);
	curPos->next = newNode;
}

int simulateSpinLock(int n) {
	Node root = { 0, nullptr };
	root.next = &root;

	Node* curPos = &root;
	int payloadData = 1;

	while (curPos->payload != 2017) {
		moveForward(&curPos, n);
		insert(curPos, payloadData);
		curPos = curPos->next;
		payloadData++;
	}

	return curPos->next->payload;
}

int spinlockTermination() {
	int len = 1;
	int pos = 0;

	int valInFront = 0;
	
	for (auto i = 1; i <= 50000000; i++) {
		pos = (pos + 394)%len;

		// Everytime the jump loops back to position 0
		// we store the value it was going to insert in the front
		if (pos == 0) {
			valInFront = i;
		}

		len += 1;
		pos += 1;
	}

	return valInFront;
}

int main() {
	cout << simulateSpinLock(394) << endl;
	cout << spinlockTermination() << endl;
}