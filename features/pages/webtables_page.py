from re import I
from xml.dom.minidom import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class webTablesPageLocator(object):

    elemOption = (By.XPATH, "//*[@id='app']/div/div/div[2]/div/div[1]/div/div[3]/h5")
    webtables = (By.XPATH, "//*[@id='item-3']/span")
    element = (By.XPATH, "//*[@id='edit-record-1']")
    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    age = (By.ID, "age")
    salary = (By.ID, "salary")
    department = (By.ID, "department")
    btn_submit = (By.ID, "submit")



class webTables(webTablesPageLocator):
    
    def __init__(self, driver):
        self.driver = driver
    
    def select_element_option(self):
        self.driver.find_element(*self.elemOption).click() 

    def select_webtables(self):
        self.driver.find_element(*self.webtables).click()

    def select_element_to_edit(self):
        self.driver.find_element(*self.element).click()

    def edit_first_name(self, firstName):
        fname = self.driver.find_element(*self.first_name)
        fname.clear()
        fname.send_keys(firstName)
    
    def edit_last_name(self, lastName):
        lname = self.driver.find_element(*self.last_name)
        lname.clear()
        lname.send_keys(lastName)

    def edit_email(self, new_email):
        uEmail = self.driver.find_element(*self.email)
        uEmail.clear()
        uEmail.send_keys(new_email)

    def edit_age(self):
        nAge = self.driver.find_element(*self.age)
        nAge.clear()
        nAge.send_keys(24)

    def edit_salary(self):
        nSalary = self.driver.find_element(*self.salary)
        nSalary.clear()
        nSalary.send_keys(1200)

    def edit_department(self, new_depart):
        nDepart = self.driver.find_element(*self.department)
        nDepart.clear()
        nDepart.send_keys(new_depart)

    def save_modification(self):
        self.driver.find_element(*self.btn_submit).click()