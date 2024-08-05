import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "QML with PyQt5"

    Rectangle {
        width: 200
        height: 200
        color: "lightblue"
        anchors.centerIn: parent

        Text {
            text: "Hello, QML!"
            anchors.centerIn: parent
            font.pixelSize: 24
        }

        Button {
            text: "Click Me"
            anchors.bottom: parent.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: {
                textElement.text = "Button Clicked!"
            }
        }
    }
}
