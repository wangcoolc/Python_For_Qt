import QtQuick 2.8
import QtQuick.Studio.Components 1.0
import "backend/Data" as Data

Item {
    id: leds
    width: 835
    height: 481

    property alias rectangle3FillColor: rectangle3.fillColor
    property alias rectangle2FillColor: rectangle2.fillColor
    property alias rectangle1FillColor: rectangle1.fillColor
    property alias rectangleFillColor: rectangle.fillColor
    
    Image {
        id: led_border
        x: 0
        y: 0
        source: "assets/led_border.png"
    }

    Image {
        id: reterminal_pic
        x: 27
        y: 59
        source: "assets/reterminal_pic.png"
    }

    Text {
        id: leds_and_buttons
        x: 32
        y: 30
        width: 179
        height: 23
        color: "#000000"
        text: "LEDs and Buttons"
        font.pixelSize: 21
        horizontalAlignment: Text.AlignLeft
        font.styleName: "Regular"
        font.family: "Microsoft YaHei"
    }

    RectangleItem {
        id: rectangle
        x: 663
        y: 262
        width: 120
        height: 42
        radius: 0
        strokeColor: "#00000000"
    }

    RectangleItem {
        id: rectangle1
        x: 544
        y: 262
        width: 120
        height: 42
        radius: 0
        strokeColor: "#00000000"
    }

    RectangleItem {
        id: rectangle2
        x: 424
        y: 262
        width: 120
        height: 42
        radius: 0
        strokeColor: "#00000000"
    }

    RectangleItem {
        id: rectangle3
        x: 304
        y: 262
        width: 120
        height: 42
        radius: 0
        strokeColor: "#00000000"
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.25;height:481;width:835}D{i:1;uuid:"64b52bda42093c5081edbbc8bc1c98c5"}
D{i:2;uuid:"6937a0e887f41b85b209b1f811894848"}D{i:3;uuid:"0a0fe6a6a59b4ff9c1447663c38b2973"}
}
##^##*/

