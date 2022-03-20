from PyQt5 import QtWidgets
from src.ui.split import Ui_Split
from src.ui_controller.split import Ui_Split_Controller

if __name__ == "__main__":
    # Setup dialog.
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Split()
    ui.setupUi(Dialog)

    # Connect buttons with their respective functionality.
    win_split = Ui_Split_Controller(ui)

    # Show dialog.
    Dialog.show()
    sys.exit(app.exec_())