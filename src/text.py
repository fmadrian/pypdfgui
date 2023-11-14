WINDOW_TITLE = 'pypdfgui'

LANG = 'es'

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

if LANG != 'en':
    MSG_SUCCESS = 'Éxito'

    ERROR_NO_NAME = 'El archivo resultante debe tener un nombre.'
    ERROR_NO_FILES = 'Seleccione al menos dos archivos PDF para unir.'
    ERROR_INVALID_PDF = 'El archivo ({}) está dañado o no es válido.'
    MSG_ABOUT = 'Hecho con PyPDF2 y PyQt5.\nIcon: https://www.iconfinder.com/DesignRevision\n\nhttps://www.github.com/fsv2860/pypdfgui'


    DIALOG_TEXT={
        "ui_main" : {
            "btn_merge": "Unir PDF",
            "btn_split": "Dividir PDF",
            "btn_about": "Acerca de",
            "btn_exit": "Salir"
        },
        "ui_merge":{
            "btn_add": "Añadir PDF",
            "lbl_name": "Nombre del archivo:",
            "btn_up": "Subir",
            "btn_down": "Mover hacia abajo",
            "btn_delete": "Eliminar",
            "btn_merge": "Unir",
            "btn_back": "Volver"
        },
        "ui_split":{
            "lbl_parts": "Partes:",
            "btn_back": "Volver",
            "btn_split": "Dividir",
            "btn_loadfile": "Cargar PDF",
            "lbl_filename": "Nombre del archivo:"
        }
    }

