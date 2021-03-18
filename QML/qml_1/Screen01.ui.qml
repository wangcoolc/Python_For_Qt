import QtQuick 2.12
import Wiotest 1.0

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Text {
        text: qsTr("Hello Wiotest")
        anchors.centerIn: parent
        font.family: Constants.font.family
    }
}
