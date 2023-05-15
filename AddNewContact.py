from training.application import Application
from contact import Contact
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.open_home_page()
    app.login(username='admin', password="secret")
    app.open_contact_page()
    app.create_contact(Contact(
        first_name="User_Full",
        middle_name="Auto",
        last_name="Test",
        nickname="AQUA",
        photo="C:\\Users\\drug_\\Pictures\\wtf.jpg",
        title="I will kick your ass",
        company="Best QA corp",
        address="Serbia, Novi-Sad, Zeleznichka 17",
        home_number="381-111-22-3",
        mobile_number="+381-999-011011",
        work_number="No number",
        fax="999-999-876",
        email="best@test.com", email2="best2@test.com", email3="best3@test.com",
        homepage="https://www.youtube.com/",
        address_sec="Serbia, Belgrad, Gagarin ring 19",
        home_sec="+9(111)-987-456-123",
        birthday="16", b_month="June", b_year="2000",
        anniversary="19", a_month="September", a_year="1997",
        notes="Best test user for creat contact testing, i hope you happy"))
    app.return_self_home_page()



# from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from contact import Contact
# from selenium.webdriver.support.select import Select
# from selenium.common.exceptions import NoSuchElementException
# import unittest
#
# class AddNewContact(unittest.TestCase):
#     def setUp(self):
#         self.wd = WebDriver()  # webdriver.Firefox()
#         self.wd.implicitly_wait(30)
#
#     def test_add_new_contact(self):
#         wd = self.wd
#         self.open_home_page(wd)
#         self.login(wd, username='admin', password="secret")
#         self.open_contact_page(wd)
#         self.create_contact(wd, Contact(
#             first_name="User_Full",
#             middle_name="Auto",
#             last_name="Test",
#             nickname="AQUA",
#             photo="C:\\Users\\drug_\\Pictures\\wtf.jpg",
#             title="I will kick your ass",
#             company="Best QA corp",
#             address="Serbia, Novi-Sad, Zeleznichka 17",
#             home_number="381-111-22-3",
#             mobile_number="+381-999-011011",
#             work_number="No number",
#             fax="999-999-876",
#             email="best@test.com", email2="best2@test.com", email3="best3@test.com",
#             homepage="https://www.youtube.com/",
#             address_sec="Serbia, Belgrad, Gagarin ring 19",
#             home_sec="+9(111)-987-456-123",
#             birthday="16", b_month="June", b_year="2000",
#             anniversary="19", a_month="September", a_year="1997",
#             notes="Best test user for creat contact testing, i hope you happy"))
#
#
#         self.return_self_home_page(wd)
#
#     def open_home_page(self, wd):
#         wd.get("http://localhost/addressbook/group.php")
#
#     def login(self, wd, username, password):
#         wd.find_element(By.NAME, "user").click()
#         wd.find_element(By.NAME, "user").clear()
#         wd.find_element(By.NAME, "user").send_keys(username)
#         wd.find_element(By.NAME, "pass").clear()
#         wd.find_element(By.NAME, "pass").send_keys(password)
#         wd.find_element(By.XPATH, "//input[@value='Login']").click()  # (xpath = //input[@value='Login'])
#
#     def open_contact_page(self, wd):
#         wd.find_element(By.LINK_TEXT, "add new").click()
#
#     def create_contact(self, wd, contact):
#
#         wd.find_element(By.NAME, "firstname").click()
#         wd.find_element(By.NAME, "firstname").clear()
#         wd.find_element(By.NAME, "firstname").send_keys(contact.first_name)
#
#         wd.find_element(By.NAME, "middlename").click()
#         wd.find_element(By.NAME, "middlename").clear()
#         wd.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
#
#         wd.find_element(By.NAME, "lastname").click()
#         wd.find_element(By.NAME, "lastname").clear()
#         wd.find_element(By.NAME, "lastname").send_keys(contact.last_name)
#
#         wd.find_element(By.NAME, "nickname").click()
#         wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
#
#         wd.find_element(By.NAME, "photo").send_keys(contact.photo)
#
#         wd.find_element(By.NAME, "title").click()
#         wd.find_element(By.NAME, "title").send_keys(contact.title)
#
#         wd.find_element(By.NAME, "company").click()
#         wd.find_element(By.NAME, "company").send_keys(contact.company)
#
#         wd.find_element(By.NAME, "address").click()
#         wd.find_element(By.NAME, "address").send_keys(contact.address)
#
#         wd.find_element(By.NAME, "home").click()
#         wd.find_element(By.NAME, "home").send_keys(contact.home_number)
#
#         wd.find_element(By.NAME, "mobile").click()
#         wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_number)
#
#         wd.find_element(By.NAME, "work").click()
#         wd.find_element(By.NAME, "work").send_keys(contact.work_number)
#
#         wd.find_element(By.NAME, "fax").click()
#         wd.find_element(By.NAME, "fax").send_keys(contact.fax)
#
#         wd.find_element(By.NAME, "email").click()
#         wd.find_element(By.NAME, "email").send_keys(contact.email)
#
#         wd.find_element(By.NAME, "email2").click()
#         wd.find_element(By.NAME, "email2").send_keys(contact.email2)
#
#         wd.find_element(By.NAME, "email3").click()
#         wd.find_element(By.NAME, "email3").send_keys(contact.email3)
#
#         wd.find_element(By.NAME, "homepage").click()
#         wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
#
#         wd.find_element(By.NAME, "address2").click()
#         wd.find_element(By.NAME, "address2").send_keys(contact.address_sec)
#
#         wd.find_element(By.NAME, "phone2").click()
#         wd.find_element(By.NAME, "phone2").send_keys(contact.home_sec)
#
#         wd.find_element(By.NAME, "notes").click()
#         wd.find_element(By.NAME, "notes").send_keys(contact.notes)
#
#         Select(wd.find_element(By.NAME, "bday")).select_by_visible_text("%s" % contact.birthday)
#         Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text("%s" % contact.b_month)
#         wd.find_element(By.NAME, "byear").send_keys("%s" % contact.b_year)
#
#         Select(wd.find_element(By.NAME, "aday")).select_by_visible_text("%s" % contact.birthday)
#         Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text("%s" % contact.a_month)
#         wd.find_element(By.NAME, "ayear").send_keys("%s" % contact.a_year)
#
#         # submit contact creation
#         wd.find_element(By.NAME, "submit").click()
#
#     def return_self_home_page(self, wd):
#         wd.find_element(By.LINK_TEXT, "home").click()
#
#     def tearDown(self):
#         self.wd.quit()
#
# if __name__ == "__main__":
#     unittest.main()