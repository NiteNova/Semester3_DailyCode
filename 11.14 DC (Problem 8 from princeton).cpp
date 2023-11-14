#include <iostream>
#include <stack>
using namespace std;

int cases;
char input;
bool leftDelimiter = false;
bool rightDelimiter = false;
stack <int> myStack;

int main() {
	cin >> cases; 
	for (int i = 0; i < cases; i++) {
		cin >> input;
		if (input == '(' && leftDelimiter == false) {
			myStack.push(input);
			leftDelimiter = true;
		}
		else if (input == '[' && leftDelimiter == false) {
			myStack.push(input);
			leftDelimiter = true;
		}
		else if (input == '{' && leftDelimiter == false) {
			myStack.push(input);
			leftDelimiter = true;
		}
		if (input == ')' && rightDelimiter == false && myStack.top() == '(') {
			myStack.pop();
			rightDelimiter = true;
		}
		else if (input == ']' && rightDelimiter == false && myStack.top() == '[') {
			myStack.pop();
			rightDelimiter = true;
		}
		else if (input == '}' && rightDelimiter == false && myStack.top() == '{') {
			myStack.pop();
			rightDelimiter = true;
		}
	}
	myStack.size();
	myStack.top();
}
