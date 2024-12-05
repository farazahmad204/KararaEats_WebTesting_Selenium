
import pytest,time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logging



from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService




    






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


# web_url="https://farazahmed204.pythonanywhere.com/menu/Weeklymenu/"

web_url="http://127.0.0.1:8000/menu/Weeklymenu/"

# This fixture will allow us to choose a browser dynamically
# Define the fixture for setting up and tearing down the browser
@pytest.fixture(autouse=True, scope="function", params=["chrome","firefox","edge"])  
def driver(request,logger):

    browser = request.param
    if browser == "chrome":
        # Initialize Chrome WebDriver
        service =Service(executable_path="chromedriver.exe")
        driver=webdriver.Chrome(service=service)
    
    elif browser == "firefox":
        # Initialize Firefox WebDriver
        service =FirefoxService(executable_path="geckodriver.exe")
        driver=webdriver.Firefox(service=service)

    elif browser == "edge":
        # Initialize Edge WebDriver
        service =EdgeService(executable_path="msedgedriver.exe")
        driver=webdriver.Edge(service=service)

    logger = logging.getLogger()
    logger.info("This is an info log")
    assert 1 == 1
    print("Test Evironment Setup")
    logger.info("logger::Test Evironment Setup")


    driver.maximize_window()  # Maximize window
    driver.set_page_load_timeout(200)  # Timeout in seconds
    driver.implicitly_wait(120)  # Timeout in seconds for each element to load

    yield driver  # Yield the driver to be used in tests
    print("Test Teardown Setup")
    driver.quit()  # Quit the driver after test execution

# Write test cases using the fixture
def test_LoginWithValidAdminUser(driver ,logger):
    # Navigate to Google
    print("Test Case LoginWithValidAdminUser  started")
    logger.info("logger::Test Case LoginWithValidAdminUser  started")          
    driver.get(web_url)
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


    LogoutUser(driver,logger)

@pytest.mark.skip(reason="Skipping this test case intentionally")
#Test2  
def test_SignUpWithNewUser(driver,logger):

        print("Test Case SignUpWithNewUser started")
        logger.info("Test Case SignUpWithNewUser started")
              
        driver.get(web_url)
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
def test_placed_Order_with_single_item(driver,logger):
      
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

      time.sleep(5)  

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

      time.sleep(5) 

      current_title =driver.title
      print(f"Current Page Title: {current_title}")
      expected_title="Order Confirmation"
      assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"

      LogoutUser(driver,logger)


#Test5
def test_placed_Order_with_multiple_item(driver,logger):
      
      print("Test test_placed_Order_with_multiple_item started")
        
      #Login
      LoginWithUser(driver,logger)

      menu_day=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Thursday')]")))

      menu_day.click()

      items_IDs=["quantities_12_1","quantities_12_3","quantities_12_4","quantities_12_7"]

      for item in items_IDs:
        item_qty = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, item))
        )

        item_qty.clear()  # Clears any pre-existing value
        item_qty.send_keys("05")
        if item == "quantities_12_7":
            item_qty.send_keys(Keys.ENTER)
            break;

      time.sleep(5) 
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
      
      time.sleep(5) 
      current_title =driver.title
      print(f"Current Page Title: {current_title}")
      expected_title="Order Confirmation"
      assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"

      LogoutUser(driver,logger)

 
#Test6
def test_placed_Order_multiple_days_with_multiple_items(driver,logger):
      
      print("TEst test_placed_Order_multiple_days_with_multiple_items started")
        
      #Login
      LoginWithUser(driver,logger)
      
      menu_days=['Thursday','Monday','Wednesday','Friday','Saturday','Sunday']
      menu_days_code=['12','10','11','13','14','15']

      for menu, code in zip(menu_days, menu_days_code):
        menu_day=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{menu}')]" )))

        menu_day.click()

        items_IDs=["quantities_"+ code +"_1","quantities_"+ code +"_3","quantities_"+ code +"_4","quantities_"+ code +"_7"]

        for item in items_IDs:
            item_qty = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, item))
            )

            item_qty.clear()  # Clears any pre-existing value
            item_qty.send_keys("05")
            if item == "quantities_15_7":
                item_qty.send_keys(Keys.ENTER)
                break;

      time.sleep(5) 
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
       
      time.sleep(5)

      current_title =driver.title
      print(f"Current Page Title: {current_title}")
      expected_title="Order Confirmation"
      assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"

      LogoutUser(driver,logger)


#################################--- Common Methods ---################################################################
def LoginWithUser(driver ,logger):


    print("going to login")

    driver.get(web_url)
    driver.maximize_window()

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
    

    profile_btn=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'dropdown-toggle') and contains(@class, 'custom-font')]"))
                       )
    profile_btn.click()

    parent_window = driver.current_window_handle
    window_handles = driver.window_handles
    for handle in window_handles:
         if handle != parent_window:
              driver.switch_to.window(handle)  # Switch to the new window

    driver.switch_to.window(parent_window)
    

    Logout_element=WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'dropdown-item') and contains(@class, 'logout-btn')]"))
                       )
    Logout_element.click()

    driver.switch_to.window(parent_window)

    current_title =driver.title
    print(f"Current Page Title: {current_title}")
    expected_title="Karara Eats"
    assert current_title == expected_title, f"Assertion failed: {current_title} is not matched to {expected_title}"