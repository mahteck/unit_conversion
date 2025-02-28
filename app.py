import streamlit as st
import time

# Streamlit Page Configuration
st.set_page_config(page_title="Advanced Unit Converter", page_icon="🔄", layout="centered")

# Custom Styles
st.markdown(
    """
    <style>
        body { font-family: Arial, sans-serif; }
        .stButton > button { width: 100%; font-size: 16px; padding: 10px; }
        .stSelectbox { font-size: 16px; }
        .stNumberInput input { font-size: 16px; }
        .header { color: #6A0DAD; text-align: center; font-size: 32px; font-weight: bold; }
        .sub-header { color: #333; text-align: center; font-size: 22px; margin-bottom: 10px; }
        .result-box { background-color: #f0f0f5; padding: 10px; border-radius: 10px; text-align: center; font-size: 18px; font-weight: bold; }
        .footer { text-align: center; color: gray; font-size: 14px; margin-top: 20px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<div class='header'>🔄 Advanced Unit Converter</div>", unsafe_allow_html=True)

# Sidebar for Selecting Unit Type
unit_type = st.sidebar.radio("Select Conversion Type:", [
    "📏 Length Converter",
    "⚖️ Weight Converter",
    "🌡️ Temperature Converter",
    "💧 Liquid Converter",
    "⏳ Time Converter",
    "📐 Area Converter"
])

# Conversion Dictionaries
unit_data = {
    "📏 Length Converter": {
        "units": {
            "Kilometre": 1000, "Metre": 1, "Centimetre": 0.01, "Millimetre": 0.001, "Mile": 1609.34,
            "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254
        }
    },
    "⚖️ Weight Converter": {
        "units": {
            "Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495
        }
    },
    "🌡️ Temperature Converter": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"],
        "custom_conversion": True
    },
    "💧 Liquid Converter": {
        "units": {
            "Litre": 1, "Millilitre": 0.001, "Gallon": 3.78541, "Pint": 0.473176, "Cup": 0.24
        }
    },
    "⏳ Time Converter": {
        "units": {
            "Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400
        }
    },
    "📐 Area Converter": {
        "units": {
            "Square Metre": 1, "Square Kilometre": 1000000, "Square Centimetre": 0.0001, "Acre": 4046.86
        }
    }
}

# Get Selected Unit Data
selected_data = unit_data[unit_type]

# Converter UI
st.markdown(f"<div class='sub-header'>{unit_type}</div>", unsafe_allow_html=True)
amount = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From:", list(selected_data["units"].keys()) if "custom_conversion" not in selected_data else selected_data["units"])
to_unit = st.selectbox("To:", list(selected_data["units"].keys()) if "custom_conversion" not in selected_data else selected_data["units"])

# Conversion Logic
if st.button("Convert", key=f"btn_{unit_type}"):
    if "custom_conversion" in selected_data:
        # Handle Temperature Conversion
        if from_unit == to_unit:
            result = amount
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (amount * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = amount + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (amount - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (amount - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = amount - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (amount - 273.15) * 9/5 + 32
    else:
        # Handle Standard Conversion
        result = amount * (selected_data["units"][to_unit] / selected_data["units"][from_unit])
    
    st.markdown(f"<div class='result-box'>{amount} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>© 2025 Advanced Unit Converter | Developed by Shoaib Munir</div>", unsafe_allow_html=True)
