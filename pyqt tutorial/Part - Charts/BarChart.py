from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QPercentBarSeries
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Bar")
        self.setWindowIcon(QIcon(''))

        self.create_bar()

        
    def create_bar(self):
        set0 = QBarSet("John")
        set1 = QBarSet("Vix")
        set2 = QBarSet("Fan")
        set3 = QBarSet("Tou")

        set0 << 1 << 2 << 3 << 4 << 5 << 6        
        set1 << 5 << 7 << 0 << 10 << 1 << 3
        set2 << 3 << 2 << 1 << 4 << 5 << 6
        set3 << 4 << 5 << 6 << 2 << 1 << 0

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)

        chart = QChart()
        chart.addSeries(series)

        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTitle("Bar Chart")

        chart.setTheme(QChart.ChartTheme.ChartThemeHighContrast)

        chartView = QChartView(chart)

        self.setCentralWidget(chartView)





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())