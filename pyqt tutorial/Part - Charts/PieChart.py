from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QPieSeries
from PyQt6.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Pie")
        self.setWindowIcon(QIcon(''))

        self.pie_chart()

    def pie_chart(self):
        series = QPieSeries()
        series.append("Python", 90)
        series.append("C++", 80)
        series.append("Java", 60)
        series.append("C#", 30)

        # add slice to highlight
        my_slice = series.slices()[2]
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)


        chart = QChart()
        chart.addSeries(series)

        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTitle("Pie Chart Example")

        chart.setTheme(QChart.ChartTheme.ChartThemeQt)
        #chart.legend().setVisible(False)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        chartView = QChartView(chart)

        self.setCentralWidget(chartView)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())