WINDOW_TITLE = 'pypdfgui'

MSG_ERROR = 'Error'
MSG_SUCCESS = 'Success'

ERROR_NO_NAME = 'The result file must have a name.'
ERROR_NO_FILES = 'Select at least two PDF files to join.'
ERROR_INVALID_PDF = 'The file ({}) is damaged or not valid.'
MSG_ABOUT = 'Made using PyPDF2 and PyQt5.\nIcon: https://www.iconfinder.com/DesignRevision\n\nhttps://www.github.com/fsv2860/pypdfgui'


DIALOG_TEXT={
    "ui_main" : {
        "btn_merge": "Merge",
        "btn_split": "Split",
        "btn_about": "About",
        "btn_exit": "Exit"
    },
    "ui_merge":{
        "btn_add":"Add PDF",
        "lbl_name":"File's name:",
        "btn_up":"Move up",
        "btn_down":"Move down",
        "btn_delete":"Remove",
        "btn_merge":"Merge",
        "btn_back":"Return"
    },
    "ui_split":{
        "lbl_parts":"Parts:",
        "btn_back":"Return",
        "btn_split":"Split",
        "btn_loadfile":"Load PDF",
        "lbl_filename":"File's name:"
    }
}