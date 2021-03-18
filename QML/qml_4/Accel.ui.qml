import QtQuick 2.8
import QtCharts 2.2
Item {
    id: accel
    width: 850
    height: 490

    property alias axisX: axis_x
    property alias axisY: axis_y
    property alias axisZ: axis_z

    Image {
        id: rect2
        x: 1
        y: 1
        source: "assets/rect2.png"
    }

    ChartView {
        id: chartview
        title: "Accelerator 3-Axis"
        // title.Alignment: Qt.AlignLeft
        anchors.fill: parent
        antialiasing: true

        //X轴
        ValueAxis {
            id: valueAxisX
            min: 0
            max: 5>axisXvalue ? 5:axisXvalue+1
            tickCount: 6
        }

        //Y轴
        ValueAxis {
            id: valueAxisY
            min: 4000
            max: 12000
            tickCount: 5
        }

        SplineSeries {
            id:axis_x
            name: "x"
            axisX: valueAxisX
            axisY: valueAxisY
        }

        SplineSeries {
            id:axis_y
            name: "y"
            axisX: valueAxisX
            axisY: valueAxisY
        }

        SplineSeries {
            id:axis_z
            name: "z"
            axisX: valueAxisX
            axisY: valueAxisY
            
        }
    }
  
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.33;height:490;width:850}D{i:1;uuid:"aaf6bc7143a0d57cda825f31f73a8f92"}
D{i:2;uuid:"1be122764b3ed4fb238e6037e603ea9d"}D{i:3;uuid:"c2c4a1d02ffacb6434a59483f5c093cc"}
D{i:4;uuid:"124edb6cdbeb845a7ab08cbd17855fe8"}D{i:5;uuid:"58e4c02e89c005ba558d7ebc4ac0f138"}
D{i:6;uuid:"ff31bc43b1515429b877f798f552ee4a"}D{i:7;uuid:"63cd90e4bde496a285838f6967d393b2"}
D{i:8;uuid:"93493948629e32af682c30a9834d8d95"}D{i:9;uuid:"190bdb98d4e0d05ada17af2a4b533b2d"}
D{i:10;uuid:"742a7fb688b48b5bc9e442f6cbd16d5f"}D{i:11;uuid:"9f58718a57be83af4eb71cb8c17cbdbd"}
D{i:12;uuid:"c403bc59a5db8fe205317414da9564e9"}D{i:13;uuid:"dd1f1bc9b5610764d234d0da72c7d0b3"}
D{i:14;uuid:"733d541d5a0313d18cca3ca6296a29c0"}D{i:15;uuid:"5add28f5b99fe9d91c08dd3bf0ea2b1a"}
D{i:16;uuid:"b75cf8f6e8999209888544378c44957a"}D{i:17;uuid:"cefcaa36665ed608343540d9c5818768"}
D{i:18;uuid:"60c39074a1dcf7c5d975e6eb98fa52c8"}D{i:19;uuid:"3bd29cab1c3693315a5188b968cb15a5"}
D{i:20;uuid:"588cc0d6e401199708189fcce9a8eefb"}D{i:21;uuid:"7a28c60837cc27454278daa4321f7f28"}
D{i:22;uuid:"8ec9e94e053896b46c99a977955e1ec2"}D{i:23;uuid:"21b2e44d792dbe381b389352fe7523af"}
D{i:24;uuid:"9465516a2f46af1a89f0d99b0fe594b7"}
}
##^##*/

