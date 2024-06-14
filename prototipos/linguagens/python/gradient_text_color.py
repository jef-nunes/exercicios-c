from types import NoneType
from typing import List, Tuple

void = NoneType
DecimalRGB = Tuple[int, int, int]

class TextColorGradient:

    colors: List[DecimalRGB]

    def __init__(self, set_colors: List[DecimalRGB]) -> void:
        if len(set_colors) >= 2:
            self.colors = set_colors
        else:
            self.colors = [(150, 150, 150), (250, 250, 250)]

    def paint(self, text: str) -> str:
        text_len = len(text)
        painted_text = ""
        if text_len >= 2:
            if text_len > len(self.colors):
                set_max = float(text_len) if text_len % 2 == 0 else float(text_len - 1)
                chars_share_color = int(set_max / len(self.colors))
                for i, char in enumerate(text):
                    color_index = min(i // chars_share_color, len(self.colors) - 1)
                    color = self.colors[color_index]
                    painted_text += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"
                painted_text += "\033[0m"
            else:
                for i, char in enumerate(text):
                    color = self.colors[i]
                    painted_text += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{char}"
                painted_text += "\033[0m"
            return painted_text
        else:
            return f"\033[38;2;{self.colors[0][0]};{self.colors[0][1]};{self.colors[0][2]}m{text}\033[0m"

def test():
    grad1 = [(255, 0, 0),(255, 69, 0),(255, 165, 0),(255, 215, 0),(255, 255, 0)]
    grad1_a = TextColorGradient(grad1)
    grad1_b = TextColorGradient(list(reversed(grad1)))
    
    grad2 = [(75, 146, 254), (73, 146, 254), (76, 164, 234), (92, 195, 254), (140, 198, 254)]
    grad2_a = TextColorGradient(grad2)
    grad2_b = TextColorGradient(list(reversed(grad2)))

    grad3 = [((37, 179, 23)),(33, 255, 44)]
    grad3_a = TextColorGradient(grad3)
    grad3_b = TextColorGradient(list(reversed(grad3)))
    

    print("{}".format(grad1_b.paint("Lorem ipsum dolor sit amet, consectetur adipiscing elit,")))
    print("{}".format(grad1_b.paint("sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")))
    print("{}".format(grad1_b.paint("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris ")))
    print("{}".format(grad1_b.paint("nisi ut aliquip ex ea commodo consequat.")))
    print("{}".format(grad2_a.paint("Duis aute irure dolor in reprehenderit in voluptate velit esse ")))
    print("{}".format(grad2_a.paint("cillum dolore eu fugiat nulla pariatur.")))
    print("{}".format(grad2_a.paint("Excepteur sint occaecat cupidatat non proident, sunt in culpa ")))
    print("{}".format(grad2_a.paint("qui officia deserunt mollit anim id est laborum.")))
    print("\n")
    print("{}".format(grad3_a.paint("██╗  ██╗███████╗██╗     ██╗      ██████╗  ")))
    print("{}".format(grad3_b.paint("██║  ██║██╔════╝██║     ██║     ██╔═══██╗ ")))
    print("{}".format(grad3_a.paint("███████║█████╗  ██║     ██║     ██║   ██║ ")))
    print("{}".format(grad3_b.paint("██╔══██║██╔══╝  ██║     ██║     ██║   ██║ ")))
    print("{}".format(grad3_a.paint("██║  ██║███████╗███████╗███████╗╚██████╔╝ ")))
    print("{}".format(grad3_b.paint("╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ")))
    print("\n")                                             
    print("{}".format(grad3_a.paint("██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ ██╗ ")))
    print("{}".format(grad3_b.paint("██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗██║ ")))
    print("{}".format(grad3_a.paint("██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║██║ ")))
    print("{}".format(grad3_b.paint("██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║╚═╝ ")))
    print("{}".format(grad3_a.paint("╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝██╗ ")))
    print("{}".format(grad3_b.paint(" ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ")))

if __name__ == "__main__":
    from os import system
    system("cls || clear")
    test()