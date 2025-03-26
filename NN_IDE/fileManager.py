from PyQt6 import QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.Qsci import *

from pathlib import Path
import shutil
import os
import subprocess
import sys

import QSS_Resources_rc

from editor import Editor

class FileManager(QTreeView):
    def __init__(self, tabView, setNewTab=None, MainWindow=None):
        super(FileManager, self).__init__(None)

        self.setNewTab = setNewTab
        self.tabView = tabView
        self.mainWindow = MainWindow

        self.isRenaming = False
        self.currentEditIndex = None
        self.previousRenameName = None

        self.isTrue = bool


        self.managerFont = QFont("Segoe UI", 10)
        #self.managerFont.setPointSize(10)
        self.model = QFileSystemModel()
        self.model.setRootPath(os.getcwd())

        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files | QDir.Drives)
        self.model.setReadOnly(False)
        self.setFocusPolicy(Qt.NoFocus)

        self.setModel(self.model)
        self.setRootIndex(self.model.index(os.getcwd()))
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QTreeView.SelectRows)
        self.setEditTriggers(QTreeView.NoEditTriggers)
        #Context menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.clicked.connect(self.treeViewClicked)
        #hidding
        self.setHeaderHidden(True)
        self.setColumnHidden(1, True)
        self.setColumnHidden(2, True)
        self.setColumnHidden(3, True)

        #drag and drop
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)

        #enable file name editing
        self.itemDelegate().closeEditor.connect(self._onCloseEditor)

    def _onCloseEditor(self, editor: QLineEdit):
        if self.isRenaming:
            self.renameFileWithIndex()

    def treeViewClicked(self, index: QModelIndex):
        path = self.model.filePath(index)
        p = Path(path)
        if p.is_file():
            self.setNewTab(p)
        self.isTrue = True
        return True
        #self.mw.ui.mainPages.setCurrentWidget(self.ui.page_16)
    
    def showContextMenu(self, pos: QPoint):
        ix = self.indexAt(pos)
        menu = QMenu()
        menu.setStyleSheet("QMenu{\n"
        "     background-color: #2D2E2E;\n"
        "     margin: 2px; /* some spacing around the menu */\n"
        "     color: #FFFFFF;\n"
        "}\n"
        "QMenu::item {\n"
        "    padding: 4px 25px 4px 20px;\n"
        "    border: 1px solid transparent; /* reserve space for selection border */\n"
        "}\n"
        "QMenu::item:selected {\n"
        "    background: #606390;\n"
        "    border-radius: 2px;\n"
        "}\n"
        "QMenu::separator{\n"
        "    border: 1px transparent;\n"
        "    height: 1px;\n"
        "    background: #baacfd;\n"
        "    margin-left: 10px;\n"
        "    margin-right: 5px;\n"
        "    margin-top: 5px;\n"
        "    margin-bottom: 4px;\n"
        "}\n"
        "\n"
        "")
        menu.addAction("New File")
        menu.addAction("New Folder")
        menu.addAction("Open in file manager")

        if ix.column() == 0:
            menu.addAction("Rename")
            menu.addAction("Delete")
        
        action = menu.exec_(self.viewport().mapToGlobal(pos))

        if not action:
            return
        
        match action.text():
            case "Rename":
                self.actionRename(ix)
            case "Delete":
                self.actionDelete(ix)
            case "New Folder":
                self.actionNewFolder()
            case "New File":
                self.actionNewFile(ix)
            case "Open in file manager":
                self.actionOpenInFileManager(ix)
            case _:
                pass

    def showDialog(self, title, msg) -> int:
        dialog = QMessageBox(self)
        dialog.setFont(self.managerFont)
        dialog.font().setPointSize(14)
        dialog.setWindowTitle(title)
        dialog.setWindowIcon(QIcon(":/icons/Icons/window_close.png"))
        dialog.setText(msg)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)
        dialog.setIcon(QMessageBox.Warning)
        return dialog.exec_()
    
    def renameFileWithIndex(self):
        newName = self.model.fileName(self.currentEditIndex)
        if self.previousRenameName == newName:
            return
        
        for editor in self.tabView.findChildren(Editor):
            if editor.path.name == self.previousRenameName:
                editor.path = editor.path.parent / newName
                self.tabView.setTabText(
                    self.tabView.indexOf(editor), newName
                )
                self.tabView.repaint()
                editor.fullPath = editor.fullPath.absolute()
                self.mainWindow.currentFile = editor.path
                break

    def actionRename(self, ix):
        self.edit(ix)
        self.previousRenameName = self.model.fileName(ix)
        self.isRenaming = True
        self.currentEditIndex = ix

    def deleteFile(self, path:Path):
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()  

    def actionDelete(self, ix):
        fileName = self.model.fileName(ix)
        dialog = self.showDialog(
            "Delete", f"Are you sure you want to delete {fileName}?"
        )
        if dialog == QMessageBox.Yes:
            if self.selectionModel().selectedRows():
                for i in self.selectionModel().selectedRows():
                    path = Path(self.model.filePath(i))
                    self.deleteFile(path)
                    for editor in self.tabView.findChildren(Editor):
                        if editor.path.name == path.name:
                            self.tabView.removeTab(
                                self.tabView.indexOf(editor)
                            )

    def actionNewFile(self, ix):
        rootPath = self.model.rootPath()
        if ix.column() != 1 and self.model.isDir(ix):
            self.expand(ix)
            rootPath = self.model.filePath(ix)
        f = Path(rootPath) / "New File"
        count = 1
        while f.exists():
            f = Path(f.parent / f"New File{count}")
            count += 1
        f.touch()
        idx = self.model.index(str(f.absolute()))
        self.edit(idx)
    
    def actionNewFolder(self):
        f = Path(self.model.rootPath()) / "New Folder"
        count = 1
        while f.exists():
            f = Path(f.parent / f"New Folder{count}")
            count += 1
        idx = self.model.mkdir(self.rootIndex(), f.name)
        self.edit(idx)

    def actionOpenInFileManager(self, ix: QModelIndex):
        path = os.path.abspath(self.model.filePath(ix))
        isDir = self.model.isDir(ix)
        if os.name == "nt":
            #For Windows
            if isDir:
                subprocess.Popen(f'explorer "{path}"')
            else:
                subprocess.Popen(f'explorer /select,"{path}"')
        elif os.name == "posix":
            #For Linux or Mac OS
            if sys.platform == "darwin":
                #Mac OS 
                if isDir:
                    subprocess.Popen(["open", path])
                else:
                    subprocess.Popen(["open", "-R", path])
            else:
                #Linux
                subprocess.Popen(["xdg-open", os.path.dirname(path)])
        else:
            raise OSError (f"Unsupported platform {os.name}")

    #Drag drop functionality
    def dragEnterEvent(self, e: QDragEnterEvent) -> None:
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e: QDropEvent) -> None:
        rootPath = Path(self.model.rootPath())
        if e.mimeData().hasUrls():
            for url in e.mimeData().urls():
                path = Path(url.toLocalFile())
                if path.is_dir():
                    shutil.copytree(path, rootPath / path.name)
                else:
                    if rootPath.samefile(self.model.rootPath()):
                        idx: QModelIndex = self.indexAt(e.pos())
                        if idx.column() == 1:
                            shutil.move(path, rootPath / path.name)
                        else:
                            folderPath = Path(self.model.filePath(idx))
                            shutil.move(path, folderPath / path.name)
                    else:
                        shutil.copy(path, rootPath / path.name)
        e.accept()
        return super().dropEvent(e)