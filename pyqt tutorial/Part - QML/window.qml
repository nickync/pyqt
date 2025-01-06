import QtQuick 2.5
import QtQuick.Controls 2.5

ApplicationWindow{

    visible:true
    width:800
    height:800
    title: "Simple Window"
    color: "green"

    menuBar: MenuBar {
        Menu {
            title: "File"
            Action {text: "New"}
            Action {text: "Open"}
            Action {text: "Save"}
            Action {text: "Save As"}
        }

        Menu {
            title: "Edit"
            Action {text: "Cut"}
            Action {text: "Copy"}
            Action {text: "Paste"}
        }

        Menu {
            title: "Help"
            Action {text: "About"}

        }
    }

    Button {
        text: "Click Me"
        id: mybutton
        //height: 40
        //width: 120
        anchors.centerIn:parent
        //x: 300
        //y: 300
        background: Rectangle {
            implicitWidth:120
            implicitHeight:40
            color: mybutton.down ? "#d6d6d6" : "#f6f6f6"
            border.color:"#26282a"
            border.width:1
            radius:4
        }

        onClicked: {
            window.hello()
        }
    }

    Row {
        Button{ text: "Click1"}
        Button{ text: "Click2"}
        Button{ text: "Click3"}
        Button{ text: "Click4"}
    }

    Column {
        y:50
        x:20
        spacing: 10
        //Rectangle{color:"red";width:100;height:100}
        Rectangle{color:"cyan";width:100;height:100}
        Rectangle{color:"white";width:100;height:100}

        Label {
            id:mylabel
            text: "this is a label"
            font.pixelSize: 22
            font.italic: true
            font.underline: true
            font.bold:true
        }

        Button {
            text: "Click to Change Label"
            height: 30
            width: 200

            onClicked:{
                mylabel.text = "Text is changed"
            }
        }

        Label{
            text: "Check Box"
            font.bold:true
        }

        CheckBox {
            checked:true
            text: "Python"
        }

        CheckBox {
            checked:false
            text: "Java"
        }

        Label{
            id: comboLabel
            text: "Combo Box"
            font.bold:true
        }

        ComboBox {
            id: combo
            model: ["Python", "Java", "C++"]
            onActivated: {
                comboLabel.text = "You have selected : " + combo.currentText
            }
        }
    }

    Column {
        
        y:50
        x:180
        spacing: 10

        Label{
            id: spinboxLabel
            text: "SpinBox "
            font.pixelSize: 16
            font.bold:true
        }

        SpinBox {
            id: spinbox
            from: 0
            value: 100
            to: 100 * 100
            stepSize: 100

            onValueModified: {
                spinboxLabel.text = "SpinBox value is : " + spinbox.displayText
            }
        }

        Label{
            id: sliderLabel
            text: "Slider"
            font.pixelSize: 16
            font.bold:true
        }

        Slider {
            id: slider
            from: 1
            value: 25
            to: 100

            onMoved: {
                sliderLabel.text = "Slider value is : " + slider.value
            }
        }

        ScrollView {
            width: 120
            height: 40

            Label {
                text: "Scrollable view area \n\n ScrollView"
                font.pixelSize: 16
                font.bold: true
            }
        }

        Row {
            spacing:5
            Switch{
                text: "Wifi"
            }
            Switch{
                text: "bluetooth"
            }
        }
    }
}