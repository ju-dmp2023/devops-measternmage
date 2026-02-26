from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class CalculatorPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "screen": "#calculator-screen",
            "btn_1": "#key-1",
            "btn_2": "#key-2",
            "btn_3": "#key-3",
            "btn_4": "#key-4",
            "btn_5": "#key-5",
            "btn_6": "#key-6",
            "btn_7": "#key-7",
            "btn_8": "#key-8",
            "btn_9": "#key-9",
            "btn_0": "#key-0",
            "btn_add": "#key-add",
            "btn_sub": "#key-subtract",
            "btn_mult": "#key-multiply",
            "btn_div": "#key-divide",
            "btn_equals": "#key-equals",
            "btn_clear": "#key-clear",
            "btn_rs": "#remote-toggle",        
            "btn_history_toggle": "#toggle-button",
            "history_display": "#history"
        })

    def _click_number(self, num):
        """Helper to click a specific number button based on the dictionary."""
        self.element(f"btn_{num}").click()

    def add(self, a, b):
        self._click_number(a)
        self.element("btn_add").click()
        self._click_number(b)
        self.element("btn_equals").click()

    def subtract(self, a, b):
        self._click_number(a)
        self.element("btn_sub").click()
        self._click_number(b)
        self.element("btn_equals").click()

    def multiply(self, a, b):
        self._click_number(a)
        self.element("btn_mult").click()
        self._click_number(b)
        self.element("btn_equals").click()

    def divide(self, a, b):
        self._click_number(a)
        self.element("btn_div").click()
        self._click_number(b)
        self.element("btn_equals").click()