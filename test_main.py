import subprocess
import pytest
from PyQt5.QtWidgets import QApplication
from main import MyApp  # Upewnij się, że masz poprawny import

# Test interfejsu
def test_ui_elements():
    app = QApplication([])  # Tworzenie aplikacji PyQt5
    window = MyApp()  # Tworzenie okna aplikacji
    assert window.text_view is not None
    assert window.centralWidget() is not None

# Test uruchamiania funkcji (np. IPv4)
def test_ipv4_info():
    assert True  # Zastąp tym, co chcesz testować

# Test działania przycisku 1
def test_button1():
    result = subprocess.run(["MyTest.exe", "button1"], capture_output=True, text=True)
    assert "IPv4 Info" in result.stdout  # Sprawdzenie czy wynik zawiera "IPv4 Info"

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyTest Application")
        self.setGeometry(200, 200, 600, 400)

        # Central Widget
        central_widget = QWidget()
        layout = QVBoxLayout()

        # TextView
        self.text_view = QTextEdit()
        self.text_view.setReadOnly(True)
        layout.addWidget(self.text_view)

        # Buttons
        buttons = [
            ("Show IPv4 Info", self.show_ipv4_info),
            ("Check Proxy", self.check_proxy),
            ("OS Details", self.show_os_details),
            ("BIOS Version", self.show_bios_version),
            ("Host Name", self.show_host_name),
        ]

        for btn_text, btn_action in buttons:
            btn = QPushButton(btn_text)
            btn.clicked.connect(btn_action)
            layout.addWidget(btn)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_ipv4_info(self):
        self.text_view.append("IPv4 Info: Placeholder")

    def check_proxy(self):
        self.text_view.append("Proxy Info: Placeholder")

    def show_os_details(self):
        self.text_view.append("OS Details: Placeholder")

    def show_bios_version(self):
        self.text_view.append("BIOS Version: Placeholder")

    def show_host_name(self):
        self.text_view.append("Host Name: Placeholder")

def handle_terminal_args():
    parser = argparse.ArgumentParser(description="MyTest Application CLI")
    parser.add_argument("command", choices=["button1", "button2", "button3", "button4", "button5", "help"])
    args = parser.parse_args()

    if args.command == "help":
        print("Available commands: button1, button2, button3, button4, button5")
    else:
        print(f"Command {args.command} executed.")


if __name__ == "__main__":
    handle_terminal_args()
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())