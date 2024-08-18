import streamlit as st
from db import *
# import qrcode
import time
import os
from PIL import Image # for image
import pandas as pd
import numpy as np # for encryption and decription
import cv2 # for digital computer visualiztaion machine learning
from pyzbar.pyzbar import decode # it can install using (pyzbar version for python 3.12) and open first link and at the bottom open link and download vcredist_x64.exe

st.title("Welcome to QrCode Generator")
choice = st.sidebar.selectbox("Menu",['Create','Read','Update','Delete','Decode','About']) #
timestrf1 = time.strftime("%Y%m%d-%H%M%S")
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=14)
def load_image(img):
    im=Image.open(img)
    return im
create()
if choice=='Create':
    st.subheader("QR Code Generate")
    col1,col2=st.columns(2)
    with col1:
        person_name=st.text_input("Student name")
        person_phoneno=st.text_input("Phone no",max_chars=12)
    with col2:
        person_course=st.selectbox("Course",['Python','Data Science','Django'])
        entry_date=st.date_input("Joining date")
    if st.button("Add record"):
        add(person_name,person_phoneno,person_course,entry_date)
        st.write(f"Record inserted {person_name} sucessufully")
    raw_text={'person Name':person_name,'Phone no':person_phoneno}
    submit_button=st.button("Generate QR Code")
    if submit_button:
        c1,c2=st.columns(2)
        with c1:
            qr.add_data(raw_text)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white') # back is for background color # fill is for color
            img_filename='generate_image_{}{}.png'.format(person_name, timestrf1)
            st.success("Qr Code generated Sucessfully")
            path_for_images= os.path.join('image_folder',img_filename) # os means current path and join
            img.save(path_for_images) # img file name want to save into path for images
            final_image = load_image(path_for_images) # Function called
            st.image(final_image)
        with c2:
            st.info("Qr code raw data")
            st.write(raw_text)

elif choice=='Read':
    st.subheader("Read a record")
    result=view_all_records() # Function called
    # st.write(result) # show in read
    d1=pd.DataFrame(result,columns=['Name','Phone no','Course','Joining date'])
    with st.expander("View all records"): # box
        st.write(d1)
    with st.expander("No of courses"):
        counts = d1['Course'].value_counts().to_frame()
        counts = counts.reset_index()
        st.dataframe(counts)
    with st.expander("Dates "):
        counts = d1['Joining date'].value_counts().to_frame()
        counts = counts.reset_index()
        st.dataframe(counts)

elif choice=='Update':
    st.subheader("Update  a record")
    result = view_all_records()  # Function called
    # st.write(result) # show in read
    d1 = pd.DataFrame(result, columns=['Name', 'Phone no', 'Course', 'Joining date'])
    with st.expander("View all records"):
        st.write(d1)
    list_of_course = view_update()
    # st.write(list_of_course)
    course_list=[i[0] for i in list_of_course]
    # st.write(course_list)
    selected_course=st.selectbox("List of courses",course_list)
    r1 = get_course(selected_course)
    if r1:
        p=r1[0][0]
        q=r1[0][1]
        r=r1[0][2]
        s=r1[0][3]
    col1, col2 = st.columns(2)
    with col1:
        person_name = st.text_input("Person name",p)
        new_person_phoneno = st.text_input("Phone no",q,max_chars=12)
    with col2:
        new_person_course = st.selectbox("Course", ['Python', 'Data Science', 'Django'])
        new_entry_date = st.date_input("Joining date",s)
    if st.button("Updated data"):
        update_data=update(new_person_phoneno,new_person_course,new_entry_date,person_name)
        st.success(f"Record sucessfully updated {person_name}")

    # st.write(r)
elif choice=='Delete':
    st.subheader("Delete a record")
    result = view_all_records()  # Function called
    # st.write(result) # show in read
    d1 = pd.DataFrame(result, columns=['Name', 'Phone no', 'Course', 'Joining date'])
    with st.expander("View all records"):
        st.write(d1)
    list_of_course = view_update()
    # st.write(list_of_course)
    course_list = [i[0] for i in list_of_course]
    # st.write(course_list)
    selected_course = st.selectbox("List of courses", course_list)
    st.warning("Do you want to delete a selected course records {}".format(selected_course))
    if st.button("Delete Data"):
        delete(selected_course)
        st.success(f"Data is deleted for {selected_course}")
    new_data=view_all_records()
    d2 = pd.DataFrame(new_data, columns=['Name', 'Phone no', 'Course', 'Joining date'])
    with st.expander("View all records"):
        st.write(d2)
elif choice=='Decode':
    st.subheader("Decode a code")
    qr_image=st.file_uploader("Qr code image",type=['png','jpeg','jpg'])
    if qr_image is not None:
        file_bytes = np.asarray(bytearray(qr_image.read()),dtype=np.uint8)
        opency_image = cv2.imdecode(file_bytes,1)
        c1, c2= st.columns(2)
        with c1:
            st.image(opency_image)
        with c2:
            st.info("Decode Qr code")
            det= decode(openstrecy_image)
            st.write(det)
            for i in det:
                st.write(i[0])

elif choice=='About':
    st.subheader("About Project")
    st.write("This is a Scanner")

