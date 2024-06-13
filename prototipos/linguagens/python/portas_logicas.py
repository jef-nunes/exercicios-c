from os import system
from types import NoneType
from typing import List, Any
from dataclasses import dataclass

@dataclass
class question:
    problem: str
    answer: Any

void = NoneType

def logical(port:str,a,b=False)->bool:
    match port:
        case "AND":
            return a and b
        case "OR":
            return a or b
        case "NOT":
            return not a
        case "NAND":
            return not(a and b)
        case "NOR":
            return not(a or b)
        case "XOR":
            return a != b
        case "XNOR":
            return a == b 

def test()->void:
    a = question('AND (1>2, 3+1 == 4)',logical("AND", 1>2, 3+1 == 4))
    b = question('OR (4+1 == 5, 3-1 == 0)', logical("OR", 4+1 == 5, 3-1 == 0))
    c = question('NOT (1+1 == 2)', logical("NOT", 1+1 == 2))
    d = question('NAND (1+1 == 2, 10+10 == -5)', logical("NAND", 1+1 == 2, 10+10 == -5))
    e = question('NOR (1-1 == 0, 1-1 == 1)', logical("NOR", 1-1 == 0, 1-1 == 1))
    f = question('XOR (0, 0)', logical("XOR", 0, 0))
    g = question('XNOR (0, 0)', logical("XNOR", 0, 0))

    results: List[question] = [a,b,c,d,e,f,g]

    for r in results:
        print("{} : {}".format(r.problem,r.answer))


if __name__ == "__main__":
    system("cls || clear")
    test()
