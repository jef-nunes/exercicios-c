// NodeJS terminal customisation

class Terminal {

private static process = require("process")
private static readline = require("readline")

  private static foregroundDecimalColor(r, g, b): string {
    return `\x1b[38;2;${r};${g};${b}m`;
  }

  private static foregroundHexColor(hexcode): string {
    let r = parseInt(hexcode.slice(1, 3), 16);
    let g = parseInt(hexcode.slice(3, 5), 16);
    let b = parseInt(hexcode.slice(5, 7), 16);
    return `\x1b[38;2;${r};${g};${b}m`;
  }

  public static textColor = {
    dec: Terminal.foregroundDecimalColor,
    hex: Terminal.foregroundHexColor,
  };

  public static clearLogs(): void {
    Terminal.readline.cursorTo(Terminal.process.stdout, 0, 0);
    Terminal.readline.clearScreenDown(Terminal.process.stdout);
  }

  public static hideCursor(): void {
    Terminal.process.stdout.write("\x1b[?25l");
  }

  public static showCursor(): void {
    Terminal.process.stdout.write("\x1b[?25h");
  }
}

module.exports = Terminal;
