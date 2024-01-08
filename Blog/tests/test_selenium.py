from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAuth(StaticLiveServerTestCase):
    port = 8000
    
    @classmethod
    def setUpClass(cls) -> None:
        ContentType.objects.clear_cache()
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        
    def setUp(self):
        self.user_password = "testpa$$w0rd"
        self.user = User.objects.create_user("testuser", "test@mail.com", self.user_password)
        self.user.is_active = True
        self.user.save()
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        super().tearDownClass()
        
    def test_title(self):
        url = self.live_server_url + "/login/"
        driver = self.driver
        driver.get(url)
        self.assertEqual("Blog", self.driver.title)
        
    def test_login(self):
        url = self.live_server_url + "/login/"
        self.driver.get(url)
        
        username_elem = self.driver.find_element(By.NAME, "username")
        username_elem.clear()
        username_elem.send_keys(self.user.username)
        
        password_elem = self.driver.find_element(By.NAME, "password")
        password_elem.clear()
        password_elem.send_keys(self.user_password)
        
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        self.assertEqual(self.driver.current_url, self.live_server_url + "/posts")
    
    def test_profile(self):
        url = self.live_server_url + "/login/"
        self.driver.get(url)
        
        username_elem = self.driver.find_element(By.NAME, "username")
        username_elem.clear()
        username_elem.send_keys(self.user.username)
        
        password_elem = self.driver.find_element(By.NAME, "password")
        password_elem.clear()
        password_elem.send_keys(self.user_password)
        
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        
        url = self.live_server_url + "/profile/"
        self.driver.get(url)
        
        username = self.driver.find_element(By.NAME, "username").text
        
        self.assertEqual(username, f"Username: {self.user.username}")
        