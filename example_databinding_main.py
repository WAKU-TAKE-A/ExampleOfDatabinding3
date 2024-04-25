# -*- coding: utf-8 -*-

"""
Data Binding Example.

* Run this file.
"""

import os

print(os.getcwd())

import wpf
from System.Windows import Application, Window
from example_databinding_viewmodel import Example_databinding_viewmodel

class Example_databinding_main(Window):

    def __init__(self):
        print('main.__Init__')
        self.vm = Example_databinding_viewmodel()
        self.DataContext = self.vm
        wpf.LoadComponent(self, 'example_databinding_view.xaml')

if __name__ == '__main__':
    Application().Run(Example_databinding_main())
