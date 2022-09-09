from kivy.lang import Builder

from kivymd.app import MDApp


class LAYMApp(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"

        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'LAYM'
            icon: 'gmail'
            badge_icon: "numeric-10"

            MDLabel:
                text: 'LOL'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Поиск'
            icon: 'twitter'
            badge_icon: "numeric-5"

            MDLabel:
                text: 'Twitter'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Настройки'
            icon: 'linkedin'

            MDLabel:
                text: 'LinkedIN'
                halign: 'center'
'''
        )


LAYMApp().run()

