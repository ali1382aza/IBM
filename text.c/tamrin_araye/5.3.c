#include <stdio.h>


int main() {
    char string[100];
    gets(string);
    char b[100];
    int a = -1;
    for (int i=0; string[i]; i++){
        if (string[i]=='(' || string[i]=='{' || string[i]=='['){
            b[++a] = string[i];
        }
        else if (string[i]==')' || string[i]=='}' || string[i]==']'){
            
            if (a==-1 || (string[i]==')' && b[a]!='(') || (string[i]=='}' && b[a]!='{') || (string[i]==']' && b[a]!='[')){
                break;
            }
            else{
                a--;
            }
        }
    }
    if (a==-1) {
        printf("correct");
    }
    else {
        printf("wrong");
    }
    return 0;
}
