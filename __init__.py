import sys
from PyQt5 import QtWidgets
from src.ui.main import Ui_Main
from src.ui.split import Ui_Split
from src.ui_controller.main import Ui_Main_Controller
from src.ui_controller.split import Ui_Split_Controller
from src.ui.merge import Ui_Merge
from src.ui_controller.merge import Ui_Merge_Controller
from src.appstate import AppState

if __name__ == "__main__":
    # Setup dialogs.
    app = QtWidgets.QApplication(sys.argv)

    Dialog_Split = QtWidgets.QDialog()
    Dialog_Merge = QtWidgets.QDialog() 
    Dialog_Main = QtWidgets.QDialog()

    ui_split = Ui_Split()
    ui_split.setupUi(Dialog_Split)

    ui_merge = Ui_Merge()
    ui_merge.setupUi(Dialog_Merge)

    ui_main = Ui_Main()
    ui_main.setupUi(Dialog_Main)

    # Connect buttons with their respective functionality.
    win_split = Ui_Split_Controller(ui_split)
    win_merge = Ui_Merge_Controller(ui_merge)
    win_main = Ui_Main_Controller(ui_main)

    # Connect dialogs with app state.
    AppState.connect(Dialog_Main,Dialog_Merge,Dialog_Split)
    AppState.open("main")
    
    sys.exit(app.exec_())
    