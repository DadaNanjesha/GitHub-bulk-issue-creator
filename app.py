import streamlit as st
import pandas as pd
from io import StringIO
from utils.github_api import create_issues_from_csv


# Function to generate the sample CSV content
def get_sample_csv():
    """Generate a sample CSV file with the specified format."""
    sample_data = {
        "title": ["Demo title-1", "Demo title-2", "Demo title-3"],
        "body": ["Description-1", "Description-2", "Description-3"],
        "labels": [
            "bug, documentation, duplicate",
            '"enhancement", "good first issue", "help wanted"',
            '"invalid", "question", "wontfix"',
        ],
        "assignee": ["USER-1", "USER-2", "USER-3"],
    }
    df = pd.DataFrame(sample_data)
    return df.to_csv(index=False).encode("utf-8")

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

    # Add a button to download the sample CSV file
    st.write("### Download Sample CSV File to create GitHub Issues")
    sample_csv = get_sample_csv()
    st.download_button(
        label="Download Sample CSV",
        data=sample_csv,
        file_name="issues.csv",
        mime="text/csv",
    )

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
