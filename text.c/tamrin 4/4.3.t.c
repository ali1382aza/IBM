#include <stdio.h>

int main() {
    int n,number=1;
    scanf("%d", &n);

    while (1) {
        int x=0,i=1;
        while(i<=number){
            if(number%i==0){
                x++;
            }
            i++;
        }

        if (x == n) {
            break;
        }
        number++;
    }

    printf("%d",number);
}
