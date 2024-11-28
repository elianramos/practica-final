import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import HtmlTestRunner  

class TestLogin(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()


        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("file:///C:/Users/elian/OneDrive/Documentos/proyecto-final/login.html")  
        self.driver.execute_script("""
            localStorage.setItem('userEmail', 'testuser@example.com');
            localStorage.setItem('userPassword', 'Test1234!');
        """)

    def test_login(self):
        driver = self.driver
        email_input = driver.find_element(By.ID, "loginEmail")
        password_input = driver.find_element(By.ID, "loginPassword")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        
        email_input.send_keys("testuser@example.com")
        password_input.send_keys("Test1234!")

        
        submit_button.click()

        
        time.sleep(2)  

        
        self.assertEqual(self.driver.current_url, "file:///C:/Users/elian/OneDrive/Documentos/proyecto-final/index.html")

    def tearDown(self):
       
        if not os.path.exists('resultado_img'):
            os.makedirs('resultado_img')  

        
        screenshot_path = 'resultado_img/test_login_screenshot.png'
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot guardado en {screenshot_path}")

        
        self.driver.quit()

if __name__ == "__main__":
   
    test_runner = HtmlTestRunner.HTMLTestRunner(output="resultados")  
    unittest.main(testRunner=test_runner)
