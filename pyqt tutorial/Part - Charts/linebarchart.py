from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QPointF
from PyQt6.QtCharts import QBarSet, QBarSeries, QChartView, QChart, QLineSeries
import sys



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("LineChart & BarChart")
        self.setWindowIcon(QIcon('images/python.png'))

        set0 = QBarSet("John")
        set1 = QBarSet("Bob")
        set2 = QBarSet("Tom")
        set3 = QBarSet("Mary")
        set4 = QBarSet("Sam")

        set0.append([1, 2, 3, 4, 5, 6])
        set1.append([5, 0, 0, 4, 0, 7])
        set2.append([3, 5, 8, 13, 8, 5])
        set3.append([5, 6, 7, 3, 4, 5])
        set4.append([9, 7, 5, 3, 1, 2])

        bar_series = QBarSeries()
        bar_series.append(set0)
        bar_series.append(set1)
        bar_series.append(set2)
        bar_series.append(set3)
        bar_series.append(set4)


        line_series = QLineSeries()
        line_series.append(QPointF(0, 4))
        line_series.append(QPointF(1, 15))
        line_series.append(QPointF(2, 20))
        line_series.append(QPointF(3, 4))
        line_series.append(QPointF(4, 12))
        line_series.append(QPointF(5, 17))


        chart = QChart()
        chart.addSeries(bar_series)
        chart.addSeries(line_series)
        chart.setTitle("Line and BarChart")

        chart_view  =QChartView(chart)

        self.setCentralWidget(chart_view)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())