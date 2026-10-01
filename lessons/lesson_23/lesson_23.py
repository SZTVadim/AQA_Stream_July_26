from time import sleep

from playwright.sync_api import Page, expect, BrowserContext, Dialog

result_selector = "#result-text"


def selector_and_locator(page: Page):
    result_selector1 = "#result-text"  # селектор, как найти элемент на странице в браузере
    result_locator = page.locator(result_selector1)  # локатор, это обернутый селектор, чтобы PW мог с ним работать


def test_visible(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/simple")

    reg_t = page.locator("div#req_text")
    req_b = page.locator("#req_header")

    expect(reg_t).not_to_be_visible()

    # expect(reg_t, "Блок не виден").to_be_visible()  # если хотям свое сообщение об ошибке, то используем формат записи из этой строки

    expect(reg_t).to_be_hidden()

    req_b.click()
    expect(reg_t).to_be_visible()


def test_write_text(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/simple")
    input_text = page.locator("input#id_text_string")
    result = page.locator("#result-text")
    text = "Hello World"
    input_text.press_sequentially(text, delay=700)
    # input_text.fill(text)
    input_text.press("Enter")

    expect(result).to_have_text(text)

def test_write_text(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/simple")
    input_text = page.locator("input#id_text_string")
    result = page.locator("#result-text")
    text = "Hello World"
    input_text.fill(text)
    input_text.press("Enter")

    expect(page.locator("strong")).to_have_text("Enter a valid string consisting of letters, numbers, underscores or hyphens.")


def test_enabled_and_select(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/disabled")

    button = page.locator("input#submit-id-submit")

    expect(button).to_be_disabled()

    page.locator("select#id_select_state").select_option("Enabled")

    expect(button).to_be_enabled()
    button.click()

    expect(button).to_be_disabled()
    expect(page.locator(result_selector)).to_have_text("Submitted")
    expect(page.locator(result_selector)).to_contain_text("bmit")


def test_value(page: Page):
    value = "qwerty"
    page.goto("https://www.qa-practice.com/elements/input/simple")
    input_field = page.locator("#id_text_string")
    input_field.fill(value)
    expect(input_field, f"input value is not {value}").to_have_value("qwerty")


def test_focused(page: Page):
    page.goto("https://www.google.com/")
    field = page.locator("[name='q']")

    expect(field).to_be_focused()

    page.locator(".acUsEb.gwogMd").click()
    expect(field).not_to_be_focused()


def test_tabs(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/link")

    lint = page.locator("#new-page-link")
    with context.expect_page() as _new_page:
        lint.click()
    new_page = _new_page.value

    result = new_page.locator(result_selector)
    expect(result).to_have_text("I am a new page in a new tab")

    pages = context.pages
    first_page = pages[0]
    second_page = pages[1]
    sleep(2)
    first_page.bring_to_front()
    sleep(2)
    second_page.bring_to_front()
    sleep(2)
    new_page.close()
    sleep(2)


def test_d_n_d(page: Page):
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")

    drag_me_locator = page.locator("div#rect-draggable")
    drop_here_locator = page.locator("div#rect-droppable")

    drag_me_locator.drag_to(drop_here_locator)

    result_locator = page.locator("p#text-droppable")

    expect(result_locator).to_be_visible()
    expect(result_locator).to_have_text("Dropped!")


def accept_alert(alert: Dialog):
    alert.accept()


def accetp_alert_with_text(alert: Dialog):
    alert.accept("Test")


def dismiss_alert(alert: Dialog):
    alert.dismiss()


def test_alert_box_with_lambda(page: Page):  # Пример с принятием через анонимную финкцию lambda
    a = 1
    page.goto("https://www.qa-practice.com/elements/alert/alert")
    print(page.url)
    page.on("dialog", lambda alert: alert.accept())
    page.locator(".a-button").click()
    print(page.url)


def test_alert_box(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/alert")
    print(page.url)
    page.on("dialog", accept_alert)
    page.locator(".a-button").click()
    print(page.url)


def test_dismiss_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", dismiss_alert)
    page.locator(".a-button").click()
    expect(page.locator("p#result-text")).to_have_text("Cancel")


def test_accept_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", accept_alert)
    page.locator(".a-button").click()
    expect(page.locator("p#result-text")).to_have_text("Ok")


def test_alert_promt(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/prompt")
    page.on("dialog", accetp_alert_with_text)
    page.locator(".a-button").click()
    expect(page.locator("#result-text")).to_have_text("Test")
