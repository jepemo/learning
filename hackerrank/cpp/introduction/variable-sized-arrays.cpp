#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q;
    int nf;
    int num;
    int pos1, pos2;
    
    cin >> n >> q;
    
    vector<int> arr[n];
    
    for (int i=0; i < n; ++i) {
        cin >> nf;
        for (int j=0; j < nf; ++j) {
            cin >> num;
            arr[i].push_back (num);
        }
    }
    
    for (int i=0; i < q; ++i) {
        cin >> pos1 >> pos2;
        cout << arr[pos1].at(pos2) << endl;
    }
    
    return 0;
}
