#include <stdio.h>

int main(){
    int size,g;
    char ch;
    scanf("%d",&size);
    char reshte[size];
    for(int i=-1;i<size;i++){
        ch=getchar();
        reshte[i]=ch;
        g=i;
    }
    g++;
    reshte[g]='\0';
    printf("%c\n",reshte[0]);
}