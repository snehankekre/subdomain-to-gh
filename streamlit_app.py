import requests
import streamlit as st


def get_gh_url(subdomain):
    r = requests.get(
        f"https://share.streamlit.io/api/v2/apps/disambiguate?subdomain={subdomain}"
    )
    try:
        coords = r.json()
        return (
            "https://github.com/"
            + coords["owner"]
            + "/"
            + coords["repository"]
            + "/blob/"
            + coords["branch"]
            + "/"
            + coords["mainModule"]
        )
    except:
        return "Error: " + r.text


subdomain = st.text_input("Streamlit Community Cloud subdomain:", placeholder="subdomain-to-gh")

if subdomain:
    gh = get_gh_url(subdomain)
    st.write("Main module:", gh)
