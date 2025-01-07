from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.app import MDApp
from plyer import filechooser

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
            
            
    MDBoxLayout:
        radius: "36dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .4, .7
        md_bg_color: self.theme_cls.onSurfaceVariantColor
        
            
        FileChoose:
        size_hint_y: 0.1
        on_release: self.choose()
        text: 'Select a file'

        FitImage:
            id: image_show
            size_hint_y: 1
            pos_hint: {"top": 1}
            radius: "36dp", "36dp", 0, 0
'''
class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    '''
    Button that triggers 'filechooser.open_file()' and processes
    the data response from filechooser Activity.
    '''

    selection = ListProperty([])

    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
        path = self.selection[0]
        print(path)
        # check path is a picture
        if path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg"):
            self.root.ids.image_show.source = path

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

Example().run()