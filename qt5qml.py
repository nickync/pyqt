import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Load the QML file
    engine.load(QUrl.fromLocalFile('qt5qml.qml'))

    # Check if the QML file was loaded successfully
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
