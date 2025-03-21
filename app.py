import streamlit as st
import pandas as pd
from io import StringIO
from utils.github_api import create_issues_from_csv


def main():
    st.title("GitHub Bulk Issue Creator from CSV")

    # Sidebar for GitHub credentials
    with st.sidebar:
        st.header("GitHub Configuration")
        username = st.text_input("GitHub Username")
        repo = st.text_input("Repository Name")
        token = st.text_input("Personal Access Token", type="password")
        st.markdown(
            "[Create GitHub Token](https://github.com/settings/tokens)")

    # Main content area
    st.write("### Upload CSV File to Create GitHub Issues")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file and username and repo and token:
        try:
            # Preview CSV
            df = pd.read_csv(uploaded_file)
            st.write("**CSV Preview:**")
            st.dataframe(df.head(3))

            # Verify required columns
            required_columns = {'title', 'body', 'labels'}
            if not required_columns.issubset(df.columns):
                st.error(
                    f"CSV missing required columns: {required_columns - set(df.columns)}")
                return

            if st.button("Create GitHub Issues"):
                # Save uploaded file to temporary in-memory file
                string_io = StringIO(uploaded_file.getvalue().decode("utf-8"))
                string_io.seek(0)

                # Create issues using your existing function
                result = create_issues_from_csv(
                    string_io, username, repo, token)

                # Display results
                st.success(result)

        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    elif uploaded_file and not (username and repo and token):
        st.warning("Please fill all GitHub credentials in the sidebar")


if __name__ == "__main__":
    main()
