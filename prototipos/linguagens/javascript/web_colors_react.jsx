import {WebColors} from "./web_colors.js";

WebColors.build();

class ReadWebColors{
static i = 0;
static next(){
  let j = ReadWebColors.i;
  const colors = WebColors.colors;
  if(j>=colors.length){
    return {index: -1, hexadecimal: "#000000", name: "Error"};
  }
  const colorInfo = {
    index: j,
    hexadecimal: colors[j].hexadecimal,
    name: colors[j].name
  };
  ReadWebColors.i++;
  return colorInfo;
}
}

const ColorSquare = () => {
  const [itemHover, setItemHover] = React.useState(false);
  const [colorNameView, setColorNameView] = React.useState("");
  const [colorHexView, setColorHexView] = React.useState("");
  const colorInfo = React.useMemo(() => ReadWebColors.next(), []);
  const defaultStyle = {
    position: "relative",
    backgroundColor: colorInfo.hexadecimal,
    opacity: "0.8",
    width: "24px",
    height: "24px",
    border: "2px solid #2F2F2F",
    borderRadius: "0px",
    marginLeft: "0px",
    marginTop: "0px"
  };
  const hoverStyle = {
    position: "relative",
    backgroundColor: colorInfo.hexadecimal,
    opacity: "1",
    width: "26px",
    height: "24px",
    border: "2px solid #2F2F2F",
    borderRadius: "5px",
    marginLeft: "0px",
    marginTop: "0px"
  };

  return (
    <div>
      <div
        style={itemHover ? hoverStyle : defaultStyle}
        onMouseEnter={() => setItemHover(true)}
        onMouseLeave={() => setItemHover(false)}
      />
      {!itemHover && (
        <div style={{ color: `${colorInfo.hexadecimal}` }}>
          {/* div mostrada quando itemHover == false */}
        </div>
      )}
      {itemHover && (
        <div>
        <div style={{ color: `${colorInfo.hexadecimal}` }}/>
        <div style={{ color: `${colorInfo.hexadecimal}`, position: "absolute", left: "50%", top: "50%"}}>{colorInfo.name}</div>
        </div>
      )}
    </div>
  );
}

const Pallette = () => {
return(<div style={{ backgroundColor: "rgba(0, 0, 0, 0.50)", width: 900, height: "70vh", position: "relative", top: "300px", left: "32px"}}>
    <div style={{display:"inline-block",backgroundColor:"rgba(0, 0, 0, 0.70)",position:"relative",top:"0px",left:"0px"}}>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    <div style={{ display: "flex", flexDirection: "row"}}>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    <ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/><ColorSquare/>
    </div>
    </div>
    </div>
  );
}

export {ColorSquare, Pallette}
