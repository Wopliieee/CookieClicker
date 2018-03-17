import cx_Freeze
import os

executables = [cx_Freeze.Executable("ClickerPyGame.py")]

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35-32\tcl\tk8.6'

cx_Freeze.setup(
    name="ClickerPyGame by Wopliieee",
    options={"build_exe":{"packages":["pygame"],"include_files":["cookie.jpg","gui.png"]}},
    description = "ClickerPyGame",
    executables = executables,
    version='1.0.0'
    )