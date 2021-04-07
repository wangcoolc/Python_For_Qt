import QtQuick 2.8
import "backend/Data" as Data

Item {
    id: hardware
    width: 1280
    height: 720

    property alias axisXvalue: accel1.count
    // property alias accelchange: accel1.timerChange()

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

        property alias axisXvalue: accel1.count
        property int count: 0
        function timerChange() {
<<<<<<< Updated upstream
            axisX.append(accel1.count,Data.Values.displayaxisX)
            axisY.append(accel1.count,Data.Values.displayaxisY)
            axisZ.append(accel1.count,Data.Values.displayaxisZ)
            accel1.count = accel1.count + 1
            if ((accel1.count % 5) == 0 ) {
                axisX.remove(0)
                axisY.remove(0)
                axisZ.remove(0)
=======
        axisX.append(count,Data.Values.displayaxisX)
        // axisY.append(count,Data.Values.displayaxisY)
        // axisZ.append(count,Data.Values.displayaxisZ)
        count = count + 1
        if ((accel1.count % 5) == 0 ) {
            accel1.axisX.remove(0)
            // accel1.axisY.remove(0)
            // accel1.axisZ.remove(0)
>>>>>>> Stashed changes
            }
        }

        // axisX: Data.Values.test1
        // axisY: Data.Values.test2
        // axisZ: Data.Values.test3
    }

    property Timer axisTimer: Timer{
        running: true
        repeat: true
        onTriggered: accel1.timerChange()
        interval: 100
    }

    Touch_panel_123 {
        id: touch_panel_123
        x: 566
        y: 295
        width: 835
        height: 481
        circle5Scale: Data.Values.circle5Scale
        circle4Scale: Data.Values.circle4Scale
        circle3Scale: Data.Values.circle3Scale
        circle2Scale: Data.Values.circle2Scale
        circle1Scale: Data.Values.circle1Scale
        circle5Visible: Data.Values.circle5Visible
        circle4Visible: Data.Values.circle4Visible
        circle3Visible: Data.Values.circle3Visible
        circle2Visible: Data.Values.circle2Visible
        circle1Visible: Data.Values.circle1Visible
        circle5Y: Data.Values.circle5y
        circle5X: Data.Values.circle5x
        circle4Y: Data.Values.circle4y
        circle4X: Data.Values.circle4x
        circle3Y: Data.Values.circle3y
        circle3X: Data.Values.circle3x
        circle2Y: Data.Values.circle2y
        circle2X: Data.Values.circle2x
        circle1Y: Data.Values.circle1y
        circle1X: Data.Values.circle1x
        scale: 0.67
    }

    Leds {
        id: leds
        x: 566
        y: -50
        width: 835
        height: 481
        scale: 0.67
        o1Visible: Data.Values.o1Visible
        f3Visible: Data.Values.f3Visible
        f2Visible: Data.Values.f2Visible
        f1Visible: Data.Values.f1Visible
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

