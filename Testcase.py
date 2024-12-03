
import pytest,time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging







# Fixture for setting up the logger
@pytest.fixture(autouse=True)
def logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Check if the logger already has handlers to avoid duplication
    if not logger.hasHandlers():
        handler = logging.StreamHandler()  # Print log to console
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.info("logger setup complete")
    return logger




# Define the fixture for setting up and tearing down the browser
@pytest.fixture(autouse=True, scope="function")
def driver(logger):
    logger = logging.getLogger()
    logger.info("This is an info log")
    assert 1 == 1
    print("Test Evironment Setup")
    logger.info("logger::Test Evironment Setup")

    service =Service(executable_path="chromedriver.exe")
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()  # Maximize window
    yield driver  # Yield the driver to be used in tests
    print("Test Teardown Setup")
    driver.quit()  # Quit the driver after test execution

# Write test cases using the fixture
def test_LoginWithValidAdminUser(driver ,logger):
    # Navigate to Google
    print("Test Case LoginWithValidAdminUser  started")
    logger.info("logger::Test Case LoginWithValidAdminUser  started")          
    driver.get("http://127.0.0.1:8000/menu/Weeklymenu/")
    assert "Menu" in driver.title  # Assert that the title contains "Login"
    driver.maximize_window()
    driver.implicitly_wait(15)  # Wait for 2 seconds 


    Login_element=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login')]"))
                       )
    Login_element.click()

    username=driver.find_element(By.ID,"id_username")
    username.send_keys("fahm")

    password=driver.find_element(By.ID,"id_password")
    password.send_keys("fahm")


    Login_btn=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'btn') and contains(@class, 'fancy-btn')]"))
                       )
    Login_btn.click()

    current_title =driver.title
    print(f"Current Page Title: {current_title}")
    logger.info(f"logger::Current Page Title: {current_title}")
    expected_title="Menus"


    time.sleep(10)
    assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"

    time.sleep(10)


    Logout_element=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'logout-btn') and contains(@class, 'custom-font')]"))
                       )
    Logout_element.click()

    current_title =driver.title
    print(f"Current Page Title: {current_title}")
    expected_title="Karara Eats"
    assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"


#Test2
def test_SignUpWithNewUser(driver,logger):

        print("Test Case SignUpWithNewUser started")
        logger.info("Test Case SignUpWithNewUser started")
              
        driver.get("http://127.0.0.1:8000/menu/Weeklymenu/")
        driver.maximize_window()
        driver.implicitly_wait(15)  # Wait for 2 seconds 

        signUp_element=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign Up')]"))
                       )
        signUp_element.click()

        current_title =driver.title
        print(f"Current Page Title: {current_title}")
        expected_title="Registration Form"
        assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"

        username=driver.find_element(By.ID,"id_username")
        username.send_keys("faraz")
        whatsapp_num=driver.find_element(By.ID,"id_whatsapp_num")
        whatsapp_num.send_keys("+61468452067")

        email=driver.find_element(By.ID,"id_email")
        email.send_keys("farazahmed204@gmail.com")

        address=driver.find_element(By.ID,"id_address")
        address.send_keys("237 R1 Johar Town Lahore")

        password1=driver.find_element(By.ID,"id_password1")
        password1.send_keys("faraz03428601213")
        password2=driver.find_element(By.ID,"id_password2")
        password2.send_keys("faraz03428601213")



        create_account_btn=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'btn') and contains(@class, 'fancy-btn')]"))
                       )
        
        create_account_btn.click()

        time.sleep(10)
        current_title =driver.title
        print(f"Current Page Title: {current_title}")
        expected_title="Weekly Menu"
        assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"
       

        Logout_element=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'logout-btn') and contains(@class, 'custom-font')]"))
                       )
        
        Logout_element.click()

        current_title =driver.title
        print(f"Current Page Title: {current_title}")
        expected_title="Karara Eats"
        assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"


#Test3
def test_LoginWithValidUser(driver,logger):
        print("Test Case LoginWithValidUser started")
        logger.info("Test Case LoginWithValidUser started")
        
        LoginWithUser(driver ,logger)
        LogoutUser(driver ,logger)



#Test4
def test_placed_Order(driver,logger):
      
      print("TEst test_placed_Order started")
        
      #Login
      LoginWithUser(driver,logger)

      menu_day=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Thursday')]")))

      menu_day.click()

      item_qty = WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable((By.ID, "quantities_12_1"))
      )
      item_qty.clear()  # Clears any pre-existing value
      item_qty.send_keys("05")
      item_qty.send_keys(Keys.ENTER)

    #   time.sleep(20)

    #   # Locate the submit button and click it
    #   submit_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[i[@class='fas fa-shopping-cart']]"))
    #    )
    #   submit_button.click();

      current_title =driver.title
      print(f"Current Page Title: {current_title}")
      expected_title="Order Placement"
      assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"

      delivery_option=WebDriverWait(driver, 10).until(
                         EC.element_to_be_clickable((By.ID, "home_delivery"))
                         )

      delivery_option.click()

      confirm_btn=WebDriverWait(driver, 10).until(
                         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm Order')]"))
                         )

      confirm_btn.click()

      current_title =driver.title
      print(f"Current Page Title: {current_title}")
      expected_title="Order Confirmation"
      assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"

 



#################################--- Common Methods ---################################################################
def LoginWithUser(driver ,logger):

    driver.get("http://127.0.0.1:8000/menu/Weeklymenu/")
    driver.maximize_window()
    driver.implicitly_wait(15)  # Wait for 2 seconds 


    Login_element=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login')]"))
                       )
    Login_element.click()


    username=driver.find_element(By.ID,"id_username")
    username.send_keys("faraz")

    password=driver.find_element(By.ID,"id_password")
    password.send_keys("faraz03428601213")


    Login_btn=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'btn') and contains(@class, 'fancy-btn')]"))
                   )
    Login_btn.click()

    
    time.sleep(10)

    current_title =driver.title
    print(f"Current Page Title: {current_title}")
    expected_title="Weekly Menu"

    assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"

def LogoutUser(driver ,logger):
    # Navigate to Google
    Logout_element=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'logout-btn') and contains(@class, 'custom-font')]"))
                       )
    Logout_element.click()

    current_title =driver.title
    print(f"Current Page Title: {current_title}")
    expected_title="Karara Eats"
    assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"