#include <stdio.h>

int main(){
    int r,c;
    scanf("%d",&r);
    scanf("%d",&c);
    if (c<=10){
        printf("Right");
    }
    else {
        printf("Left");
    }
    switch (r){
        case 1:
        printf(" 10");
        break;
        case 2:
        printf(" 9");
        break;
        case 3:
        printf(" 8");
        break;
        case 4:
        printf(" 7");
        break;
        case 5:
        printf(" 6");
        break;
        case 6:
        printf(" 5");
        break;
        case 7:
        printf(" 4");
        break;
        case 8:
        printf(" 3");
        break;
        case 9:
        printf(" 2");
        break;
        case 10:
        printf(" 1");
        break;
    }
    if(c<=10){
        printf(" %d",c);
    }
    else{
        printf(" %d",c-9);
    }
}