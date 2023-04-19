import streamlit as st
import pandas as pd
import folium
import altair as alt
import numpy as np
from datetime import datetime
from streamlit_folium import folium_static
from folium.plugins import HeatMap
import random
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import branca.colormap as cm
import bar_chart_race as bcr
from streamlit.components.v1 import html


import math
from shapely.geometry import Point, Polygon








def welcome():
    selected2 = option_menu(None, ["ABOUT",'PEOPLE','DISCLAIMER'], 
    #icons=['house', 'cloud-upload', "list-task"], 
    menu_icon="cahst", default_index=0, orientation="horizontal",
    styles={
    "container": {"padding": "0!important", "background-color": "#a6e7ed"},
    "icon": {"color": "#a6e7ed", "font-size": "25px"}, 
    "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#f7f7f7"},
    "nav-link-selected": {"background-color": "#a6e7ed"},
    }
    )
    if selected2=="ABOUT":
        st.image('homepage.png')
        st.markdown("<div style='text-align: justify; font-size: 20px'>Welcome to the El Paso Data Dashboard of Transportation, Environment and Community Health. This website is created as part of the project A Prototype Data Dashboard for Transportation, Environment and Community Health, funded by the Center for Transportation, Environment and Community Health for 15 months, from January 1, 2022 to March 31, 2023.</div>", unsafe_allow_html=True)
        st.write('')
        st.markdown("<div style='text-align: justify; font-size: 20px'>The objective of this project is to develop a customizable, scalable prototype data dashboard for visualization of transportation, environment, and community health data. This prototype data dashboard is a deliverable for this project. </div>", unsafe_allow_html=True)
        st.write('')
        st.markdown("<div style='text-align: justify; font-size: 20px'>This dashboard has a collection of four layers of data:</div>", unsafe_allow_html=True)
        st.write('')
        st.write("<ul style='list-style-type: disc;'><li style='margin-left: 40px; font-size: 20px;'>Demographic data: Population and median income by zip code from 2016 to 2020.</li></ul>", unsafe_allow_html=True)
        st.write("<ul style='list-style-type: disc;'><li style='margin-left: 40px; font-size: 20px;'>Crash data: Traffic crashes at intersections in the City of El Paso, Texas from 1/1/2016 to 10/18/2021, downloaded from the Texas Department of Transportation’s (TxDOT’s) Crash Report Information System (CRIS) database. </li></ul>", unsafe_allow_html=True)
        st.write("<ul style='list-style-type: disc;'><li style='margin-left: 40px; font-size: 20px;'>Traffic data: Selected vehicle trajectory data in the City of El Paso, Texas from 10/25/2021 to 11/21/2021 acquired from Wejo.</li></ul>", unsafe_allow_html=True)
        st.write("<ul style='list-style-type: disc;'><li style='margin-left: 40px; font-size: 20px;'>Health data: Live data from the City of El Paso, Texas COVID-19 website. </li></ul>", unsafe_allow_html=True)
        

        st.markdown(
            """
            <style>
            .stButton button {
                width: 350px;
                height: 80px;
                font-size: 80px;
                font-weight: bold;
                float: right;
                background-color: #a6e7ed;
                
            }
            </style>
            """,
            unsafe_allow_html=True,
            )
       

        if st.button('Double Click Enter El Paso Data Dashboard'):
            # Set the session state to True to indicate that the user has entered the dashboard
            st.session_state['dashboard_entered'] = True   
    elif selected2=='PEOPLE':
        st.image('homepage.png')
        st.markdown("<div style='text-align: justify; font-size: 20px'> Contact:</div>", unsafe_allow_html=True)
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Dr. Kelvin Cheu</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> Professor, Department of Civil Engineering</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> The University of Texas at El Paso</div>", unsafe_allow_html=True)
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Email: rcheu@utep.edu</div>", unsafe_allow_html=True) 

        st.write('')  
##############################################################################################
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Dr. Ruimin Ke</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> Assistant Professor, Department of Civil Engineering</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> The University of Texas at El Paso</div>", unsafe_allow_html=True)
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Email: rke@utep.edu</div>", unsafe_allow_html=True) 
        st.write('')   

##############################################################################################
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Dr. Jeffrey Weidner</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> Assistant Professor, Department of Civil Engineering</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> The University of Texas at El Paso</div>", unsafe_allow_html=True)
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Email: jweidner@utep.edu</div>", unsafe_allow_html=True)  
        st.write('')  

##############################################################################################
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Chengyue Wang</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> Graduate Student Assistant, Department of Civil Engineering</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> The University of Texas at El Paso</div>", unsafe_allow_html=True)
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Email: cwang5@miners.utep.edu</div>", unsafe_allow_html=True)  
        st.write('')  

##############################################################################################
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Swapnil S Samant</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> Graduate Student Assistant, Department of Civil Engineering</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: justify; font-size: 20px'> The University of Texas at El Paso</div>", unsafe_allow_html=True)
    
        st.markdown("<div style='text-align: justify; font-size: 20px'> Email: sssamant@miners.utep.edu</div>", unsafe_allow_html=True)  
      


        st.markdown(
            """
            <style>
            .stButton button {
                width: 350px;
                height: 80px;
                font-size: 80px;
                font-weight: bold;
                float: right;
                background-color: #a6e7ed;
                
            }
            </style>
            """,
            unsafe_allow_html=True,
            )
       

        if st.button('Double Click Enter El Paso Data Dashboard'):
            # Set the session state to True to indicate that the user has entered the dashboard
            st.session_state['dashboard_entered'] = True   
    
    elif selected2=="DISCLAIMER":
        st.image('homepage.png')

        st.markdown("<div style='text-align: justify; font-size: 20px'>The data presented in this dashboard is for illustrative purposes. It should not be used to make a conclusion or policy decision.</div>", unsafe_allow_html=True)
        st.write('')
        st.markdown("<div style='text-align: justify; font-size: 20px'>The contents of this dashboard reflect the views of the authors, who are responsible for the facts and the accuracy of the information presented herein. This document is disseminated in the interest of information exchange. The project is funded, partially or entirely, by a grant from the U.S. Department of Transportation’s University Transportation Centers Program. However, the U.S. Government assumes no liability for the contents or use thereof.</div>", unsafe_allow_html=True) 


        st.markdown(
            """
            <style>
            .stButton button {
                width: 350px;
                height: 80px;
                font-size: 80px;
                font-weight: bold;
                float: right;
                background-color: #a6e7ed;
                
            }
            </style>
            """,
            unsafe_allow_html=True,
            )
       

        if st.button('Double Click Enter El Paso Data Dashboard'):
            # Set the session state to True to indicate that the user has entered the dashboard
            st.session_state['dashboard_entered'] = True   


def dashboard(): 
    # Load the data
    crash_data = pd.read_csv('crash_data.csv')
    covid_data = pd.read_csv('covid_data.csv')
    traffic_data = pd.read_csv('traffic_data.csv')
    bar_data=pd.read_csv('barrace.csv')

    # Set up the Streamlit app
    #st.title('El Paso Data Dashboard')
    # Set up the Streamlit app
    #st.set_page_config(page_title='El Paso Data Dashboard', page_icon=':bar_chart:')

    # Two lines
    st.title('El Paso Data Dashboard')
    st.subheader('Transportation, Environment and Community Health')
    st.sidebar.markdown("<div style='text-align: justify; font-size: 36px'><b>Main menu<b></div>", unsafe_allow_html=True) 

    # One Line
    #st.title('El Paso Data Dashboard \n Transportation, Environment and Community Health')

    # Add a dropdown to allow the user to select a data module
    #data_module = st.sidebar.selectbox('Select a data module', ['Crash Data', 'Traffic Data', 'Health Data'])
    with st.sidebar:
        option7=['Demographic 👪','Crash Data 🚗', 'Traffic Data 🚦', 'Health Data 🏥']
        selected = option_menu(None,option7, 
            icons=['car', 'traffic light','hospital','sfbu'], menu_icon="nn", default_index=0,
            styles={
            "container": {"padding": "0!important", "background-color": "#a6e7ed"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#f7f7f7"},
            "nav-link-selected": {"background-color": "#a6e7ed"},
            }
            )

        #selected

    #tab1, tab2, tab3 = st.tabs(['Crash Data 🚗', 'Traffic Data 🚦', 'Health Data 🏥'])
    # Add a radio button group to allow the user to select a data module
    #data_module = st.radio('Select a data module', ['Crash Data 🚗', 'Traffic Data 🚦', 'Health Data 🏥'])



    # Define a dictionary of icons for each data module option
    # icons = {
    #     'Crash Data': '🚗',
    #     'Traffic Data': '🚦',
    #     'Health Data': '🏥',
    # }

    # # Add a selectbox to allow the user to select a data module
    # data_module = st.selectbox('Select a data module', ['Crash Data', 'Traffic Data', 'Health Data'], format_func=lambda x: icons[x]+' '+x)

    #if data_module == 'Crash Data':
    if selected=='Demographic 👪':
        year = st.sidebar.selectbox('Year', ['2016','2017','2018','2019','2020'])
        attribute=st.sidebar.selectbox('Attribute', ['Population','Median Household Income'])
        if year=='2016' and attribute=='Population':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the population in that Zip code area')
            st.image('population_16.png')
        elif year=='2017' and attribute=='Population':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the population in that Zip code area')
            st.image('population_17.png')
        elif year=='2018' and attribute=='Population':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the population in that Zip code area')
            st.image('population_18.png')
        elif year=='2019' and attribute=='Population':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the population in that Zip code area')
            st.image('population_19.png')
        elif year=='2020' and attribute=='Population':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the population in that Zip code area')
            st.image('population_20.png')
        elif year=='2016' and attribute=='Median Household Income':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the Median Household Income in that Zip code area')
            st.image('income_16.png')
        elif year=='2017' and attribute=='Median Household Income':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the Median Household Income in that Zip code area')
            st.image('income_17.png')
        elif year=='2018' and attribute=='Median Household Income':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the Median Household Income in that Zip code area')
            st.image('income_18.png')
        elif year=='2019' and attribute=='Median Household Income':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the Median Household Income in that Zip code area')
            st.image('income_19.png')
        elif year=='2020' and attribute=='Median Household Income':
            st.markdown('##### The '+attribute+' of'+' Year '+ year)
            st.write('The black number represents the Zip code of that area')
            st.write('The red number and the bar represents the Median Household Income in that Zip code area')
            st.image('income_20.png')










    elif selected=='Crash Data 🚗':



        

        # Add options to select the type of map display
        option1=['Marker Cluster', 'Heat Map', 'Markers','Crash Map']
        map_type = st.sidebar.selectbox('Display Mode', option1)

        # Add options to filter by crash severity

        if map_type=='Crash Map':
            attribute=st.sidebar.selectbox('Attribute', ['Crashes','Crash Rate'])
            if attribute=='Crashes':
                year = st.sidebar.selectbox('Period', ['2016-2019','2020'])
                st.sidebar.image(['utep_new_logo.png','CTECH.jpeg'], width=150)
                if year=='2016-2019':
                    st.markdown('##### The '+attribute+' number of'+' Year '+ year)
                    st.write('The black number represents the Zip code of that area')
                    st.write('The red number and the bar represents the average crashes number in that Zip code area')
                    st.image('crash2016.png')
                elif year=='2020':
                    st.markdown('##### The '+attribute+' number of'+' Year '+ year)
                    st.write('The black number represents the Zip code of that area')
                    st.write('The red number and the bar represents the crashes number in that Zip code area')
                    st.image('crash2020.png')
            elif attribute=='Crash Rate':
                
                st.markdown('##### Crash Rate comparison before and after COVID')
                st.write('The black number represents the Zip code of that area')
                st.write('The purple number and the bar represents the Crash rate(Crashes/year /10,000 pop) in that Zip code area before COVID')
                st.write('The green number and the bar represents the Crash rate(Crashes/year /10,000 pop) in that Zip code area during COVID')
                st.image('compare.png')
                st.sidebar.image(['utep_new_logo.png','CTECH.jpeg'], width=150)


        else:
        
            # Set default values for start_date and end_date
            default_start_date = pd.to_datetime('2020-01-01')
            default_end_date = pd.to_datetime('2020-03-31')

            # Add a slider to allow the user to select a time frame
            start_date = st.sidebar.date_input('Start date', default_start_date)
            end_date = st.sidebar.date_input('End date', default_end_date)
                    # Add options to filter by crash severity
            option2=['All','Not Injured', 'Suspected Minor Injury', 'Possible Injury', 'Suspected Serious Injury', 'Fatal Injury', 'Unknown']
            crash_severity = st.sidebar.selectbox('Crash Severity', option2)


            crash_data['Crash Date'] = pd.to_datetime(crash_data['Crash Date'], format='%m/%d/%Y')

            # Filter the data based on the user's selection
            filtered_data = crash_data[(crash_data['Crash Date'] >= pd.Timestamp(start_date)) & (crash_data['Crash Date'] <= pd.Timestamp(end_date))]

            if crash_severity != 'All':
                filtered_data = filtered_data[filtered_data['Crash Severity'] == crash_severity.upper()]

            # Create a map using Folium
            m = folium.Map(location=[31.7619, -106.4850], zoom_start=11)


            # Add markers to the map for each crash in the filtered data
            #for index, row in filtered_data.iterrows():
            #    lat = row['Crash Latitude']
            #    lon = row['Crash Longitude']
            #    marker = folium.Marker([lat, lon])
            #    marker.add_to(m)
            # Add markers, heatmap, or marker clusters to the map based on user selection

            # st.sidebar.subheader('Authors:')
            # st.sidebar.write('- Kelvin Cheu')
            # st.sidebar.write('- Ruimin Ke')
            # st.sidebar.write('- Chengyue Wang')
            # st.sidebar.write('- Swapnil Samat')
            # st.sidebar.write('- Jeffrey Weidner') 
            # CTECH logo and UTEP logo are side-by-side
            st.sidebar.image(['utep_new_logo.png','CTECH.jpeg'], width=150)
            #CTECH logo is below to UTEP logo
            #st.sidebar.image('utep_new_logo.png', width=200)
            #st.sidebar.image('CTECH.jpeg', width=200)
            if map_type == 'Markers':
                st.write('Each icon represents one crash')

                #st.write('Green N icon represents the crash severity is NOT INJURED')
                #st.write('Blue I icon represents the crash severity is SUSPECTED MINOR INJURY or POSSIBLE INJURY SUSPECTED or SERIOUS INJURY')
                #st.write('Red F icon represents the crash severity is FATAL INJURY')
                #st.write('Pink U icon represents the crash severity is UNKNOWN')
                #if crash_severity!='SUSPECTED SERIOUS INJURY':
                for index, row in filtered_data.iterrows():
                    lat = row['Crash Latitude']
                    lon = row['Crash Longitude']
                    ser= row['Crash Severity']
                    if ser=='NOT INJURED':
                        folium.Marker(location=[lat, lon], tooltip='Not Injured', icon=folium.Icon(color='green',icon="o",prefix='fa')).add_to(m)
                    elif ser=='FATAL INJURY':
                        folium.Marker(location=[lat, lon], tooltip='Fatal Injury', icon=folium.Icon(color='red',icon="k",prefix='fa')).add_to(m)
                    elif ser=='UNKNOWN':
                        folium.Marker(location=[lat, lon], tooltip='Unknown', icon=folium.Icon(color='black',icon="u",prefix='fa')).add_to(m)
                    elif ser=='SUSPECTED SERIOUS INJURY': 
                        folium.Marker(location=[lat, lon], tooltip='Suspected Serious Injury', icon=folium.Icon(color='blue',icon="a",prefix='fa')).add_to(m)
                    elif ser=='SUSPECTED MINOR INJURY': 
                        folium.Marker(location=[lat, lon], tooltip='Suspected Minor Injury', icon=folium.Icon(color='orange',icon="b",prefix='fa')).add_to(m)
                    elif ser=='POSSIBLE INJURY': 
                        folium.Marker(location=[lat, lon], tooltip='Possible Injury', icon=folium.Icon(color='pink',icon="c",prefix='fa')).add_to(m)
                            ################################################3
                #else:
                #    st.write('None crashes occurred with the severity of suspected serious injury')
                #lgd_txt = '<span style="color: {col};">{txt}</span>'
                #fg1 = folium.FeatureGroup(name= lgd_txt.format( txt= 'N icon is Not Injured Carsh', col='green'))
                
    #           m.add_child( fg1)
    






                ############################################3
                #folium.map.LayerControl('bottomleft', collapsed= False).add_to(m)


                    
                # marker = folium.Marker([lat, lon])
                    
                    #marker.add_to(m)


                
                
            elif map_type == 'Heat Map':
                data = filtered_data[['Crash Latitude', 'Crash Longitude']].values.tolist()
                st.write('The colors represent the likelihood of a crash happen in that area')
                heatmap_layer = HeatMap(data, name='Crashes Location Heat Map', min_opacity=0.2,
                                blur=5, max_zoom=10, radius=10, gradient={0.2: 'green', 0.4: 'blue', 0.6: 'yellow', 0.8: 'red', 1:'maroon'})
                heatmap_layer.add_to(m)
                ###########################################################################



                step = cm.StepColormap(['green','blue','yellow','red','maroon'],
                                    vmin=0, vmax=1, index=[0,0.2,0.4,0.6,0.8,1],
                                    caption='Density')
                #folium.map.LayerControl('topleft', collapsed= False).add_to(m)

                step.add_to(m)
        ###############################################################################################################


                #folium_static(m)
                #folium.plugins.heatmap_layer.add_to(m)
            else:
                from folium.plugins import MarkerCluster
                st.write('The number in the circle is the number of crashes happened in that area')
        

                marker_cluster = MarkerCluster(name='Marker Cluster')

    

                for index, row in filtered_data.iterrows():
                    lat = row['Crash Latitude']
                    lon = row['Crash Longitude']
                    ser= row['Crash Severity']
                    if ser=='NOT INJURED':
                        marker=folium.Marker(location=[lat, lon], tooltip='Not Injured', icon=folium.Icon(color='green',icon="o",prefix='fa'))
                    elif ser=='FATAL INJURY':
                        marker=folium.Marker(location=[lat, lon], tooltip='Fatal Injury', icon=folium.Icon(color='red',icon="k",prefix='fa'))
                    elif ser=='UNKNOWN':
                        marker=folium.Marker(location=[lat, lon], tooltip='Unknown', icon=folium.Icon(color='black',icon="u",prefix='fa'))
                    elif ser=='SUSPECTED SERIOUS INJURY': 
                        marker=folium.Marker(location=[lat, lon], tooltip='Suspected Serious Injury', icon=folium.Icon(color='blue',icon="a",prefix='fa'))
                    elif ser=='SUSPECTED MINOR INJURY': 
                        marker=folium.Marker(location=[lat, lon], tooltip='Suspected Minor Injury', icon=folium.Icon(color='orange',icon="b",prefix='fa'))
                    elif ser=='POSSIBLE INJURY': 
                        marker=folium.Marker(location=[lat, lon], tooltip='Possible Injury', icon=folium.Icon(color='pink',icon="c",prefix='fa'))

                    marker_cluster.add_child(marker)
                
                marker_cluster.add_to(m)



        

            # Display the map in the Streamlit app
            folium_static(m)

    #elif data_module == 'Traffic Data':
    elif selected=='Traffic Data 🚦':
        # Filter the data by date and time
        #date = st.date_input('Select a date', min_value=traffic_data['capturedtimestamp'].min().date(), max_value=traffic_data['capturedtimestamp'].max().date())
        #time = st.time_input('Select a time')
        # Speed-based pattern analysis
        traffic_data['postalcode'].replace([np.nan, np.inf, -np.inf], 0, inplace=True)
        traffic_data['postalcode'] = traffic_data['postalcode'].astype(int)
        option3=sorted(traffic_data['postalcode'].unique())
        option3[0]="All"

        zip_code = st.sidebar.selectbox('Zip Code', option3)
        option4=['Table','Density Heat Map','Trajectory Visualization','Speed Map','Markers With Speed']
        disply_type = st.sidebar.selectbox('Display Mode', option4)
        # if zip_code == -1:
        #     zip_code = 'All'
        if zip_code != "All":
            traffic_data = traffic_data[traffic_data['postalcode'] == zip_code]

        # st.sidebar.subheader('Authors:')
        # st.sidebar.write('- Kelvin Cheu')
        # st.sidebar.write('- Ruimin Ke')
        # st.sidebar.write('- Chengyue Wang')
        # st.sidebar.write('- Swapnil Samat')
        # st.sidebar.write('- Jeffrey Weidner') 

        # CTECH logo and UTEP logo are side-by-side
        #st.sidebar.image(['utep_new_logo.png','CTECH.jpeg'], width=150)
        #CTECH logo is below to UTEP logo
        #st.sidebar.image('utep_new_logo.png', width=200)
        #st.sidebar.image('CTECH.jpeg', width=200)

        #st.subheader('Speed-based Pattern Analysis')
        #st.write("Use this slider to filter the data of your interest by selecting a speed range (km/h)")
        #speed_threshold = st.slider('Only', min_value=0, max_value=120, step=5, value=50,label_visibility="collapsed")
        speed_df = traffic_data#[traffic_data['speed'] >= speed_threshold]
        #disply_type = st.sidebar.selectbox('Select a zip code', ['Table','Density Heatmap','Trajectory Visualization'])
        if disply_type == 'Table':
            if len(speed_df) > 0:
                st.write('Number of datapoints:', str(len(speed_df)))
                st.write(speed_df)
                st.write('Average speed:', str(round(speed_df['speed'].mean(),2)),'km/h')#round(answer, 2)
                st.write('Max speed:', str(speed_df['speed'].max()),'km/h')
                st.write('Min speed:', str(speed_df['speed'].min()),'km/h')
                st.write('Standard deviation:', str(round(speed_df['speed'].std(),2)),'km/h')


            else:
                st.write('No datapoints above the speed threshold')
        
        
        elif disply_type=='Density Heat Map':

            # Density analysis

            st.markdown('#### Density Heat Map ')
            st.write('The colors represent the traffic volume in the area')
            m = folium.Map(location=[31.771959, -106.438233], zoom_start=10)
            data = traffic_data[['latitude', 'longitude']].values.tolist()
            heatmap_layer = HeatMap(data, name='Crashes Location Heat Map', min_opacity=0.2,
                                blur=5, max_zoom=10, radius=10, gradient={0.2: 'green', 0.4: 'blue', 0.6: 'yellow', 0.8: 'red', 1:'maroon'})
            heatmap_layer.add_to(m)
                ###########################################################################



            step = cm.StepColormap(['green','blue','yellow','red','maroon'],
                                vmin=0, vmax=1, index=[0,0.2,0.4,0.6,0.8,1],
                                caption='Density')
            

            step.add_to(m)
            
        ###############################################################################################################

            
            folium_static(m)
        elif disply_type=='Trajectory Visualization':

            # Trajectory analysis based on journeyid
            st.markdown('#### Trajectory Visualization')
            st.write('Each trip is represented by a color coded marker with the origin O and the destination D')
            #st.write('O icon means the origin, D icon means destination')
            m2 = folium.Map(location=[31.771959, -106.438233], zoom_start=10)
            colors=['blue', 'lightblue', 'white', 'gray', 'beige', 'darkred', 'darkgreen', 'pink', 'orange', 'red', 'cadetblue', 'black', 'lightgreen', 'purple', 'lightgray', 'lightred', 'darkpurple', 'green', 'darkblue']
            #colors = ['blue','red','green','purple','black','gray','yellow']
            grouped = traffic_data.groupby(by='journeyid')
            for name, group in grouped:
                original_points = [group['latitude'].tolist(), group['longitude'].tolist()]
                
                points = [list(row) for row in zip(*original_points)]
                thecolor=colors[random.randrange(0,len(colors)-1)]
                #print('points:',points)
                #print('################################################')
                #print('original:',original_points)
                folium.Marker(location=points[0], tooltip='Origin', icon=folium.Icon(color=thecolor,icon="o",prefix='fa')).add_to(m2)
                folium.Marker(location=points[-1], tooltip='Destination', icon=folium.Icon(color=thecolor,icon="d",prefix='fa')).add_to(m2)
                folium.PolyLine(points, color=thecolor, weight=4, opacity=0.75).add_to(m2)
                                   ################################################3
     

            folium_static(m2)
        # journeyids = traffic_data['journeyid'].unique()
        # selected_journeyid = st.selectbox('Select a journeyid', ['All'] + list(journeyids))
        # if selected_journeyid != 'All':
        #     journey_df
        elif disply_type=='Speed Map':
            rect_coords1 = [
                [31.785590146507584, -106.50633886050541],
                [31.785519017419706, -106.50654373655537],
                [31.785440116256606, -106.50669609987328],
                [31.78538198556584, -106.50679848838172],
                [31.785329474676455, -106.50674925819219],#guaiwan
                [31.78538746395495, -106.50666521511947],
                [31.785445681884624, -106.5065255199026],
                [31.785532506613087, -106.50631724253319]
            ]



            rect_coords2 = [
                [31.785590146507584, -106.50633886050541],
                [31.785519017419706, -106.50654373655537],
                [31.785440116256606, -106.50669609987328],
                [31.78538198556584, -106.50679848838172],
                [31.785421383331773, -106.50682925511762],#guaiwan
                [31.785484632495702, -106.50672986557348],
                [31.785553314877305, -106.5065685667387],
                [31.78564496044706, -106.50635111526474]
            ]    
            rect_coords3 = [

                [31.78538198556584, -106.50679848838172],#zhongdian
                [31.785421383331773, -106.50682925511762],#guaiwan
                [31.785307954482583, -106.50696584450057],
                [31.785207827589158, -106.50707186540912],
                [31.785136550971554, -106.5071184222367],
                [31.78504152962508, -106.50719615327684],#guaiwan
                [31.785007218945555, -106.5071529013864],#zhongdian
                [31.785107551766867, -106.50708451475963],
                [31.785276441008914, -106.50692586030482]

            ]       
            rect_coords4 = [



                [31.785007218945555, -106.5071529013864],#zhongdian
                [31.785107551766867, -106.50708451475963],
                [31.785276441008914, -106.50692586030482],
                [31.78538198556584, -106.50679848838172],#zhongdian
                [31.785329474676455, -106.50674925819219],#guaiwan
                [31.78522384960199, -106.50688295659515],
                [31.785139326896953, -106.50696380607235],
                [31.785068002010462, -106.50701978644916],
                [31.78497025007966, -106.50709129515258]

            ] 
            rect_coords5 = [



                [31.785007218945555, -106.5071529013864],#zhongdian
                [31.78497025007966, -106.50709129515258],
                [31.784478884590328, -106.50736861192183],
                [31.78449474787003, -106.50744947959869],#zhongdian
                [31.78473513213546, -106.50732456865131],

            ]
            rect_coords6 = [

                [31.78449474787003, -106.50744947959869],#zhongdian
                [31.78473513213546, -106.50732456865131],
                [31.785007218945555, -106.5071529013864],#houzhongdian
                [31.78504152962508, -106.50719615327684],#guaiwan
                [31.78475636943989, -106.50737143352933],
                [31.784508012172132, -106.50751851435861]#guaiwan
            ]
            rect_coords7 = [

                [31.78449474787003, -106.50744947959869],#zhongdian
                [31.784508012172132, -106.50751851435861],#guaiwan
                [31.784412564527806, -106.5075528450727],
                [31.784132378686994, -106.50756892287365],
                [31.783838380692824, -106.50753362782437],#guaiwan
                [31.783864828729865, -106.50746216020296],#zhongdian
                [31.78396813714825, -106.5074720869729],
                [31.784113845919304, -106.50748482634403],
                [31.78426182940279, -106.50749380045936]
                
                
                
            ]
            rect_coords8 = [

                

                [31.783864828729865, -106.50746216020296],#zhongdian
                [31.78396813714825, -106.5074720869729],
                [31.784113845919304, -106.50748482634403],
                [31.78426182940279, -106.50749380045936],
                [31.78449474787003, -106.50744947959869],#zhongdian
                [31.784475558050868, -106.50738127175774],
                [31.784383462001696, -106.50740966995552],
                [31.784127084207377, -106.50741318878721],
                [31.783885986051704, -106.5073937548308],#guaiwan
                
                
                
            ]
            rect_coords9 = [

                

                [31.783864828729865, -106.50746216020296],#zhongdian
                [31.783885986051704, -106.5073937548308],#guaiwan
                [31.78307870921669, -106.50723821109742],
                [31.78251834735184, -106.50718021078447],
                [31.78251061454291, -106.50723538532286],#zhongdian
                [31.78307347043351, -106.50729989847396],
                
                
                
            ]
            rect_coords10 = [

                [31.78251061454291, -106.50723538532286],#zhongdian
                [31.78307347043351, -106.50729989847396],
                [31.783864828729865, -106.50746216020296],#zhongdian
                [31.783838380692824, -106.50753362782437],#guaiwan
                [31.78307287746508, -106.50738295958516],
                [31.78247078237203, -106.50730602080209]
                
                
                
            ]
            rect_coords11 = [

                


                [31.78251834735184, -106.50718021078447],
                [31.782475857123334, -106.50717115756102],#zhongdian
                [31.782544709657742, -106.50549245877288],#zhongdian
                [31.782586291851107, -106.50549790627572]

                
                
                
            ]
            rect_coords12 = [

                [31.782475857123334, -106.50717115756102],#zhongdian
                [31.782544709657742, -106.50549245877288],#zhongdian
                [31.782482278976044, -106.50548090756683],
                [31.782392955114727, -106.50717398999748]                
            ]

            rect7=[
                [31.78551296180724,-106.5061947990217],
                [31.78547846695954,-106.5063115826307],
                [31.78433286132817,-106.5060059423108],
                [31.78435785837267,-106.5058685513861]
                
                
                ]
            rect8=[
                [31.78263905582947,-106.5055261884843],
                [31.78265432920957,-106.5053717625435],
                [31.78433850586656,-106.5058663604294],
                [31.78431590602613,-106.5060011636788]
                
                
                ]
            rect9=[
                [31.78495452203802,-106.505992131438],
                [31.78497511058762,-106.5058659475662],
                [31.78555604663832,-106.5060328678583],
                [31.78551522919348,-106.5061641085935]
                
                
                ]
            rect10=[
                [31.78264701431556,-106.5053227033138],
                [31.78266119749574,-106.5052007627926],
                [31.78482870248905,-106.5057947347421],
                [31.78479623203576,-106.5059539293017],
                [31.78427650353702,-106.5058025142571],
                [31.78374452022924,-106.5056285130224],
                [31.78264701431556,-106.5053227033138]
                
                
                ]
            zip_code = st.sidebar.selectbox('Period', ['Mon-Sat','Sunday'])
        
            if zip_code=='Mon-Sat':
                df=pd.read_csv('mon_sat.csv')
                st.write('#### Average Speed Around Mesa Street COVID-19 Test Site During Monday to Saturday')
                st.write('The colors represent the average speed of traffic in that road segment')
            elif zip_code=='Sunday':
                df=pd.read_csv('sunday.csv')
                st.write('#### Average Speed Around Mesa Street COVID-19 Test Site During Sunday')
                st.write('The colors represent the average speed of traffic in that road segment')

   
            points=df[['latitude','longitude','speed','heading']].values.tolist()
            def is_within_polygon(row, polygon):
                point = Point(row['latitude'], row['longitude'])
                return polygon.contains(point)
            def get_color(speed):
                if speed <= 21:
                    return 'brown'
                elif speed <= 36:
                    return 'red'
                elif speed <= 72:
                    return 'yellow'
                elif speed > 72:
                    return 'green'
            def get_color_small(speed):
                if speed <= 14:
                    return 'brown'
                elif speed <= 24:
                    return 'red'
                elif speed <= 48:
                    return 'yellow'
                elif speed > 48:
                    return 'green'

            def draw_polygon_folium(m,coor): 
                polygon = Polygon(coor)
                filtered_df = df[df.apply(is_within_polygon, args=(polygon,), axis=1)]
                
                speed=filtered_df['speed'].mean()
                if len(filtered_df)==0:
                    color='dark'
                else:
                    color=get_color(speed)
                #print(color,filtered_df.shape[0])
                folium.Polygon(
                    locations=coor,
                    color=color,
                    fill_color=color,
                    fill_opacity=0.5).add_to(m)
            def draw_polygon_folium_small(m,coor): 
                polygon = Polygon(coor)
                filtered_df = df[df.apply(is_within_polygon, args=(polygon,), axis=1)]
                
                speed=filtered_df['speed'].mean()
                if len(filtered_df)==0:
                    color='dark'
                else:
                    color=get_color_small(speed)
                #print(color,filtered_df.shape[0])
                folium.Polygon(
                    locations=coor,
                    color=color,
                    fill_color=color,
                    fill_opacity=0.5).add_to(m)
            m = folium.Map(location=[31.784015821496766, -106.50658067115639], zoom_start=17)  # (lat,lon)

            draw_polygon_folium_small(m,rect_coords1)
            draw_polygon_folium_small(m,rect_coords2)
            draw_polygon_folium_small(m,rect_coords3)
            draw_polygon_folium_small(m,rect_coords4)
            draw_polygon_folium_small(m,rect_coords5)
            draw_polygon_folium_small(m,rect_coords6)
            draw_polygon_folium_small(m,rect_coords7)
            draw_polygon_folium_small(m,rect_coords8)
            draw_polygon_folium_small(m,rect_coords9)
            draw_polygon_folium_small(m,rect_coords10)
            draw_polygon_folium_small(m,rect_coords11)
            draw_polygon_folium_small(m,rect_coords12)
            draw_polygon_folium(m,rect7)
            draw_polygon_folium(m,rect8)
            draw_polygon_folium(m,rect9)
            draw_polygon_folium(m,rect10)
            folium_static(m)



        elif disply_type=='Markers With Speed':
            zip_code = st.sidebar.selectbox('Period', ['Mon-Sat','Sunday'])
            if zip_code=='Mon-Sat':
                df=pd.read_csv('mon_sat.csv')
                st.write('#### Traffic Distribution Around Mesa Street COVID-19 Test Site During Monday to Saturday')
                st.write('Each icon represents one way point')
            elif zip_code=='Sunday':
                df=pd.read_csv('sunday.csv')
                st.write('#### Traffic Distribution Around Mesa Street COVID-19 Test Site During Sunday')
                st.write('Each icon represents one way point')
            points=df[['latitude','longitude','speed','heading']].values.tolist()
            m = folium.Map(location=[31.784015821496766, -106.50658067115639], zoom_start=17)  # (lat,lon)
            for i in range(len(points)):
                #if points[i][2]!=0:
                arc=6371.393*1000
                location=points[i][:2]
                azimuth=points[i][3]

                if points[i][2]>50:
                    end_lon = location[1] + 20 * math.sin(math.radians(azimuth))/(arc*math.cos(location[0])*2*math.pi/360)
                    end_lat = location[0] + 20 * math.cos(math.radians(azimuth))/(arc*2*math.pi/360)
                    end_location = [end_lat, end_lon]

                    #########################################
                    arrow1_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1_lat=end_lat+10 * math.cos(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1=[arrow1_lat,arrow1_lon]
                    arrow2_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2_lat=end_lat+ 10 * math.cos(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2=[arrow2_lat,arrow2_lon]
                    #################################


                    folium.PolyLine(
                        locations=[location, end_location],
                        color='green',
                    ).add_to(m)
                    folium.PolyLine(
                        locations=[end_location, arrow1],
                        color='green',
                    ).add_to(m)
                    folium.PolyLine(
                        locations=[end_location, arrow2],
                        color='green',
                    ).add_to(m)
                    folium.Marker(location=points[i][:2], tooltip=points[i][2], icon=folium.Icon(color='green',icon="car",prefix='fa')).add_to(m)
                elif points[i][2]>35:
                    end_lon = location[1] + 20 * math.sin(math.radians(azimuth))/(arc*math.cos(location[0])*2*math.pi/360)
                    end_lat = location[0] + 20 * math.cos(math.radians(azimuth))/(arc*2*math.pi/360)
                    end_location = [end_lat, end_lon]

                    #########################################
                    arrow1_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1_lat=end_lat+10 * math.cos(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1=[arrow1_lat,arrow1_lon]
                    arrow2_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2_lat=end_lat+ 10 * math.cos(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2=[arrow2_lat,arrow2_lon]
                    #################################


                    folium.PolyLine(
                        locations=[location, end_location],
                        color='blue',
                    ).add_to(m)
                    folium.PolyLine(
                        locations=[end_location, arrow1],
                        color='blue',
                    ).add_to(m)
                    folium.PolyLine(
                        locations=[end_location, arrow2],
                        color='blue',
                    ).add_to(m)
                    folium.Marker(location=points[i][:2], tooltip=points[i][2], icon=folium.Icon(color='blue',icon="car",prefix='fa')).add_to(m)
                elif points[i][2]>19:
                    end_lon = location[1] + 20 * math.sin(math.radians(azimuth))/(arc*math.cos(location[0])*2*math.pi/360)
                    end_lat = location[0] + 20 * math.cos(math.radians(azimuth))/(arc*2*math.pi/360)
                    end_location = [end_lat, end_lon]

                    #########################################
                    arrow1_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1_lat=end_lat+10 * math.cos(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1=[arrow1_lat,arrow1_lon]
                    arrow2_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2_lat=end_lat+ 10 * math.cos(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2=[arrow2_lat,arrow2_lon]
                    #################################


                    folium.PolyLine(
                        locations=[location, end_location],
                        color='orange',
                    ).add_to(m)
                    folium.PolyLine(
                        locations=[end_location, arrow1],
                        color='orange',
                    ).add_to(m)
                    folium.PolyLine(
                        locations=[end_location, arrow2],
                        color='orange',
                    ).add_to(m)
                    folium.Marker(location=points[i][:2], tooltip=points[i][2], icon=folium.Icon(color='orange',icon="car",prefix='fa')).add_to(m)
                elif points[i][2]>0:
                    end_lon = location[1] + 20 * math.sin(math.radians(azimuth))/(arc*math.cos(location[0])*2*math.pi/360)
                    end_lat = location[0] + 20 * math.cos(math.radians(azimuth))/(arc*2*math.pi/360)
                    end_location = [end_lat, end_lon]

                    #########################################
                    arrow1_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1_lat=end_lat+10 * math.cos(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1=[arrow1_lat,arrow1_lon]
                    arrow2_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2_lat=end_lat+ 10 * math.cos(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2=[arrow2_lat,arrow2_lon]
                    #################################


                    folium.PolyLine(
                        locations=[location, end_location],
                        color='pink',
                    ).add_to(m)
                    folium.PolyLine(
                        locations=[end_location, arrow1],
                        color='pink',
                    ).add_to(m)
                    folium.PolyLine(
                        locations=[end_location, arrow2],
                        color='pink',
                    ).add_to(m)
                    folium.Marker(location=points[i][:2], tooltip=points[i][2], icon=folium.Icon(color='pink',icon="car",prefix='fa')).add_to(m)
                else:
                    end_lon = location[1] + 20 * math.sin(math.radians(azimuth))/(arc*math.cos(location[0])*2*math.pi/360)
                    end_lat = location[0] + 20 * math.cos(math.radians(azimuth))/(arc*2*math.pi/360)
                    end_location = [end_lat, end_lon]

                    #########################################
                    arrow1_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1_lat=end_lat+10 * math.cos(math.radians(azimuth-180+10))/(arc*2*math.pi/360)
                    arrow1=[arrow1_lat,arrow1_lon]
                    arrow2_lon=end_lon  + 10 * math.sin(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2_lat=end_lat+ 10 * math.cos(math.radians(azimuth-180-10))/(arc*2*math.pi/360)
                    arrow2=[arrow2_lat,arrow2_lon]
                    #################################


                    folium.Marker(location=points[i][:2], tooltip=points[i][2], icon=folium.Icon(color='red',icon="car",prefix='fa')).add_to(m)
            folium_static(m)
        st.sidebar.image(['utep_new_logo.png','CTECH.jpeg'], width=150)





















    #elif data_module == 'Health Data':
    elif selected=='Health Data 🏥':
 



        # Filter the data based on the user's selection
        option5=sorted(covid_data['zip code'].unique())
        
        option5.insert(0,'All')
        zip_code = st.sidebar.selectbox('Zip Code', option5)


        # Set the date column as the index of the DataFrame
        #filtered_zip_data = filtered_zip_data.set_index('date')

        # Create a line chart of the total positive cases, recoveries, and deaths over time
        #option6=['Total COVID cases table','Bar chart race','Cumulative positive cases', 'Cumulative recoveries', 'Cumulative deaths']
        #variable = st.sidebar.selectbox('Data Display', option6)
        if zip_code=='All':
            variable=st.sidebar.selectbox('Display Mode', ['Table','Bar Chart'])
        else:
            variable = st.sidebar.selectbox('Display Mode', ['Cumulative Positive Curve', 'Cumulative Recovery Curve', 'Cumulative Death Curve'])

        if variable=='Bar Chart':
            default_start_date = pd.to_datetime('2020-03-01')
            default_end_date = pd.to_datetime('2022-04-01')

            # Add a slider to allow the user to select a time frame
            
            start_date = st.sidebar.date_input('Start date', default_start_date)
            end_date = st.sidebar.date_input('End date', default_end_date)
        else:
            # Set default values for start_date and end_date
            default_start_date = pd.to_datetime('2021-09-01')
            default_end_date = pd.to_datetime('2022-03-31')

            # Add a slider to allow the user to select a time frame
            
            start_date = st.sidebar.date_input('Start date', default_start_date)
            end_date = st.sidebar.date_input('End date', default_end_date)
                # Filter the data based on the user's selection
        # Filter the data based on the user's selection
        covid_data['date'] = pd.to_datetime(covid_data['date'], format='%m/%d/%y')
        filtered_data = covid_data[(covid_data['date'] >= pd.Timestamp(start_date)) & (covid_data['date'] <= pd.Timestamp(end_date))]

        #################################################################
        #bar_data['Zipcode']=pd.to_datetime(bar_data['Zipcode'], format="%Y-%m-%d")
        #filtered_bar = bar_data[(bar_data['Zipcode'] >= pd.Timestamp(start_date)) & (bar_data['Zipcode'] <= pd.Timestamp(end_date))]
        
        #####################################################################

        grouped_data = filtered_data.groupby('zip code').max()[['Cumulative Positive Curve', 'Cumulative Recovery Curve', 'Cumulative Death Curve']]

        # Reset the index to make zip code a column
        grouped_data = grouped_data.reset_index()
        if zip_code=='All':
            filtered_zip_data=filtered_data
        else:
            filtered_zip_data = filtered_data[filtered_data['zip code'] == zip_code]

        # st.sidebar.subheader('Authors:')
        # st.sidebar.write('- Kelvin Cheu')
        # st.sidebar.write('- Ruimin Ke')s
        # st.sidebar.write('- Chengyue Wang')
        # st.sidebar.write('- Swapnil Samat')
        # st.sidebar.write('- Jeffrey Weidner') 


        # CTECH logo and UTEP logo are side-by-side
        st.sidebar.image(['utep_new_logo.png','CTECH.jpeg'], width=150)
    
        if variable=='Table':
            st.write(' Total COVID Cases by Zip Code from ' + str(start_date) + ' to ' + str(end_date))
            grouped_data['zip code']=grouped_data['zip code'].apply(str)
            st.write(grouped_data) 
        elif variable=='Cumulative Positive Curve' or variable=='Cumulative Recovery Curve' or variable=='Cumulative Death Curve':
            st.markdown('##### The '+variable+' from ' + str(start_date) + ' to ' + str(end_date) +' in ' +' Zip code '+ str(zip_code))
            filtered_zip_data = filtered_zip_data.rename(columns={'date': 'Date'})
            if variable == 'Cumulative Positive Curve':
                chart = alt.Chart(filtered_zip_data,width=700).mark_area().encode(
                x='Date:T',
                y=alt.Y(variable + ':Q', stack=True),
                color=alt.value('orange')
                )
            elif variable == 'Cumulative Recovery Curve':
                chart = alt.Chart(filtered_zip_data,width=700).mark_area().encode(
                x='Date:T',
                y=alt.Y(variable + ':Q', stack=True),
                color=alt.value('green')
                )
            elif variable == 'Cumulative Death Curve':
                chart = alt.Chart(filtered_zip_data,width=700).mark_area().encode(
                x='Date:T',
                y=alt.Y(variable + ':Q', stack=True),
                color=alt.value('black')
                )
            #y2='0'
            
            

            #).properties(
            #title=f'               The {variable} over selected time range for zip code {zip_code}',
            #width=800,
            #height=400
            #)
        # Display the line chart in the Streamlit app using altair_chart
        
            
            chart=chart.configure_axis(labelFontSize=13)

            #filtered_zip_data['date']=pd.to_datetime(filtered_zip_data['date']).dt.strftime('%Y-%m')
            
#################################################################
            st.altair_chart(chart)
            #chart_data =filtered_zip_data.set_index("date")
            #chart_data=chart_data[variable]








            #st.area_chart(chart_data)
#################################################################
            
            
            
            
            #df=filtered_zip_data
            #color_scale=alt.Scale(domain=['blue', 'lightblue', 'white', 'gray', 'beige', 'darkred', 'darkgreen', 'pink', 'orange', 'red', 'cadetblue', 'black', 'lightgreen', 'purple', 'lightgray', 'lightred', 'darkpurple', 'green', 'darkblue'],range=['blue', 'lightblue', 'white', 'gray', 'beige', 'darkred', 'darkgreen', 'pink', 'orange', 'red', 'cadetblue', 'black', 'lightgreen', 'purple', 'lightgray', 'lightred', 'darkpurple', 'green', 'darkblue'])
            #fig, ax = plt.subplots()
            #X=df['date'].dt.strftime('%Y-%m-%d')
            #ax.bar(X,df[variable])
            #ax.tick_params(axis='x', labelrotation=90)

            # Add labels and title
            #ax.set_xlabel('Date')
            #ax.set_ylabel(variable)
            #ax.set_title('Bar Chart of '+variable+'in Zip Code' + str(zip_code))

  
           

            # Display the plot in Streamlit
            #st.pyplot(fig)
        elif variable=='Bar Chart':
            st.write('The cumulative positive cases of each Zip code in El Paso from 2020-03-01 to 2022-04-01')
            #filtered_bar=filtered_bar.set_index("Zipcode")
            #fig=bcr.bar_chart_race(filtered_bar)



  
            
      







            video_file = open('bar_chart_race.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)       

            


        #CTECH logo is below to UTEP logo
        #st.sidebar.image('utep_new_logo.png', width=200)
        #st.sidebar.image('CTECH.jpeg', width=200)

        #chart = alt.Chart(filtered_zip_data).mark_line().encode(
        #    x='date:T',
        #    y=alt.Y(variable + ':Q', stack=True),
        #    color=variable + ''
            

        #).properties(
        #    title=f'The {variable} over selected time range for zip code {zip_code}',
        #    width=800,
        #    height=400
        #)
        # Display the line chart in the Streamlit app using altair_chart
        #st.altair_chart(chart)

        # Create a table of the total positive cases, recoveries, and deaths by zip code
        #st.markdown('### Total Cases by Zip Code from ' + str(start_date) + ' to ' + str(end_date))
        #pd.set_option('display.max_colwidth', 100)
        # Set the width of each column to 150 pixels
        #styles = [dict(selector="th", props=[("max-width", "150px")])]
        #st.write(grouped_data) 


        # # Set default values for start_date and end_date
        # default_start_date = pd.to_datetime('2021-01-01')
        # default_end_date = pd.to_datetime('2021-03-31')

        # # Add a slider to allow the user to select a time frame
        # start_date = st.sidebar.date_input('Start date', default_start_date)
        # end_date = st.sidebar.date_input('End date', default_end_date)

        # # Add options to select the zip code
        # zip_code = st.sidebar.selectbox('Zip Code', [79901, 79902, 79903, 79904, 79905, 79907, 79911, 79912, 79915, 
        #                                              79922, 79924, 79925, 79927, 79928, 79930, 79932, 79934, 79935, 79936, 79938])
        # # Add options to select the type of map display
        # display_type = st.sidebar.selectbox('Data Display', ['Positive Cases', 'Recoveries', 'Deaths'])

        # # Data filtering
        # covid_data['date'] = pd.to_datetime(covid_data['date'], format='%m/%d/%Y')
        # filtered_data = covid_data[(covid_data['date'] >= start_date) & (covid_data['date'] <= end_date)]
        # if zip_code != 'ALL':
        #     filtered_data = filtered_data[filtered_data['zip code'] == zip_code]
#st.set_page_config(page_title='El Paso Data Dashboard',layout='wide')'centered'
st.set_page_config(page_title='El Paso Data Dashboard', layout='wide',page_icon=':bar_chart:')  

if 'dashboard_entered' not in st.session_state:
    st.session_state['dashboard_entered'] = False


if st.session_state['dashboard_entered']:
    dashboard()

elif not st.session_state['dashboard_entered']:
    welcome()




