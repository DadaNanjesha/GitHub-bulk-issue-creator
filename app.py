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
            "enhancement, good first issue, help wanted",
            "invalid, question, wontfix",
        ],
        "assignee": ["USER-1", "USER-2", "USER-3"],
    }
    df = pd.DataFrame(sample_data)
    return df.to_csv(index=False).encode("utf-8")

def main():
    # Page Configuration
    st.set_page_config(page_title="GitHub Bulk Issue Creator",
                       page_icon=":rocket:", layout="wide")

    # Custom CSS
    st.markdown("""
    <style>
        .main {padding: 2rem;}
        .stDownloadButton, .stButton>button {width: 100%;}
        .stAlert {border-radius: 10px;}
        .header {color: #1f4172; border-bottom: 2px solid #1f4172;}
        .sidebar .sidebar-content {background-color: #f0f2f6;}
        .csv-format {background-color: #f8f9fa; padding: 1rem; border-radius: 10px;}
    </style>
    """, unsafe_allow_html=True)

    # Main Title
    st.markdown("<h1 class='header'>🚀 GitHub Bulk Issue Creator</h1>",
                unsafe_allow_html=True)
    st.write("<h4>📌 Automate your GitHub Issue creation effortlessly!</h4>",
             unsafe_allow_html=True)
    st.write("<p>Tired of manually creating GitHub issues? The GitHub Issue Creator is a Python-based tool designed to automate this process, saving you valuable time and ensuring efficient task tracking. Whether you're managing a personal project or a large open-source repository, this tool is your go-to solution.<p>", unsafe_allow_html=True)

    # Sidebar for GitHub credentials
    with st.sidebar:
        st.header("🔐 GitHub Configuration")
        username = st.text_input(
            "GitHub Username", placeholder="Enter your GitHub username")
        repo = st.text_input("Repository Name", placeholder="owner/repo-name")
        token = st.text_input("Personal Access Token", type="password",
                              help="[Create GitHub Token](https://github.com/settings/tokens)")
        st.markdown("---")
        st.markdown(
            "**Need help?**\n\n1. Enter your GitHub credentials\n2. Download sample CSV\n3. Upload your CSV\n4. Create issues!")

    # Main content columns
    col1, col2 = st.columns([3, 2])

    with col1:
        # File Upload Section
        st.subheader("📤 Upload CSV File")
        uploaded_file = st.file_uploader("Choose a CSV file", type=[
                                         "csv"], label_visibility="collapsed")

        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file)
                with st.expander("📋 CSV Preview (First 3 Rows)", expanded=True):
                    st.table(df.head(3))

                # Validate CSV
                required_columns = {'title', 'body', 'labels'}
                missing_columns = required_columns - set(df.columns)
                if missing_columns:
                    st.error(
                        f"❌ Missing required columns: {', '.join(missing_columns)}")
                else:
                    st.success("✅ CSV format is valid!")

            except Exception as e:
                st.error(f"❌ Error reading CSV file: {str(e)}")

    with col2:
        # Sample CSV Section
        st.subheader("📥 Sample CSV Format")
        st.markdown("""
        <div class="csv-format">
            <p>Required columns:</p>
            <ul>
                <li><code>title</code> (required)</li>
                <li><code>body</code> (required)</li>
                <li><code>labels</code> (required, comma-separated)</li>
                <li><code>assignee</code> (optional)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        sample_csv = get_sample_csv()
        st.download_button(
            label="⬇️ Download Sample CSV",
            data=sample_csv,
            file_name="github_issues_template.csv",
            mime="text/csv",
            help="Download template CSV file with example data"
        )

    # Create Issues Button
    if uploaded_file and username and repo and token:
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Create GitHub Issues", type="primary", use_container_width=True):
                try:
                    with st.spinner("Creating issues..."):
                        string_io = StringIO(
                            uploaded_file.getvalue().decode("utf-8"))
                        string_io.seek(0)
                        result = create_issues_from_csv(
                            string_io, username, repo, token)
                        st.success(result)
                        st.toast("✅ Issues created successfully!", icon="🎉")
                except Exception as e:
                    st.error(f"❌ Error creating issues: {str(e)}")
    elif uploaded_file and not (username and repo and token):
        st.warning("⚠️ Please complete all GitHub credentials in the sidebar")

if __name__ == "__main__":
    main()
