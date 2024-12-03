import pytest
from main import MyApp

def test_ui_elements(qtbot):
    app = MyApp()
    assert app.text_view is not None
    assert app.centralWidget() is not None

def test_ipv4_info():
    # Test logic for IPv4 information
    assert True
