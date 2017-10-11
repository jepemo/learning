#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<string> parse_tree(int n) {
    vector<string> tree;
    
    for (int i=0; i < n; ++i) {
        bool end_line = false;
        string input;
        
        cin >> input;
        if (input[input.size()-1] == '>')
            continue;
        
        tree.push_back(input.substr(1));
        
        while (!end_line) {
            cin >> input;
            if (input[input.size()-1] == '>') {
                tree.push_back(input.substr(1, input.size()-3));
                end_line = true;
            }
            else if (input == "=") {
                continue;
            }
            else if (input[0] == '"') {
                tree.push_back(input.substr(1, input.size()-2));
            }
            else {
                tree.push_back(input.substr(0, input.size()));
            }
        }
    }
    
    return tree;
}

vector<string> get_path(vector<string> tree, string query) {
    vector<string> path;
    string param = "";
    //cout << query << " " << query.length() << endl;
    for (int i=0; i <= query.length(); ++i) {
        //cout << i << "==" << query.length()-1 << " -> CONCAT: " << iswalnum(query[i]) << " - " << query[i] << endl;
        if (iswalnum(query[i])) {
            param += query[i];
        } 
        else {
            //cout << param << endl;
            path.push_back(param);
            param = "";
        }
    }
    
    return path;
}

int find_pos(vector<string> tree, string attr_name, int ini_pos) {
    int pos = -1;
    
    int ipos = ini_pos == -1 ? 0 : ini_pos;
    
    for (int i=ipos; i < tree.size(); ++i) {
        string elem = tree.at(i);
        //cout << attr_name << "==" << elem << endl;
        if (tree.at(i) == attr_name)
            return i;
    }
    
    return pos;
}

string resolve_query(vector<string> tree, string query) {
    vector<string> path = get_path(tree, query);
    
    //for (int i=0; i < tree.size(); ++i) cout << tree.at(i) << ", ";
    //cout << endl;
    
    int ini_pos = -1;
    for (int p=0; p < path.size(); ++p) {
        string tag = path.at(p);
        int ppos = find_pos(tree, path.at(p), ini_pos);
        
        //cout << "tag=" << tag << " p=" << p << " - " << "ppos=" << ppos << ", ultim=" << (p == path.size()-1) << endl;
        if (p == path.size()-1 || ppos == -1) {
            if (ppos == -1) {
                return "Not Found!";
            }
            else {
                return tree.at(ppos+1);
            }
        }
        else {
            ini_pos = ppos;
            //cout << "ENTRA: ini_pos=" << ini_pos << endl;
        }
    }
    
    return "NO DEURIA";
}

int main() {
    int n, q;
    cin >> n >> q;
    
    vector<string> tree = parse_tree(n);
    
    string query;
    for (int i=0; i < q; ++i) {
        cin >> query;
        cout << resolve_query(tree, query) << endl;
    }
    
    return 0;
}
