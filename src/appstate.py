from heapq import merge
import sys
"""
    Handles the dialog state (whether if they're being shown or not).
"""
class AppState:
    # dialog
    Dialog_Main = None
    Dialog_Merge = None
    Dialog_Split = None
    
    @staticmethod
    def connect(dmain, dmerge,dsplit):
        AppState.Dialog_Main = dmain
        AppState.Dialog_Merge = dmerge
        AppState.Dialog_Split = dsplit

    @staticmethod
    def open(name):
        AppState.hideAll()    
        if(name == "main"):
            AppState.Dialog_Main.show()
        elif(name == "merge"):
            AppState.Dialog_Merge.show()
        elif(name == "split"):
            AppState.Dialog_Split.show()

    @staticmethod
    def hide(name):
        if(name == "main"):
            AppState.Dialog_Main.hide()
        elif(name == "merge"):
            AppState.Dialog_Merge.hide()
        elif(name == "split"):
            AppState.Dialog_Split.hide()

    @staticmethod
    def hideAll():
        for dialog in [AppState.Dialog_Main, AppState.Dialog_Merge, AppState.Dialog_Split]:
            dialog.hide()
            
    @staticmethod
    def exit():
        sys.exit()

    
       
