#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// Quantidade de grupos de cores e tonalidades
#define ColorGroups 3
#define ColorShades 5
// Estruturas de cores
typedef struct{
  int red;
  int green;
  int blue;
} decimalRGB;

typedef struct{
  char name[20];
  decimalRGB dec;
  char hex[10];
} color;

// Logica da Matriz
// 3 grupos de cores (0: Vermelho, 1: Verde, 2: Azul)
// 5 tonalidades em cada
color Colors[ColorGroups][ColorShades];

void setColors(){
// Vermelho
color _00 = {
  .name="Red0",
  .dec={
    .red=230,
    .green=0,
    .blue=0
   },
  .hex="#e60000"
};
color _01 = {
  .name="Red1",
  .dec={
    .red=180,
    .green=0,
    .blue=0
   },
  .hex="#b40000"
};
color _02 = {
  .name="Red2",
  .dec={
    .red=226,
    .green=38,
    .blue=5
   },
  .hex="#e22605"
};
color _03 = {
  .name="Red3",
  .dec={
    .red=150,
    .green=38,
    .blue=11
   },
  .hex="#96260b"
};
color _04 = {
  .name="Red4",
  .dec={
    .red=129,
    .green=0,
    .blue=15
   },
  .hex="#81000f"
};
color _10 = {
  .name="Green0",
  .dec={
    .red=0,
    .green=230,
    .blue=42
   },
  .hex="#00e62a"
};
color _11 = {
  .name="Green1",
  .dec={
    .red=59,
    .green=177,
    .blue=0
   },
  .hex="#3bb100"
};
color _12 = {
  .name="Green2",
  .dec={
    .red=22,
    .green=146,
    .blue=26
   },
  .hex="#16921a"
};
color _13 = {
  .name="Green3",
  .dec={
    .red=43,
    .green=231,
    .blue=50
   },
  .hex="#2be732"
};
color _14 = {
  .name="Green4",
  .dec={
    .red=0,
    .green=194,
    .blue=74
   },
  .hex="#00c24a"
};
// Azul
color _20 = {
  .name="Blue0",
  .dec={
    .red=24,
    .green=8,
    .blue=255
   },
  .hex="#1808ff"
};
color _21 = {
  .name="Blue1",
  .dec={
    .red=8,
    .green=144,
    .blue=255
   },
  .hex="#0890ff"
};
color _22 = {
  .name="Blue2",
  .dec={
    .red=9,
    .green=104,
    .blue=219
   },
  .hex="#0968db"
};
color _23 = {
  .name="Blue3",
  .dec={
    .red=0,
    .green=178,
    .blue=187
   },
  .hex="#00b2bb"
};
color _24 = {
  .name="Blue4",
  .dec={
    .red=3,
    .green=0,
    .blue=156
   },
  .hex="#03009c"
};

Colors[0][0] = _00;
Colors[0][1] = _01;
Colors[0][2] = _02;
Colors[0][3] = _03;
Colors[0][4] = _04;

Colors[1][0] = _10;
Colors[1][1] = _11;
Colors[1][2] = _12;
Colors[1][3] = _13;
Colors[1][4] = _14;

Colors[2][0] = _20;
Colors[2][1] = _21;
Colors[2][2] = _22;
Colors[2][3] = _23;
Colors[2][4] = _24;
}

void printColors(){
int i;
for(i=0;i<ColorGroups;i++){
printf("\n");
int j=0;
    while(j<ColorShades){
    char red[5];
    char green[5];
    char blue[5];
    sprintf(red,"%d",Colors[i][j].dec.red);
    sprintf(green,"%d",Colors[i][j].dec.green);
    sprintf(blue,"%d",Colors[i][j].dec.blue);
    printf("\033[38;2;%s;%s;%sm",red,green,blue);
    printf("\n \"%s\": ",Colors[i][j].name);
    printf("[\"%s,%s,%s\", ",red,green,blue);
    printf("\"%s\"]",Colors[i][j].hex);
    j++;
    }
}
printf("\n");
}

int main(){
setColors();
printColors();
printf("\n");
return 0;
}
