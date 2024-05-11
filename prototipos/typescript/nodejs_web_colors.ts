// Cores padrão HTML / Web em Node JS (TypeScript)
class WebColors {
    private static id = 1;
    public static colors: any[] = [];

    private constructor() { }
    public static build(): void {
        let _arr = ["skip_index_0"];
        for (let i = 1; i < 142; i++) {
          _arr[i] = `color_${i}`;
        }
        let __skip = _arr[0];
        _arr = stringToObject(_arr);
        _arr = insertKey(_arr, "name");
        _arr = insertKey(_arr, "hexadecimal");
        _arr[0] = __skip;
        WebColors.colors = _arr;
        WebColors.__make_colors();
   }
  
    // Method returns a hexadecimal rgb from a HTML color name
    public static hex(str: string): string {
      for (let i = 1; i < WebColors.length; i++) {
        if (WebColors.colors[i].name.toLowerCase() === str.toLowerCase()) {
          return WebColors.colors[i].hexadecimal;
        }
      }
      return "#123456";
    }
  
    private static __add(name: string, hexadecimal: string): void {
      WebColors.colors[WebColors.id].name = name;
      WebColors.colors[WebColors.id].hexadecimal = hexadecimal;
      WebColors.id++;
    }
  
    private static __make_colors(): void{
      const f=function(name:string,hexadecimal:string): void{
        if(name != undefined && hexadecimal != undefined){
        WebColors.__add(name,hexadecimal);
        }
       } 
       f("Pink", "#FFC0CB");
       f("LightPink", "#FFB6C1");
       f("HotPink", "#FF69B4");
       f("DeepPink", "#FF1493");
       f("PaleVioletRed", "#DB7093");
       f("MediumVioletRed", "#C71585");  
       f("Lavender", "#E6E6FA");
       f("Thistle", "#D8BFD8");
       f("Plum", "#DDA0DD");
       f("Orchid", "#DA70D6");
       f("Violet", "#EE82EE");
       f("Fuchsia", "#FF00FF");
       f("Magenta", "#FF00FF");
       f("MediumOrchid", "#BA55D3");
       f("DarkOrchid", "#9932CC");
       f("DarkViolet", "#9400D3");
       f("BlueViolet", "#8A2BE2");
       f("DarkMagenta", "#8B008B");
       f("Purple", "#800080");
       f("MediumPurple", "#9370DB");
       f("MediumSlateBlue", "#7B68EE");
       f("SlateBlue", "#6A5ACD");
       f("DarkSlateBlue", "#483D8B");
       f("RebeccaPurple", "#663399");
       f("Indigo", "#4B0082");
       f("LightSalmon", "#FFA07A");
       f("Salmon", "#FA8072");
       f("DarkSalmon", "#E9967A");
       f("LightCoral", "#F08080");
       f("IndianRed", "#CD5C5C");
       f("Crimson", "#DC143C");
       f("Red", "#FF0000");
       f("FireBrick", "#B22222");
       f("DarkRed", "#8B0000");
       f("Orange", "#FFA500");
       f("DarkOrange", "#FF8C00");
       f("Coral", "#FF7F50");
       f("Tomato", "#FF6347");
       f("OrangeRed", "#FF4500");     
       f("Gold", "#FFD700");
       f("Yellow", "#FFFF00");
       f("LightYellow", "#FFFFE0");
       f("LemonChiffon", "#FFFACD");
       f("LightGoldenRodYellow", "#FAFAD2");
       f("PapayaWhip", "#FFEFD5");
       f("Moccasin", "#FFE4B5");
       f("PeachPuff", "#FFDAB9");
       f("PaleGoldenRod", "#EEE8AA");
       f("Khaki", "#F0E68C");
       f("DarkKhaki", "#BDB76B");
       f("GreenYellow", "#ADFF2F");
       f("Chartreuse", "#7FFF00");
       f("LawnGreen", "#7CFC00");
       f("Lime", "#00FF00");
       f("LimeGreen", "#32CD32");
       f("PaleGreen", "#98FB98");
       f("LightGreen", "#90EE90");
       f("MediumSpringGreen", "#00FA9A");
       f("SpringGreen", "#00FF7F");
       f("MediumSeaGreen", "#3CB371");
       f("SeaGreen", "#2E8B57");
       f("ForestGreen", "#228B22");
       f("Green", "#008000");
       f("DarkGreen", "#006400");
       f("YellowGreen", "#9ACD32");
       f("OliveDrab", "#6B8E23");
       f("DarkOliveGreen", "#556B2F");
       f("MediumAquaMarine", "#66CDAA");
       f("DarkSeaGreen", "#8FBC8F");
       f("LightSeaGreen", "#20B2AA");
       f("DarkCyan", "#008B8B");
       f("Teal", "#008080");
       f("Aqua", "#00FFFF");
       f("Cyan", "#00FFFF");
       f("LightCyan", "#E0FFFF");
       f("PaleTurquoise", "#AFEEEE");
       f("Aquamarine", "#7FFFD4");
       f("Turquoise", "#40E0D0");
       f("MediumTurquoise", "#48D1CC");
       f("DarkTurquoise", "#00CED1");
       f("CadetBlue", "#5F9EA0");
       f("SteelBlue", "#4682B4");
       f("LightSteelBlue", "#B0C4DE");
       f("LightBlue", "#ADD8E6");
       f("PowderBlue", "#B0E0E6");
       f("LightSkyBlue", "#87CEFA");
       f("SkyBlue", "#87CEEB");
       f("CornflowerBlue", "#6495ED");
       f("DeepSkyBlue", "#00BFFF");
       f("DodgerBlue", "#1E90FF");
       f("RoyalBlue", "#4169E1");
       f("Blue", "#0000FF");
       f("MediumBlue", "#0000CD");
       f("DarkBlue", "#00008B");
       f("Navy", "#000080");
       f("MidnightBlue", "#191970");
       f("Cornsilk", "#FFF8DC");
       f("BlanchedAlmond", "#FFEBCD");
       f("Bisque", "#FFE4C4");
       f("NavajoWhite", "#FFDEAD");
       f("Wheat", "#F5DEB3");
       f("BurlyWood", "#DEB887");
       f("Tan", "#D2B48C");
       f("RosyBrown", "#BC8F8F");
       f("SandyBrown", "#F4A460");
       f("GoldenRod", "#DAA520");
       f("DarkGoldenRod", "#B8860B");
       f("Peru", "#CD853F");
       f("Chocolate", "#D2691E");
       f("Olive", "#808000");
       f("SaddleBrown", "#8B4513");
       f("Sienna", "#A0522D");
       f("Brown", "#A52A2A");
       f("Maroon", "#800000");
       f("White", "#FFFFFF");
       f("Snow", "#FFFAFA");
       f("HoneyDew", "#F0FFF0");
       f("MintCream", "#F5FFFA");
       f("Azure", "#F0FFFF");
       f("AliceBlue", "#F0F8FF");
       f("GhostWhite", "#F8F8FF");
       f("WhiteSmoke", "#F5F5F5");
       f("SeaShell", "#FFF5EE");
       f("Beige", "#F5F5DC");
       f("OldLace", "#FDF5E6");
       f("FloralWhite", "#FFFAF0");
       f("Ivory", "#FFFFF0");
       f("AntiqueWhite", "#FAEBD7");
       f("Linen", "#FAF0E6");
       f("LavenderBlush", "#FFF0F5");
       f("MistyRose", "#FFE4E1");
       f("Gainsboro", "#DCDCDC");
       f("LightGray", "#D3D3D3");
       f("Silver", "#C0C0C0");
       f("DarkGray", "#A9A9A9");
       f("DimGray", "#696969");
       f("Gray", "#808080");
       f("LightSlateGray", "#778899");
       f("SlateGray", "#708090");
       f("DarkSlateGray", "#2F4F4F");
       f("Black", "#000000");
    }
}
  
  // Tools for working on arrays
  // (also distributed on module array_tools.ts)
  function stringToObject(arr: string[]) {
    let _arr: any[] = [];
    arr.forEach((element) => {
      let _element = { [`${element}`]: "" };
      _arr.push(_element);
    });
    return _arr;
  }
  
  function insertKey(arr: any[], key: string) {
    let _arr: any[] = [];
    arr.forEach((element) => {
      let _element = element;
      _element[`${key}`] = "";
      _arr.push(_element);
    });
    return _arr;
  }
  
  WebColors.build();
  export { WebColors };
  
