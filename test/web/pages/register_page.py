from playwright.sync_api import Page
from test.web.pages.page_base import PageBase

class RegisterPage(PageBase):
    def __init__(self, page: Page) -> None:
        super().__init__(page, 
        elements={            
            "username": "#username",
            "password": "#password1",          
            "confirm_password": "#password2",  
            "register_button": "#register",    
            "success_message": "#errormsg"     
        })