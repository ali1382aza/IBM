#include <stdio.h>

int main() {
    int n,g=0,i=0;
    scanf("%d\n",&n);
    char input[n];
    char ch,output[100];

    scanf("%s",input);

    for(int i2=0;i2<n;i2++){
        if(input[i2]!=input[i2+1]){
            output[g]=input[i2];
            output[g+1]=input[i2+1];
            i2+=1;
        }
    }
    printf("%s",output);

    return 0;
}

