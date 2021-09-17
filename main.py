import streamlit as st
import plotly.express as px
import pandas as pd
from functools import reduce
import numpy as np
import plotly.graph_objects as go



df = pd.read_csv("C:/Users/j.elachkar/Desktop/ED.csv")
df['Date']=pd.to_datetime(df['Date'])
df['Month']=df['Date'].dt.month
df['Year']=df['Date'].dt.year
df['Period'] = df['Month'].astype(str) + "-" + df['Year'].astype(str)
df['Period']= pd.to_datetime(df['Period'])
df['Period']= df['Period'].dt.strftime('%Y-%b')
print(df.dtypes)
#
# # visualization # 1 - # of visits
#

df1 = df[['Period','patient_number ']]
df1_count_per_month= df1.groupby("Period").agg(Number_of_visits=("patient_number ","count"))
df1_count_per_month = df1_count_per_month.reset_index("Period")
print(df1_count_per_month)


# get the weekdays names from a dataframe
df['weekdays']=df['Date'].dt.day_name()
# get the week number from a dataframe
df['week']=df['Date'].dt.week

# create a table - week 35
df2 = df[['weekdays','week','patient_number ']]
# order week days by order
df2['weekdays'] = pd.Categorical(df2['weekdays'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)
df2_week = df2[df2['week']==35].groupby("weekdays").agg(week_35=('patient_number ','count'))
df2_week = df2_week.reset_index('weekdays')
print(df2_week)

# create a table - week 36
df2 = df[['weekdays','week','patient_number ']]
# order week days by order
df2['weekdays'] = pd.Categorical(df2['weekdays'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)
df2_week2 = df2[df2['week']==36].groupby("weekdays").agg(week_36=('patient_number ','count'))
df2_week2 = df2_week2.reset_index('weekdays')
print(df2_week2)

# create a table - week 37
df2 = df[['weekdays','week','patient_number ']]
# order week days by order
df2['weekdays'] = pd.Categorical(df2['weekdays'], categories=
    ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'],
    ordered=True)
df2_week3 = df2[df2['week']==37].groupby("weekdays").agg(week_37=('patient_number ','count'))
df2_week3 = df2_week3.reset_index('weekdays')
print(df2_week3)

# create a table - week 38
df2_week4 = df2[df2['week']==38].groupby('weekdays').agg(week_38=('patient_number ','count'))
df2_week4=df2_week4.reset_index('weekdays')
print(df2_week4)

# create a table - week 39
df2_week5 = df2[df2['week']==39].groupby('weekdays').agg(week_39=('patient_number ','count'))
df2_week5=df2_week5.reset_index('weekdays')
print(df2_week5)

# create a table - week 40
df2_week6 = df2[df2['week']==40].groupby('weekdays').agg(week_40=('patient_number ','count'))
df2_week6=df2_week6.reset_index('weekdays')
print(df2_week6)

# create a table - week 41
df2_week7 = df2[df2['week']==41].groupby('weekdays').agg(week_41=('patient_number ','count'))
df2_week7=df2_week7.reset_index('weekdays')
print(df2_week7)

# create a table - week 42
df2_week8 = df2[df2['week']==42].groupby('weekdays').agg(week_42=('patient_number ','count'))
df2_week8=df2_week8.reset_index('weekdays')
print(df2_week8)

# create a table - week 43
df2_week9 = df2[df2['week']==43].groupby('weekdays').agg(week_43=('patient_number ','count'))
df2_week9=df2_week9.reset_index('weekdays')
print(df2_week9)

# create a table - week 44
df2_week10 = df2[df2['week']==44].groupby('weekdays').agg(week_44=('patient_number ','count'))
df2_week10=df2_week10.reset_index('weekdays')
print(df2_week10)

# create a table - week 45
df2_week11=df2[df2['week']==45].groupby('weekdays').agg(week_45=('patient_number ','count'))
df2_week11=df2_week11.reset_index('weekdays')
print(df2_week11)

# create a table - week 46
df2_week12=df2[df2['week']==46].groupby('weekdays').agg(week_46=('patient_number ','count'))
df2_week12=df2_week12.reset_index('weekdays')
print(df2_week12)

# create a table - week 47
df2_week13=df2[df2['week']==47].groupby('weekdays').agg(week_47=('patient_number ','count'))
df2_week13=df2_week13.reset_index('weekdays')
print(df2_week13)

# create a table - week 48
df2_week14=df2[df2['week']==48].groupby('weekdays').agg(week_48=('patient_number ','count'))
df2_week14=df2_week14.reset_index('weekdays')
print(df2_week14)


# create a table - week 49
df2_week15=df2[df2['week']==49].groupby('weekdays').agg(week_49=('patient_number ','count'))
df2_week15=df2_week15.reset_index('weekdays')
print(df2_week15)

# create a table - week 50
df2_week16=df2[df2['week']==50].groupby('weekdays').agg(week_50=('patient_number ','count'))
df2_week16=df2_week16.reset_index('weekdays')
print(df2_week16)

# create a table - week 51
df2_week17=df2[df2['week']==51].groupby('weekdays').agg(week_51=('patient_number ','count'))
df2_week17=df2_week17.reset_index('weekdays')
print(df2_week17)

# create a table - week 52
df2_week18=df2[df2['week']==52].groupby('weekdays').agg(week_52=('patient_number ','count'))
df2_week18=df2_week18.reset_index('weekdays')
print(df2_week18)

# merge all tables together with weekdays as unique identifier
data_frame=[df2_week,df2_week2,df2_week3,df2_week4,df2_week5,df2_week6,df2_week7,df2_week8
            ,df2_week9,df2_week10,df2_week11,df2_week12,df2_week13,df2_week14,df2_week15
            ,df2_week16,df2_week17,df2_week18]

df_merged = reduce( lambda left,right: pd.merge(left,right, on=['weekdays'],
                                                how='outer'),data_frame)

print(df_merged)
st.header("ED Dashboard - AMAN Hospital")

# chart per day time
from datetime import datetime
df3 = df[['registration_time','patient_number ']]
df3['registration_time']=pd.to_datetime(df3['registration_time'])
df3['hour']=df3['registration_time'].dt.hour

df4 = df3.groupby('hour').agg(numb_of_patients=('patient_number ','count'))
df4=df4.reset_index('hour')



if st.sidebar.checkbox("Click to see - Number of Visits"):

    select1 = st.sidebar.selectbox("Number of Visits", ['Per month', 'Per week','Per hour'])
    if select1 == "Per month":
        st.subheader("Number of Visits per Month")
        fig = px.bar(df1_count_per_month,x='Period',y='Number_of_visits',color='Period')
        st.plotly_chart(fig)

    elif select1 =='Per week':
        st.subheader("Number of Visits per Week")
        fig1=px.line(df_merged,x='weekdays',y=['week_35','week_36','week_37','week_38'])
        st.plotly_chart(fig1)
        st.write(df_merged)
    else:
        select1 =='Per hour'
        st.subheader("Number of patients per hour of day")
        fig2 = px.line(df4,x='hour',y='numb_of_patients',markers=True)
        st.plotly_chart(fig2)

# visits per day
df6=df['Date'].value_counts()
data_f = pd.DataFrame({'date':df6.index,'count':df6.values})
# sort dates
data_f = data_f.sort_values(by='date')
data_f['date']=pd.to_datetime(data_f['date'])
print(data_f)

data_s =data_f[data_f['date']<'2021-09-30']
data_o = data_f[(data_f['date'] > '2021-09-30') & (data_f['date'] <'2021-10-30')]
data_n =data_f[(data_f['date'] > '2021-10-30') & (data_f['date'] < '2021-11-30')]
if st.sidebar.checkbox("click to see Number of Patients Per day"):
    st.subheader("Number of Patients per day")
    selecto = st.sidebar.selectbox("select month",['Sept-2021','Oct-2021','Nov-2021'])
    if selecto =='Sept-2021':
        figu = px.line(data_s,x='date',y='count',markers=True)
        st.plotly_chart(figu)
    elif selecto =='Oct-2021':
        figo =px.line(data_o,x='date',y='count',markers=True)
        st.plotly_chart(figo)
    else:
        selecto=='Nov-2021'
        fign=px.line(data_n,x='date',y='count',markers=True)
        fign.update_traces(marker=dict(size=9,

                                                color='red'))

        st.plotly_chart(fign)



# visu # 3
# slider = st.sidebar.slider("select month",['Oct-2021','Nov-2021','Dec-2021'])

df_age =df['age '].value_counts()
df_a = pd.DataFrame({'age':df_age.index,'count':df_age.values})

df_gender =df['gender'].value_counts()
df_g =pd.DataFrame({'gender':df_gender.index,'values':df_gender.values})


# visualization # 3
if st.sidebar.checkbox("select to see patients by demographic info"):
    col1,col2 =st.columns(2)
    with col1:
        st.subheader("Number of patients by Age group")
        fig100 = px.histogram(df_a, x='age', nbins=5, y='count', histfunc='sum',width=470,height=470)
        st.plotly_chart(fig100)

    with col2:
        st.subheader("Number of patients by gender")

        fig101=px.histogram(df_g,x='gender',y='values',width=470,height=470)
        st.plotly_chart(fig101)


# figure by region

df_map = df[['Date','registration_time','latitude','longitude']]
# first convert registratime time from object to datetime
df_map['registration_time']= pd.to_datetime(df_map['registration_time'])
# create hour column and have it as datetime
df_map['hour']= pd.to_datetime(df_map['registration_time'],format='%H:%M').dt.hour
print(df_map)

if st.sidebar.checkbox("Select to see Map"):
    slider = st.sidebar.slider("select the hour",min_value=7,max_value=19)
    data_slid = df_map[df_map['hour']==slider]
    st.subheader("Patients distribution by Location")
    st.markdown("%i:00 patients presented to ED between %i:00 and %i:00"%(len(data_slid),slider,(slider+3)%24))
    st.map(df)


# visualization # 5
df_triage = df['triage'].value_counts()
df_tr = pd.DataFrame({'triage_score':df_triage.index,'count':df_triage.values})

df_guarant = df['guarantor'].value_counts()
df_g = pd.DataFrame({'guarantor':df_guarant.index,'count':df_guarant.values})
print(df_g)

df_arrival = df['arrival_mode'].value_counts()
df_arr = pd.DataFrame({'arrival_mode':df_arrival.index,'count':df_arrival.values})
print(df_arr)

if st.sidebar.checkbox("triage and guarantor distribtuion"):
    col1, col2,col3 = st.columns(3)
    with col1:
        st.subheader("Triage distribution")
        fig101 = px.bar(df_tr,x='triage_score',y='count',width=300,height=300)
        st.plotly_chart(fig101)
    with col2:
        st.subheader("patients by guarantor")
        fig102= px.bar(df_g,x='guarantor',y='count',width=300,height=300)
        st.plotly_chart(fig102)
    with col3:
        st.subheader("patients by arrival mode")
        fig103= px.bar(df_arr,x='arrival_mode',y='count',
                       width=300,height=300)
        st.plotly_chart(fig103)


# chart by age and triage category

df_agecat = df[['age ','triage']]
print(df_agecat)
if st.sidebar.checkbox("Triage by Age group"):
    st.subheader("Triage by Age group")
    fig33 = px.histogram(df_agecat,x='age ',nbins=7,y='triage',histfunc='count',facet_col='triage',


                         )
    st.plotly_chart(fig33)

# visual # 6 - top 10 complaints by Adult ED visits
# pediatrics
df_chief = df[['chief_complaint','age ']]
df_aging = df_chief[df_chief['age '] < 18]
df_ag = df_aging['chief_complaint'].value_counts()
df_ag1 = pd.DataFrame({'chief_complaint':df_ag.index,'count':df_ag.values})
print(df_ag1)
# adult
df_chief = df[['chief_complaint','age ']]
df_ager = df_chief[df_chief['age '] > 18]
df_agers = df_ager['chief_complaint'].value_counts()
df_agers1 = pd.DataFrame({'chief_complaint':df_agers.index,'count':df_agers.values})
print(df_agers1)
if st.sidebar.checkbox("Top complaints for Adult and Pediatrics"):
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Chief Complaints for Adults")
        fig909 = px.bar(df_agers1,x='chief_complaint',y='count',width=450,height=450)
        st.plotly_chart(fig909)
    with col2:
        st.subheader("Chief Complaits for Pediatrics")
        fig808 = px.bar(df_ag1, x='chief_complaint',y='count',width=450,height=450)
        st.plotly_chart(fig808)

# chart # 8

df_diag = df[['age ','diagnosis']]
df_diag_pds = df_diag[df_diag['age '] <18]
df_diag_peds = df_diag_pds.groupby("diagnosis").agg(number = ('age ','count'))
df_diag_peds = df_diag_peds.reset_index()

df_diag_adt = df_diag[df_diag['age ']>18]
df_diag_adut= df_diag_adt.groupby('diagnosis').agg(number =('age ','count'))
df_diag_adut= df_diag_adut.reset_index()

if st.sidebar.checkbox("Diagosis Peds Vs Adult"):
    st.subheader("Diagnosis Adult Vs Peds")
    col1,col2 =st.columns(2)
    with col1:
        st.subheader("Diagnosis - Adult population")
        fig001 = px.bar(df_diag_adut,x='diagnosis',y='number',height=400,width=400)
        st.plotly_chart(fig001)
    with col2:
        st.subheader("Diagnosis - Peds population")
        fig002 = px.bar(df_diag_peds,x='diagnosis',y='number',height=400,width=400)
        st.plotly_chart(fig002)


# chart 9
# waiting time in ED and LOS
df_wait = df[['registration_time','triage_started ','roomed_in_ED ']]
# to calculate different in time between 2 columns, change to datetime
df_wait['registration_time'] = pd.to_datetime(df_wait['registration_time'])
df_wait['triage_started '] =pd.to_datetime(df_wait['triage_started '])
df_wait['roomed_in_ED '] = pd.to_datetime(df_wait['roomed_in_ED '])
# extract hour and minute only from date
# df_wait['reg_time'] = df_wait['registration_time'].dt.strftime('%H:%M')
# df_wait['diff1'] = (df_wait['roomed_in_ED '] - df_wait['triage_started ']) + (df_wait['triage_started '] - df_wait['registration_time'])
# the type of diff1 is timedelta, let us convert it to datetime
# df_fin =df_wait['diff1'].mean()
# print(df_fin)
# if st.sidebar.checkbox("Waiting time & Length of Stay"):
#     st.subheader(" Waiting time & Length of Stay")




