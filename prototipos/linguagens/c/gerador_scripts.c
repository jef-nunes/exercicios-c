#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// detectando sistema
// 0 = windows, 1 = unix
#ifdef _WIN32
#include <windows.h>
#define OS 0
#else
#define OS 1
#endif

// tamanho de string
// para comandos shell
#define SHELL_STR_LEN 100

// logica para gerar um arquivo de script
// e em seguida mover para o diretorio 
// /scripts/
void genscript(char* archive_name, char* script) {
    FILE *a = fopen(archive_name, "w");
    if (a == NULL) {
        printf("\nError");
        return;
    }
    fputs(script, a);
    fclose(a);
    printf("\n '%s' created",archive_name);
    if(OS == 1){
         char m[SHELL_STR_LEN];
         snprintf(m, SHELL_STR_LEN, "mv %s %s", archive_name, "scripts");
         system(m);
    } else {
         char m[SHELL_STR_LEN];
         snprintf(m, SHELL_STR_LEN, "move %s %s", archive_name, "scripts");
         system(m);
    }
    printf("\n '%s' moved to /scripts/",archive_name);
}

void testing(){
    // gerando scripts 
    // hello world
    // c
    genscript("hello_world.c",\
    "#include <stdio.h>"
    "\n int main(){"
    "\n printf(\"Hello world\");"
    "\n return 0;"
    "\n }");  
    // c++
    genscript("hello_world.cc",\
    "#include <iostream>"
    "\n int main(){"
    "\n std::cout << \"Hello world\" << std::endl;"
    "\n return 0;"
    "\n }");
    // go
    genscript("hello_world.go",\
    "package main\n\nimport \"fmt\"\n\nfunc main() {\n\tfmt.Println(\"Hello world\")\n}");
    // haskell
    genscript("hello_world.hs",\
    "main = putStrLn \"Hello world\"");
    // java
    genscript("HelloWorld.java",\
    "class HelloWorld {"
    "\npublic static void main(String[] args){"
    "\n\tSystem.out.println(\"Hello world\");"
    "\n }"
    "\n}");
    // javascript
    genscript("hello_world.js",\
    "console.log(\"Hello world\");");
    // lua
    genscript("hello_world.lua",\
    "print(\"Hello world\")");
    // perl
    genscript("hello_world.pl",\
    "print \"Hello world\\n\";");
    // php
    genscript("hello_world.php",\
    "<?php"
    "\necho \"Hello world\";"
    "\n?>");
    // python
    genscript("hello_world.py",\
    "def hello_world():"
    "\n\tprint(\"Hello world\")");
    // ruby
    genscript("hello_world.rb",\
    "puts \"Hello world\"");
    // rust
    genscript("hello_world.rs",\
    "fn main() {\n\tprintln!(\"Hello world\");\n}");
    // scala
    genscript("hello_world.scala",\
    "object HelloWorld extends App {\n\tprintln(\"Hello world\")\n}");
    // swift
    genscript("hello_world.swift",\
    "import Swift\n\nprint(\"Hello world\")");
    
    printf("\n\n");
    system("ls || dir");
    printf("\n");
    system("ls scripts || dir scripts");
}

int main(){
    // apagando o diretorio gerado
    // anteriormente caso exista
    if(OS == 1){
        system("rm -r scripts");
    } else{
        system("rmdir /s /q scripts");
    }

    // criando novo diretorio
    system("mkdir scripts");
	  printf("\033[38;2;50;254;30m");
    system("cls || clear");
    printf("\n[Gerador de scripts]\n");

    // testando
    testing();

    printf("\n");
    return 0;
}
