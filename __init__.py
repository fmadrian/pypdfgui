from PyQt5 import QtWidgets
from src.ui.split import Ui_Split
from src.ui_controller.split import Ui_Split_Controller
from src.ui.merge import Ui_Merge
from src.ui_controller.merge import Ui_Merge_Controller

if __name__ == "__main__":
    # Setup dialog.
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Dialog_Split = QtWidgets.QDialog()
    Dialog_Merge = QtWidgets.QMainWindow() 

    ui_split = Ui_Split()
    ui_split.setupUi(Dialog_Split)

    ui_merge = Ui_Merge()
    ui_merge.setupUi(Dialog_Merge)

    # Connect buttons with their respective functionality.
    win_split = Ui_Split_Controller(ui_split)
    win_merge = Ui_Merge_Controller(ui_merge)

    # Show dialog.
    Dialog_Split.show()
    sys.exit(app.exec_())