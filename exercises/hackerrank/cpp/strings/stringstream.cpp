#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    vector<int> result;
    
    stringstream ss(str);
   
    int n;
    char c;
    
    while (ss.good()) {
        ss >> n;   
        if (ss.good()) {
            ss >> c;
        }
        
        result.push_back(n);
    }

    
    return result;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
