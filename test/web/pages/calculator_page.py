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