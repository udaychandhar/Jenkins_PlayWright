import pytest
from playwright.sync_api import Page,expect

#page.get_by_alt_text()
def test_locators(page:Page):

    page.goto("https://automationexercise.com/")
    # page.get_by_alt_text()
    logo=page.get_by_alt_text("Website for automation practice")
    expect(logo).to_be_visible()

    #page.get_by_text()
    text_value=page.get_by_text("Products")
    expect(text_value).to_be_visible()
    expect(page.get_by_text("Products")).to_be_visible()

    # page.get_by_placeholder()
    page.goto("https://demo.nopcommerce.com/")
    page.get_by_placeholder("Search store").fill("Books")
    page.wait_for_timeout(3000)

    #page.get_by_label()
    # page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    # page.get_by_label("First name:").fill("Uday")
    # page.get_by_label("Last name:").fill("Chandhar")
    # page.get_by_label("Email:").fill("uday12@gmail.com")
    # page.wait_for_timeout(3000)


    #page.get_by_title()
    # title_value=page.get_by_title("Show products in category Apparel")
    # expect(title_value).to_have_text("Apparel")
    # expect(page.get_by_title("Show products in category Apparel")).to_have_text("Apparel")

    #page.get_by_role()
    role_value=page.get_by_role("button",name="Electronics")
    expect(role_value).to_be_visible()