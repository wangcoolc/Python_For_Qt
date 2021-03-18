import QtQuick 2.12
import FlowView 1.0
import QtQuick.Controls 2.15

FlowView {
    width: Constants.width
    height: Constants.height
    flowTransitions: [
        FlowTransition {
            id: flowTransition3
            to: settings_Page
            from: fHomeScreen
        },
        FlowTransition {
            id: flowTransition
            to: fHomeScreen
            from: settings_Page
        },
        FlowTransition {
            id: flowTransition1
            to: dashBoard
            from: fHomeScreen
        },
        FlowTransition {
            id: flowTransition2
            to: fHomeScreen
            from: dashBoard
        },
        FlowTransition {
            id: flowTransition4
            to: dashBoard
            from: fHomeScreen
        },
        FlowTransition {
            id: flowTransition5
            to: settings_Page
            from: dashBoard
        },
        FlowTransition {
            id: flowTransition6
            to: dashBoard
            from: settings_Page
        }
    ]

    defaultTransition: FlowTransition {
        id: defaultTransition
    }

    FHomeScreen {
        id: fHomeScreen

        FlowActionArea {
            target: flowTransition3
            x: 14
            y: 923
            width: 137
            height: 138
        }

        FlowActionArea {
            target: flowTransition1
            x: 14
            y: 241
            width: 137
            height: 136
        }

        FlowActionArea {
            target: flowTransition4
            x: 235
            y: 598
            width: 424
            height: 426
        }
    }

    Settings_Page {
        id: settings_Page

        FlowActionArea {
            target: flowTransition
            x: 16
            y: 18
            width: 136
            height: 184
        }

        FlowActionArea {
            target: flowTransition6
            x: 16
            y: 236
            width: 136
            height: 148
        }
    }

    DashBoard {
        id: dashBoard

        FlowActionArea {
            target: flowTransition2
            x: 8
            y: 16
            width: 145
            height: 162
        }

        FlowActionArea {
            target: flowTransition5
            x: 8
            y: 924
            width: 145
            height: 148
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.2;height:10000;uuid:"db758c043a516da3a6cc8edd0f479654";width:10000}
D{i:9;flowX:1252;flowY:1460}D{i:13;flowX:2696;flowY:2943}D{i:16;flowX:4136;flowY:988}
}
##^##*/

