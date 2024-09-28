import streamlit as st
from playwright.sync_api import sync_playwright
import setup_playwright

# Function to automate browser interaction
def run_playwright(query):
    with sync_playwright() as p:
        # Launch browser with additional arguments for Linux environments
        browser = p.chromium.launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])
        page = browser.new_page()
        page.goto("https://www.google.com")

        # Type in the search box and press Enter
        page.fill('input[name="q"]', query)
        page.press('input[name="q"]', 'Enter')
        
        # Wait for search results
        page.wait_for_selector('h3')

        # Get the text of the first result
        first_result = page.text_content('h3')
        browser.close()
        return first_result

# Streamlit interface
st.title('Playwright in Streamlit Example')

# Input field for user to enter a search term
search_query = st.text_input('Enter search query', '')

# Button to trigger the search
if st.button('Search'):
    if search_query:
        result = run_playwright(search_query)
        st.write('First search result:', result)
    else:
        st.write('Please enter a search query.')
