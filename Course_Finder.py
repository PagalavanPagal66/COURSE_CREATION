import streamlit as st
import sqlite3

from PIL import Image
import cv2

Domains =('DeepLearning',
		  'MachineLearning',
		  'WebDevelopment',
		  'Agriculture',
		  'Marketing',
		  'AppDevelopment',
		  'FashionTech',
		  'IOT',
		  'ARVR',
		  'CloudComputing',
		  'CyberSecurity',
		  'SoftwareTesting',
		  'DataStructures',
		  'SocialMediaBranding',
		  'FoodTechnology',
		  'Chemistry',
		  'Physics',
		  'Biology',
		  'BigData',
		  'BlockChain',
		  'Networking',
		  'Aeronautics',
		  'QuantumComputing',
		  'DroneTechnology',
		  'Economics',
		  'Cinematography',
		  'Robotics',
		  'GraphicsDesign',
		  'DatabaseConnectivity',
		  'Accounting'
)

def create_hash_table(Domain):
	coursesconn = sqlite3.connect(r'C:\Users\pagal\PycharmProjects\TEXT\PSG_iTech\DataBases\Courses_Data.db')
	coursecursor = coursesconn.cursor()
	coursecursor.execute('CREATE TABLE IF NOT EXISTS ' + Domain + '(coursename TEXT NOT NULL UNIQUE,courseduration TEXT NOT NULL,coursedescription TEXT NOT NULL,coursecreator TEXT NOT NULL,coursedifficulty TEXT NOT NULL,courseamt TEXT NOT NULL,coursevideo BLOB NOT NULL,coursetemplate BLOB NOT NULL);')
	coursesconn.commit()

def view_all(Domain):
	create_hash_table(Domain)
	conn = sqlite3.connect(r'C:\Users\pagal\PycharmProjects\TEXT\PSG_iTech\DataBases\Courses_Data.db')
	c = conn.cursor()
	c.execute('SELECT * FROM ' + Domain)
	data = c.fetchall()
	return data

for iter in Domains:
	value = view_all(iter)
	for i in range(0,len(value),3):
		col1 , col2, col3  = st.columns(3)
		try:
			with col1:
				coursename = st.write("COURSE NAME : " +  value[i][0])
				courseduration = st.write("DURATION : "  + value[i][1])
				coursedescription = st.write("DESCRIPTION : "+value[i][2])
				coursecreator = st.write("CREATOR : ",value[i][3])
				coursedifficulty = st.write("DIFFICULTY : " + value[i][4])
				courseamt = st.write("AMT : " + value[i][5])
				coursevideo  = st.video(value[i][6])
				coursetemplate = st.image(value[i][7])
			with col2:
				coursename = st.write("COURSE NAME : " +  value[i+1][0])
				courseduration = st.write("DURATION : "  + value[i+1][1])
				coursedescription = st.write("DESCRIPTION : "+value[i+1][2])
				coursecreator = st.write("CREATOR : ",value[i+1][3])
				coursedifficulty = st.write("DIFFICULTY : " + value[i+1][4])
				courseamt = st.write("AMT : " + value[i+1][5])
				coursevideo  = st.video(value[i+1][6])
				coursetemplate = st.image(value[i+1][7])
			with col3:
				coursename = st.write("COURSE NAME : " +  value[i+2][0])
				courseduration = st.write("DURATION : "  + value[i+2][1])
				coursedescription = st.write("DESCRIPTION : "+value[i+2][2])
				coursecreator = st.write("CREATOR : ",value[i+2][3])
				coursedifficulty = st.write("DIFFICULTY : " + value[i+2][4])
				courseamt = st.write("AMT : " + value[i+2][5])
				coursevideo  = st.video(value[i+2][6])
				coursetemplate = st.image(value[i+2][7])
		except:
			pass
		st.write("-------------------------------------------------")