import sys
from PyQt6.QtWidgets import *

class mainIcon(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 700, 100)

        layout = QGridLayout()
        self.setLayout(layout)

        min_label = QLabel()
        min_label.setText("Dette er en Label")
        layout.addWidget(min_label,0,0)

        minKnapp = QPushButton("Min knapp")
        layout.addWidget(minKnapp,0,1)

        minInputlinje = QLineEdit()
        layout.addWidget(minInputlinje,0,2)


        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    vindu = hovedVindu()
    sys.exit(app.exec())