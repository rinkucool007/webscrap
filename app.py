import streamlit as st
from scraper import scrape_website, save_to_file
from rag_ollama import query_ollama
import pandas as pd

st.title("Website Scraper")

# Input fields for URL and query
url = st.text_input("Website URL")
query = st.text_input("Query")

if st.button("Scrape"):
    if url and query:
        try:
            # Scrape the website and save HTML to output folder
            content = scrape_website(url)
            filepath = save_to_file(content, 'scraped_content.html')
            st.success('File saved as output/scraped_content.html')
            
            # Query the local RAG Ollama model
            results = query_ollama(query, filepath)
            
            if results:
                # Display the results in tabular format
                st.write("Query Results")
                df = pd.DataFrame(results)
                st.table(df)
            else:
                st.error("No results found or JSON parsing error.")

        except Exception as e:
            st.error(f"Error: {e}")
