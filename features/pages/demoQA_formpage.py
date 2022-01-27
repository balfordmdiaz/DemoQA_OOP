from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class demoqaPageLocator(object):
    txtfirstName = (By.ID, "firstName")
    txtlastName = (By.ID, "lastName")
    txtemail = (By.ID, "userEmail")
    gender = (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]/label")
    phone = (By.ID, "userNumber")
    inptdate = (By.XPATH, "//*[@id='dateOfBirthInput']")
    year = (By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[98]")
    month = (By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[2]")
    day = (By.XPATH, "//*[@id='dateOfBirth']/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[6]")
    subject = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[6]/div[2]/div/div/div[1]/div[2]/div/input")
    hobbieSport = (By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]/label")
    hobbieMusic = (By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[3]/label")
    picture = (By.ID, "uploadPicture")
    addss = (By.ID, "currentAddress")
    state = (By.XPATH, "//*[@id='react-select-3-input']")
    city = (By.XPATH, "//*[@id='react-select-4-input']")
    btnSubmit = (By.ID, "submit")
    


class demoqaPage(demoqaPageLocator):

    def __init__(self, driver):
        self.driver = driver

    def fill_first_name(self, fname):
        self.driver.find_element(*self.txtfirstName).send_keys(fname)

    def fill_last_name(self, lname):
        self.driver.find_element(*self.txtlastName).send_keys(lname)

    def fill_email(self, email):
        self.driver.find_element(*self.txtemail).send_keys(email)

    def select_gender(self):
        self.driver.find_element(*self.gender).click()

    def fill_number(self, number):
        self.driver.find_element(*self.phone).send_keys(number)

    def select_date_birth(self):
        self.driver.find_element(*self.inptdate).click()
        self.driver.find_element(*self.year).click()
        self.driver.find_element(*self.month).click()
        self.driver.find_element(*self.day).click()

    def select_subjects(self):
        math = self.driver.find_element(*self.subject)
        math.send_keys("math")
        math.send_keys(Keys.TAB)
        science = self.driver.find_element(*self.subject)
        science.send_keys("science")
        science.send_keys(Keys.TAB)

    def select_hobbies(self):
        self.driver.find_element(*self.hobbieSport).click()
        self.driver.find_element(*self.hobbieMusic).click()

    def upload_picture(self):
        self.driver.find_element(*self.picture).send_keys("C:\\Users\\Balford\\OneDrive\\Documents\\QA_Automated_Gherkin\\profile.png")

    def insert_address(self, addr):
        self.driver.find_element(*self.addss).send_keys(addr)

    def select_state(self, sta):
        states = self.driver.find_element(*self.state)
        states.send_keys(sta)
        states.send_keys(Keys.TAB)
    
    def select_city(self, cty):
        cities = self.driver.find_element(*self.city)
        cities.send_keys(cty)
        cities.send_keys(Keys.TAB)

    def submit_form(self):
        self.driver.find_element(*self.btnSubmit).click()