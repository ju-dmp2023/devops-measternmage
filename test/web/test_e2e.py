import sys
import os
import time
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from playwright.sync_api import expect
from test.web.test_base import WebBase
from test.web.pages.login_page import LoginPage
from test.web.pages.register_page import RegisterPage
from test.web.pages.calculator_page import CalculatorPage

class TestCalculatorWeb(WebBase):
    
    def _register_and_setup(self):
        """Helper method to register a user and get to the calculator page."""
        unique_name = f"user_{int(time.time())}"
        self.page.goto(f"{self.app_url}/login.html", wait_until="networkidle")
        
        login_page = LoginPage(self.page)
        login_page.element("register_link").click()
        
        register_page = RegisterPage(self.page)
        register_page.register_user(unique_name, "Pass123!")
        
        expect(self.page).to_have_url(f"{self.app_url}/index.html", timeout=10000)
        return unique_name

    def test_register_user(self):
        unique_name = self._register_and_setup()
        
        expect(self.page.get_by_text(unique_name)).to_be_visible(timeout=5000)

    def test_add_operation(self):
        self._register_and_setup()
        calc_page = CalculatorPage(self.page)
        calc_page.element("btn_clear").click()
        
        calc_page.add(1, 2)
        expect(calc_page.element("screen")).to_have_value("3", timeout=5000)

    def test_subtract_operation(self):
        self._register_and_setup()
        calc_page = CalculatorPage(self.page)
        calc_page.element("btn_clear").click()
        
        calc_page.subtract(3, 1)
        expect(calc_page.element("screen")).to_have_value("2", timeout=5000)

    def test_multiply_operation(self):
        self._register_and_setup()
        calc_page = CalculatorPage(self.page)
        calc_page.element("btn_clear").click()
        
        calc_page.multiply(2, 3)
        expect(calc_page.element("screen")).to_have_value("6", timeout=5000)

    def test_divide_operation(self):
        self._register_and_setup()
        calc_page = CalculatorPage(self.page)
        calc_page.element("btn_clear").click()
        
        calc_page.divide(6, 2)
        expect(calc_page.element("screen")).to_have_value("3", timeout=5000)

    def test_history_function(self):
        self._register_and_setup()
        calc_page = CalculatorPage(self.page)
        calc_page.element("btn_clear").click()
        
        calc_page.add(1, 2)
        expect(calc_page.element("screen")).to_have_value("3", timeout=5000)
        
        calc_page.element("btn_history_toggle").click()
        expect(calc_page.element("history_display")).to_have_value(re.compile(r"1\+2=3"), timeout=5000)