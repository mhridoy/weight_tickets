import streamlit as st
from fpdf import FPDF
import base64

# Function to create a download link for the PDF
def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

# Main Streamlit App
def main():
    st.title("Weight Ticket Generator")
    
    # Input fields for weight ticket data
    with st.form("weight_ticket_form"):
        date = st.date_input("Date")
        time = st.time_input("Time")
        first_weight = st.number_input("First Weight (kg)")
        second_weight = st.number_input("Second Weight (kg)")
        net_weight = st.number_input("Net Weight (kg)")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)  # Set font size to 15
        
        # Add date and time
        pdf.cell(0, 10, txt=f"Date: {date}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Time: {time}", ln=True, align='L')
        
        # Add weights
        pdf.cell(0, 10, txt=f"1st Weight: {first_weight} kg", ln=True, align='L')
        pdf.cell(0, 10, txt=f"2nd Weight: {second_weight} kg", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Net Weight: {net_weight} kg", ln=True, align='L')
        
        # Create download link
        html = create_download_link(pdf.output(dest="S").encode("latin-1"), "weight_ticket")
        st.markdown(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
