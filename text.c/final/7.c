#include <stdio.h>
#include <string.h>

int main(){
    char c[100],new[100];
    gets(c);
    int andaze=strlen(c),g=0;
    while(strlen(new)!=1){
        for(int i=0;i<andaze;i++){
            andaze=strlen(new);
            if(c[i]==c[i+1]){
               new[g]=c[i];
               g++; 
            }
            else if(c[i]!=c[i+1]){
                if(((c[i])=='s') && ((c[i+1])=='m')){
                    new[g]='e';
                    g++;
                }
                else if(((c[i])=='m') && ((c[i+1])=='s')){
                    new[g]='e';
                    g++;
                }
                else if(((c[i])=='e') && ((c[i+1])=='m')){
                    new[g]='s';
                    g++;
                }
                else if(((c[i])=='m') && ((c[i+1])=='e')){
                    new[g]='s';
                    g++;
                }
                else if(((c[i])=='e') && ((c[i+1])=='s')){
                    new[g]='m';
                    g++;
                }
                else if(((c[i])=='s') && ((c[i+1])=='e')){
                    new[g]='m';
                    g++;
                }

            }
        }
        g=0;
    }
    printf("%s",new);
    

}