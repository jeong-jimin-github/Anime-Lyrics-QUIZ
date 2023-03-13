from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty, ObjectProperty, ListProperty
from kivy.core.window import Window
import csv
import webbrowser
from discord_webhook import DiscordWebhook
import pandas as pd
import time
from kivy.lang import Builder

def write_df_to_local(df, file_path):
    df.to_csv(file_path, index=False)

Builder.load_file("uiquiz.kv")

class Home(Screen):
    data = {
        'Developer Site': 'account',
        'Support': 'email',
        'Review': 'star-shooting',
    }
    def callback(self, instance):
        if instance.icon == 'account':
            webbrowser.open("https://info.jeong-jimin.com")
        elif instance.icon == 'email':
            self.manager.current = 'Bug'
        elif instance.icon == 'star-shooting':
            webbrowser.open("market://details?id=PackageName")


class End(Screen):
    pass

class Bug(Screen):
    def report(self):
        text = self.ids.input.text
        if text == '':
            pass
        else:
            try:
                webhook = DiscordWebhook(url='YOUR DISCORD WEBHOOK URL', content=text)
                response = webhook.execute()
            except:
                pass

class QuizScreen(Screen):
    question= StringProperty()
    ans= StringProperty()
    ans1= StringProperty()
    ans2= StringProperty()
    Ans_data= StringProperty()
    error= StringProperty()
    error_number= NumericProperty(0)
    page_number=NumericProperty()
    no=NumericProperty()
    df=ListProperty()
    correct_answer=StringProperty()
    level = StringProperty()

    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.no=int(1)
        self.page_number= int(1)
        op=open('data.csv', 'r', encoding='utf-8')
        self.df=list(csv.reader(op))
        self.question=self.df[self.no][0].replace('br', '\n\n')
        self.correct_answer=self.df[self.no][1]
        self.ans=self.df[self.no][2]
        self.ans1=self.df[self.no][3]
        self.ans2=self.df[self.no][4]
        self.level=self.df[self.no][5]

    def restart(self):
        self.no= int(1)
        self.error_number=int(0)
        self.page_number=int(1)
        self.question=self.df[self.no][0].replace('br', '\n\n')
        self.correct_answer=self.df[self.no][1]
        self.ans=self.df[self.no][2]
        self.ans1=self.df[self.no][3]
        self.ans2=self.df[self.no][4]  
        self.level=self.df[self.no][5]
        self.error=''
        

    def go_next(self, find):
        self.error =''

        if  self.correct_answer == find:
            try:
                self.no=self.no+1
                self.page_number=self.page_number + 1
                self.question=self.df[self.no][0].replace('br', '\n\n')
                self.correct_answer=self.df[self.no][1]
                self.ans=self.df[self.no][2]
                self.ans1=self.df[self.no][3]
                self.ans2=self.df[self.no][4]  
                self.level=self.df[self.no][5]
            except:
                self.no= int(1)
                self.error_number=int(0)
                self.page_number=int(1)
                self.question=self.df[self.no][0].replace('br', '\n\n')
                self.correct_answer=self.df[self.no][1]
                self.ans=self.df[self.no][2]
                self.ans1=self.df[self.no][3]
                self.ans2=self.df[self.no][4]  
                self.level=self.df[self.no][5]
                self.manager.current = 'End'                
        else:
            self.error='[color=#FF0000]   답이 틀렸습니다. 다시 도전해 보세요.[/color]'
            self.error_number=self.error_number+1
    
class QuizApp(MDApp):
    def __init__(self, **kwargs):
        super(QuizApp, self).__init__(**kwargs)
        Window.clearcolor = (1,1,1,1)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='HomeScreen'))
        sm.add_widget(QuizScreen(name='QuizScreen'))
        sm.add_widget(Bug(name='Bug'))
        sm.add_widget(End(name='End'))
        return sm

if __name__ == '__main__':
    QuizApp().run()
