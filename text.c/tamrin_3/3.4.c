#include <stdio.h>

int main(){
    char a ,b ,c ,d ;
    scanf("%c %c %c %c",&a,&b,&c,&d);
    if (a==b || c==d || c==b || d==a){
        printf("YES");
    }
    else{
        printf("NO");
    }


}