#include <iostream>
using namespace std;


string ADT[20];
int bluetop = -1;
int redtop = 9;

void blue_push(string blue) {
	if (bluetop >= 9)
		cout << "stack is full \n";
	else {
		bluetop++;
		ADT[bluetop] = blue;
	}
}

void blue_pop() {
	if (bluetop <= -1)
		cout << "stack is empty\n";
	else {
		cout << "The popped element is " << ADT[bluetop] << "\n";
		bluetop--;
	}
}

void blue_display() {
	if (bluetop > -1) {
		cout << "blue elements are: ";
		for (int i = bluetop; i <= 9; i--)
			cout << ADT[i] << "";
		cout << "\n";
	}
	else
		cout << "Stack is empty\n";
}

void blue_size() {
	if (bluetop >= 0) {
		int len = 0;
		for (int i = bluetop; i >= 0; i--) {
			len++;
		}
		cout << "Size of stack: " << len << "\n";
	}
	else
		cout << "Stack is empty\n";
}

void red_push(string red) {
	if (redtop >= 20)
		cout << "stack is full \n";
	else {
		redtop++;
		ADT[redtop] = red;
	}
}

void red_pop() {
	if (redtop <= 9)
		cout << "stack is empty\n";
	else {
		cout << "The popped element is " << ADT[redtop] << "\n";
		redtop--;
	}
}

void red_display() {
	if (redtop > 9) {
		cout << "red elements are: ";
		for (int i = redtop; i >= 0; i--)
			cout << ADT[i] << " ";
		cout << "\n";
	}
	else
		cout << "Stack is empty\n";
}

void red_size() {
	if (redtop > 9) {
		int len = 0;
		for (int i = redtop; i >= 0; i--) {
			len++;
		}
		cout << "Red size of stack: " << len << "\n";
	}
	else
		cout << "Stack is empty\n";
}




int main() {
	char choice;
	while (1) {
		cout << "(R) = Red\n(B) = Blue\n";
		cin >> choice;
		cout << "\n";
		if (choice == 'r') {
			int red_choices = 0;
			cout << "(1) = red_push\n(2) = red_pop\n(3) = red_display\n(4) = red_size\n";
			cin >> red_choices;
			switch (red_choices) {
			case 1: {
				string red_add;
				cin >> red_add;
				red_push(red_add);
				break;
			}
			case 2:
				red_pop();
				break;
			case 3:
				red_display();
				break;
			case 4:
				red_size();
				break;
			}
		}
		else {
			int blue_choices = 0;
			cout << "(1) = blue_push\n(2) = blue_pop\n(3) = blue_display\n(4) = blue_size\n";
			cin >> blue_choices;
			switch (blue_choices) {
			case 1: {
				string blue_add;
				cin >> blue_add;
				blue_push(blue_add);
				break;
			}
			case 2:
				blue_pop();
				break;
			case 3:
				blue_display();
				break;
			case 4:
				blue_size();
				break;
			}
		}
	}
};

