#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int x1; 
    int v1; 
    int x2; 
    int v2; 
    scanf("%d %d %d %d",&x1,&v1,&x2,&v2);
    
    /*
    match = False
if v2 > v1:
    match = False
else:
    while x1 <= x2:
        if x1 == x2:
            match = True
            break

        x1 = x1 + v1
        x2 = x2 + v2
        
if match:
    print("YES")
else:
    print("NO")
        */
    
    int match = 0;
    if (v2 > v1) {
        match = 0;
    }
    else {
        while (x1 <= x2) {
            if (x1 == x2) {
                match = 1;
                break;
            }
            
            x1 += v1;
            x2 += v2;
        }
    }
    
    if (match) {
        printf("YES");
    }
    else {
        printf("NO");
    }
    
    return 0;
}
