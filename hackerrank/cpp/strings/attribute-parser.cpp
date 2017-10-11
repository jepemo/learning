#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<vector<string>> parse_tree(int n) {
    vector<vector<string>> root;
    
    for (int i=0; i < n; ++i) {
        bool end_line = false;
        string input;
        
        vector<string> tree;
        
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
        
        root.push_back(tree);
    }
    
    return root;
}

vector<string> get_path(string query) {
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

int find_tag(vector<vector<string>> root, string tag_name, int tag_pos) {
    int pos =  -1;
    
    int ipos = tag_pos == -1 ? 0 : tag_pos;
    
    for (int i=ipos; i < root.size(); ++i) {
        if (tag_name == root.at(i).at(0))
            return i == tag_pos+1 ? i : -1;
    }
    
    return pos;
}
string get_atribute(vector<string> attributes, string attr_name) {
    for (int i=1; i < attributes.size(); ++i) {
        //cout << attributes.at(i) << "==" << attr_name << endl;
        if (attributes.at(i) == attr_name) {
            return attributes.at(i+1);
        }
    }
    
    return "";   
}

string resolve_query(vector<vector<string>> root, string query) {
    vector<string> path = get_path(query);
    
    /*
    for (int i=0; i < root.size(); ++i) {
        for (int j=0; j < root.at(i).size(); ++j) {
            cout << root.at(i).at(j) << ", ";
        }
        cout << endl;
    }
    */
    
    int tag_pos = -1;
    for (int p=0; p < path.size(); ++p) {
        string tag = path.at(p);
        
        //cout << "1)" << tag << " " << p << endl;
        if (p < path.size()-1) {
            tag_pos = find_tag(root, tag, tag_pos);
            if (tag_pos == -1)
                return "Not Found!";
        }
        else {
            vector<string> attrs = root.at(tag_pos);
            string value = get_atribute(attrs, tag);
            if (value != "") {
                return value;
            }
            else {
                return "Not Found!";
            }
        }
    }
    
    return "Error!!!";
}

int main() {
    int n, q;
    cin >> n >> q;
    
    vector<vector<string>> root = parse_tree(n);
    
    string query;
    for (int i=0; i < q; ++i) {
        cin >> query;
        cout << resolve_query(root, query) << endl;
    }
    
    return 0;
}

/*
INPUT:
10 10
<a value = "GoodVal">
<b value = "BadVal" size = "10">
</b>
<c height = "auto">
<d size = "3">
<e strength = "2">
</e>
</d>
</c>
</a>
a~value
b~value
a.b~size
a.b~value
a.b.c~height
a.c~height
a.d.e~strength
a.c.d.e~strength
d~sze
a.c.d~size

OUTPUT:
GoodVal
Not Found!
10
BadVal
Not Found!
auto
Not Found!
2
Not Found!
3
*/
