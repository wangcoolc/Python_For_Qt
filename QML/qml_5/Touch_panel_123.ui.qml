import QtQuick 2.8

Item {
    id: touch_panel_123
    width: 835
    height: 481

    Image {
        id: touch_border
        x: 0
        y: 0
        source: "assets/touch_border.png"
    }

    Text {
        id: touch_panel
        x: 45
        y: 25
        width: 128
        height: 26
        color: "#000000"
        text: "Touch Panel"
        font.pixelSize: 21
        horizontalAlignment: Text.AlignLeft
        font.styleName: "Regular"
        font.family: "Microsoft YaHei"
    }
}

/*##^##
Designer {
    D{i:0;height:481;width:835}D{i:1;uuid:"f4f6d6b59c6d43eba80dfe6225b74ee7"}D{i:2;uuid:"341dd9e6d422d3af13b56aa034c3fb0e"}
}
##^##*/

