#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
    char input[100],before_e[100],after_e[100];
    
    scanf("%s",input);
    int i=0;

    while(input[i]!='e' && input[i]!='\0'){
        before_e[i]=input[i];
        i++;
    }

    before_e[i]='\0';

    if(input[i]=='e'){
        i++;
        int j=0;
        while(input[i]!='\0'){
            after_e[j]=input[i];
            i++;
            j++;
        }
        after_e[j]='\0';
    }
    long double asli=atof(before_e),tavan=atof(after_e);

    long double kol=(asli*pow(10,(int)tavan));
    int kol1=(int)kol,barg=0,remaining;
    
    while(kol1>=1){
        remaining=kol1%10;
        switch(remaining){
            case 0:
            barg+=6;
            break;

            case 1:
            barg+=2;
            break;

            case 2:
            barg+=5;
            break;

            case 3:
            barg+=5;
            break;

            case 4:
            barg+=4;
            break;

            case 5:
            barg+=5;
            break;

            case 6:
            barg+=6;
            break;

            case 7:
            barg+=3;
            break;

            case 8:
            barg+=7;
            break;

            case 9:
            barg+=6;
            break;
        }
        kol1/=10;
    }
    printf("%d",barg);
}