from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QLineSeries
from PyQt6.QtCore import QPointF
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 LineChart")
        self.setWindowIcon(QIcon(''))

        self.line_chart()

    def line_chart(self):
        series = QLineSeries()

        series.append([
            QPointF(1, 1), QPointF(2, 73), QPointF(3, 268), QPointF(4, 17), QPointF(5, 120), QPointF(6, 210)
        ])

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("LineChart example")
        
        # animation
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)

        chartview = QChartView(chart)
        self.setCentralWidget(chartview)
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())