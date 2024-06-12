"""
Marker width adjustment tool.

Creates sidebar element that allows the control of width of orthogonal transects made via the
transect marker tool.
"""

import kivy.uix as ui
from kivy.uix.textinput import TextInput
import functions as func


class MarkerWidth(ui.boxlayout.BoxLayout):
    """
    Marker width adjustment tool.

    Creates sidebar element that allows the control of width of orthogonal transects made via the
    transect marker tool.

    Attributes:
        txt: TextInput widget where user enters their desired width
        btn: 'Go' Button
        marker: Current MultiMarker instance
        min: Int, minimum width allowed
        max: Int, maximum width allowed

        Inherits additional attributes from kivy.uix.boxlayout.Boxlayout (see kivy docs)
    """
    def __init__(self, marker, **kwargs):
        """
        Defines graphical elements.

        Args:
            marker: Active MultiMarker instance
        """
        super(MarkerWidth, self).__init__(**kwargs)
        self.txt = TextInput(hint_text="Width", size_hint=(.7, 1))
        self.btn = func.RoundedButton(text="Go", size_hint=(.3, 1), font_size=marker.home.font)
        self.btn.bind(on_press=lambda x: self.update())
        self.add_widget(self.txt)
        self.add_widget(self.btn)
        self.marker = marker
        self.min = 1
        self.max = 400

    def font_adapt(self, font):
        """
        Update go button font size

        Args:
            font: Float, new font size
        """
        self.btn.font_size = font

    def update(self):
        """
        Update width of current marker if given a valid width.
        """
        num = self.txt.text
        if num.isnumeric():
            num = int(num)
            if self.min <= num <= self.max:
                self.marker.update_width(num)
