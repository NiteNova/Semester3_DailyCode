#include <iostream>
using namespace std;

string Laundry[10];
int top = -1;

void push(string clothing) {
	if (top >= 9)
		cout << "stack is full \n";
	else {
		top++;
		Laundry[top] = clothing;
	}
}

void pop() {
	if (top <= -1)
		cout << "stack is empty\n";
	else {
		cout << "The popped element is " << Laundry[top] << "\n";
		top--;
	}
}

void display() {
	if (top >= 0) {
		cout << "stack elements are: ";
		for (int i = top; i >= 0; i--)
			cout << Laundry[i] << " ";
		cout << "\n";
	}
	else
		cout << "Stack is empty";
}
void size() {
	if (top >= 0) {
		int len = 0;
		for (int i = top; i >= 0; i--) {
			len++;
		}
		cout << "Size of stack: " << len << "\n";
	}
	else
		cout << "Stack is empty";
}

int main() {
	push("T-Shirt");
	push("Sweater");
	push("Pants");
	push("Underwear");
	push("Socks");
	display();
	size();

	
	
};
