import QtQuick 2.8
import QtQuick.Controls 2.1

ApplicationWindow {
    title: "ReTerminal UI"
    width: 1280
    height: 720
    visible: true


    property var iniITEM: "Home.ui.qml"

    StackView {
        id: stackview
        width: 1920
        height: 1080

        replaceEnter: Transition {
                  PropertyAnimation{
                      property: "opacity"
                      from: 0
                      to: 1
                      duration: 300
                  }
              }

        replaceExit: Transition {
                  PropertyAnimation{
                      property: "opacity"
                      from: 1
                      to: 0
                      duration: 250
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
        anchors.centerIn: parent
        width: 172
        height: 181
        opacity: 0
        anchors.verticalCenterOffset: -445
        anchors.horizontalCenterOffset: -874
        onClicked: {
            stackview.replace("Home.ui.qml")
        }
    }


    Button {
        anchors.centerIn: parent
        width: 172
        height: 181
        opacity: 0
        anchors.verticalCenterOffset: -258
        anchors.horizontalCenterOffset: -874
        onClicked: {
            stackview.replace("Ui.ui.qml")
        }
    }

    Button {
        anchors.centerIn: parent
        width: 158
        height: 212
        opacity: 0
        anchors.verticalCenterOffset: -39
        anchors.horizontalCenterOffset: -880
        onClicked: {
            stackview.replace("Hardware.ui.qml")
        }
    }

    Button {
        anchors.centerIn: parent
        width: 159
        height: 210
        opacity: 0
        anchors.verticalCenterOffset: 204
        anchors.horizontalCenterOffset: -880
        onClicked: {
            stackview.replace("Hmi_config.ui.qml")
        }
    }

    Button {
        anchors.centerIn: parent
        width: 172
        height: 181
        opacity: 0
        anchors.verticalCenterOffset: 450
        anchors.horizontalCenterOffset: -874
        onClicked: {
            stackview.replace("Settings.ui.qml")
        }
    }

}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}
}
##^##*/
