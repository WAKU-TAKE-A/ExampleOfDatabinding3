# -*- coding: utf-8 -*-

"""
ViewModel.
"""

import clr
import os.path as path
from sys import path as systemPath
systemPath.append(path.join(path.dirname(__file__), "InfrastructureAssemblies"))
clr.AddReferenceToFile("Livet.dll")
from Livet import ViewModel as BindableBase
from Livet.Commands import ViewModelCommand as DelegateCommand

class Example_databinding_viewmodel(BindableBase):

    def __init__(self):
        # Set command.
        self.Run_Btn_One_Command = DelegateCommand(self.Run_Btn_One)
        # Init command.
        self.InitCommand = DelegateCommand(self.Init)
        # Close command.
        self.CloseCommand = DelegateCommand(self.Close)
        
    def Close(self):
        print("Close")
        
    def Init(self):
        print("Init")

    # Txt_One property.
    _Txt_One = 1.0
    @property
    def Txt_One(self):
        print("Txt_One getter")
        return self._Txt_One
    @Txt_One.setter
    def Txt_One(self, value):
        print("Txt_One setter")
        if self._Txt_One == value:
            return
        self._Txt_One = value
        self.RaisePropertyChanged("")

    # Txt_Two property.
    _Txt_Two = 2.0
    @property
    def Txt_Two(self):
        print("Txt_Two getter")
        return self._Txt_Two
    @Txt_Two.setter
    def Txt_Two(self, value):
        print("Txt_Two setter")
        if self._Txt_Two == value:
            return
        self._Txt_Two = value
        self.RaisePropertyChanged("")
    
    def Run_Btn_One(self):
        print("Run_Btn_One")
        self.Txt_Two = self.Txt_One