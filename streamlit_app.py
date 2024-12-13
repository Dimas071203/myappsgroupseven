import streamlit as st
from PIL import Image
import io

# Sidebar - My Member
st.sidebar.title("My Member")
st.sidebar.write("Group 7")

# Member Button
if st.image("logo pu text.jpg"):
    st.sidebar.button("Show My Members")
    st.sidebar.image("foto dimas.jpeg", caption="Dimas Andriawan")
    st.sidebar.image("foto beby.jpeg", caption="Beby")
    st.sidebar.image("foto viky.jpeg", caption="Viky")

# Main app
def main():
    st.title("Merotasi Gambar menggunakan Python")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Rotation slider
        rotation_angle = st.slider("Select rotation angle (degrees)", 0, 360, 0)

        # Rotate image
        rotated_image = image.rotate(rotation_angle, expand=True)

        # Display the rotated image
        st.image(rotated_image, caption="Rotated Image", use_container_width=True)

        # Download options
        st.subheader("Download Rotated Image")
        download_format = st.radio("Select format to download:", ["JPG", "PNG"])

        if st.button("Download"):
            # Save the image in memory
            img_buffer = io.BytesIO()
            rotated_image.save(img_buffer, format=download_format)
            img_buffer.seek(0)

            # Provide download link
            st.download_button(
                label="Download Rotated Image",
                data=img_buffer,
                file_name=f"rotated_image.{download_format.lower()}",
                mime=f"image/{download_format.lower()}"
            )

if __name__ == "__main__":
    main()
