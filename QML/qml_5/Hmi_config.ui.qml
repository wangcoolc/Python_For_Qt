import QtQuick 2.8

Item {
    id: hmi_config
    width: 1920
    height: 1080

    Image {
        id: hmi_configAsset
        x: 0
        y: 0
        source: "assets/hmi_config.png"
    }

    Hmi_diagram {
        id: hmi_diagram
        x: 224
        y: 55
        width: 1634
        height: 885
    }

    Ui_navigate_3 {
        id: ui_navigate_3
        x: 0
        y: 0
        width: 159
        height: 1080
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75;uuid:"db758c043a516da3a6cc8edd0f479654"}D{i:1;uuid:"db758c043a516da3a6cc8edd0f479654_asset"}
}
##^##*/
