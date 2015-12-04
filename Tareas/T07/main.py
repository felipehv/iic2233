from PyQt4 import QtGui, QtCore, uic
import dropbox
from dropbox.files import FileMetadata, FolderMetadata
from dropbox import DropboxOAuth2FlowNoRedirect
import datetime
import os
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from classes import *
import pickle


#Varios contenidos son extraidos del ejemplo de la API de Dropbox
#Estos son modificados con el fin de ajustarlos al enunciado
formulario = uic.loadUiType("error.ui")
class ErrorWidget(formulario[0],formulario[1]):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.okButton.clicked.connect(self.ok)

    def ok(self, button):
        self.hide()

    def Show(self, m):
        self.label.setText(m)
        self.show()

formulario = uic.loadUiType("log.ui")
class Login(formulario[0],formulario[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.auth_flow = DropboxOAuth2FlowNoRedirect("o03x4f6y9dw5hsc", "zgt1fwtne4de6ed")
        self.authorize_url = self.auth_flow.start()
        url = QtCore.QUrl(self.authorize_url)
        self.dbxauth.load(url)

        self.errorwidget = ErrorWidget()


        #buttons connection
        self.loginButton.clicked.connect(self.init_dbx)

    def init_dbx(self,button):
        try:
            access_token, self.user_id = self.auth_flow.finish(self.token.text())
            self.dbx = dropbox.Dropbox(access_token)
        except Exception as err:
            self.errorwidget.Show("Error de autenticacion {}".format(err))
        else:
            self.hide()
            self.mainwidget = DropWidget(self.dbx,self.errorwidget)
            self.mainwidget.show()


formulario = uic.loadUiType("chat.ui")
class DropWidget(formulario[0], formulario[1]):
    def __init__(self,dbx, popup):
        super().__init__()
        self.setupUi(self)
        self.dbx = dbx
        self.popup = popup

        self.chooseButton.clicked.connect(self.selectFile)
        self.uploadButton.clicked.connect(self.upload)
        self.downloadButton.clicked.connect(self.download)
        self.openButton.clicked.connect(self.open)
        self.returnbutton.clicked.connect(self.comeback)
        self.newfolderButton.clicked.connect(self.new_folder)
        self.historyButton.clicked.connect(self.history)
        self.renameButton.clicked.connect(self.rename)
        self.originButton.clicked.connect(self.move1)
        self.moveButton.clicked.connect(self.move2)

        self.treeView.dw = self
        self.treeView.itemPressed.connect(self.treeView.dw.clicked)
        self.treeView.itemDoubleClicked.connect(self.open)

        self.actualpath = ""
        self.showItems("")

    def comeback(self, button):
        name = self.actualpath.split("/")[-1]
        path = self.actualpath[0:-len(name)-1]
        self.showItems(path)

    def open(self, e, b):
        path = self.actualpath + "/{}".format(e.text(0))
        md = self.get_metadata(path)
        if isinstance(md,dropbox.files.FolderMetadata):
            self.showItems(path)

    def clicked(self, e, b):
        text = e.text(0)
        self.label3.setText(text)

    def showItems(self, path):
        self.treeView.clear()
        self.actualpath = path
        self.model = QStandardItemModel()
        subitems = self.dbx.files_list_folder(self.actualpath).entries

        for subitem in subitems:
            self.treeView.addTopLevelItem(QTreeWidgetItem([subitem.name]))
        self.pathlabel.setText(self.actualpath)

    def get_metadata(self,path):
        return self.dbx.files_get_metadata(path)

    def selectFile(self):
        self.fileroot.setText(QtGui.QFileDialog.getOpenFileName())


    #Files and folders functions
    def history(self, button):
        path = self.actualpath + "/{}".format(self.label3.text())
        md = self.get_metadata(path)
        self.popup.Show(str(md))

    def new_folder(self, button):
        if self.newname.text() == "":
            return
        path = self.actualpath + "/{}".format(self.newname.text())
        self.dbx.files_create_folder(path)
        self.showItems(self.actualpath)

    def rename(self, button):
        if self.label3.text() == "":
            return
        path = self.actualpath + "/{}".format(self.label3.text())
        try:
            md,res = self.dbx.files_download(path)
            data = res.content
        except:
            return
        self.dbx.files_delete(path)
        newpath = self.actualpath + "/{}".format(self.newname.text())
        try:
            res = self.dbx.files_upload(
                data, newpath, mode=dropbox.files.WriteMode.add,
                client_modified=md.client_modified,
                mute=True)
        except dropbox.exceptions.ApiError as err:
            print('*** API error', err)
            return None
        self.showItems(self.actualpath)

    def move1(self, button):
        path = self.actualpath + "/{}".format(self.label3.text())
        self.origin.setText(path)

    def move2(self, button):
        path = self.actualpath + "/{}".format(self.label3.text())
        try:
            md = self.get_metadata(path)
        except:
            return
        if isinstance(md,dropbox.files.FolderMetadata):
            print(self.origin.text(),path + "{}".format(self.origin.text()))
            self.dbx.files_move(self.origin.text(),path + "{}".format(self.origin.text()))
            self.showItems(self.actualpath)
        

    def download_folder(self, path, localpath):
        folder_name = localpath.split("/")[-1]
        if folder_name not in os.listdir(localpath[0:-(len(folder_name)+1)]):
            os.mkdir(localpath)
        folders_list = self.dbx.files_list_folder(path).entries
        for entry in folders_list:
            path2 = path + "/{}".format(entry.name)
            localpath2 = localpath + "/{}".format(entry.name)
            if isinstance(entry, dropbox.files.FolderMetadata):
                print("folder",entry.name)
                self.download_folder(path2,localpath2)
            else:
                self.download(path2, localpath2)

    def download(self, path, localpath="."):
        if not path:
            path = self.actualpath + "/{}".format(self.label3.text())
        md = self.get_metadata(path)
        if isinstance(md,dropbox.files.FolderMetadata):
            self.download_folder(path,localpath="{}/{}".format(localpath,md.name))
            return
        try:
            md, res = self.dbx.files_download(path)
        except:
            print("Error")
        data = res.content
        localpath = localpath if md.name in localpath else localpath + "/{}".format(md.name)
        with open(localpath,"wb") as writer:
            pickle.dump(data,writer)

    def upload(self, name, overwrite=False):
        localpath = self.fileroot.text()
        print(localpath)
        name = localpath.split('/')[-1]
        path = self.pathlabel.text() + "/{}".format(name)
        mode = (dropbox.files.WriteMode.overwrite
                if overwrite
                else dropbox.files.WriteMode.add)
        mtime = os.path.getmtime(localpath)
        with open(localpath, 'rb') as f:
            data = f.read()
        try:
            res = self.dbx.files_upload(
                data, path, mode,
                client_modified=datetime.datetime(*time.gmtime(mtime)[:6]),
                mute=True)
        except dropbox.exceptions.ApiError as err:
            print('*** API error', err)
            return None
        print('uploaded as', res.name.encode('utf8'))
        self.popup.Show("Upload Successfull")
        self.showItems(self.actualpath)
        return res

    def filecopy(self, frompath, topath):
        self.dbx.files_copy(from_path, to_path)




if __name__ == "__main__":
    app = QtGui.QApplication([])
    dropboxint = Login()
    dropboxint.show()
    #test = DropWidget(False)
    #test.show()
    app.exec_()