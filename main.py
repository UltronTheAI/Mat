from kivy.animation import Animation
from kivy.uix.screenmanager import Screen, Builder
from kivymd.app import MDApp
from kivymd.uix.button import *
from kivymd.uix.label import *
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.taptargetview import MDTapTargetView
import random

i = 0
ch = f'Write Ans... 1/0'
n = random.randint(0, 99 + i)
n1 = random.randint(90, 260)
n2 = 2
pi = 10
if n2 == 0:
    pi = n * n1
if n2 == 1:
    pi = n - n1
if n2 == 2:
    pi = n + n1
if n2 == 3:
    pi = n / n1
lis = ['x', '-', '+', '/']
ali = '5 + 5'
qus = 10
num = 0
ans = 0
wa = 0
wra = 0


class app(MDApp):
    dialog = None

    def check(self):
        global pi, qus, ans, wa, wra
        if self.settings4.text == '':
            int_str = 0
        else:
            v_int = str(self.settings4.text).replace(' ', '')
            int_str = int(v_int)
        ans = int_str
        print(ans)
        print(qus)
        if ans == qus:
            print('ok')
            wa += 1
            self.settings2.text = f'Write Ans... {wa}/{wra}'
            # print(self.settings2.text)
        else:
            print('no')
            wra += 1
            self.settings2.text = f'Wrong Ans, Ans IS {qus} | {wa}/{wra}'
        self.settings4.text = ''
        n = random.randint(0, 99 + i)
        n1 = random.randint(90, 260)
        n2 = random.randint(0, 3)
        pi = 10
        if n2 == 0:
            pi = n * n1
        if n2 == 1:
            pi = n - n1
        if n2 == 2:
            pi = n + n1
        if n2 == 3:
            pi = n / n1
        self.settings3.text = f'{n} {lis[n2]} {n1}'
        qus = pi

    def build(self):
        self.s = Screen()
        self.settings = MDIconButton(user_font_size=600, pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.settings1 = MDIcon(pos_hint={'center_x': 0.4, 'center_y': 0.1}, icon='teacher.jpg')
        self.settings2 = Builder.load_string('''
MDLabel:
    text: "QUSTION"
    pos_hint: {'center_x': 0.5, 'center_y': 0.95}
    halign: 'center'
    text_theme_color: 'Custom'
    font_size: 30
        ''')
        self.settings3 = Builder.load_string('''
MDLabel:
    text: """5 + 5"""
    pos_hint: {'center_x': 0.5, 'center_y': 0.87}
    halign: 'center'
    text_theme_color: 'Custom'
        ''')
        self.tol = Builder.load_string('''
MDBoxLayout:

    # Will always be at the bottom of the screen.
    MDBottomAppBar:

        MDToolbar:
            title: "NO"
            icon: "git"
            type: "bottom"
            # left_action_items: [["menu", lambda x: x]]
            opacity: 0.50
        ''')
        self.settings4 = Builder.load_string('''
MDTextField:
    hint_text: """ANS"""
    helper_text: """ANS"""
    helper_text_mode: "on_focus"
    size_hint_x: 0.5
    pos_hint: {'center_x': 0.5, 'center_y': 0.8}
    halign: 'center'
    text_theme_color: 'Custom'
        ''')
        self.settings5 = Builder.load_string('''
MDRoundFlatButton:
    text: """OK"""
    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
    # halign: 'center'
    text_theme_color: 'Custom'
    on_release: app.check()
        ''')
        # self.s.add_widget(self.tap_target_view)
        self.s.add_widget(self.settings2)
        self.s.add_widget(self.settings3)
        self.s.add_widget(self.settings4)
        self.s.add_widget(self.settings5)
        self.s.add_widget(self.settings1)
        self.s.add_widget(self.settings)
        # self.s.add_widget(self.tol)
        # app().show_alert_dialog()
        # self.settings4.text = '9'
        # app().check()
        return self.s


app().run()
