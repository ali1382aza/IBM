#include <stdio.h>

int main(){
    int a,b;
    printf("mojoodi:");
    scanf("%d",&a);
    scanf("%d",&b);
    if (a<b) {
        printf("gheir gabel bardasht:");
    }
    else {
        printf("%d bardasht shod  mojoodi shoma:%d",b,a-b);
    }

}