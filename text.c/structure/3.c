#include <stdio.h>

struct my{
    int age;
    char name[100];
    
};


int main(){
    struct my s1;

    s1.age =10;
    s1.name = "ali";

    printf("%d",s1.age);

}