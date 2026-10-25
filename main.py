import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# ضبط خلفية التطبيق باللون الداكن
Window.clearcolor = (0.1, 0.1, 0.12, 1)

class FazlakaNetApp(App):
    def build(self):
        self.title = "Fazlaka Net - MikroTik Manager"
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # العنوان الرئيس
        header = Label(
            text="فذلكا نت - إدارة الشبكة", 
            font_size='22sp', 
            bold=True, 
            size_hint_y=None, 
            height=50,
            color=(0.2, 0.7, 1, 1)
        )
        main_layout.add_widget(header)
        
        # منطقة المدخلات (IP - Username - Password)
        inputs_layout = BoxLayout(orientation='vertical', spacing=8, size_hint_y=None, height=160)
        
        self.ip_input = TextInput(text="192.168.88.1", hint_text="راوتر MikroTik IP", multiline=False)
        self.user_input = TextInput(text="admin", hint_text="اسم المستخدم", multiline=False)
        self.pass_input = TextInput(text="", hint_text="كلمة السر", password=True, multiline=False)
        
        inputs_layout.add_widget(self.ip_input)
        inputs_layout.add_widget(self.user_input)
        inputs_layout.add_widget(self.pass_input)
        
        main_layout.add_widget(inputs_layout)
        
        # زر الاتصال والاختبار
        btn_connect = Button(
            text="اتصال بالشبكة", 
            size_hint_y=None, 
            height=50, 
            background_color=(0.1, 0.6, 0.3, 1)
        )
        btn_connect.bind(on_press=self.check_connection)
        main_layout.add_widget(btn_connect)
        
        # منطقة السجلات والنتائج (Logs)
        scroll = ScrollView(size_hint=(1, 1))
        self.log_label = Label(
            text="التطبيق جاهز للاتصال...\n", 
            size_hint_y=None, 
            color=(0.8, 0.8, 0.8, 1)
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        scroll.add_widget(self.log_label)
        
        main_layout.add_widget(scroll)
        
        return main_layout

    def check_connection(self, instance):
        ip = self.ip_input.text
        user = self.user_input.text
        self.log_label.text += f"\n[+] جاري محاولة الاتصال بالراوتر: {ip} باسم {user}..."

if __name__ == '__main__':
    FazlakaNetApp().run()
