import os
from LinkedInJobApplier import LinkedInJobApplier

# Retrieve environment variables for login credentials and phone number
EMAIL = os.environ.get("email")
PASSWORD = os.environ.get("linkedin_password")
PHONE_NUMBER = os.environ.get("my_phone_number")

# Specify the path to your ChromeDriver executable
DRIVER_PATH = 'C:/Users/Ashley/Downloads/chromedriver-win64/chromedriver.exe'

# Create an instance of the LinkedInJobApplier class and call its methods to apply to a job
job_applier = LinkedInJobApplier(EMAIL, PASSWORD, PHONE_NUMBER, DRIVER_PATH)
job_applier.open_linkedin()
job_applier.login()
# job_applier.apply_to_first_job()
job_applier.apply_all_jobs()
