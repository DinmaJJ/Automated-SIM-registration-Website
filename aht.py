import streamlit as st
import plotly.express as px
import pandas as pd
import time

# Initialize session state for tracking AHTs
if 'streamlined_ahts' not in st.session_state:
    st.session_state.streamlined_ahts = []

# Sample traditional AHT data (simulating longer handling times)
traditional_ahts = [120, 150, 130, 140, 110]  # in seconds

st.title("Chidinma Streamlined Prepaid SIM Activation System")
st.markdown("""
This system streamlines customer verification for prepaid SIM activation to reduce Average Handling Time (AHT).
It provides a simple form for individual input, automated verification simulation, and now supports bulk upload for companies.
The dashboard compares traditional vs. streamlined AHT.
""")

# Tabs for individual and bulk upload
tab1, tab2 = st.tabs(["Individual Verification", "Bulk Upload for Companies"])

with tab1:
    # Verification Form for individual
    with st.form("Customer Verification Form"):
        name = st.text_input("Customer Name")
        id_number = st.text_input("ID Number")
        address = st.text_area("Address")
        phone_number = st.text_input("Phone Number")
        reg_date = st.date_input("Registration Date")
        submit = st.form_submit_button("Verify and Activate")

    if submit:
        if name and id_number and address and phone_number:
            start_time = time.time()
            # Simulate streamlined verification process (quick checks)
            time.sleep(0.5)  # Reduced time for streamlined process
            end_time = time.time()
            aht = end_time - start_time
            st.session_state.streamlined_ahts.append(aht)
            st.success(f"Verification successful! SIM activated for {name}. AHT: {aht:.2f} seconds.")
        else:
            st.error("Please fill in all fields.")

with tab2:
    st.markdown("""
    ### Bulk Upload Instructions
    Upload a CSV file with the following columns (exact names required):
    - name
    - phone_number
    - id_number
    - address
    - reg_date
    """)
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            required_columns = ["name", "phone_number", "id_number", "address", "reg_date"]
            if all(col in df.columns for col in required_columns):
                st.success("File uploaded successfully. Processing verifications...")
                batch_ahts = []
                for index, row in df.iterrows():
                    name = row["name"]
                    id_number = row["id_number"]
                    address = row["address"]
                    phone_number = row["phone_number"]
                    reg_date = row["reg_date"]

                    
                    if pd.notna(name) and pd.notna(id_number) and pd.notna(address) and pd.notna(phone_number) and pd.notna(reg_date):
                        start_time = time.time()
                        # Simulate streamlined verification process
                        time.sleep(0.5)  # Reduced time per entry
                        end_time = time.time()
                        aht = end_time - start_time
                        batch_ahts.append(aht)
                        st.write(f"Verified: {name} - AHT: {aht:.2f} seconds")
                    else:
                        st.warning(f"Skipping row {index+1}: Missing data.")
                
                st.session_state.streamlined_ahts.extend(batch_ahts)
                st.success(f"Batch processing complete. {len(batch_ahts)} entries verified.")
            else:
                st.error(f"Missing required columns. Expected: {', '.join(required_columns)}")
        except Exception as e:
            st.error(f"Error processing file: {e}")

# AHT Dashboard
st.header("AHT Dashboard")

if st.session_state.streamlined_ahts:
    avg_streamlined = sum(st.session_state.streamlined_ahts) / len(st.session_state.streamlined_ahts)
else:
    avg_streamlined = 0

avg_traditional = sum(traditional_ahts) / len(traditional_ahts) if traditional_ahts else 0

# Prepare data for visualization
data = pd.DataFrame({
    "Method": ["Traditional", "Streamlined"],
    "Average AHT (seconds)": [avg_traditional, avg_streamlined]
})

# Bar chart for AHT comparison
fig_bar = px.bar(data, x="Method", y="Average AHT (seconds)", title="AHT Comparison: Traditional vs. Streamlined",
                 color="Method", text="Average AHT (seconds)")
fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
st.plotly_chart(fig_bar)

# Line chart for streamlined AHT over activations
if st.session_state.streamlined_ahts:
    streamlined_df = pd.DataFrame({
        "Activation Number": list(range(1, len(st.session_state.streamlined_ahts) + 1)),
        "AHT (seconds)": st.session_state.streamlined_ahts
    })
    fig_line = px.line(streamlined_df, x="Activation Number", y="AHT (seconds)",
                       title="Streamlined AHT Over Multiple Activations")
    st.plotly_chart(fig_line)

st.markdown("""
### How This Reduces AHT:
- **Streamlined Process**: Minimal fields, instant submission, and simulated quick verification reduce manual steps.
- **Bulk Upload**: Allows companies to upload multiple entries at once for faster processing.
- **Traditional Simulation**: Assumes higher AHT based on sample data (e.g., manual checks, more fields).
- Perform verifications (individual or bulk) to see the average AHT update in real-time.
""")