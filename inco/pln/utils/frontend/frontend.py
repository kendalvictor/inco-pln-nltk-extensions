import ttk

from inco.pln.utils.frontend.control_parse import ControlParse
from inco.pln.utils.frontend.control_tag import ControlTag
from inco.pln.utils.frontend.control_tokenize import ControlTokenize
from inco.pln.utils.frontend.menu_bar import MenuBar


__author__ = 'Matias'

from Tkinter import *

root = Tk()
root.wm_title('Demo Frontend')

toplevel = root.winfo_toplevel()
toplevel.wm_state('zoomed')

n = ttk.Notebook(root)
MenuBar(root)

n.add(ControlTokenize(n).frame, text='Tokenize')
n.add(ControlTag(n).frame, text='Tag')
n.add(ControlParse(n).frame, text='Parse')
n.pack(expand=True, fill=BOTH)

#2B2B2B


root.mainloop()