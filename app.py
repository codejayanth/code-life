import streamlit as st
from PIL import Image

# Set up page layout
st.set_page_config(page_title="Digital IKEA - Subscription Packages", layout="wide")

# Helper function to load images
def load_image(image_path):
    return Image.open(image_path)

# Packages data
packages = {
    "Office Package": {
        "description": "Set up a fully functional office at home with our premium package.",
        "price": 150,
        "items": [
            {"name": "Office Chair", "image": "images/office_chair.jpg", "price": 20},
            {"name": "Office Desk", "image": "images/office_desk.jpg", "price": 40},
            {"name": "Monitor", "image": "images/monitor.jpg", "price": 50},
            {"name": "Internet Setup", "image": "images/internet.jpg", "price": 40},
        ],
    },
    "Bedroom Package": {
        "description": "Transform your bedroom into a cozy retreat with our package.",
        "price": 120,
        "items": [
            {"name": "Bed Frame", "image": "images/bed_frame.jpg", "price": 50},
            {"name": "Mattress", "image": "images/mattress.jpg", "price": 40},
            {"name": "Wardrobe", "image": "images/wardrobe.jpg", "price": 20},
            {"name": "Bedside Table", "image": "images/bedside_table.jpg", "price": 10},
        ],
    },
    "Kids Room Package": {
        "description": "Create a fun and safe environment for your kids.",
        "price": 100,
        "items": [
            {"name": "Bunk Bed", "image": "images/bunk_bed.jpg", "price": 50},
            {"name": "Study Desk", "image": "images/study_desk.jpg", "price": 20},
            {"name": "Toy Storage", "image": "images/toy_storage.jpg", "price": 15},
            {"name": "Kids Chair", "image": "images/kids_chair.jpg", "price": 15},
        ],
    },
}

# Initialize session states
if "selected_package" not in st.session_state:
    st.session_state.selected_package = None
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []
if "checkout" not in st.session_state:
    st.session_state.checkout = False

# Header section
st.title("Digital IKEA - Subscription Packages")
st.subheader("Subscribe to fully furnished packages for your home or office.")

# Main content: Package Showcase
if not st.session_state.selected_package and not st.session_state.checkout:
    st.write("---")
    st.header("Choose a Package")
    cols = st.columns(3)

    for idx, (package_name, package_data) in enumerate(packages.items()):
        with cols[idx]:
            st.image(load_image(f"images/{package_name.lower().replace(' ', '_')}.jpg"), use_container_width=True)
            st.subheader(package_name)
            st.write(package_data["description"])
            st.write(f"**Monthly Subscription:** ${package_data['price']}")
            if st.button(f"View {package_name} Details", key=f"view_{package_name}"):
                st.session_state.selected_package = package_name

# Package Details and Item Selection
if st.session_state.selected_package and not st.session_state.checkout:
    st.write("---")
    selected_package = st.session_state.selected_package
    st.header(f"{selected_package} - Details")
    package_data = packages[selected_package]
    st.write(package_data["description"])
    st.write(f"**Monthly Cost:** ${package_data['price']}")

    # Display items in the package with selection options
    st.subheader("Select Items to Include:")
    selected_items = []
    for item in package_data["items"]:
        cols = st.columns([1, 3, 1])
        with cols[0]:
            st.image(load_image(item["image"]), use_container_width=True)
        with cols[1]:
            st.write(f"**{item['name']}**")
            st.write(f"${item['price']}")
        with cols[2]:
            if st.checkbox(f"Add {item['name']}", key=f"{item['name']}"):
                selected_items.append(item)

    if st.button("Proceed to Checkout"):
        st.session_state.selected_items = selected_items
        st.session_state.checkout = True

# Checkout Section
if st.session_state.checkout:
    st.write("---")
    st.header("Checkout")
    st.subheader("Review Your Selected Items:")
    total_cost = 0
    for item in st.session_state.selected_items:
        st.write(f"- **{item['name']}**: ${item['price']}")
        total_cost += item["price"]

    st.write(f"**Total Cost:** ${total_cost}")

    # User Details Form
    st.subheader("Enter Your Details:")
    user_name = st.text_input("Full Name")
    user_address = st.text_area("Home Address")
    user_bank_details = st.text_input("Bank Account Number")
    user_email = st.text_input("Email Address")

    if st.button("Complete Payment"):
        if user_name and user_address and user_bank_details and user_email:
            st.success("Payment Completed Successfully!")
            st.balloons()
            # Reset session state
            st.session_state.selected_package = None
            st.session_state.selected_items = []
            st.session_state.checkout = False
        else:
            st.error("Please fill in all details to complete the payment.")

# Back Button for Navigation
if st.session_state.selected_package or st.session_state.checkout:
    if st.button("Go Back"):
        st.session_state.selected_package = None
        st.session_state.checkout = False
