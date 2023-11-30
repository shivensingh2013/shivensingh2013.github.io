import pathlib
import os
import streamlit as st
from PIL import Image

from Scripts.image_extract import cam2bev_image, nuscene_image

rad = st.sidebar.radio("Navigation",["About the app","Play with cam2bev data","Play with Nuscenes data"])
def display_value(val):
    st.write("The value of the slider is:", val)

if rad == "About the app":
    
    st.title("Generating Bird's Eye View from Camera images ")
    st.text("In this web app, we generate bird's eye view from raw images which can be leveraged in many computer vision vehicle problems.")

    st.header("Input to the algorithm")
    path =r"Cam2BEV\data\cam2bev-data\1_FRLR\examples\\"
    name = ["front","rear","left","right"]
    cols = st.columns(len(name))
    for i,stg in enumerate(name):
        img = Image.open(path+stg+".png")
        cols[i].image(img, caption = stg ,width = 200,use_column_width = False)

    st.header("Output of the algorithm")
    image = Image.open(r"Cam2BEV\data\cam2bev-data\1_FRLR\examples\homography.png")
    st.image(image, caption = "Drone View ",width = 400)

elif rad== "Play with cam2bev data":
    st.text("Please provide the inputs below and press the run button")
    # input_img = st.text_input("CAM2BEV Image",value = "t_0_0_0006000.png")

    input_lst  = os.listdir(r"Cam2BEV\data\cam2bev-data\1_FRLR\train\bev")
    input = st.selectbox("Select the Input image name ",input_lst)
    st.write("You selected - ",input)
    val = st.button("Run")
    if val ==True:
        cam2bev_obj = cam2bev_image(input,r"./Cam2BEV/data/cam2bev-data/1_FRLR/train/")   
        st.text("Run complete , Printing Results now ... ")
        cam2bev_obj.print_image(cam2bev_obj.input_path,cam2bev_obj.image_name)
        
elif rad =="Play with Nuscenes data":
    st.text("Please provide the inputs below and press the run button")
    scene = st.text_input("Scene Number (1-10)",value = "1")
    dataroot = st.text_input("Dataroot Path for nuscenes ",value = './nuscene/data/sets/nuscenes/')
    folder_name = st.text_input("Folder name for storing data ",value = '\sample_default_temp')

    input_parent = r"C:\Users\IHG6KOR\Desktop\shiv\Portfolio\shivensingh2013.github.io\P3_Cam2BEV\testing\input\nuscenes\nuscene"

    output_parent = r"C:\Users\IHG6KOR\Desktop\shiv\Portfolio\shivensingh2013.github.io\P3_Cam2BEV\testing\out\nuscene"

    nuscene_obj = nuscene_image(scene = int(scene) ,dataroot_nuscene = dataroot ,dir  = folder_name ,parent = input_parent,out_parent = output_parent)

    val = st.button("regenerate Images")

    # test_sample = nuscene_obj.nuscene_data_obj.get('sample',nuscene_obj.first_sample_token) 
    # nuscene_obj.generate_1_bev(test_sample,1)

    if val == True:
        nuscene_obj.generate_n_BEV()
        st.write("Processing complete")

    frame_num = st.slider('Frame Number', 0, 10, 5)
    nuscene_obj.print_result(input_parent,output_parent,folder_name,frame_num)

        
else: 
    st.text("Not available")
