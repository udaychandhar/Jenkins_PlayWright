
from playwright.sync_api import Page, expect

def test_verifyPage(page:Page):
    page.goto("https://automationexercise.com/") # passing url

    myurl=page.url
    print("URL of the application:",myurl)

    expect(page).to_have_url(myurl)  #expected url


def test_verifyTitle(page:Page):
    page.goto("https://automationexercise.com/")
    my_title=page.title()
    print("Title of the application:",my_title)