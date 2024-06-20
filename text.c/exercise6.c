#include <stdio.h>

int main(){
    int c=0;
    int i=0;
    while(i<=10) {
        c=i+c;
        i++;
    }
    printf("%d jam baraye adad 1 ta %d",c,i-1);
}
