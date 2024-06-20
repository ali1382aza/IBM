#include <stdio.h>

void setare_fard(){
    printf("* * * * * *\n");
}
void setare_zoj(){
    printf(" * * * * * *\n");
}
void print(int x){
    for(int i=1;i<=x;i++){
        if(i%2!=0){
            setare_fard();
        }
        else{
            setare_zoj();
        }
    }
}
int main(){
    int x;
    scanf("%d",&x);
    print(x);
    return 0;
}