package tools;
public class StyledTerminal{
    public static void clearLogs() {
        String os = System.getProperty("os.name").toLowerCase();
        boolean isWindows = os.contains("win");

        if (isWindows) {
            try {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {
            try {
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static void hideCursor(){
        System.out.print("\033[?25l");
    }

    public static void allTextColor(int r, int g, int b) {
        System.out.print("\033[38;2;" + r + ";" + g + ";" + b + "m");
    }
}
