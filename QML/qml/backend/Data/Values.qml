pragma Singleton
import QtQuick 2.10

QtObject {
    id: values

    Component.onCompleted: {
        // 绑定python中的信号到qml中的函数
        _CpuUsage.CpuSignal.connect(cpuchangevalue)
        _RamUsage.RamSignal.connect(ramchangevalue)
        _StorageUsage.StoragSignal.connect(flashchangevalue)
        _Accelerator.AxisSignal.connect(axischangevalue)
    }

    
    property int cpu_data: 0
    property int cpu_redata: 0
    function cpuchangevalue(value) {
        if(value != undefined) {
            values.cpu_data = Number(value)
        }  
    }
    function cpudisplay(){
        if(values.cpu_redata > values.cpu_data)
        {
            values.cpu = Number(values.cpu_redata * 10)
            values.displaycpu = String(values.cpu_redata)
            values.cpu_redata -= 1
        }
        if(values.cpu_redata < values.cpu_data)
        {
            values.cpu = Number(values.cpu_redata * 10)
            values.displaycpu = String(values.cpu_redata)
            values.cpu_redata += 1
        }
        
    }
    

    property int ram_data: 0
    property int ram_redata: 0
    function ramchangevalue(value) {
        if(value != undefined) {
            values.ram_data = Number(value) 
        }  
    }
    function ramdisplay(value) {
        if(values.ram_redata > values.ram_data)
        {
            values.ram = Number(values.ram_redata * 10)
            values.displayram = String(values.ram_redata)
            values.ram_redata -= 1
        }
        if(values.ram_redata < values.ram_data)
        {
            values.ram = Number(values.ram_redata * 10)
            values.displayram = String(values.ram_redata)
            values.ram_redata += 1
        }
  
    }


    property int flash_data: 0
    property int flash_redata: 0
    function flashchangevalue(value) {
        if(value != undefined) {
            values.flash_data = Number(value) 
        }  
    }
    function flashdisplay(value) {
        if(values.flash_redata > values.flash_data)
        {
            values.flash = Number(values.flash_redata * 10)
            values.displayflash = String(values.flash_redata)
            values.flash_redata -= 1
        }
        if(values.flash_redata < values.flash_data)
        {
            values.flash = Number(values.flash_redata * 10)
            values.displayram = String(values.flash_redata)
            values.flash_redata += 1
        }

    }


    property int displayaxisX: 0
    property int displayaxisY: 0
    property int displayaxisZ: 0
    property int displaycount: 0
    function axischangevalue(value1,value2,value3) {
        values.displayaxisX = Number(value1)
        console.log("displayaxisX",displayaxisX)
        values.displayaxisY = Number(value2)
        console.log("displayaxisY",displayaxisY)
        values.displayaxisZ = Number(value3)
        console.log("displayaxisZ",displayaxisZ)
        values.displaycount += 5
        console.log(displaycount)
    }
  

    
    // // cpu dial values
    property int cpu: 0
    property string displaycpu: "0"

    property Timer cpuTimer: Timer{
        running: true
        repeat: true
        onTriggered: cpudisplay()
        interval: 10
    }

    // ram dial values
    property int ram: 0
    property string displayram: "0"

    property Timer ramTimer: Timer{
        running: true
        repeat: true
        onTriggered: ramdisplay()
        interval: 10
    }

    // flash dial values
    property int flash: 0
    property string displayflash: "0"

    property Timer flashTimer: Timer{
        running: true
        repeat: true
        onTriggered: flashdisplay()
        interval: 10
    }


}
