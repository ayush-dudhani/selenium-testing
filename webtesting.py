from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def login_to_phptravels(driver, username, password, test_case_no):
    try:
        driver.get("https://www.phptravels.net/")

        time.sleep(5)
        
        dropdown_button = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a')
        dropdown_button.click()


        action = ActionChains(driver)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ENTER)
        action.perform()    

       
        assert "Login" in driver.title
        print("Selected 'Login' option from the dropdown")

        time.sleep(3)  

   
        assert "Login" in driver.title
        print("Login Page is opened")

   
        username_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = driver.find_element(By.XPATH, '//*[@id="submitBTN"]')
        login_button.click()

    
        time.sleep(3)

        login_successful_element = driver.find_element(By.XPATH, '//*[@id="fadein"]/div[2]/div/div/div[1]/div/div/div/div[3]/span')  # Replace with the actual selector
        if "Welcome Back" in login_successful_element.text:
            print(f"Login successful for user: {username}")
            dropdown_button = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/a')
            dropdown_button.click()

            logout_button = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[2]/ul/li[3]/ul/li[6]/a')
            logout_button.click()

            print("Logged out successfully")
            print(f"Test case {test_case_no} passed successfully✅")
        else:
            print(f"Login failed for user: {username}")
            print(f"Test case {test_case_no} failed❌")

    except Exception as e:
        print(f"Login failed for user: {username}")
        print(f"Test case {test_case_no} failed❌")


def test_blog_button(driver, test_case_no):
    try:
        driver.get("https://www.phptravels.net/")

        blog_button = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div[1]/ul/li[5]/a')
        blog_button.click()

        time.sleep(3)

        h2_element = driver.find_element(By.XPATH, '//*[@id="fadein"]/section[1]/div[1]/div/div/div/div/div/h2')
        if "PHPTRAVELS Blogs" in h2_element.text:
            print("Blog page is opened")
            print(f"Test case {test_case_no} passed successfully✅")
        else:
            print("Blog page is not opened")
            print(f"Test case {test_case_no} failed❌")
        

    except Exception as e:
        print("Test for the 'Blog' button failed❌")


def main():
    driver = webdriver.Chrome()

    try:
        test_blog_button(driver, 1)
        print()
        login_to_phptravels(driver, "sehol31813@jybra.com", "Pass@1234", 2) # username correct pass correct
        print()
        login_to_phptravels(driver, "sehol1813@jybra.com", "Password123", 3) # username wrong pass wrong
        print()
        login_to_phptravels(driver, "sehol31813@jybra.comm", "Pass@1234", 4) # username wrong pass correct
        print()
        login_to_phptravels(driver, "sehol31813@jybra.com", "", 5) # username correct pass wrong
        print()
        
        
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
