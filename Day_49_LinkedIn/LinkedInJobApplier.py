from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By


class LinkedInJobApplier:
    """A class to automate job applications on LinkedIn."""

    LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

    def __init__(self, email, password, phone_number, driver_path):
        """
        Initialize the LinkedInJobApplier with the necessary credentials and Chrome driver path.

        :param email: LinkedIn email address
        :param password: LinkedIn password
        :param phone_number: Phone number to be used in the job application
        :param driver_path: File path to the ChromeDriver executable
        """
        self.email = email
        self.password = password
        self.phone_number = phone_number

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    def open_linkedin(self):
        """Open the LinkedIn job search page and click the sign-in button."""
        self.driver.get(self.LINKEDIN_URL)
        sign_in_button_FIRST_PAGE = self.driver.find_element_by_css_selector(".btn-md.btn-secondary-emphasis")
        sign_in_button_FIRST_PAGE.click()
        time.sleep(3)

    def login(self):
        """Log in to the LinkedIn account using the provided email and password."""
        username_button = self.driver.find_element(By.ID, "username")
        password_button = self.driver.find_element_by_id("password")
        sign_in_button_LOGIN_PAGE = self.driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

        username_button.send_keys(self.email)
        password_button.send_keys(self.password)
        time.sleep(3)
        sign_in_button_LOGIN_PAGE.click()
        time.sleep(15)

    def apply_to_first_job(self):
        """Apply to the first job in the list on the LinkedIn job search page."""
        job_list = self.driver.find_elements(By.CLASS_NAME, "scaffold-layout__list-container")
        job_titles = job_list[0].find_elements(By.TAG_NAME, "a")
        first_job_on_list = job_titles[0]

        first_job_on_list.click()
        time.sleep(10)

        first_job_link = first_job_on_list.get_attribute('href')
        self.driver.get(first_job_link)
        time.sleep(10)

        easy_apply_button = self.driver.find_element(By.CSS_SELECTOR, "div.jobs-apply-button--top-card")
        easy_apply_button.click()
        time.sleep(5)

        phone_number_input_bar = self.driver.find_element(By.XPATH,
                                                          '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3691744644-9-phoneNumber-nationalNumber"]')
        phone_number_input_bar.send_keys(self.phone_number)
        time.sleep(3)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'div.display-flex.justify-flex-end.ph5.pv4 button')
        submit_button.click()

    def apply_all_jobs(self):
        """
        Automatically apply to all jobs listed on the LinkedIn job search page.

        This method iterates over all job postings found on the LinkedIn job search page and attempts to apply to each one using the "Easy Apply" button. If the "Easy Apply" button is not found on a job's page (indicating that the job cannot be applied to with "Easy Apply"), it skips to the next job. It logs a message for each job it skips, whether due to the absence of the "Easy Apply" button or due to any other unexpected error.

        After attempting to apply to all jobs, it quits the webdriver, closing the browser.
        """
        job_list = self.driver.find_elements(By.CLASS_NAME, "scaffold-layout__list-container")

        for job in job_list:
            job_names = job.find_elements(By.TAG_NAME, "a")
            clickable_link_list = [link.get_attribute('href') for link in job_names]

            for clickable_link in clickable_link_list:
                self.driver.get(clickable_link)
                time.sleep(5)

                try:
                    easy_apply_button = self.driver.find_element(By.CSS_SELECTOR, "div.jobs-apply-button--top-card")
                    easy_apply_button.click()
                    time.sleep(5)

                    phone_number_input_bar = self.driver.find_element(By.XPATH,
                                                                      '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3691744644-9-phoneNumber-nationalNumber"]')
                    phone_number_input_bar.send_keys(self.phone_number)
                    time.sleep(3)

                    submit_button = self.driver.find_element(By.CSS_SELECTOR,
                                                             'div.display-flex.justify-flex-end.ph5.pv4 button')
                    submit_button.click()

                except NoSuchElementException as error:
                    print(f"The application is not a 1-step standard application hence the {error}\n")
                    continue
                except Exception as e:
                    print(f"An unexpected error occurred while applying for job at {clickable_link}: {e}")

        # Quit the driver after finishing applying to all jobs
        self.driver.quit()

