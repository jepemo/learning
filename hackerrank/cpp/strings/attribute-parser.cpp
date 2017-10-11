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

int find_pos(vector<string> tree, string attr_name) {
    int pos = -1;
    
    for (int i=0; i < tree.size(); ++i) {
        if (tree.at(i) == attr_name)
            return i;
    }
    
    return pos;
}

string resolve_query(vector<string> tree, string query) {
    vector<string> path = get_path(tree, query);
    
    int ppos = find_pos(tree, path.at(path.size()-1));
    if (ppos == -1) {
        return "Not Found!";
    }
    else {
        return tree.at(ppos+1);
    }
    
    /*
    for (int vpos=0; vpos < tree.size(); ++vpos) {
        string elem = tree.at(vpos);
        
        for
    }*/
    
    //return "Not Found!";
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
