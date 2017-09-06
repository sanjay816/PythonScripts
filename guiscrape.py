# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 16:04:37 2017

@author: NCM346
"""

from tkinter import *
from tkinter import ttk, filedialog, messagebox
import base64
import json
import os
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    _root = Tk()
    _root.title('Scrape app')
    
    
    _mainframe = ttk.Frame(_root, padding='5 5 5 5')
    _mainframe.grid(row=0, column=0, sticky=(E, W, N, S))