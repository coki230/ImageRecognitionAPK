from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.utils import platform
import net
import os

KV = '''
MDScreen:
    BoxLayout:
        orientation: 'vertical'
        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5}
            on_release: app.file_manager_open()
        FitImage:
            pos_hint: {'center_x': .5}
            size_hint: 0.5, 0.3
            id: image_show
        MDLabel:
            halign: "center"
            id: image_label
            font_size: 36
'''


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True
        )

    def build(self):
        return Builder.load_string(KV)

    def file_manager_open(self):
        self.file_manager.show_disks()
        PATH = os.path.dirname(os.path.abspath(__file__))
        if platform == "android":
          PATH = "/storage/emulated/0/Pictures" #app_folder
        self.file_manager.show(PATH)  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        self.root.ids.image_show.source = path
        try:
            catigory = net.parse_img(path)
            self.root.ids.image_label.text = catigory
        except Exception as e:
            self.root.ids.image_label.text = str(e)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


Example().run()

# a = net.parse_img("hua2.jpg")
# print(a)