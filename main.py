from kivy.lang import Builder
from kivymd.app import MDApp
from plyer import filechooser

KV = '''
MDScreen:
    BoxLayout:
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .4, .7

        MDRectangleFlatButton:
            on_release: app.choose()
            pos_hint: {"center_x": .5}
            text: "Select a file"
        FitImage:
            id: image_show
            size_hint_y: 1
            pos_hint: {"top": 1}
'''

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def choose(self):
        # 打开文件选择器
        filepath = filechooser.open_file(title="Pick a file..", filters=[("All Files", "*.*")])
        # 更新标签显示所选文件路径
        if filepath:
            path = filepath[0]
            if path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg"):
                self.root.ids.image_show.source = path


MainApp().run()