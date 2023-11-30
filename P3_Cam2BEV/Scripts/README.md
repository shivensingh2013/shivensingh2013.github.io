## 1. Introduction

The files in this folder contains the functionality to run IPM for nuscenes dataset

### Installation

#### Cam2Bev data and scripts

Step1 -  git clone - https://gitlab.ika.rwth-aachen.de/cam2bev/cam2bev-data.git into the specific folder

Incase git clone is not working , you can also download using the steps given below:

Download the data manually as a tar file
input_path = r"./Cam2BEV/data/cam2bev-data/2_F/val/"
path = pathlib.Path(input_path)

for file in tqdm(path.glob("*.tar.gz")):
    data = tarfile.open(file)
    print("extracting  file" , file)
data.extractall(input_path)
print("extraction done " , file)
data.close()


#### Nuscene Dataset and scripts

Steps1:  downaload data to the righ paths
Step2 : !mkdir -p "nuscene/data/sets/nuscenes" 
Step3 : !wget https://www.nuscenes.org/data/v1.0-mini.tgz  # Download the nuScenes mini split.
Step4 :  Uncompress the nuScenes mini split.
Step 5: !tar -xf "C:\Users\IHG6KOR\Downloads\v1.0-mini.tgz" -C "nuscene\data\sets\nuscenes"  
Step 6: !pip install nuscenes-devkit &> /dev/null  # Install nuScenes.