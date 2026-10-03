from playwright.sync_api import expect


class HelperAssertions:
    def assert_text_present_on_page(self, element, text):
        expect(element).to_have_text(text)