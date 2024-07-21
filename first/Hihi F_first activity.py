import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
new_1=[]
test2=[]

emotion_dict = {#This is the dictory
    'anticipation': 0.7,'excitement': 0.9,'satisfaction': 0.7,'good': 1.0,'anxious': -0.5,'curious': 0.3,'challenging': 0.4,'nervous': -0.4,'hopeful': 0.7,
    'ready': 0.6,'optimistic': 0.7,'naive': 0.0,'unprepared': -0.6,'stressful': -0.7,'chill': 0.4,'tiresome': -0.6,'okay': 0.2,'completely': 0.0,
    'utterly': 0.0,'not': -0.2,'prepared': 0.6,'useful': 0.7,'tired': -0.6,'confused': -0.4,
    'open': 0.5,'lookingforwardto': 0.7,'wary': -0.5,'buzzing': 0.8,'extraordinary': 0.9,'expectation': 0.6,'practice': 0.5,'pass': 0.5,
    'cooperative': 0.7,'exciting': 0.9,'anticipated': 0.7,'difficulty': -0.4,'lookforward': 0.7,'afraid': -0.8,'tough': -0.3,
    'collaborative': 0.7,'excited': 0.9,'fear': -0.9,'fine': 0.2,'keen': 0.6,
    'ambitious': 0.6,'confident': 0.8,'difficult': -0.4,'passionate': 0.8,'happy': 1.0,'cumulative': 0.1,'hardworking': 0.7,
    'thrilling': 0.9,'integration': 0.4,'engaged': 0.7,'exercise': 0.3,'anticipating': 0.7,'challenge': 0.4,'impressive': 0.8,
    'eager': 0.7,'complicate': -0.5,'stress': -0.7,'fun': 0.9,'heavyload': -0.6,'enthusiastic': 0.8,'resolved': 0.6,'worried': -0.6,
    'hope': 0.7,'interested': 0.6,'cool': 0.7,'scary': -0.7,'active': 0.6,'intrigued': 0.5,'apprehensive': -0.4,'unknown': 0.0,
    'hard': -0.3,'new': 0.0,'stressed': -0.7,
    'neutral': 0.0,'practical': 0.5,'different': 0.0,'fresh': 0.4,
    'sad': -0.6,'uneasy': -0.5,'concerned': -0.4,'scared': -0.7,'strain': -0.3,'try': 0.2,'sigh': -0.3,'overthinking': -0.5,
    'stresses': -0.7,'uncertain': -0.3,'challengeable': 0.4,'expected': 0.6,'doubtful': -0.4,'fast-paced': -0.1,
    'compelled': 0.3,'mandated': 0.2,'dread': -0.6,'lost': -0.4,'overwhelming': -0.7,'worrying': -0.5,'intimidated': -0.4,'look forward': 0.7,
    'overwhelmed': -0.7,'unsure': -0.3,'breeze':0.7,'excite':0.9,'enjoy':1,'helpful':0.4,'inpatience': -0.7,'curiosity':0.3,'expect':0.6,
    'evil':-1,'equipped':0.5,
    'delighted':1,'exalted':1,'normally':0,'knowledgeable':0.6,'expectant':0.6,'repeated':-0.5,'determined':1,'conventional':0.3,'interest':0.7,'welcoming':0.9,
    'equal':0,'great':0.6,'meaningful':1,'relaxed':0.4,'depressed':-1,'beneficial':0.6,'thankful':0.6,'relief':0.3,'earnest':0.1,
    'important':1,'tedious':-0.8,'worrisome':-0.6,'nerivous':-0.8,'nice':0.8,'clueless':-0.4,'mysterious':0.2,'hectic':-0.8,'indifferent':-0.6,'wondering':0.8,
    'interesting':0.6,'Complicated':-0.5,'motivated':0.8 
}

def convert_strings_to_scores(string_array, emotion_dict):#To change the string into emotion score 
    scores = []
    for string in string_array:
        if string in emotion_dict:
            scores.append(emotion_dict[string])
        else:
            scores.append(0)
    return scores

def read_column_csv(file_path,number):
    try:
        df = pd.read_csv(file_path)
        first_column = df.iloc[:, number].tolist()  # 获取第一列数据并转换为列表
        return first_column
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: Failed to read CSV file '{file_path}'. {str(e)}")
        return []

def test(data):#Count the quantity for each category 
    number1=0
    number2=0
    number3=0
    number4=0
    number5=0
    clean=[]
    for i in data:
        print(i)
        if -3<=float(i)<-1.5:
            number1= number1+1
        elif -1.5<=float(i)<0:
            number2=number2+1
        elif float(i)==0:
            number3 = number3+1
        elif 0<float(i)<=1.5:
            number4 = number4+1
        elif 1.5<float(i)<=3:
            number5 =number5+1
    clean.append(number1)
    clean.append(number2)
    clean.append(number3)
    clean.append(number4)
    clean.append(number5)
    return clean

def plot_pie_chart(categories, data):#draw the picture
    explode = [0.1] * len(categories)  
    fig, ax = plt.subplots(figsize=(8, 8))
    patches, texts, autotexts = ax.pie(data, labels=categories, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})
    ax.axis('equal') 
    # add interactive feature
    annot = ax.annotate("", xy=(0, 0), xytext=(-20, 20), textcoords="offset points",bbox=dict(boxstyle="round,pad=0.5", fc="yellow", alpha=0.5),arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))
    annot.set_visible(False)

    def update_annot(i):
        text = f"{categories[i]}: {data[i]}"
        annot.xy = patches[i].center
        annot.set_text(text)
        annot.get_bbox_patch().set_alpha(0.8)

    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            for i, patch in enumerate(patches):
                if patch.contains(event)[0]:  
                    update_annot(i)
                    annot.set_visible(True)
                    patches[i].set_edgecolor('red')  
                    patches[i].set_linewidth(2.0)   
                    fig.canvas.draw_idle()
                    return
        if vis:
            for patch in patches:
                patch.set_edgecolor('black') 
                patch.set_linewidth(1.5)      
            annot.set_visible(False)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)
    notes = {
        'Very Negative (-3 to -1.5)': 'blue',
        'Negative (-1.5 to 0)': 'orange',
        'Neutral (0)': 'green',
        'Positive (0 to 1.5)': 'red',
        'Very Positive (1.5 to 3)': 'purple'
    }
    handles = [plt.Rectangle((0,0),1,1, color=color) for label, color in notes.items()]
    labels = list(notes.keys())
    plt.legend(handles, labels, loc='lower right')
    
    plt.title('Student attitude toward 399',fontsize= 20)
    plt.show()

def calum(score1,score2,score3,classmate,intro):#get the final score 
    finnal = []
    for i in range(len(score1)):
        score_total = score1[i]#*0.4+score2[i]*0.3+score3[i]*0.3
        finnal.append(score_total)
    return finnal

#def replace_column_in_csv(input_file, output_file, column_name, new_data):

    df = pd.read_csv(input_file)

    if len(new_data) != len(df):
        raise ValueError("mistake")

    df[column_name] = new_data

    df.to_csv(output_file, index=False)

    print(f"done {output_file}")

if __name__ == "__main__":
    class_new=[]
    intro_new = []
    file_path = "cleaned-sentiment.csv" 

    first_column_data = read_column_csv(file_path,3)
    second_column_data =read_column_csv(file_path,4)
    third_column_data = read_column_csv(file_path,5)
    forth_column_data = read_column_csv(file_path,6)
    second_question = read_column_csv(file_path,7)
    third_question = read_column_csv(file_path,8)
    class_if = read_column_csv(file_path,10)
    intro_if = read_column_csv(file_path,11)

    first_column_score=convert_strings_to_scores(first_column_data,emotion_dict)
    #replace_column_in_csv("cleaned-sentiment.csv","cleaned-sentiment1.csv","Word1",first_column_score)
    second_column_score=convert_strings_to_scores(second_column_data,emotion_dict)
    #replace_column_in_csv("cleaned-sentiment1.csv","cleaned-sentiment2.csv","Word2",second_column_score)
    third_column_score=convert_strings_to_scores(third_column_data,emotion_dict)
    #replace_column_in_csv("cleaned-sentiment2.csv","cleaned-sentiment3.csv","Word3",third_column_score)
    forth_column_score=convert_strings_to_scores(forth_column_data,emotion_dict)
    #replace_column_in_csv("cleaned-sentiment3.csv","cleaned-sentiment4.csv","Word4",forth_column_score)
    second_question=convert_strings_to_scores(second_question,emotion_dict)
    #replace_column_in_csv("cleaned-sentiment4.csv","cleaned-sentiment5.csv","Q2",second_question)
    third_question = convert_strings_to_scores(third_question,emotion_dict)
    #replace_column_in_csv("cleaned-sentiment5.csv","cleaned-sentiment6.csv","Q3",third_question)
    for i in range(len(first_column_score)):
        total_score=first_column_score[i]+second_column_score[i]+third_column_score[i]+forth_column_score[i]
        new_1.append(total_score)
    
    
    finall = calum(new_1,second_question,third_question,class_if,intro_if)
    clean = test(finall)
    clean1 = ["very negative", "negative", "neutral", "positive", "very positive"]
    plot_pie_chart(clean1,clean)