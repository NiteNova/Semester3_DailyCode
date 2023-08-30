#include <iostream>
using namespace std;

int main() {

	// Medium for 8/30


	for (int i = 70; i <= 80; i++) 
		cout << i << endl;

	cout << endl;

	for (int g = 100; g <= 300; g += 20)
		cout << g << endl;

	cout << endl;

	for (int k = 25; k >= -25; k -= 5)
		cout << k << endl;

	cout << endl << endl;
	// Spicy for 8/30

	for (int a = 1; a <= 10;) {
		cout << -5 + 9 * (a - 1) << endl;
		a++;
	}
	for (int b = 1; b <= 7;) {
		cout << 20-17 * (b - 1) << endl;
		b++;
	}

	for (int c = 1; c <= 20;) {
		cout << 2 +0.4 * (c - 1) << endl;
		c++;
	}

	cout << endl << endl;

	int j = -5;
	cout << j << endl;
	for (int o = 2; o <= 4; o++) {
		j += 9;
		cout << j << endl;
	}

	cout << endl << endl;

	int p = 20;
	cout << p << endl;
	for (int m = 2; m <= 3; m++) {
		p -= 17;
		cout << p << endl;
	}

	cout << endl << endl;

	float v = 2;
	cout << v << endl;
	for (int l = 2; l <= 5; l++) {
		v += 0.4;
		cout << v << endl;
	}

}
