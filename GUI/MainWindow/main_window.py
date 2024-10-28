from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QWidget, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon
from Style.style import CONST_WINDOW, CONST_MESSAGE_BOX
from Logics.calculations import distance_calculation, fuel_consumption_calculation


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Расчет расстояния и потребностей в топливе")
        self.setFixedSize(500, 500)
        
        self.setStyleSheet(CONST_WINDOW)
        self.icon = 'Image\icon.jpg'
        self.setWindowIcon(QIcon(self.icon))
        
        self.error = None
        self.result = None
        self.err = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        starting_city = QLabel(text="Введите начальный город")
        self.entering_the_starting_city = QLineEdit()
        
        final_city = QLabel(text="Введите конечный город")
        self.entering_the_final_city = QLineEdit()
        
        machine_consumption = QLabel(text="Введите ваш расход на 100км")
        self.entering_the_machine_consumption = QLineEdit()
        
        start_of_calculation = QPushButton(text="Начать расчет")
        start_of_calculation.clicked.connect(self.button_operation)
        
        control_UI.addWidget(starting_city)
        control_UI.addWidget(self.entering_the_starting_city)
        control_UI.addWidget(final_city)
        control_UI.addWidget(self.entering_the_final_city)
        control_UI.addWidget(machine_consumption)
        control_UI.addWidget(self.entering_the_machine_consumption)
        control_UI.addWidget(start_of_calculation)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def button_operation(self):
        try:
            start = str(self.entering_the_starting_city.text())
            end = str(self.entering_the_final_city.text())
            consumption_car = int(self.entering_the_machine_consumption.text())
        except:
            self.error = QMessageBox()
            self.error.setStyleSheet(CONST_MESSAGE_BOX)
            self.error.setWindowIcon(QIcon(self.icon))
            self.error.setWindowTitle("Ошибка")
            self.error.setText("Проверьте название городов и точно ли вы свой расход ввели в цифровом формате")
            
            self.error.show()
            
        ds = distance_calculation(start, end, self.err)
        flow_rate = fuel_consumption_calculation(consumption_car, ds)
        
        self.result = QMessageBox()
        self.result.setStyleSheet(CONST_MESSAGE_BOX)
        self.result.setWindowIcon(QIcon(self.icon))
        self.result.setWindowTitle("Результат расчетов")
        self.result.setText(f"Расстояние: {round(ds, 2)} \nСколько нужно топлива: {round(flow_rate, 2)}")
        
        self.result.show()