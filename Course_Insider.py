import streamlit as st
import sqlite3
from PIL import Image
import cv2
conn = sqlite3.connect(r'C:\Users\pagal\PycharmProjects\TEXT\PSG_iTech\DataBases\Courses_Data.db')
c = conn.cursor()

def image_to_text(path):
    with open(path,'rb') as file:
        photo = file.read()
    return photo


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

def add_coursesdata(Domain,coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate):
    create_hash_table(Domain)
    conn = sqlite3.connect(r'C:\Users\pagal\PycharmProjects\TEXT\PSG_iTech\DataBases\Courses_Data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO '+Domain + ' (coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate) VALUES (?,?,?,?,?,?,?,?)',(coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate))
    conn.commit()

def view_all_courses(c,Domain):
    create_hash_table(Domain)
    c.execute('SELECT * FROM '+Domain)
    data = c.fetchall()
    return data

def isvalidcourse(c,conn,Domain,coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt):
    create_hash_table(Domain)
    c.execute('SELECT * FROM '+Domain+' WHERE coursename =(?) AND courseduration = (?) AND coursedescription = (?) AND coursecreator = (?) AND coursedifficulty = (?) AND courseamt = (?)',(coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt))
    li=c.fetchall()
    return len(li)

def delete_course(c,conn,Domain,coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate):
    create_hash_table(Domain)
    c.execute("DELETE FROM "+Domain+' WHERE coursename =(?) AND courseduration = (?) AND coursedescription = (?) AND coursecreator = (?) AND coursedifficulty = (?) AND courseamt = (?) AND coursevideo = (?) AND coursetemplate = (?) ',(coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate))
    st.write("DELETED - ",coursename,"From table ",Domain)
    conn.commit()

def update_course(c,conn,Domain,coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate,ucoursename,ucourseduration,ucoursedescription,ucoursecreator,ucoursedifficulty,ucourseamt,ucoursevideo,ucoursetemplate):
    create_hash_table(Domain)
    c.execute("UPDATE "+Domain+" SET coursename =(?) , courseduration = (?) , coursedescription = (?) , coursecreator = (?) , coursedifficulty = (?) , courseamt = (?) , coursevideo = (?) , coursetemplate = (?)  WHERE coursename =(?) AND courseduration = (?) AND coursedescription = (?) AND coursecreator = (?) AND coursedifficulty = (?) AND courseamt = (?) AND coursevideo = (?) AND coursetemplate = (?)",(ucoursename,ucourseduration,ucoursedescription,ucoursecreator,ucoursedifficulty,ucourseamt,ucoursevideo,ucoursetemplate,coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate))
    conn.commit()

def find_course_in_domain(Domain,creatorname):
    create_hash_table(Domain)
    c.execute("SELECT * FROM "+Domain+' WHERE coursecreator =(?)',(creatorname,))
    li = c.fetchall()
    return li

def body():
    add_selectbox = st.sidebar.selectbox(
        "Type of CRUD operation to be performed : ",
        ("ADD","EDIT","DELETE")
    )
    @st.cache_data
    def load_image(image_file):
        img = Image.open(image_file)
        return img

    if(add_selectbox == 'DELETE'):
        count = 0
        creatorname = st.text_input("ENTER COURSE CREATOR NAME : ")
        for iter in Domains:
            create_hash_table(iter)
            value = find_course_in_domain(iter,creatorname)
            count += len(value)
            if(len(value)!=0):
                st.success(iter) #Domain
            for i in range(0,len(value)):
                col1,col2,col3 = st.columns(3)
                with col1:
                    st.write("NAME : " + value[i][0])
                    st.write("DURATION  : " + value[i][1])
                    st.write("DESCRIPTION  : " + value[i][2])
                with col2:
                    st.write("CREATOR :  " + value[i][3])
                    st.write("DIFFICULTY : " +value[i][4])
                    st.write("AMT : " + value[i][5])
                with col3:
                    if(st.button("DELETE",key=str(i)+iter)):
                        delete_course(c,conn,iter,value[i][0],value[i][1],value[i][2],value[i][3],value[i][4],value[i][5],value[i][6],value[i][7])
                        st.error("DELETED SUCCESSFULLY")
                st.video(value[i][6])
                st.image(value[i][7])
                st.write("--------------------------------------")

    # (Domain,coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate)


    if(add_selectbox == 'ADD'):
        col1, col2 = st.columns(2)
        domain = st.text_input("Domain : ")
        with col1:
            coursename = st.text_input("ENTER COURSE NAME : ")
            courseduration = st.text_input("DURATION : ")
            coursedescription = st.text_input("DESCRIPTION : ")
        with col2:
            coursecreator = st.text_input("CREATOR : ")
            coursedifficulty = st.selectbox("DIFFICULTY : ",("EASY","MEDIUM","HARD"))
            courseamt = st.text_input("AMT : ")

        uploaded_files = st.file_uploader("Choose a IMAGE file", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.info("IMAGE UPLOADED SUCCESSFULLY")
            coursetemplate = bytes_data

        uploaded_files = st.file_uploader("Choose a VIDEO file", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            video_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.info("VIDEO UPLOADED SUCCESSFULLY")
            coursevideo = video_data

        if(st.button("SUBMIT")):
            add_coursesdata(domain,coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate)
            st.video(coursevideo)

            st.success("ADDED SUCCESSFULLY...!")

    if(add_selectbox=="EDIT"):
        count = 0
        creatorname = st.text_input("ENTER COURSE CREATOR NAME : ")
        coursecreator = creatorname
        if(st.checkbox("SUBMIT",key = "BUTTON-KEY-SUBMIT")):
            for iter in Domains:
                create_hash_table(iter)
                value = find_course_in_domain(iter, creatorname)
                count += len(value)
                if (len(value) != 0):
                    st.success(iter)  # Domain
                for i in range(0, len(value)):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        coursename = st.text_input("COURSE NAME : ",value= value[i][0])
                        courseduration = st.text_input("DURATION : ",value=value[i][1])
                        coursedescription =  st.text_input("DESCRIPTION : ",value = value[i][2])
                    with col2:
                        coursedifficulty = value[i][4]
                        #st.selectbox("DIFFICULTY : ",("Easy","Medium","Hard"),index=value[i][4])
                        courseamt = st.text_input("AMT : ",value= value[i][5])
                    with col3:

                        uploaded_files = st.file_uploader("Choose a IMAGE file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            bytes_data = uploaded_file.read()
                            st.write("filename:", uploaded_file.name)
                            st.info("IMAGE UPLOADED SUCCESSFULLY")
                            ucoursetemplate = bytes_data

                        uploaded_files = st.file_uploader("Choose a VIDEO file", accept_multiple_files=True)
                        for uploaded_file in uploaded_files:
                            video_data = uploaded_file.read()
                            st.write("filename:", uploaded_file.name)
                            st.info("VIDEO UPLOADED SUCCESSFULLY")
                            ucoursevideo = video_data

                        if st.button("SUBMIT",key=str(i)+iter):
                            update_course(c,conn,iter,value[i][0],value[i][1],value[i][2],value[i][3],value[i][4],value[i][5],value[i][6],value[i][7],coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,ucoursevideo,ucoursetemplate)
                            st.info("UPDATED SUCCESSFULLY")
                    st.write("----------------------------------------------------------")
            if count==0:
                st.write("NO JOBS ADDED")

if __name__ == '__main__':
    body()
# coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate)
# (c,conn,Domain,coursename,courseduration,coursedescription,coursecreator,coursedifficulty,courseamt,coursevideo,coursetemplate,ucoursename,ucourseduration,ucoursedescription,ucoursecreator,ucoursedifficulty,ucourseamt,ucoursevideo,ucoursetemplate):
