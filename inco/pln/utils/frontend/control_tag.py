from Tkconstants import END, INSERT, E, W, S, N, BOTH, LEFT
from Tkinter import Text, Tk
import json
import tkMessageBox
import ttk
from inco.pln.common import UIUtils

from inco.pln.tag.freeling import FreeLing
from inco.pln.tag.treetagger.treetagger import TreeTagger
from inco.pln.utils.frontend.configuration_manager import ConfigurationManager


__author__ = 'Matias'


class ControlTag:
    input_text_area = None
    """:type: Tkinter.Text """

    def __init__(self, parent):
        self.parent = parent
        self.frame = ttk.Frame(parent)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)

        # self.frame
        columns = 4
        #
        ttk.Label(self.frame, text="Input").grid(row=0, column=0, columnspan=columns)
        self.input_text_area = Text(self.frame, height=10)
        self.input_text_area.grid(row=1, column=0, columnspan=columns, sticky=W+E+S+N)

        ttk.Button(self.frame, text="Tag with FreeLing", command=self.__tag_with_freeling)\
            .grid(row=2, column=1, sticky=N+W+S+E)
        ttk.Button(self.frame, text="Tag with TreeTagger", command=self.__tag_with_treetagger)\
            .grid(row=2, column=2, sticky=N+W+S+E)

        ttk.Label(self.frame, text="Output").grid(row=3, column=0, columnspan=columns)
        self.output_text_area = Text(self.frame, height=10)
        self.output_text_area.grid(row=4, column=0, columnspan=columns, sticky=W+E+S+N)
        self.output_text_area['state'] = 'disabled'

        UIUtils.set_vertical_scroll(self.input_text_area)
        UIUtils.set_vertical_scroll(self.output_text_area)

    def __tag_with_freeling(self):
        freeling_path = ConfigurationManager.load()['freeling_path']

        if freeling_path is None:
            tkMessageBox.showerror(message='Path to FreeLing not set')
            return

        string = self.input_text_area.get("1.0", END)
        tokenizer = FreeLing(freeling_path)

        tokens_dict = tokenizer.raw_tag_full(string)

        tokens_dict_array = [json.dumps(x) for x in tokens_dict]

        tokenized_string = "\n".join(tokens_dict_array)

        self.output_text_area['state'] = 'normal'

        self.output_text_area.delete(1.0, END)
        self.output_text_area.insert(INSERT, tokenized_string)

        self.output_text_area['state'] = 'disabled'

    def __tag_with_treetagger(self):
        path = ConfigurationManager.load()['treetagger_path']

        if path is None:
            tkMessageBox.showerror(message='Path to TreeTagger not set')
            return

        string = self.input_text_area.get("1.0", END)
        tokenizer = TreeTagger(path)

        tokens_dict = tokenizer.raw_tag_full(string)

        tokens_dict_array = [str(x) for x in tokens_dict]

        tokenized_string = "\n".join(tokens_dict_array)

        self.output_text_area['state'] = 'normal'

        self.output_text_area.delete(1.0, END)
        self.output_text_area.insert(INSERT, tokenized_string)

        self.output_text_area['state'] = 'disabled'