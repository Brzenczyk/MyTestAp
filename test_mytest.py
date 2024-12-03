# test_mytest.py

import unittest
from PyQt5.QtWidgets import QApplication
from mytest_ui import MyTestApp

app = QApplication([])

class TestMyTestApp(unittest.TestCase):
    def setUp(self):
        self.window = MyTestApp()

    def test_ui_elements(self):
        # Test UI setup
        self.assertEqual(self.window.text_browser.toPlainText(), "")
        self.assertEqual(len(self.window.buttons), 5)

    def test_ipv4_info(self):
        self.window.show_ipv4_info()
        output = self.window.text_browser.toPlainText()
        self.assertIn("IPv4 Address:", output)

    # Add more tests for each button functionality

if __name__ == "__main__":
    unittest.main()
