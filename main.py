import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, get_body
from parser import parse_with_ollama

st.title('Welcome to web scraper')
url = st.text_input('Enter the website to scrape')

if st.button('Scrape'):
    st.write("Scraping...")
    result = scrape_website(url)
    body_content = get_body(result)
    content_clean = clean_body_content(body_content)

    st.session_state.dom_content = content_clean

    with st.expander("view DOM content"):
        st.text_area("Content:",content_clean, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            final_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(final_result)