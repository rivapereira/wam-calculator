
import streamlit as st
import pandas as pd
import re

def parse_input(input_text):
    headers = ["Year", "Session", "Campus/Delivery", "Subject Code", "NomCP", "Mark", "Grade", "Status"]
    row_end_keywords = r"(Complete|Withdrawn|Removed|Enrolled)"
    potential_rows = re.split(rf"({row_end_keywords})", input_text)

    rows = []
    current_row = ""
    for part in potential_rows:
        if re.match(row_end_keywords, part.strip(), re.IGNORECASE):
            current_row += f"\t{part.strip()}"
            rows.append(current_row.strip())
            current_row = ""
        else:
            current_row += f" {part.strip()}"

    parsed_rows = []
    for row in rows:
        parts = row.split("\t")
        if len(parts) == len(headers):
            parsed_rows.append(parts)

    if not parsed_rows:
        raise ValueError("No valid rows found. Please check the input formatting.")

    df = pd.DataFrame(parsed_rows, columns=headers)
    df['NomCP'] = pd.to_numeric(df['NomCP'], errors='coerce')
    df['Mark'] = pd.to_numeric(df['Mark'], errors='coerce')
    return df

def calculate_gpa(df):
    def mark_to_gpa(mark):
        if mark >= 85:
            return 4.0
        elif 75 <= mark < 85:
            return 3.7
        elif 65 <= mark < 75:
            return 3.0
        elif 50 <= mark < 65:
            return 2.0
        else:
            return 0.0

    df['GPA Points'] = df['Mark'].apply(mark_to_gpa)
    total_weighted_gpa = (df['GPA Points'] * df['NomCP']).sum()
    total_credits = df['NomCP'].sum()

    if total_credits == 0:
        return 0.0

    return total_weighted_gpa / total_credits

def calculate_wam(df):
    completed = df[df['Status'].str.strip().str.lower() == 'complete']
    if completed.empty:
        raise ValueError("No rows with status 'Complete' were found.")
    completed = completed.dropna(subset=['Mark', 'NomCP'])

    total_marks = (completed['Mark'] * completed['NomCP']).sum()
    total_credits = completed['NomCP'].sum()

    if total_credits == 0:
        raise ValueError("No valid credit points found for completed courses.")

    wam = total_marks / total_credits
    gpa = calculate_gpa(completed)

    credit_100 = completed[completed['Subject Code'].str.match(r'.*1\d{2}$', na=False)]['NomCP'].sum()
    credit_200 = completed[completed['Subject Code'].str.match(r'.*2\d{2}$', na=False)]['NomCP'].sum()
    credit_300 = completed[completed['Subject Code'].str.match(r'.*3\d{2}$', na=False)]['NomCP'].sum()

    return wam, gpa, credit_100, credit_200, credit_300

def main():
    st.set_page_config(page_title="UOWD WAM & GPA Calculator", layout="centered")
    st.title("🎓 WAM & GPA Calculator for UOWD Students")

    with st.expander("ℹ️ About this app"):
        st.markdown("""
        This tool calculates your **Weighted Average Mark (WAM)** and **Grade Point Average (GPA)** based on your subject transcript.
        
        Paste your subject records from SOLS (no headers needed). Example format:
        ```
        2023 Autumn Dubai Math101 6 85 HD Complete
        ```
        Created by [Riva Pereira](https://linkedin.com/in/riva-pereira/), 3rd year UOWD student 💛
        """)

    input_text = st.text_area("📋 Paste your transcript data below:", height=250)

    if st.button("Calculate WAM and GPA"):
        try:
            df = parse_input(input_text)
            st.write("✅ **Parsed Transcript Preview:**")
            st.dataframe(df)

            wam, gpa, credit_100, credit_200, credit_300 = calculate_wam(df)

            st.success(f"🎯 Your WAM is: **{wam:.2f}**")
            st.success(f"🎓 Your GPA is: **{gpa:.2f}**")

            st.subheader("📊 Credit Points Breakdown")
            st.markdown(f"- **100-Level Credits:** {credit_100}")
            st.markdown(f"- **200-Level Credits:** {credit_200}")
            st.markdown(f"- **300-Level Credits:** {credit_300}")

        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
