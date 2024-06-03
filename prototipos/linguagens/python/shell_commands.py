import platform
import subprocess
from os import system
from types import NoneType
from typing import Dict, List

static = staticmethod
void = NoneType
Red = "\033[91m"
Green = "\033[92m"
Yellow = "\033[93m"
Blue = "\033[94m"
Purple = "\033[95m"
Aqua = "\033[96m"
White = "\033[97m"
DarkRed = "\033[31m"

class _Unix_:

    @static
    def pwd()->void:
        p = Shell.run("pwd")
        output, error = p.communicate()
        print(Blue+output+Green)

    @static
    def ls(target: str = "?")->void:
        _Unix_.pwd()
        command: List[str]=["ls"]     
        if target != "?":
            command.append(target)
        p = Shell.run(command)
        output, error = p.communicate()
        splited_lines: List = output.splitlines()
        if len(splited_lines) <= 0:
            print(DarkRed+error+Green)
        else:
            splited_lines.sort()
            print(Blue)
            i: int = 0
            for element in splited_lines:
                print("{} - {}".format(i,element))
                i+=1
            print(Green)
    @static
    def localhost_details()->void:
        # ip adresses
        p1 = Shell.run(["ip","addr"])
        p1_output, p1_error = p1.communicate()
        p1_edit: List = p1_output.splitlines()
        for i in range(0,len(p1_edit)):
            p1_edit[i] = "  ".join(p1_edit[i].split())
            if not p1_edit[i][0].isdigit():
                p1_edit[i] = "   {}".format(p1_edit[i])
            else:
                p1_edit[i] = p1_edit[i][2:]
                if p1_edit[i].find("<") != -1:
                    p1_edit[i] = "\n{}{}{}".format(\
                        Aqua,\
                        p1_edit[i].split("<")[0],\
                        Green)
                else:
                   p1_edit[i] = "\n{}{}{}".format(\
                        Aqua,\
                        p1_edit[i],\
                        Green)

        p1_final: str = ""
        for line in p1_edit:
            p1_final+="\n{}".format(line)

        # ports
        p2 = Shell.run(["netstat","-tuln"])
        p2_output, p2_error = p2.communicate()
        print("__________ Localhost details __________\
            \n\n{}IP addresses:{}\
                 {}\n\n{}Open ports:{} {}".format(\
                        White,Green,p1_final,\
                            White,Green,p2_output))

class _SetColor_:
    @static
    def red()->void:
        print("\033[91m")
    @static
    def green()->void:
        print("\033[92m")
    @static
    def blue()->void:
        print("\033[94m")

class Shell:
    set_color = _SetColor_()
    unix = _Unix_()
    @static
    def clear_logs()->void:
        system("cls || clear")
    @static
    def run(command: List[str]|str|None = None) -> subprocess.Popen:
        if command == None:
            print("Error - No command specified")
            command = ["echo","?"]
        print("\n {}» {}{}".format(Purple,command,Green))
        process = subprocess.Popen(command,\
            stdout=subprocess.PIPE,\
            stderr=subprocess.PIPE,\
            text=True)
        return process

def main()->void:
    x: str = platform.system()
    # debug
    if x == "Linux" or x == "Darwin":
        Shell.clear_logs()
        Shell.set_color.green()
        Shell.unix.localhost_details()
        Shell.unix.pwd()
        Shell.unix.ls()
        Shell.unix.ls("../")
        Shell.set_color.green()
    else:
        pass

if __name__ == "__main__":
    main()
