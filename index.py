# DISEASE PREDICTION USING PATIENT SYMPTOMS

# IMPORTING PACKAGES AND LIBRARIES
from tkinter import *
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import os
from flask import Flask, request, render_template ,redirect


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
print(PROJECT_ROOT)

# symptoms - 91
# PATIENT POSSIBLE SYMPTOMS
l1=["back_pain","constipation","abdominal_pain","diarrhoea","mild_fever","yellow_urine","yellowing_of_eyes","acute_liver_failure",
    "fluid_overload","swelling_of_stomach","swelled_lymph_nodes","blurred_and_distorted_vision","phlegm","throat_irritation",
    "redness_of_eyes","sinus_pressure","runny_nose","congestion","chest_pain","weakness_in_limbs","fast_heart_rate",
    "pain_during_bowel_movements","pain_in_anal_region","bloody_stool","irritation_in_anus","neck_pain","dizziness","cramps",
    "bruising","obesity","swollen_legs","swollen_blood_vessels","puffy_face_and_eyes","enlarged_thyroid","brittle_nails",
    "swollen_extremeties","excessive_hunger","extra_marital_contacts","drying_and_tingling_lips","slurred_speech","knee_pain",
    "hip_joint_pain","muscle_weakness","stiff_neck","swelling_joints","movement_stiffness","spinning_movements","loss_of_balance",
    "unsteadiness","weakness_of_one_body_side","loss_of_smell","bladder_discomfort","foul_smell_of urine","continuous_feel_of_urine",
    "passage_of_gases","internal_itching","depression","irritability","muscle_pain","altered_sensorium","red_spots_over_body","belly_pain",
    "abnormal_menstruation","watering_from_eyes","increased_appetite","polyuria","mucoid_sputum","rusty_sputum","lack_of_concentration",
    "visual_disturbances","receiving_blood_transfusion","receiving_unsterile_injections","coma","stomach_bleeding","distention_of_abdomen",
    "history_of_alcohol_consumption","fluid_overload","blood_in_sputum","prominent_veins_on_calf","palpitations","painful_walking",
    "pus_filled_pimples","blackheads","scurring","skin_peeling","silver_like_dusting","small_dents_in_nails","inflammatory_nails","blister",
    "red_sore_around_nose","yellow_crust_ooze"]

# LIST OF DISEASES
disease=["Fungal infection","Allergy","GERD","Chronic cholestasis","Drug Reaction","Peptic ulcer disease","AIDS","Diabetes",
         "Gastroenteritis","Bronchial Asthma","Hypertension","Migraine","Cervical spondylosis","Paralysis","Jaundice",
         "Malaria","Chicken pox","Dengue","Typhoid","Hepatitis A","Hepatitis B","Hepatitis C","Hepatitis D",
         "Hepatitis E","Alcoholic hepatitis","Tuberculosis","Common Cold","Pneumonia","Dimorphic Hemmorhoids(Piles)",
         "Heart Attack","Varicose Veins","Hypothyroidism","Hyperthyroidism","Hypoglycemia","Osteoarthristis", "Arthritis",
         "Paroymsal Positional Vertigo","Acne","Urinary tract infection","Psoriasis", "Impetigo"]
l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# READING TRAINING DATA AND CONVERTING CATEGORICAL VARIABLES TO NUMERIC VARIABLES
df=pd.read_csv(os.path.join(PROJECT_ROOT,"Training.csv"))
df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,'Peptic ulcer diseae':5,
                         'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10, 'Migraine':11,
                         'Cervical spondylosis':12,'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,
                         'Dengue':17,'Typhoid':18,'hepatitis A':19,'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,
                         'Alcoholic hepatitis':24,'Tuberculosis':25, 'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,
                         'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31, 'Hyperthyroidism':32,'Hypoglycemia':33,
                         'Osteoarthristis':34,'Arthritis':35,'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,
                         'Urinary tract infection':38,'Psoriasis':39,'Impetigo':40}},inplace=True)
X= df[l1]
y = df[["prognosis"]]
np.ravel(y)

# READING TESTING DATA AND CONVERTING CATEGORICAL VARIABLES TO NUMERIC VARIABLES
tr=pd.read_csv(os.path.join(PROJECT_ROOT,"Testing.csv"))
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,'Peptic ulcer diseae':5,
                         'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10, 'Migraine':11,
                         'Cervical spondylosis':12,'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,
                         'Dengue':17,'Typhoid':18,'hepatitis A':19,'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,
                         'Alcoholic hepatitis':24,'Tuberculosis':25, 'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,
                         'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31, 'Hyperthyroidism':32,'Hypoglycemia':33,
                         'Osteoarthristis':34,'Arthritis':35,'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,
                         'Urinary tract infection':38,'Psoriasis':39,'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# Doc
doc ={"Fungal infection":[0,"Dr. Mahboob Jahan Ahmed","1712290927","Adhunik Sadar Hospital, Chapainawabganj"],
"Allergy":[1,"Dr. Bipad Bhanjan Karmakar","1556333100","Vill-Sultanabad,PO-Ghora Mara,PS-Boalia,Dist-Rajshahi."],
"GERD":[2,"Dr.Md.Monirul Islam","1748991574","Sadar Hospital Chapainawabganj"],
"Chronic cholestasis":[3,"Dr. Md. Shahid-ul-islam Khan","1711003283","JUNIOR CONSULTANT, SURGERY, ADHUNIK SADAR HOSPITAL, CHAPAI NAWABGANJ, 6300"],
"Drug Reaction":[4,"Dr. Ayesha Julekha","1715171009","Adhuink Sadar Hospital, Chapainawabganj."],
"Peptic ulcer disease":[5,"Dr.Md.Hassan Jamil Hedyatullah","1711014088","Upazila Health Complex, Bagha,Rajshahi."],
"AIDS":[6,"Mst. Ilham Munira","1732267340","Sadar Hospital, Chapainawabganj."],
"Diabetes":[7,"Dr. Nazir Ahmed","1712023521","Village & Post office-Chhaikola,Upazila-Chatmohar,Dist-Pabna."],
"Gastroenteritis":[8,"Dr. Md. Nadeem Sarkar","1718003417","Vill-Bhakum,Po- Singair,Dist-Manikgong."],
"Bronchial Asthma":[9,"Dr. Md. Shafiqul Islam","1711061814","AUSTOMONISHA,CHATMOHAR,PABNA."],
"Hypertension":[10,"Dr. Most. Nuri Zunnatul Fardous.","1711069461","CHOWDORY PARA,CHATMOHAR,PABNA."],
"Migraine":[11,"Dr. Rezaul Alam","1711000230","Director Rajshahi Medical College Hospital"],
"Cervical spondylosis":[12,"Dr. Md. Abdul Hye","1714363809","Deputy director (C.C) Rajshahi Medical college Hospital Rajshahi"],
"Paralysis":[13,"Dr. Md. Tohidur Rahaman","1718505414","Kashuri Vila,Holding No-67, Word No-3, New Bilshimla, Rajshahi Cantonment, Rajshahi."],
"Jaundice":[14,"Dr. Bappy Kumer Biswas","1722095885","Asstt Director(Finance & Store) Rajshahi Medical Collehe Hospital."],
"Malaria":[15,"Dr. Md. Masud Rana","1750712695","Sr.Conseltant (Gyn&Obs) Model Family Planning Clinic Rajshahi Medical College Hospital"],
"Chicken pox":[16,"Dr. Debashis Biswas","1717306650","House No:2,Ward No:1,Vill:Horogram,P.O: Rajshahi C"],
"Dengue":[17,"Dr. Md. Saiful Islam","1712104554","V-Ghanosampur.Po-Ghanosampur.Up-Godagari.Rajshahi"],
"Typhoid":[18,"Dr. Md. Abul Hossain","1711902725","Hold-167,Ward-3.Baharampur.Rajpara.Rajshahi"],
"Hepatitis A":[19,"Dr Arundhuti Kundu","1711966237","Senior Store Officer Rajshahi MCH"],
"Hepatitis B":[20,"Dr. S. M. Bayezid - Ul-islam","1749994000","Rajshahi Medical College Hospital. Rajshahi"],
"Hepatitis C":[21,"Dr. Rehana Pervin Ruma","1717473897","Anesthesiology Department Rajshahi Medical College Hospital. Rajshahi"],
"Hepatitis D":[22,"Dr Mst Arifa Sultana","1715673328","Rajshahi Medical College Hospital"],
"Hepatitis E":[23,"Dr. S, M, Golam Moula","1751371832","Rajshahi Medical College Hospital. Rajshahi"],
"Alcoholic hepatitis":[24,"Md. Shahidullah","1716008153","A/73.Uposhasar. Rajshahi"],
"Tuberculosis":[25,"Md.Aminul Islam","1718823702","Nadananpu,Sathia, Pabna"],
"Common Cold":[26,"Md.Motiur Rahman","1718270102","C/O.Awal Nanzil,Sagorpara,Ghoramara,Boalia,Rajshah"],
"Pneumonia":[27,"A F M Rafiqul Islam","1713091559","Vill- Charshadipur, P.O. Philipnagar, Upazila- Daulatpur, Dist- Kushtia"],
"Dimorphic Hemmorhoids(Piles)":[28,"Dr. Ghazi Shaiful Alam Choudhury","1711393227","Vill+Post:Baliadanga, P.S: Nawabgonj Sadar, Dist: Chapai Nawabgonj"],
"Heart Attack":[29,"Dr. Md. Serajul Karim","1712269875","W-19-B, Rajshahi University Campus,Rajshahi-6205"],
"Varicose Veins":[30,"Dr. Toufiqul Islam Md. Belal","1711578618","Quarter No-3/c, RMCH Campus,"],
"Hypothyroidism":[31,"Dr. Rina Akhter","1817521890","Vill : Charsadipur,p.O : Philipnager, P.S : Dalutpur, Dist : Kushtia."],
"Hyperthyroidism":[32,"Dr. Partho Moni Bhattacharyya","1715059079","House no- 26, Road no - 2 , Sector no - 2 , Housing estate , Upashahr , PO -Cantonment , Thana - Boalia , Rajshahi - 6202"],
"Hypoglycemia":[33,"Dr. Mohammad Nasim Hossain","1715508534","HOLDING NO-103. MEHERCHONDI.PURBO PARA.PADMAR/A-6207.BOALIA RAJSHAHI"],
"Osteoarthristis":[34,"Dr. Md. Golam Mostofa","1717571587","MONIRA VILLA.NEW STABIUM ROAD.TEROKHADIA.RAJSHAHI"],
"Arthritis":[35,"Dr..Mohammad Ali Akbar Sarkar","1715360163","Vill- Chawgacha, PO& Upazilla- Gangni, Meherpur."],
"Paroymsal Positional Vertigo":[36,"Dr. Md. Abul Ehsan","1717517288","Vill, Jalibagan po. Rohanpur Th. Gomostapur , Chapai Nawabgong"],
"Acne":[37,"Dr. Mohd. Iqbal Kabir","1819129977","VILL:RUKINDIPUR,POST:JAMALGONG.AKKELPUR.JOYPURHAT"],
"Urinary tract infection":[38,"Dr. Bidhan Kumar Fowjdar","1712503197","Village-Chatra,Union-Parswadanga,ChatrmoharPabna."],
"Psoriasis":[39,"Dr. Mohammad Ali Chowdhury","1715405870","177/2.UposhaharHousing Estart.Cantorment-6202.Boalia.Rajshahi"],
"Impetigo":[40,"Dr. Md. Tahmid-ur-rahaman","1712682796","Asst. Registrar, Surgery, RMCH"]}
# PREDICTION USING NAIVE BAYES CLASSIFIER

def NaiveBayes(psymptoms):
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))
    y_pred=gnb.predict(X_test)
    #print(accuracy_score(y_test, y_pred))
    #print(accuracy_score(y_test, y_pred,normalize=False))
    #lenSym = input("Enter no of symptoms : ")
    #psymptoms = []
    #for i in range(0,int(lenSym)):
    #    temp = input("Enter Symptom : ")
    #    psymptoms.append(temp)

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]
    h=0
    for a in range(0,len(disease)):
        if(predicted == a):
            return [disease[a],doc[disease[a]][0],doc[disease[a]][1],doc[disease[a]][2],doc[disease[a]][3]]
    """if (h==1):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")"""


app = Flask(__name__)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/',methods=['POST','GET'])

def index():
    return render_template('index.html')

@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['POST','GET'])
def about():    
    return render_template('about.html')

@app.route('/services',methods=['POST','GET'])
def services():    
    return render_template('services.html')

@app.route('/contacts',methods=['POST','GET'])
def contacts():    
    return render_template('contacts.html')

@app.route('/feedback',methods=['POST','GET'])
def feedback():    
    return render_template('feedback.html')

@app.route('/signup',methods=['POST','GET'])
def signup():    
    return render_template('signup.html')

@app.route('/recommend',methods=['POST','GET'])

def recommend():    
    if request.method == "POST":
        temp = request.data
        temp = temp.decode()
        temp = temp.split(',')

        doc_info = NaiveBayes(temp)
        path = os.path.join(PROJECT_ROOT,"static")
        path = os.path.join(path,"script")
        path = os.path.join(path,"docitems.js")
        file = open(path,'w')
        file.write('''var doc_info = "'''+str(doc_info[0])+'''?'''+str(doc_info[1])+'''?'''+str(doc_info[2])+'''?'''+str(doc_info[3])+'''?'''+str(doc_info[4])+'''"
        doc_info = doc_info.split("?")
var docblock = document.getElementById("docblock")
var html = `<div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Disease: </span><span class="ml-auto text-gray-900">${doc_info[0]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Doctor Name: </span><span class="ml-auto text-gray-900">${doc_info[2]}</span></div><div class="flex border-t border-gray-200 py-2"><span class="text-gray-500">Mobile No: </span><span class="ml-auto text-gray-900">${doc_info[3]}</span></div><div class="flex border-t border-b mb-6 border-gray-200 py-2"><span class="text-gray-500">Address: </span><span class="ml-auto text-gray-900">${doc_info[4]}</span></div>`
docblock.innerHTML =  html

var docimage = document.getElementById("docimage")

async function getUsers() {
  let response =await fetch("https://fakeface.rest/face/json?gender=male&minimum_age=35")
  let data = await response.json()
  return data
}

getUsers().then(data => docimage.innerHTML=`<img alt="doctor" width="400" height="400" src="${data.image_url}">`)''')
        file.close()

    return render_template('recommend.html')

@app.route('/doc',methods=['POST','GET'])
def docinfo():
    return render_template('docinfo.html')
