#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

static int cur_id_prof = 1;
static int cur_id_stud = 1;


class Person {
    public:
        virtual void getdata() {}
        virtual void putdata() {}
    protected:
        string name;
        string age;
        int cur_id;
};

class Professor: public Person {
    public:
        int publications;
        virtual void getdata() {
            cur_id = cur_id_prof; ++cur_id_prof;;
            cin >> name >> age >> publications;
        }
        virtual void putdata() {
            cout << name << " " << age << " " << publications << " " << cur_id << endl;
        }
};

class Student: public Person {
    public:
        int marks[6];
        void getdata() {
            cur_id = cur_id_stud; ++cur_id_stud;
            cin >> name >> age;
            for (int i=0; i < 6; ++i)  cin >> marks[i];
        }
        void putdata() {
            int summarks = 0;
            for(int i=0; i < 6; ++i) summarks += marks[i];
            
            cout << name << " " << age << " " << summarks << " " << cur_id << endl;
        }
};

nt main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
