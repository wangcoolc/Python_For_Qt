import QtQuick 2.8
import QtQuick.Controls 2.1
import QtQuick.Studio.Effects 1.0

Item {
    id: settings
    width: 1920
    height: 1080

    // 定义信号 
    Image {
        id: settingsAsset
        x: 0
        y: 0
        source: "assets/settings.png"

        Slider {
            id: slider
            x: 1069
            y: 884
            width: 548
            height: 62
            scale: 1.5
            stepSize: 1
            to: 100
            value: 50
            onValueChanged:
            {
                settings.sendClicked(value)
            }
        }

        Switch {
            id: switch1
            x: 1279
            y: 121
            width: 62
            height: 41
            text: "dasdad"
            checkable: true
            scale: 2.5
            onClicked: {
                console.log(1111111111111)
            }
            
        }

        Text {
            id: text1
            x: 1129
            y: 111
            text: qsTr("OFF")
            font.pixelSize: 50
        }

        Text {
            id: text2
            x: 1413
            y: 112
            text: qsTr("ON")
            font.pixelSize: 50
        }

        Switch {
            id: switch2
            x: 1280
            y: 239
            width: 62
            height: 41
            text: "dasdad"
            checkable: true
            scale: 2.5
        }

        Switch {
            id: switch4
            x: 1285
            y: 615
            width: 62
            height: 41
            text: "dasdad"
            checkable: true
            scale: 2.5
        }

        Switch {
            id: switch5
            x: 1282
            y: 491
            width: 62
            height: 41
            text: "dasdad"
            checkable: true
            scale: 2.5
        }

        Switch {
            id: switch6
            x: 1281
            y: 365
            width: 62
            height: 41
            text: "dasdad"
            checkable: true
            scale: 2.5
        }

        Switch {
            id: switch7
            x: 1286
            y: 751
            width: 62
            height: 41
            text: "dasdad"
            checkable: true
            scale: 2.5
        }

        Text {
            id: text3
            x: 1129
            y: 230
            text: qsTr("OFF")
            font.pixelSize: 50
        }

        Text {
            id: text4
            x: 1129
            y: 356
            text: qsTr("OFF")
            font.pixelSize: 50
        }

        Text {
            id: text5
            x: 1129
            y: 482
            text: qsTr("OFF")
            font.pixelSize: 50
        }

        Text {
            id: text6
            x: 1129
            y: 606
            text: qsTr("OFF")
            font.pixelSize: 50
        }

        Text {
            id: text7
            x: 1129
            y: 742
            text: qsTr("OFF")
            font.pixelSize: 50
        }

        Text {
            id: text8
            x: 1413
            y: 230
            text: qsTr("ON")
            font.pixelSize: 50
        }

        Text {
            id: text9
            x: 1413
            y: 356
            text: qsTr("ON")
            font.pixelSize: 50
        }

        Text {
            id: text10
            x: 1413
            y: 482
            text: qsTr("ON")
            font.pixelSize: 50
        }

        Text {
            id: text11
            x: 1413
            y: 606
            text: qsTr("ON")
            font.pixelSize: 50
        }

        Text {
            id: text12
            x: 1413
            y: 742
            width: 68
            height: 60
            text: qsTr("ON")
            font.pixelSize: 50
        }
    }

    Textlist {
        id: textlist
        x: 553
        y: 111
        width: 325
        height: 829
    }

    Ui_navigate_2 {
        id: ui_navigate_2
        x: 0
        y: 0
        width: 160
        height: 1080
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75;height:1080;width:1920}D{i:5}D{i:6}D{i:7}D{i:8}D{i:9}D{i:10}
D{i:11}D{i:12}D{i:13}D{i:14}D{i:15}D{i:16}D{i:17}D{i:18}D{i:19}D{i:20}D{i:1;uuid:"db758c043a516da3a6cc8edd0f479654_asset"}
}
##^##*/

