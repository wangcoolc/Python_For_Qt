import QtQuick 2.8
import "backend/Data" as Data
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.11
import QtQuick.Studio.Components 1.0
import QtQuick.Studio.Effects 1.0

Item {
    id: home
    width: 1920
    height: 1080

    Image {
        id: homeAsset
        x: 0
        y: 0
        source: "assets/home.png"
    }

    Hmiblock {
        id: hmiblock
        x: 692
        y: 574
        width: 476
        height: 480
    }

    Dashboardblock {
        id: dashboardblock
        x: 208
        y: 576
        width: 476
        height: 480
    }

    Reterminalblock {
        id: reterminalblock
        x: 208
        y: 50
        width: 960
        height: 524
    }

    Home_navigate {
        id: home_navigate
        x: 0
        y: 0
        width: 159
        height: 1080
    }

    Touch_panel12 {
        id: touch_panel12
        x: 1177
        y: 51
        width: 713
        height: 1001
        n_aText: Data.Values.displaywifi
        gadgetText: Data.Values.displayethernet
        gadget1Text: Data.Values.displaykernel
        raspberry_pi_os_marcText: Data.Values.displayos
        rt02cm4Text: Data.Values.displaybuildcode
        cm4104032Text: Data.Values.displaycompute
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5;uuid:"db758c043a516da3a6cc8edd0f479654"}D{i:1;uuid:"db758c043a516da3a6cc8edd0f479654_asset"}
}
##^##*/

