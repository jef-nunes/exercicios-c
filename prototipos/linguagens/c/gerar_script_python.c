#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#define PY_ARCHIVE_NAME "arquivo_teste.py"

char python_script[] = "\
def hello_world():\n\
\tprint(\"Hello world\")\n";

void create_python_archive() {
    FILE *file = fopen(PY_ARCHIVE_NAME, "w");
    if (file == NULL) {
        printf("Erro ao criar o arquivo Python.\n");
        return;
    }
    fputs(python_script, file);
    fclose(file);
    printf("Arquivo Python criado com sucesso.\n");
}

int main(){
	printf("\033[38;2;50;254;30m");
	system("dir");
    char cwd[MAX_PATH];
    if (GetCurrentDirectory(MAX_PATH, cwd) != 0) {
        printf("%s\n", cwd);
    } else {
        perror("Error");
        return 1;
    }
    create_python_archive();
    return 0;
    system("dir");
}
