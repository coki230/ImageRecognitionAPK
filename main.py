import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDButton:
        pos_hint: {"center_x": .5, "center_y": 0.9}
        on_release: app.file_manager_open()
        

        MDButtonText:
            text: "Open manager"
            
            
    MDBoxLayout:
        radius: "36dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .4, .7
        md_bg_color: self.theme_cls.onSurfaceVariantColor

        FitImage:
            id: image_show
            size_hint_y: 1
            pos_hint: {"top": 1}
            radius: "36dp", "36dp", 0, 0
'''
class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
        )

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def file_manager_open(self):
        self.file_manager.show(
            os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path: str):
        '''
        It will be called when you click on the file name
        or the catalog selection button.

        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        MDSnackbar(
            MDSnackbarText(
                text=path,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
        ).open()

        print(path)
        # check path is a picture
        if path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg"):
            self.root.ids.image_show.source = path

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