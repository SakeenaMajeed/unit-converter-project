import streamlit as st


conversion_factors = {
     
        "Plane Angle": {
        "Degree": 1.0,
        "Arcsecond": 1 / 3600,
        "Gradian": 0.9,
        "Milliradian": 0.0572958,
        "Minute of arc": 1 / 60,
        "Radian": 57.2958
    },
    "Length": {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 0.000001,
        "Nanometer": 0.000000001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852.0,
        "Fathom": 1.8288,  # Added unit
        "Furlong": 201.168,  # Added unit
        "Light Year": 9.461e+15  # Added unit
    },
    "Mass": {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Microgram": 0.000000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Stone": 6.35029,
        "Ton (metric)": 1000.0
    },
    "Temperature": {
        "Celsius": {"to_base": lambda x: x, "from_base": lambda x: x},
        "Fahrenheit": {"to_base": lambda x: (x - 32) * 5/9, "from_base": lambda x: (x * 9/5) + 32},
        "Kelvin": {"to_base": lambda x: x - 273.15, "from_base": lambda x: x + 273.15}
    },
    "Speed": {
        "Meters per second": 1.0,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Knots": 0.514444,
        "Feet per second": 0.3048
    },
    "Time": {
        "Second": 1.0,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0,
        "Week": 604800.0,
        "Month": 2629746.0,
        "Year": 31556952.0
    },
    "Volume": {
        "Liter": 1.0,
        "Milliliter": 0.001,
        "Cubic meter": 1000.0,
        "Cubic centimeter": 0.001,
        "Gallon (US)": 3.78541,
        "Gallon (UK)": 4.54609,
        "Quart": 0.946353,
        "Pint": 0.473176
    },
    "Pressure": {
        "Pascal": 1.0,
        "Kilopascal": 1000.0,
        "Bar": 100000.0,
        "Atmosphere": 101325.0,
        "PSI": 6894.76,
        "Torr": 133.322
    },
    "Energy": {
        "Joule": 1.0,
        "Kilojoule": 1000.0,
        "Calorie": 4.184,
        "Kilocalorie": 4184.0,
        "Kilowatt-hour": 3600000.0,
        "Electronvolt": 1.60218e-19
    },
    "Power": {
        "Watt": 1.0,
        "Kilowatt": 1000.0,
        "Megawatt": 1000000.0,
        "Horsepower": 745.7
    },
    "Fuel Economy": {
        "Miles per gallon (US)": 1.0,
        "Miles per gallon (UK)": 1.20095,
        "Kilometers per liter": 0.425144,
        "Liters per 100km": 235.215
    },
    "Data Transfer Rate": {
        "Bits per second": 1.0,
        "Kilobits per second": 1000.0,
        "Megabits per second": 1000000.0,
        "Gigabits per second": 1000000000.0
    },
    "Digital Storage": {
        "Bit": 1.0,
        "Byte": 8.0,
        "Kilobyte": 8000.0,
        "Megabyte": 8000000.0,
        "Gigabyte": 8000000000.0,
        "Terabyte": 8000000000000.0
    },
}

def convert_units(value, from_unit, to_unit, category):
    factors = conversion_factors.get(category, {})
    if category == "Temperature":
        # Special handling for temperature
        base_value = factors[from_unit]["to_base"](value)
        return factors[to_unit]["from_base"](base_value)
    else:
        return (value * factors[from_unit]) / factors[to_unit]


st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("⚡ Advanced Unit Converter")


conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))


col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    from_unit = st.selectbox("From Unit", list(conversion_factors[conversion_type].keys()))

with col2:
    st.markdown("<h2 style='text-align: center;'>=</h2>", unsafe_allow_html=True)

with col3:
    to_unit = st.selectbox("To Unit", list(conversion_factors[conversion_type].keys()))

value1 = st.number_input("Enter Value", value=1.0, step=0.1, format="%f") 

try:
    value2 = convert_units(value1, from_unit, to_unit, conversion_type)
    st.markdown(f"<h2 style='text-align: center; color: blue;'>Result: {value2:.4f}</h2>", unsafe_allow_html=True)
except Exception as e:
    st.markdown(f"<h2 style='text-align: center; color: red;'>Error: {str(e)}</h2>", unsafe_allow_html=True)

