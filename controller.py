from PyQt5.QtWidgets import QApplication , QMainWindow
import sys
from Maincode.seldasforUSST import *
from Maincode.untitled import *
from threading import Thread
import inspect
import ctypes,threading

class OpenScrapy(QMainWindow, Ui_Form):
    spy=None
    optor = scrapyclass()
    def __init__(self):
        super(OpenScrapy, self).__init__()
        self.setupUi(self)

    def acti(self):
        self.spy = Thread(target=self.optor.getCourseData,args=(self.info,self.path.text(),self.term.currentText()))
        self.spy.start()
        self.pushButton.setDisabled(True)
        self.pushButton_2.setEnabled(True)

    def totheend(self):
        self.info.moveCursor(self.info.verticalScrollBar().maximum())

    def termi(self):
        self.abort()

    def quit(self):
        if self.spy==None:
            sys.exit()
        elif self.spy.is_alive():
            self.abort()
            sys.exit()
        else:
            sys.exit()

    def abort(self):
        self.info.append("终止爬虫线程中...")
        if self.spy.is_alive():
            self._async_raise(self.spy.ident,SystemExit)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setDisabled(True)
        time.sleep(5)
        count=threading.active_count()
        self.info.append("爬虫已终止，当前线程总数："+str(count))

    def _async_raise(self,tid, exctype):#强行终止进程方法
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

if __name__=="__main__":
    os.system("taskkill /f /im IEDriverServer.exe")
    # os.system("taskkill /f /im chrome.exe")
    app = QApplication(sys.argv)
    myWin = OpenScrapy()
    myWin.show()
    sys.exit(app.exec_())

