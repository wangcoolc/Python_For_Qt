pragma Singleton
import QtQuick 2.10
import "simulation.js" as JS

QtObject {
    id: values

    // pi Compute module
    property string displaycompute: "0"

    //reterminal build code
    property string displaybuildcode: "0"

    //system version
    property string displayos: "0"

    //kernel version
    property string displaykernel: "0"

    //Ethernet Connect
    property string displayethernet: "0"

    //wifi connection
    property string displaywifi: "0"

    // cpu dial values
    property int cpu: 0
    property string displaycpu: "0"
    


    Component.onCompleted: {
        // 绑定python中的信号到qml中的函数
        _CpuUsage.CpuSignal.connect(cpuchangevalue)
        _RamUsage.RamSignal.connect(ramchangevalue)
        _StorageUsage.StoragSignal.connect(flashchangevalue)
        _Accelerator.AxisSignal.connect(axischangevalue)
        _Systeminfo.SystemSignal.connect(systeminfo)
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
        values.displayaxisY = Number(value2)
        values.displayaxisZ = Number(value3)
        values.displaycount += 1
    }

     
    function systeminfo(str1,str2,str3,str4,str5,str6) {
        console.log("11111111111111111111111111")
        displaycompute = String(str1)
        displaybuildcode = String(str2)
        displayos = String(str3)
        displaykernel = String(str4)
        displayethernet = String(str5)
        displaywifi = String(str6)
    }

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
        interval: 20
    }

    // flash dial values
    property int flash: 0
    property string displayflash: "0"

    property Timer flashTimer: Timer{
        running: true
        repeat: true
        onTriggered: flashdisplay()
        interval: 30
    }


}
