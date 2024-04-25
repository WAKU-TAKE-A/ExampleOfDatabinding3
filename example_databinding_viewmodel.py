# -*- coding: utf-8 -*-

"""
ViewModel.
"""

import clr
import os.path as path
from sys import path as systemPath
systemPath.append(path.join(path.dirname(__file__), "InfrastructureAssemblies"))
clr.AddReferenceToFile("Livet.Behaviors.dll")
clr.AddReferenceToFile("Livet.Core.dll")
clr.AddReferenceToFile("Livet.Mvvm.dll")
clr.AddReferenceToFile("Microsoft.Xaml.Behaviors.dll")
from Livet import ViewModel
from Livet.Commands import ViewModelCommand

class Example_databinding_viewmodel(ViewModel):

    def __init__(self):
        print("viewmodel.__Init__")
        # Set command.
        self.Run_Btn_One_Command = ViewModelCommand(self.Run_Btn_One)
        # Init command.
        self.Init = ViewModelCommand(self.Init)
        # Close command.
        self.Closed = ViewModelCommand(self.Closed)
        
    def Init(self):
        print("Init")

    def Closed(self):
        print("Close")

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