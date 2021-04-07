import QtQuick 2.8
import QtQuick.Controls 2.1

ApplicationWindow {
    id: application
    title: "ReTerminal UI"
    width: 1280
    height: 720
    visible: true
    visibility: "FullScreen"

    property var iniITEM: "Home.ui.qml"

    StackView {
        id: stackview
        width: 1280
        height: 720
        // transform: Rotation {
        //     origin.x: 600; origin.y:500; angle: 90
        // }
        replaceEnter: Transition {
                  PropertyAnimation{
                      property: "opacity"
                      from: 0
                      to: 1
                      duration: 1/20
                  }
              }

        replaceExit: Transition {
                  PropertyAnimation{
                      property: "opacity"
                      from: 1
                      to: 0
                      duration: 1/20
                  }
        }

        initialItem: iniITEM

        // Hardware {
        //     id: hardware
        //     x: 0
        //     y: 0
        // }
    }

    Button {
        id: button
        x: -21
        y: -22
        width: 172
        height: 181
        opacity: 0
        scale: 0.76
        onClicked: {
            stackview.replace("Home.ui.qml")
        }
    }

    Button {
            id: button5
            x: 135
            y: 454
            width: 362
            height: 360
            opacity: 0
            scale: 0.76
            onClicked: {
                stackview.replace("Ui.ui.qml")
            }
        }

    
    Button {
            id: button6
            x: 566
            y: 454
            width: 362
            height: 360
            opacity: 0
            scale: 0.76
            onClicked: {
                stackview.replace("Hmi_config.ui.qml")
            }
        }

    Button {
        id: button1
        x: -21
        y: 114
        width: 172
        height: 181
        opacity: 0
        scale: 0.76
        onClicked: {
            stackview.replace("Ui.ui.qml")
        }
    }

    Button {
        id: button2
        x: 0
        y: 246
        width: 172
        height: 212
        opacity: 0
        scale: 0.76
        onClicked: {
            stackview.replace("Hardware.ui.qml")
        }
    }

    Button {
        id: button3
        x: 0
        y: 439
        width: 172
        height: 210
        opacity: 0
        scale: 0.76
        onClicked: {
            stackview.replace("Hmi_config.ui.qml")
        }
    }

    Button {
        id: button4
        x: -21
        y: 569
        width: 172
        height: 172
        opacity: 0
        scale: 0.76
        onClicked: {
            stackview.replace("Settings.ui.qml")
        }
    }

    // Button {
    //     id: closebutton
    //     x: 1200
    //     y: 0
    //     width: 80
    //     height: 31
    //     palette {
    //         button: "red"
    //         buttonText: "white"
    //     }
    //     opacity: 100
    //     text: "X"
    //     anchors.right: parent.right
    //     anchors.top: parent.top
    //     autoRepeat: false
    //     flat: false
    //     font.family: "Verdana"
    //     onClicked: {
    //         application.close()
    //         }
    // }

}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}
}
##^##*/
