from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QBarSet, QStackedBarSeries, QValueAxis, QBarCategoryAxis
import sys
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 LineChart")
        self.setWindowIcon(QIcon(''))

        low = QBarSet("Min")
        high = QBarSet("Max")

        low.append([-52, -50, -45, -37, -25, -8, 0, 2, 4, 5, -4, -20])
        high.append([11.9, 12.8, 18.5, 26.5, 32, 34.8, 40, 40, 38, 32, 2, -5])

        series = QStackedBarSeries()
        series.append(low)
        series.append(high)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Temperature")

        categories = ["Jan", "Feb", "March", "April", "May","June", "July","Aug", "Sep","Oct", "Nov","Dec" ]

        ax = QBarCategoryAxis()
        ax.append(categories)
        ax.setTitleText("Month")

        chart.addAxis(ax, Qt.AlignmentFlag.AlignBottom)

        ay = QValueAxis()
        ay.setRange(-52, 52)
        ay.setTitleText("Temperature [&deg;C]")

        chart.addAxis(ay, Qt.AlignmentFlag.AlignLeft)

        series.attachAxis(ax)
        series.attachAxis(ay)

        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())