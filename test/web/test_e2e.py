import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from playwright.sync_api import expect
from test.web.test_base import WebBase
from test.web.pages.login_page import LoginPage
from test.web.pages.register_page import RegisterPage
from test.web.pages.calculator_page import CalculatorPage

class TestCalculatorWeb(WebBase):
    
    def test_full_calculator_flow(self):
        unique_name = f"user_{int(time.time())}"
        self.page.goto(f"{self.app_url}/login.html", wait_until="networkidle")
        
        login_page = LoginPage(self.page)
        login_page.element("register_link").click()
        
        expect(self.page).to_have_url(f"{self.app_url}/register.html")
        
        register_page = RegisterPage(self.page)
        register_page.element("username").fill(unique_name) 
        register_page.element("password").fill("Pass123!")
        register_page.element("confirm_password").fill("Pass123!")
        
        register_page.element("register_button").click()
        
        expect(self.page).to_have_url(f"{self.app_url}/index.html", timeout=10000)
        
        calc_page = CalculatorPage(self.page)
        calc_page.element("btn_clear").click()
        
        calc_page.element("btn_1").click()
        calc_page.element("btn_add").click()
        calc_page.element("btn_2").click()
        calc_page.element("btn_equals").click()
        
        expect(calc_page.element("screen")).to_have_value("3", timeout=5000)