CONST_WINDOW = """
            QMainWindow {
                background-color: #f5f5f5;
            }
            
            QLabel {
                color: #333333;
                font-size: 16px;
                margin-bottom: 5px;
                font-weight: bold;
            }
            
            QLineEdit {
                width: 200px;
                padding: 8px;
                font-size: 14px;
                border: 1px solid #cccccc;
                border-radius: 4px;
                background-color: #ffffff;
                color: #333333;
            }
            
            QPushButton {
                width: 200px;
                padding: 10px;
                margin: 15px, 15px;
                font-size: 16px;
                color: #ffffff;
                background-color: #0078d7;
                border: none;
                border-radius: 5px;
            }
            
            QPushButton:hover {
                background-color: #005fa3;
            }
            
            QPushButton:pressed {
                background-color: #003f73;
            }
        """
        
CONST_MESSAGE_BOX = """
    QMessageBox {
        background-color: #f0f0f0;
    }

    QMessageBox QLabel {
        color: #333333;
        font-size: 14px;
        font-weight: normal;
        padding: 5px;
    }

    QMessageBox QPushButton {
        width: 80px;
        padding: 6px;
        font-size: 14px;
        color: #ffffff;
        background-color: #0078d7;
        border: none;
        border-radius: 4px;
    }

    QMessageBox QPushButton:hover {
        background-color: #005fa3;
    }

    QMessageBox QPushButton:pressed {
        background-color: #003f73;
    }
"""