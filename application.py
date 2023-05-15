from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class Application:

    def __init__(self):
        self.wd = WebDriver()  # webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()  # (xpath = //input[@value='Login'])

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_contact_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create_contact(self, contact):
        wd = self.wd

        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.first_name)

        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middle_name)

        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.last_name)

        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)

        wd.find_element(By.NAME, "photo").send_keys(contact.photo)

        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").send_keys(contact.title)

        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(contact.company)

        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact.address)

        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").send_keys(contact.home_number)

        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_number)

        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").send_keys(contact.work_number)

        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)

        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").send_keys(contact.email)

        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)

        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)

        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)

        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").send_keys(contact.address_sec)

        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").send_keys(contact.home_sec)

        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").send_keys(contact.notes)

        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text("%s" % contact.birthday)
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text("%s" % contact.b_month)
        wd.find_element(By.NAME, "byear").send_keys("%s" % contact.b_year)

        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text("%s" % contact.birthday)
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text("%s" % contact.a_month)
        wd.find_element(By.NAME, "ayear").send_keys("%s" % contact.a_year)

        # submit contact creation
        wd.find_element(By.NAME, "submit").click()

    def return_self_home_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def destroy(self):
        self.wd.quit()
