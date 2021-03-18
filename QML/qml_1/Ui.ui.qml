import QtQuick 2.8
import "backend/Data" as Data
import QtQuick.Layouts 1.3
//import Qt.SafeRenderer 1.1
import QtQuick.Controls 2.1

//import QtStudio3D 2.3
Item {
    id: ui
    width: 1920
    height: 1080

    property alias axisXvalue: axis.count

    Image {
        id: uiAsset
        x: 0
        y: 0
        source: "assets/ui.png"
    }

    Touch_panel {
        id: touch_panel
        x: 1065
        y: 488
        width: 821
        height: 489
    }

    Axis {
        id: axis
        x: 195
        y: 487
        width: 850
        height: 490
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
        onTriggered: axis.timerChange()
        interval: 1000
    }

    Storage_usage {
        id: storage_usage
        x: 1342
        y: 110
        width: 545
        height: 316
        displaystore: Data.Values.displayflash
        storeframe: Data.Values.flash
    }

    Ram_usage {
        id: ram_usage
        x: 769
        y: 110
        width: 544
        height: 315
        ramdisplay: Data.Values.displayram
        ramframe: Data.Values.ram
    }

    Cpu_usage {
        id: cpu_usage
        x: 196
        y: 110
        width: 544
        height: 316
       displaycpu: Data.Values.displaycpu
       cpuframe: Data.Values.cpu
    }

    Ui_navigate {
        id: ui_navigate
        x: 0
        y: 0
        width: 159
        height: 1080
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/


/*##^## Designer {
    D{i:5;invisible:true}
}
 ##^##*/

