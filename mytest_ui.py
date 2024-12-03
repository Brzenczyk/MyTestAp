import sys
import platform
import socket
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextBrowser, QPushButton, QWidget

class MyTestApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("MyTest - Info Checker")
        self.setGeometry(100, 100, 600, 400)

        # Central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()

        # Text browser
        self.text_browser = QTextBrowser(self)
        layout.addWidget(self.text_browser)

        # Buttons
        self.buttons = {
            "IPv4 Info": self.show_ipv4_info,
            "Proxy Info": self.show_proxy_info,
            "System Info": self.show_system_info,
            "BIOS Version": self.show_bios_version,
            "Host Name": self.show_host_name
        }

        for btn_name, func in self.buttons.items():
            btn = QPushButton(btn_name, self)
            btn.clicked.connect(func)
            layout.addWidget(btn)

        central_widget.setLayout(layout)

    def append_output(self, text):
        self.text_browser.append(text)

    # Button functionalities
    def show_ipv4_info(self):
        ip = socket.gethostbyname(socket.gethostname())
        self.append_output(f"IPv4 Address: {ip} (Static/Dynamic detection not implemented)")

    def show_proxy_info(self):
        # Example stub
        self.append_output("Proxy Info: Not detected")

    def show_system_info(self):
        cores = platform.architecture()[0]
        memory = "8GB (stub)"
        self.append_output(f"System Info: {platform.system()}, {cores}, Memory: {memory}")

    def show_bios_version(self):
        self.append_output("BIOS Version: Not implemented (requires platform-specific code)")

    def show_host_name(self):
        host_name = socket.gethostname()
        self.append_output(f"Host Name: {host_name}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyTestApp()
    window.show()
    sys.exit(app.exec_())

