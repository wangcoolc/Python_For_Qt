import QtQuick 2.8
import "backend/Data" as Data

Item {
    id: hardware
    width: 1280
    height: 720

    property alias axisXvalue: accel1.count

    Image {
        id: hardwareAsset
        x: 0
        y: 0
        width: 1280
        height: 720
        source: "assets/hardware.png"
    }

    Light {
        id: light
        x: -5
        y: -50
        width: 833
        height: 480
        scale: 0.67
    }

    Accel1 {
        id: accel1
        x: -5
        y: 295
        width: 833
        height: 480
        scale: 0.67

        property int count: 0
        function timerChange() {
            console.log("displaycount",Data.Values.displaycount)
            console.log("displayaxisX123",Data.Values.displayaxisX)
            axisX.append(Data.Values.displaycount,Data.Values.displayaxisX)
            axisY.append(Data.Values.displaycount,Data.Values.displayaxisY)
            axisZ.append(Data.Values.displaycount,Data.Values.displayaxisZ)
            count++;
            // if (count > 5) {
            //     axisX.remove(0)
            //     axisY.remove(0)
            //     axisZ.remove(0)
            // }
        }
    }

    property Timer axisTimer: Timer{
        running: true
        repeat: true
        onTriggered: accel1.timerChange()
        interval: 1000
    }

    Touch_panel_123 {
        id: touch_panel_123
        x: 566
        y: 295
        width: 835
        height: 481
        scale: 0.67
    }

    Leds {
        id: leds
        x: 566
        y: -50
        width: 835
        height: 481
        scale: 0.67
    }

    Ui_navigate_4 {
        id: ui_navigate_4
        x: -26
        y: -178
        width: 159
        height: 1080
        scale: 0.67
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75;uuid:"db758c043a516da3a6cc8edd0f479654"}D{i:1;uuid:"db758c043a516da3a6cc8edd0f479654_asset"}
}
##^##*/

