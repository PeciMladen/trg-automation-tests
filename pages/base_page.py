"""
Base Page class with common methods for all page objects
"""
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.trgint.com"
    
    def navigate_to(self, path: str = ""):
        """Navigate to a specific path on the website"""
        url = f"{self.base_url}{path}"
        self.page.goto(url, wait_until="networkidle")
    
    def click_element(self, selector: str):
        """Click on an element"""
        self.page.click(selector)
    
    def scroll_to_element(self, selector: str):
        """Scroll to a specific element"""
        element = self.page.locator(selector).first
        element.scroll_into_view_if_needed()
    
    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        return self.page.locator(selector).first.inner_text()
    
    def get_all_elements(self, selector: str):
        """Get all elements matching selector"""
        return self.page.locator(selector).all()
    
    def wait_for_element(self, selector: str, timeout: int = 10000):
        """Wait for element to be visible"""
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def download_image(self, img_url: str, save_path: str):
        """Download an image from URL"""
        if img_url and not img_url.startswith('http'):
            img_url = f"{self.base_url}{img_url}"
        
        response = self.page.request.get(img_url)
        with open(save_path, 'wb') as f:
            f.write(response.body())