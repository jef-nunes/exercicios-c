// Manipulate arrays
class ArrayTools {
  // From an array of strings, create an array of objects
  public static stringToObject(arr: string[]) {
    let _arr: any[] = [];
    arr.forEach((element) => {
      let _element = { [`${element}`]: "" };
      _arr.push(_element);
    });
    return _arr;
  }

  // Insert keys on each element of array
  public static insertKey(arr: any[], key: string) {
    let _arr: any[] = [];
    arr.forEach((element) => {
      let _element = element;
      _element[`${key}`] = "";
      _arr.push(_element);
    });
    return _arr;
  }
}

if(typeof module !== 'undefined' && module.exports){
  module.exports = ArrayTools;
}

if(typeof exports !== 'undefined'){
  export {ArrayTools};
}
