import QtQuick 2.8
import QtQuick.Controls 2.1
import "backend/Data" as Data

Item {
    id: settings
    width: 1920
    height: 1080

    Image {
        id: settingsAsset
        x: 0
        y: 0
        source: "assets/settings.png"
    }

    Ui_navigate_2 {
        id: ui_navigate_2
        x: 0
        y: 0
        width: 160
        height: 1080
    }

    Settings_controls {
        id: settings_controls
        buttonChecked: Data.Values.logoutbutton
        button2Checked: Data.Values.rebootbutton
        button1Checked: Data.Values.shutdownbutton
        sliderValue: Data.Values.brightness
        switch6Checked: Data.Values.serialbutton
        switch5Checked: Data.Values.i2cbutton
        switch4Checked: Data.Values.spibutton
        switch3Checked: Data.Values.vncbutton
        switch2Checked: Data.Values.sshbutton
        switch1Checked: Data.Values.cambutton
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}
}
##^##*/

