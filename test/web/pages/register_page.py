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
        
    def register_user(self, username, password):
        self.element("username").fill(username)
        self.element("password").fill(password)
        self.element("confirm_password").fill(password)
        self.element("register_button").click()