#include <iostream>
#include <string>
using namespace std;

int main() {
   // Complete the program
    string a, b;
    cin >> a;
    cin >> b;
    
    cout << a.size() << " " << b.size() << endl;
    cout << a + b << endl;
    
    char fa = a[0];
    char fb = b[0];
    a[0] = fb;
    b[0] = fa;
    
    cout << a << " " << b << endl;
    
    return 0;
}
