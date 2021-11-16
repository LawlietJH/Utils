
# Tested in: Python 3.8.8 - Windows
# By: LawlietJH
# Utils v1.0.9

# Banner:
# ███    █▄      ███      ▄█   ▄█          ▄████████    
# ███    ███ ▀█████████▄ ███  ███         ███    ███    █▄▄ █▄█ ▀   █   ▄▀█ █ █ █ █   █ █▀▀ ▀█▀   █ █ █
# ███    ███    ▀███▀▀██ ███▌ ███         ███    █▀     █▄█  █  ▄   █▄▄ █▀█ ▀▄▀▄▀ █▄▄ █ ██▄  █  █▄█ █▀█
# ███    ███     ███   ▀ ███▌ ███         ███           
# ███    ███     ███     ███▌ ███       ▀███████████    ██    ██  ██     ██████      █████
# ███    ███     ███     ███  ███                ███    ██    ██ ███    ██  ████    ██   ██
# ███    ███     ███     ███  ███▌    ▄    ▄█    ███    ██    ██  ██    ██ ██ ██     ██████
# ████████▀     ▄████▀   █▀   █████▄▄██  ▄████████▀      ██  ██   ██    ████  ██         ██
#                             ▀                           ████    ██ ██  ██████  ██  █████

from datetime import datetime, timedelta
import pywintypes
import binascii
import requests						# python -m pip install requests
import hashlib
import atexit
import locale
import psutil						# python -m pip install psutil
import random
import socket
import string
import numpy						# python -m pip install numpy
import json
import math
import time
import cv2							# python -m pip install opencv-python scipy
import bz2
import mss							# python -m pip install mss
import PIL							# python -m pip install pillow
import sys
import wmi							# python -m pip install wmi
import re
import os

#=======================================================================
#=======================================================================
# Interfaz en Utils.Actions.Explorer ===================================
try:
	from Tkinter import Tk
	from Tkinter import filedialog
except:
	from tkinter import Tk
	from tkinter import filedialog
#=======================================================================

# Manipulacion de DLLs de Windows ======================================
import ctypes
import comtypes						# python -m pip install comtypes
from ctypes import wintypes
#=======================================================================

# pip install pywin32 ==================================================
from win32com.shell  import shell, shellcon
from win32com.client import Dispatch
import win32api			as WA
import win32con			as WC		# All Constants
import win32gui			as WG
import win32console		as WCS
import win32ui			as WU
import win32security	as WS
import win32clipboard	as WCB
import win32net			as WN
import winreg			as WR
import win32com			as WCM
import win32process		as WP
#=======================================================================
#=======================================================================
#=======================================================================
__author__  = 'LawlietJH'	# Desarrollador
__title__   = 'Utils'		# Nombre
__version__ = 'v1.0.9'		# Version
#=======================================================================
#=======================================================================
# Constants ============================================================

WC.MB_CANCELTRYCONTINUE = 6

#=======================================================================
#=======================================================================
#=======================================================================

class ObjectList(list):
	
	def __init__(self, list_):
		super().__init__(list_)
		self.list = list_
	
	def __add__(self, val):
		if val.__class__.__name__ == 'str':
			for l in self.list:
				if not l.__class__.__name__ == 'str':
					return str(self.list) + val
			return ', '.join(self.list) + val
		elif val.__class__.__name__ == 'list':
			return ObjectList(self.list+val)
		else:
			return val
	
	def __radd__(self, val):
		if val.__class__.__name__ == 'str':
			for l in self.list:
				if not l.__class__.__name__ == 'str':
					return val + str(self.list)
			return val + ', '.join(self.list)
		elif val.__class__.__name__ == 'list':
			return ObjectList(val+self.list)
		else:
			return val

class ObjectInt(int):
	
	def __init__(self, int_):
		self.int = int_
	
	def __add__(self, val):
		if val.__class__.__name__ == 'int':
			return ObjectInt(self.int+val)
		elif val.__class__.__name__ == 'str':
			return str(self.int) + val
		else:
			return val
	
	def __radd__(self, val):
		if val.__class__.__name__ == 'int':
			return ObjectInt(val+self.int)
		elif val.__class__.__name__ == 'str':
			return val + str(self.int)
		else:
			return val

class ObjectClassNames: #Use    # Obtiene todos los nombres de las clases en los objetos de 'Utils' y la cantidad.    Detecta Clases con Formato de primer letra Mayúscula. Ejemplo: 'PrimeroSegundoTercero'
	
	def __init__(self, obj):
		self.use = '''
		\r Función: ObjectClassNames(obj)
		\r |
		\r + Ejemplos de uso:
		\r |
		\r |    utils = Utils()
		\r |
		\r |    # utils.classes --> str: <'list':[...], 'qty':0>
		\r |    print(utils.classes)
		\r |
		\r |    # utils.classes.list + list--> list
		\r |    # utils.classes.list --> list
		\r |    print('Classes list:', utils.classes.list)
		\r |
		\r |    # utils.classes.qty + int --> int
		\r |    # utils.classes.qty --> int
		\r |    print('Classes qty:', utils.classes.qty)
		\r |
		\r |    # Al sumar con string se convierte en string, sino, seguira siendo una lista.
		\r |    # utils.classes.list + str --> str
		\r |    print('Classes str(list): ' + utils.classes.list)
		\r |
		\r |    # Al sumar con string se convierte en string, sino, seguira siendo un entero.
		\r |    # utils.classes.qty + str --> str
		\r |    print('Classes str(qty): ' + utils.classes.qty)
		\r \\
		'''
		list_ = [
			a for a in dir(obj)
			if a[0] == a[0].upper()
			and not a[0] == '_'
			and not a.startswith('not_')
			and not self.isException(obj, a)
		]
		error_list = [
			a for a in dir(obj)
			if a[0] == a[0].upper()
			and not a[0] == '_'
			and not a.startswith('not_')
			and self.isException(obj, a)
		]
		self.error_list = ObjectList(error_list)
		self.list = ObjectList(list_)
		self.qty  = ObjectInt(len(list_))
		self.cls  = obj.__class__.__name__
	
	def __str__(self):
		output = '<{}: '+repr(self.cls) + ', {}: '+str(self.list) + ', {}: '+str(self.error_list) + ', {}: '+str(self.qty) + '>'
		return output.format(repr('class'), repr('list'), repr('error_list'), repr('qty'))
	
	def isException(self, obj, class_name):
		try:
			return isinstance(eval('obj.'+class_name+'(error_msg="")'), Exception)
		except:
			return False
	
	@property
	def dict(self):
		return {
			'class': self.cls,
			'list': self.list,
			'qty': self.qty
		}

class ObjectFunctionNames: #Use # Obtiene todos los nombres de las funciones en los objetos de 'Utils' y la cantidad. Detecta funciones con Formato de primer letra minúscula. Ejemplo: 'primeroSegundoTercero'
	
	def __init__(self, obj):
		self.use = '''
		\r Función: ObjectFunctionNames(obj)
		\r |
		\r + Ejemplos de uso:
		\r |
		\r |    utils = Utils()
		\r |
		\r |    # utils.functions --> str: <'list':[...], 'qty':0>
		\r |    print(utils.functions)
		\r |
		\r |    # utils.functions.list + list --> list
		\r |    # utils.functions.list --> list
		\r |    print('Functions list:', utils.functions.list)
		\r |
		\r |    # utils.functions.qty + int --> int
		\r |    # utils.functions.qty --> int
		\r |    print('Functions qty:', utils.functions.qty)
		\r |
		\r |    # Al sumar con string se convierte en string, sino, seguira siendo una lista.
		\r |    # utils.functions.list + str --> str
		\r |    print('Functions str(list): ' + utils.functions.list)
		\r |
		\r |    # Al sumar con string se convierte en string, sino, seguira siendo un entero.
		\r |    # utils.functions.qty + str --> str
		\r |    print('Functions str(qty): ' + utils.functions.qty)
		\r \\
		'''
		list_ = [
			a for a in dir(obj) 
			if  not a[0] == a[0].upper()
			and not a[0] == '_'
			and not a.startswith('not_')
		]
		self.list = ObjectList(list_)
		self.qty  = ObjectInt(len(list_))
		self.cls  = obj.__class__.__name__
	
	def __str__(self):
		output = '<{}: '+repr(self.cls) + ', {}: '+str(self.list) + ', {}: '+str(self.qty) + '>'
		return output.format(repr('class'), repr('list'), repr('qty'))
	
	@property
	def dict(self):
		return {
			'class': self.cls,
			'list': self.list,
			'qty': self.qty
		}

#=======================================================================
#=======================================================================
#=======================================================================

class Utils:
	
	def __init__(self):
		
		self.classes   = ObjectClassNames(self)
		self.functions = None
		self.functions = ObjectFunctionNames(self)
		
		self.Actions      = self.Actions(self)
		self.EditRegistry = self.EditRegistry()
		self.MemoryInfo   = self.MemoryInfo()
		self.NetworkInfo  = self.NetworkInfo()
		self.SystemInfo   = self.SystemInfo()
		self.Utilities    = self.Utilities()
	
	class Actions:		# Interacciones con el Systema (Mayormente Windows)
		
		class BeepError(Exception):
			def __init__(self, error_msg): self.error_msg = error_msg
			def __str__(self): return repr(self.error_msg)
		
		class EmptyingTheTrashError(Exception):
			def __init__(self, error_msg): self.error_msg = error_msg
			def __str__(self): return repr(self.error_msg)
		
		class ExitWindowsError(Exception):
			def __init__(self, error_msg): self.error_msg = error_msg
			def __str__(self): return repr(self.error_msg)
		
		class StyleOfWindowError(Exception):
			def __init__(self, error_msg): self.error_msg = error_msg
			def __str__(self): return repr(self.error_msg)
		
		def __init__(self, utils):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.load_uses()
			self.run_command = lambda command: os.popen(command).read()	# Ejecuta cualquier comando en consola
			
			# Clases Internas:
			self.Clipboard = self.Clipboard()
			self.Explorer  = self.Explorer()
			self.Keyboard  = self.Keyboard()
			self.Mouse     = self.Mouse()
			self.VBS       = self.VBS()
			self.Volume    = self.Volume()
			
			# Conexiones a Clases hermanas:
			self.SystemInfo = utils.SystemInfo()
		
		#---------------------------------------------------------------
		
		class Clipboard:												# Manipula el clipboard (Copiar/Pegar)
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.use = '''\
				\r Clase: Clipboard
				\r |
				\r + Ejemplo de uso: 
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Pegar: Devuelve el contenido que se haya copiado.
				\r |    print(utils.Actions.Clipboard.text)
				\r |    
				\r |    # Copiar: Remplaza el contenido para poder Pegarlo.
				\r |    utils.Actions.Clipboard.text = 'Texto'
				\r |    
				\r |    # Vaciar: Vacia el Clipboard.
				\r |    del utils.Actions.Clipboard.text
				\r \\\
				'''
			
			# print(Clipboard.text)										# Pegar: Devuelve el contenido que se haya copiado.
			@property
			def text(self):
				WCB.OpenClipboard()
				try:
					text = WCB.GetClipboardData()
					WCB.CloseClipboard()
					return text
				except TypeError:
					return ''
			
			# Clipboard.text = 'Texto'									# Copiar: Remplaza el contenido para poder Pegarlo.
			@text.setter
			def text(self, text):
				WCB.OpenClipboard()
				WCB.EmptyClipboard()
				WCB.SetClipboardText(text, WCB.CF_TEXT)
				WCB.CloseClipboard()
			
			# del Clipboard.text										# Vaciar: Vacia el Clipboard.
			@text.deleter
			def text(self):
				WCB.OpenClipboard()
				WCB.EmptyClipboard()
				WCB.SetClipboardText(b'', WCB.CF_TEXT)
				WCB.CloseClipboard()
		
		#---------------------------------------------------------------
		
		class Explorer: #Use											# Permite controlar las ventanas 'Abrir', 'Seleccionar carpeta' y 'Guardar como' para obtener las rutas seleccionadas.
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.use = '''
				\r Clase: Explorer()
				\r │
				\r │ # Default params:
				\r │
				\r ├─ getFileName(
				\r │      title = 'Abrir',
				\r │      file_types = [
				\r │          ['Todos los Archivos','.*'],
				\r │          ['Archivos de Texto','.txt']
				\r │      ],
				\r │      init_dir = os.getcwd(),
				\r │      topmost  = True
				\r │  )
				\r │ 
				\r ├─ getFolderName(
				\r │      title = 'Seleccionar Carpeta',
				\r │      init_dir = os.getcwd(),
				\r │      topmost = True
				\r │  )
				\r │
				\r ├─ getFileNameSave(
				\r │      title = 'Guardar como',
				\r │      file_types = [
				\r │          ['Todos los Archivos','.*'],
				\r │          ['Archivos de Texto','.txt']
				\r │      ],
				\r │      init_dir = os.getcwd(),
				\r │      topmost = True
				\r │  )
				\r |
				\r + Ejemplos de uso:
				\r |
				\r |    utils = Utils()
				\r |
				\r |    # Obtiene la ruta completa y el nombre del archivo para 'Abrir':
				\r |    file_name = utils.Actions.Explorer.getFileName()
				\r |    print(file_name)
				\r |
				\r |    # Obtiene la ruta completa de la Carpeta Seleccionada para 'Seleccionar Carpeta':
				\r |    folder_path = utils.Actions.Explorer.getFolderName()
				\r |    print(folder_path)
				\r |
				\r |    # Obtiene la ruta completa y el nombre de Archivo indicado para 'Guardar como':
				\r |    file_name_save = utils.Actions.Explorer.getFileNameSave()
				\r |    print(file_name_save)
				\r \\    
				'''
				self.root = Tk()
				self.root.withdraw()
			
			def __str__(self): return self.use
			
			def getFileName(self, title='Abrir', file_types=[ 
						['Todos los Archivos','.*'], ['Archivos de Texto','.txt']
					], init_dir=os.getcwd(), topmost=True):
				
				if topmost == True:
					self.root.wm_attributes('-topmost', True)
				else:
					self.root.wm_attributes('-topmost', False)
				
				f_name = filedialog.askopenfile(title = title,
												initialdir = init_dir,
												filetypes = file_types)
				if not f_name == None:
					return f_name.name
			
			def getFolderName(self, title='Seleccionar Carpeta', init_dir=os.getcwd(), topmost=True):
				
				if topmost == True:
					self.root.wm_attributes('-topmost', True)
				else:
					self.root.wm_attributes('-topmost', False)
				
				d_path = filedialog.askdirectory(title = title, initialdir = init_dir)
				
				if not d_path == '':
					return d_path
			
			def getFileNameSave(self, title='Guardar como', file_types=[
							['Todos los Archivos','.*'], ['Archivos de Texto','.txt']
						], init_dir=os.getcwd(), topmost=True):
				
				if topmost == True:
					self.root.wm_attributes('-topmost', True)
				else:
					self.root.wm_attributes('-topmost', False)
				
				f_name = filedialog.asksaveasfilename(title = title,
													  initialdir = init_dir,
													  filetypes = file_types)
				if not f_name == '':
					return f_name
		
		#---------------------------------------------------------------
		
		class Keyboard:													# Controla eventos del Teclado
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				# Giant dictonary to hold key name and VK value
				# http://www.kbdedit.com/manual/low_level_vk_list.html
				# https://gist.github.com/chriskiehl/2906125
				self.VK = {
					'left button': 0x01,
					'right button': 0x02,
					'middle button': 0x04,
					'x button 1': 0x05,
					'x button 2': 0x06,
					'backspace': 0x08,
					'tab': 0x09,
					'clear': 0x0C,
					'enter': 0x0D,
					'shift': 0x10,
					'ctrl': 0x11,
					'alt': 0x12,
					'pause': 0x13,
					'caps lock': 0x14,
					'esc': 0x1B,
					'spacebar': 0x20,
					' ': 0x20,
					'page up': 0x21,
					'page down': 0x22,
					'end': 0x23,
					'home': 0x24,
					'left arrow': 0x25,
					'up arrow': 0x26,
					'right arrow': 0x27,
					'down arrow': 0x28,
					'select': 0x29,
					'print': 0x2A,
					'execute': 0x2B,
					'print screen': 0x2C,
					'ins': 0x2D,
					'del': 0x2E,
					'help': 0x2F,
					'windows': 0x5B,
					'sleep': 0x5F,
					'0': 0x30,
					'1': 0x31,
					'2': 0x32,
					'3': 0x33,
					'4': 0x34,
					'5': 0x35,
					'6': 0x36,
					'7': 0x37,
					'8': 0x38,
					'9': 0x39,
					'a': 0x41,
					'b': 0x42,
					'c': 0x43,
					'd': 0x44,
					'e': 0x45,
					'f': 0x46,
					'g': 0x47,
					'h': 0x48,
					'i': 0x49,
					'j': 0x4A,
					'k': 0x4B,
					'l': 0x4C,
					'm': 0x4D,
					'n': 0x4E,
					'o': 0x4F,
					'p': 0x50,
					'q': 0x51,
					'r': 0x52,
					's': 0x53,
					't': 0x54,
					'u': 0x55,
					'v': 0x56,
					'w': 0x57,
					'x': 0x58,
					'y': 0x59,
					'z': 0x5A,
					'numpad 0': 0x60,
					'numpad 1': 0x61,
					'numpad 2': 0x62,
					'numpad 3': 0x63,
					'numpad 4': 0x64,
					'numpad 5': 0x65,
					'numpad 6': 0x66,
					'numpad 7': 0x67,
					'numpad 8': 0x68,
					'numpad 9': 0x69,
					'multiply key': 0x6A,
					'add key': 0x6B,
					'separator key': 0x6C,
					'subtract key': 0x6D,
					'decimal key': 0x6E,
					'divide key': 0x6F,
					'f1': 0x70,
					'f2': 0x71,
					'f3': 0x72,
					'f4': 0x73,
					'f5': 0x74,
					'f6': 0x75,
					'f7': 0x76,
					'f8': 0x77,
					'f9': 0x78,
					'f10': 0x79,
					'f11': 0x7A,
					'f12': 0x7B,
					'f13': 0x7C,
					'f14': 0x7D,
					'f15': 0x7E,
					'f16': 0x7f,
					'f17': 0x80,
					'f18': 0x81,
					'f19': 0x82,
					'f20': 0x83,
					'f21': 0x84,
					'f22': 0x85,
					'f23': 0x86,
					'f24': 0x87,
					'num lock': 0x90,
					'scroll lock': 0x91,
					'left shift': 0xA0,
					'right shift': 0xA1,
					'left control': 0xA2,
					'right control': 0xA3,
					'left menu': 0xA4,
					'right menu': 0xA5,
					'browser back': 0xA6,
					'browser forward': 0xA7,
					'browser refresh': 0xA8,
					'browser stop': 0xA9,
					'browser search': 0xAA,
					'browser favorites': 0xAB,
					'browser start and home': 0xAC,
					'volume mute': 0xAD,
					'volume down': 0xAE,
					'volume up': 0xAF,
					'next track': 0xB0,
					'previous track': 0xB1,
					'stop media': 0xB2,
					'play/pause media': 0xB3,
					'start mail': 0xB4,
					'select media': 0xB5,
					'start application 1': 0xB6,
					'start application 2': 0xB7,
					'attn key': 0xF6,
					'crsel key': 0xF7,
					'exsel key': 0xF8,
					'play key': 0xFA,
					'zoom key': 0xFB,
					'clear key': 0xFE,
					'<': 0xE2,
					# Por Defecto:
					# ~ '+': 0xBB,
					# ~ ',': 0xBC,
					# ~ '-': 0xBD,
					# ~ '.': 0xBE,
					# ~ '/': 0xBF,
					# ~ '`': 0xC0,
					# ~ ';': 0xBA,
					# ~ '[': 0xDB,
					# ~ '\\': 0xDC,
					# ~ ']': 0xDD,
					# ~ "'": 0xDE
					# Teclado: Español (España)
					'º': 0xDC,
					'\'': 0xDB,
					'¡': 0xDD,
					'`': 0xBA,
					'+': 0xBB,
					'ç': 0xBF,
					'ñ': 0xC0,
					'´': 0xDE,
					',': 0xBC,
					'.': 0xBE,
					'-': 0xBD
					# Teclado: Español (México)
					# ~ '|': 0xDC,
					# ~ '\'': 0xDB,
					# ~ '¿': 0xDD,
					# ~ '´': 0xBA,
					# ~ '+': 0xBB,
					# ~ '}': 0xBF,
					# ~ 'ñ': 0xC0,
					# ~ '{': 0xDE,
					# ~ ',': 0xBC,
					# ~ '.': 0xBE,
					# ~ '-': 0xBD
				}
				
				self.use = '''
				\r Clase: Keyboard
				\r │ 
				\r │ # Descripción: Permite manipular los eventos del
				\r │ teclado. Permite presionar teclas, mantenerlas
				\r │ cuanto tiempo se desee y soltarla cuando se indique.
				\r │ 
				\r │ # Default params:
				\r │ 
				\r ├─ getKeyState(
				\r │    vk = ''         # Se indica el nombre de alguna tecla listada en Keyboard.VK
				\r │  )
				\r | 
				\r + Ejemplos de uso:
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Presiona y suelta de inmediato cada tecla. Simula pulsaciones típicas.
				\r |    # Acepta tantas teclas como desee. Pueden ser una sola o varias teclas:
				\r |    utils.Actions.Keyboard.press('Left Arrow', 'A','B')
				\r |    
				\r |    # Presiona y mantiene la combinación de teclas pero no las suelta.
				\r |    # Acepta tantas teclas como desee. Pueden ser una sola o varias teclas:
				\r |    utils.Actions.Keyboard.pressAndHold('Left Arrow', 'A','B')
				\r |    
				\r |    # Suelta la combinación de teclas presionadas.
				\r |    # Acepta tantas teclas como desee. Pueden ser una sola o varias teclas:
				\r |    utils.Actions.Keyboard.release('Left Arrow', 'A','B')
				\r |    
				\r |    # Presiona y mantiene la combinación de teclas, después las suelta en el mismo orden.
				\r |    # Acepta tantas teclas como desee. Pueden ser una sola o varias teclas:
				\r |    utils.Actions.Keyboard.pressHoldRelease('Ctrl', 'Alt', 'Del')
				\r |    # También sirve para poner mayúsculas:
				\r |    utils.Actions.Keyboard.pressHoldRelease('Shift','A')
				\r |    
				\r |    # Una forma más sencilla para poner mayúsculas o cualquier combinación con mayus izquierdo:
				\r |    utils.Actions.Keyboard.typeWithShift('A')
				\r |    
				\r |    # Para escribir en automático todo un texto:
				\r |    utils.Actions.Keyboard.typer('Hola Mundo!')
				\r \\    
				'''
			
			def getVK(self, vk=''):
				try:
					return self.VK[vk.lower()]
				except:
					return None
			
			def getKeyState(self, vk=''):
				return WA.GetKeyState(self.VK[vk.lower()])
			
			def getAsyncKeyState(self, vk=''):
				return WA.GetAsyncKeyState(self.VK[vk.lower()])
			
			def press(self, *args, sleep=.05):
				'''
				one press, one release.
				accepts as many arguments as you want. e.g. press('left arrow', 'a','b').
				'''
				for char in args:
					WA.keybd_event(self.VK[char.lower()], 0, 0, 0)
					time.sleep(sleep)
					WA.keybd_event(self.VK[char.lower()], 0, WC.KEYEVENTF_KEYUP, 0)
			
			def pressAndHold(self, *args, sleep=.05):
				'''
				press and hold. Do NOT release.
				accepts as many arguments as you want.
				e.g. pressAndHold('left arrow', 'a','b').
				'''
				for char in args:
					WA.keybd_event(self.VK[char.lower()], 0, 0, 0)
					time.sleep(sleep)
			
			def release(self, *args, sleep=.05):
				'''
				release depressed keys
				accepts as many arguments as you want.
				e.g. release('left arrow', 'a','b').
				'''
				for char in args:
					WA.keybd_event(self.VK[char.lower()], 0, WC.KEYEVENTF_KEYUP, 0)
					time.sleep(sleep)
			
			def pressHoldRelease(self, *args, sleep=.05):
				'''
				press and hold passed in strings. Once held, release
				accepts as many arguments as you want.
				e.g. pressAndHold('left arrow', 'a', 'b').

				this is useful for issuing shortcut command or shift commands.
				e.g. pressHoldRelease('ctrl', 'alt', 'del'), pressHoldRelease('shift','a')
				'''
				for char in args:
					WA.keybd_event(self.VK[char.lower()], 0, 0, 0)
					time.sleep(sleep)
						
				for char in args[::-1]:
					WA.keybd_event(self.VK[char.lower()], 0, WC.KEYEVENTF_KEYUP, 0)
					time.sleep(sleep)
			
			def typeWithShift(self, char='', sleep=.05):
				WA.keybd_event(self.VK['left shift'], 0, 0, 0)
				WA.keybd_event(self.VK[char.lower()], 0, 0, 0)
				time.sleep(sleep)
				WA.keybd_event(self.VK['left shift'], 0, WC.KEYEVENTF_KEYUP, 0)
				WA.keybd_event(self.VK[char.lower()], 0, WC.KEYEVENTF_KEYUP, 0)
			
			def typer(self, string='', sleep=.05):
				for char in string:
					if   char == '!': self.typeWithShift('1', sleep=sleep)
					elif char == '@': self.typeWithShift('2', sleep=sleep)
					elif char == '{': self.typeWithShift('[', sleep=sleep)
					elif char == '?': self.typeWithShift('/', sleep=sleep)
					elif char == ':': self.typeWithShift(';', sleep=sleep)
					elif char == '"': self.typeWithShift('\'', sleep=sleep)
					elif char == '}': self.typeWithShift(']', sleep=sleep)
					elif char == '#': self.typeWithShift('3', sleep=sleep)
					elif char == '$': self.typeWithShift('4', sleep=sleep)
					elif char == '%': self.typeWithShift('5', sleep=sleep)
					elif char == '^': self.typeWithShift('6', sleep=sleep)
					elif char == '&': self.typeWithShift('7', sleep=sleep)
					elif char == '*': self.typeWithShift('8', sleep=sleep)
					elif char == '(': self.typeWithShift('9', sleep=sleep)
					elif char == ')': self.typeWithShift('0', sleep=sleep)
					elif char == '_': self.typeWithShift('-', sleep=sleep)
					elif char == '=': self.typeWithShift('+', sleep=sleep)
					elif char == '~': self.typeWithShift('`', sleep=sleep)
					elif char == '<': self.typeWithShift(',', sleep=sleep)
					elif char == '>': self.typeWithShift('.', sleep=sleep)
					elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						self.typeWithShift(char, sleep=sleep)
					else:
						self.press(char, sleep=sleep)
		
		#---------------------------------------------------------------
		
		class Mouse:													# Controla eventos del Mouse
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
				self.MOUSEEVENTF_LEFTDOWN   = 0x0002
				self.MOUSEEVENTF_LEFTUP     = 0x0004
				self.MOUSEEVENTF_RIGHTDOWN  = 0x0008
				self.MOUSEEVENTF_RIGHTUP    = 0x0010
				self.MOUSEEVENTF_MIDDLEDOWN = 0x0020
				self.MOUSEEVENTF_MIDDLEUP   = 0x0040
				# ~ self.MOUSEEVENTF_MOVE       = 0x0001
				# ~ self.MOUSEEVENTF_WHEEL      = 0x0800
				# ~ self.MOUSEEVENTF_XDOWN      = 0x0080
				# ~ self.MOUSEEVENTF_XUP        = 0x0100
				# ~ self.MOUSEEVENTF_HWHEEL     = 0x01000
				''# ~ self.MOUSEEVENTF_ABSOLUTE   = 0x8000
			
			# print(Mouse.position)
			@property
			def position(self):											# Devuelve la posición actual del cursor en pantalla en (X, Y) pixeles
				return WA.GetCursorPos()
			
			# Mouse.position = (100, 100)
			@position.setter
			def position(self, position):								# Posiciona el cursor en (X, Y)
				WA.SetCursorPos(position)
			
			def leftClick(self, qty=1, sleep=0.01):									# Da un clic izquierdo en la posición actual del cursor
				for x in range(qty):
					ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
					time.sleep(sleep)
					ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_LEFTUP,   0, 0, 0, 0)
			
			def leftClickDown(self):									# Da un clic izquierdo en la posición actual del cursor y lo mantiene
				ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
			
			def leftClickUp(self):										# Deja de presionar el clic izquierdo
				ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
			
			def rightClick(self, qty=1, sleep=0.01):								# Da un clic derecho en la posición actual del cursor
				for x in range(qty):
					ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
					time.sleep(sleep)
					ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_RIGHTUP,   0, 0, 0, 0)
			
			def rightClickDown(self):									# Da un clic derecho en la posición actual del cursor y lo mantiene
				ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
			
			def rightClickUp(self):										# Deja de presionar el clic derecho
				ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
			
			def middleClick(self, qty=1, sleep=0.01):								# Da un clic central (rueda del mouse) en la posición actual del cursor
				for x in range(qty):
					ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
					time.sleep(sleep)
					ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_MIDDLEUP,   0, 0, 0, 0)
			
			def middleClickDown(self):									# Da un clic central (presionando rueda del mouse) en la posición actual del cursor y lo mantiene
				ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
			
			def middleClickUp(self):										# Deja de presionar el clic central (rueda del mouse)
				ctypes.windll.user32.mouse_event(self.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
		
		#---------------------------------------------------------------
		
		class VBS:														# Ejecuta Scripts VBS
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.load_uses()
				
				self.run_command = lambda command: os.popen(command).read()	# Ejecuta cualquier comando en consola
			
			@property
			def use(self):
				self.load_uses(1)
				use = '''\
				\r Clase: VBS
				\r |
				\r + Lista de usos:
				\r |  
				\r |  utils = Utils()
				\r |  
				\r |  print(utils.Actions.VBS.minimizeAll_use)
				\r |  
				\r {0}
				\r |  
				\r |  print(utils.Actions.VBS.ejectCDROM_use)
				\r |  
				\r {1}
				\r |  
				\r |  print(utils.Actions.VBS.getWindowsProductKey_use)
				\r |  
				\r {2}
				\r |  
				\r |  print(utils.Actions.VBS.setVolume_use)
				\r |  
				\r {3}
				\r |  
				\r \\\
				'''.format(
					self.minimizeAll_use,
					self.ejectCDROM_use,
					self.getWindowsProductKey_use,
					self.setVolume_use
				)
				self.load_uses()
				return use
			
			def load_uses(self, indent=0):
				pipe = '|    '*indent
				self.minimizeAll_use = '''\
				\r {0}Función: ejectCDROM(rm=True)
				\r {0}|
				\r {0}| Minimiza todas las ventas que esten activas en pantalla.
				\r {0}|
				\r {0}+ Ejemplo de uso: 
				\r {0}|
				\r {0}|    # El parametro rm (remove) indica si el archivo generado
				\r {0}|    # en la carpeta temporal será removido o no.
				\r {0}|    # Por defecto siempre será removido, rm=True.
				\r {0}|    
				\r {0}|    utils.Actions.VBS.minimizeAll()
				\r {0}\\\
				'''.format(pipe)
				self.ejectCDROM_use = '''\
				\r {0}Función: ejectCDROM(rm=True)
				\r {0}|
				\r {0}| Expulsa las bandejas de disco disponibles en el sistema.
				\r {0}|
				\r {0}+ Ejemplo de uso: 
				\r {0}|
				\r {0}|    # El parametro rm (remove) indica si el archivo generado
				\r {0}|    # en la carpeta temporal será removido o no.
				\r {0}|    # Por defecto siempre será removido, rm=True.
				\r {0}|    
				\r {0}|    utils.Actions.VBS.ejectCDROM()
				\r {0}\\\
				'''.format(pipe)
				self.getWindowsProductKey_use = '''\
				\r {0}Función: getWindowsProductKey(return_key=True, save_key=False, rm=True)
				\r {0}|
				\r {0}| Obtiene la clave de producto de windows.
				\r {0}|
				\r {0}+ Ejemplo de uso: 
				\r {0}|
				\r {0}|    # El parametro rm (remove) indica si el archivo generado
				\r {0}|    # en la carpeta temporal será removido o no.
				\r {0}|    # Por defecto siempre será removido, rm=True.
				\r {0}|    
				\r {0}|    # save_key=True Permite guardar la clave en un archivo
				\r {0}|    key = utils.Actions.VBS.getWindowsProductKey(save_key=True)
				\r {0}|    print('\\nClave de Producto de Windows:', key)
				\r {0}\\\
				'''.format(pipe)
				self.setVolume_use = '''\
				\r {0}Función: setVolume(percent=72, rm=True)
				\r {0}|
				\r {0}| Permite cambiar el volumen del sistema.
				\r {0}|
				\r {0}+ Ejemplo de uso: 
				\r {0}|    
				\r {0}|    # El parametro rm (remove) indica si el archivo generado
				\r {0}|    # en la carpeta temporal será removido o no.
				\r {0}|    # Por defecto siempre será removido, rm=True.
				\r {0}|    
				\r {0}|    # percent permite ajustar el volumen entre 0 y 100
				\r {0}|    utils.Actions.VBS.setVolume(percent=50)
				\r {0}\\\
				'''.format(pipe)
			
			def runScriptVBS(self, name, payload, rm, ret=False):		# Ejecuta el script VBS
				
				temp_path = os.getenv('TEMP') + '\\_odin_\\'			# Obtiene la ruta de la carpeta de archivos temporales en windows
				name = temp_path + name									# Indica la ruta y nombre del archivo
				
				if not os.path.isdir(temp_path):						# Crea la carpeta _odin_ en los archivos temporales si no existe
					os.mkdir(temp_path)
				
				if not os.path.isfile(name):							# Crea el archivo si no existe en la carpeta %temp%\_odin_
					with open(name,'w') as File:
						File.write(payload)								# Añade el código dentro del archivo
						File.close()
				
				output = self.run_command('cscript ' + name)			# Ejecuta el código del script
				
				if rm: os.remove(name)									# Elimina el archivo min.vbs
				
				if len(os.listdir(temp_path)) == 0:						# Elimina la carpeta _odin_ si esta vacia 
					os.rmdir(temp_path)
				
				if ret: return output									# Si ret=True: Devuelve el texto generado por el script.
			
			def minimizeAll(self, rm=True):								# Minimiza todas las ventanas
				name = 'minimizeAll.vbs'									# Indica el nombre del archivo
				payload = '''\
					\r ' VBS Script para Minimizar todas las ventanas.
					\r Set var = CreateObject("Shell.Application")
					\r var.MinimizeAll
				'''
				self.runScriptVBS(name, payload, rm)
			
			def ejectCDROM(self, rm=True):								# Expulsa la bandeja de disco.
				name = 'ejectCDROM.vbs'
				payload = '''\
					\r ' VBS Script para Expulsar la bandeja de Disco.
					\r Set oWMP = CreateObject("WMPlayer.OCX.7")
					\r Set CDROMs = oWMP.cdromCollection
					\r if CDROMs.Count >= 1 then
					\r     For i = 0 to CDROMs.Count - 1
					\r         CDROMs.Item(i).Eject
					\r     Next
					\r End if
				'''
				self.runScriptVBS(name, payload, rm)
			
			def getWindowsProductKey(self, save_key=False, rm=True): # use	# Obtiene la Clave de Producto de Windows y la muestra en pantalla.
				# save_key: Si es True Guarda la clave en un archvio.
				# rm:       Si es True Elimina el archivo del Script.
				
				name = 'gwpk.vbs'
				payload = '''\
					\r ' VBS Script para obtener la Clave de Producto Original de Windows.
					\r
					\r Set WshShell = WScript.CreateObject("WScript.Shell")
					\r KeyPath = "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\DigitalProductId"
					\r
					\r Function ExtractKey(KeyInput)
					\r 	Const KeyOffset = 52
					\r 	i = 28
					\r 	CharWhitelist = "BCDFGHJKMPQRTVWXY2346789"
					\r 	Do
					\r 		Cur = 0
					\r 		x = 14
					\r 		Do
					\r 			Cur = Cur * 256
					\r 			Cur = KeyInput(x + KeyOffset) + Cur
					\r 			KeyInput(x + KeyOffset) = (Cur \ 24) And 255
					\r 			Cur = Cur Mod 24
					\r 			x = x -1
					\r 		Loop While x >= 0
					\r 		i = i -1
					\r 		KeyOutput = Mid(CharWhitelist, Cur + 1, 1) & KeyOutput
					\r 		If (((29 - i) Mod 6) = 0) And (i <> -1) Then
					\r 			i = i -1
					\r 			KeyOutput = "-" & KeyOutput
					\r 		End If
					\r 	Loop While i >= 0
					\r 	ExtractKey = KeyOutput
					\r End Function
					\r
					\r ' Guardar Clave en un archivo
					\r {0}Dim fso, my_file
					\r {0}Set fso = CreateObject("Scripting.FileSystemObject")
					\r {0}Set my_file = fso.CreateTextFile("WinProductKey.zion", True)
					\r {0}my_file.WriteLine(ExtractKey(WshShell.RegRead(KeyPath)))
					\r {0}my_file.Close
					\r
					\r WScript.Echo ExtractKey(WshShell.RegRead(KeyPath))
				'''.format('\' ' if not save_key else '')
				
				# Equipo\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform --> BackupProductKeyDefault
				# ~ powershell "(Get-WmiObject -query ‘select * from SoftwareLicensingService’).OA3xOriginalProductKey"
				
				key = self.runScriptVBS(name, payload, rm, ret=True)
				key = key.split('\n')
				
				while '' in key: key.remove('')
				return key[-1]
			
			def setVolume(self, percent=72, rm=True): # use				# Permite ajustar el volumen del sistema. Nota: Ver la clase 'Actions.Volume' para una mejor manejo del volumen del sistema.
				if not 0 <= percent <= 100: return
				percent = percent//2
				name = 'vol.vbs'
				# VolumeMute: 173
				# VolumeDown: 174
				# VolumeUp:   175
				payload = '''
					' VBS Script para Subir o Bajar el Volumen del Sistema Activo.
					
					Set WshShell = CreateObject("WScript.Shell")
					
					for i = 1 to 50
						WshShell.SendKeys(chr(174))
					next
					
					for i = 1 to {}
						WshShell.SendKeys(chr(175))
					next
				'''.format(percent)
				self.runScriptVBS(name, payload, rm)
		
		#---------------------------------------------------------------
		
		class Volume:												# Controlador de Volumen del Sistema
			
			class VolumeControlIsNotSupported(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			class MuteControlIsNotSupported(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			class ChannelDoesNotExists(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			class VolumeHandler:
				
				MMDeviceApiLib = comtypes.GUID('{2FDAAFA3-7523-4F66-9957-9D5E7FE698F6}')
				
				class IAudioEndpointVolume(comtypes.IUnknown):
					IID_IAudioEndpointVolume = comtypes.GUID(
						'{5CDF2C82-841E-4546-9722-0CF74078229A}')
					LPCGUID = ctypes.POINTER(comtypes.GUID)
					LPFLOAT = ctypes.POINTER(ctypes.c_float)
					LPDWORD = ctypes.POINTER(wintypes.DWORD)
					LPUINT = ctypes.POINTER(wintypes.UINT)
					LPBOOL = ctypes.POINTER(wintypes.BOOL)
					_iid_ = IID_IAudioEndpointVolume
					_methods_ = (
						comtypes.STDMETHOD(ctypes.HRESULT, 'RegisterControlChangeNotify', []),
						comtypes.STDMETHOD(ctypes.HRESULT, 'UnregisterControlChangeNotify', []),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'GetChannelCount',
							(['out', 'retval'], LPUINT, 'pnChannelCount')),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'SetMasterVolumeLevel',
							(['in'], ctypes.c_float, 'fLevelDB'),
							(['in'], LPCGUID, 'pguidEventContext', None)),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'SetMasterVolumeLevelScalar',
							(['in'], ctypes.c_float, 'fLevel'),
							(['in'], LPCGUID, 'pguidEventContext', None)),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'GetMasterVolumeLevel',
							(['out','retval'], LPFLOAT, 'pfLevelDB')),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'GetMasterVolumeLevelScalar',
							(['out','retval'], LPFLOAT, 'pfLevel')),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'SetChannelVolumeLevel',
							(['in'], wintypes.UINT, 'nChannel'),
							(['in'], ctypes.c_float, 'fLevelDB'),
							(['in'], LPCGUID, 'pguidEventContext', None)),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'SetChannelVolumeLevelScalar',
							(['in'], wintypes.UINT, 'nChannel'),
							(['in'], ctypes.c_float, 'fLevel'),
							(['in'], LPCGUID, 'pguidEventContext', None)),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'GetChannelVolumeLevel',
							(['in'], wintypes.UINT, 'nChannel'),
							(['out','retval'], LPFLOAT, 'pfLevelDB')),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'GetChannelVolumeLevelScalar',
							(['in'], wintypes.UINT, 'nChannel'),
							(['out','retval'], LPFLOAT, 'pfLevel')),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'SetMute',
							(['in'], wintypes.BOOL, 'bMute'),
							(['in'], LPCGUID, 'pguidEventContext', None)),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'GetMute',
							(['out','retval'], LPBOOL, 'pbMute')),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'GetVolumeStepInfo',
							(['out','retval'], LPUINT, 'pnStep'),
							(['out','retval'], LPUINT, 'pnStepCount')),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'VolumeStepUp',
							(['in'], LPCGUID, 'pguidEventContext', None)),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'VolumeStepDown',
							(['in'], LPCGUID, 'pguidEventContext', None)),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'QueryHardwareSupport',
							(['out','retval'], LPDWORD, 'pdwHardwareSupportMask')),
						comtypes.COMMETHOD([], ctypes.HRESULT, 'GetVolumeRange',
							(['out','retval'], LPFLOAT, 'pfLevelMinDB'),
							(['out','retval'], LPFLOAT, 'pfLevelMaxDB'),
							(['out','retval'], LPFLOAT, 'pfVolumeIncrementDB')))
					
					@classmethod
					def method(cls):
						
						class IMMDeviceEnumerator(comtypes.IUnknown):
							
							class IMMDevice(comtypes.IUnknown):
								IID_IMMDevice = comtypes.GUID(
									'{D666063F-1587-4E43-81F1-B948E807363F}')
								REFIID = ctypes.POINTER(comtypes.GUID)
								LPDWORD = ctypes.POINTER(wintypes.DWORD)
								PIUnknown = ctypes.POINTER(comtypes.IUnknown)
								_iid_ = IID_IMMDevice
								_methods_ = (
									comtypes.COMMETHOD([], ctypes.HRESULT, 'Activate',
										(['in'], REFIID, 'iid'),
										(['in'], wintypes.DWORD, 'dwClsCtx'),
										(['in'], LPDWORD, 'pActivationParams', None),
										(['out','retval'], ctypes.POINTER(PIUnknown), 'ppInterface')),
									comtypes.STDMETHOD(ctypes.HRESULT, 'OpenPropertyStore', []),
									comtypes.STDMETHOD(ctypes.HRESULT, 'GetId', []),
									comtypes.STDMETHOD(ctypes.HRESULT, 'GetState', []))
							
							PIMMDevice = ctypes.POINTER(IMMDevice)
							
							class IMMDeviceCollection(comtypes.IUnknown):
								IID_IMMDeviceCollection = comtypes.GUID(
									'{0BD7A1BE-7A1A-44DB-8397-CC5392387B5E}')
								_iid_ = IID_IMMDeviceCollection
							
							PIMMDeviceCollection = ctypes.POINTER(IMMDeviceCollection)
							
							#---------------------------------------------------------
							
							IID_IMMDeviceEnumerator = comtypes.GUID(
								'{A95664D2-9614-4F35-A746-DE8DB63617E6}')
							_iid_ = IID_IMMDeviceEnumerator
							_methods_ = (
								comtypes.COMMETHOD([], ctypes.HRESULT, 'EnumAudioEndpoints',
									(['in'], wintypes.DWORD, 'dataFlow'),
									(['in'], wintypes.DWORD, 'dwStateMask'),
									(['out','retval'], ctypes.POINTER(PIMMDeviceCollection),
									 'ppDevices')),
								comtypes.COMMETHOD([], ctypes.HRESULT, 'GetDefaultAudioEndpoint',
									(['in'], wintypes.DWORD, 'dataFlow'),
									(['in'], wintypes.DWORD, 'role'),
									(['out','retval'], ctypes.POINTER(PIMMDevice), 'ppDevices')))
							@classmethod
							def get_default(cls, dataFlow, role):
								CLSID_MMDeviceEnumerator = comtypes.GUID(
									'{BCDE0395-E52F-467C-8E3D-C4579291692E}')
								enumerator = comtypes.CoCreateInstance(
									CLSID_MMDeviceEnumerator, cls, comtypes.CLSCTX_INPROC_SERVER)
								return enumerator.GetDefaultAudioEndpoint(dataFlow, role)
						
						# EDataFlow
						eRender = 0 # audio rendering stream
						eCapture = 1 # audio capture stream
						eAll = 2 # audio rendering or capture stream
						# ERole
						eConsole = 0 # games, system sounds, and voice commands
						eMultimedia = 1 # music, movies, narration
						eCommunications = 2 # voice communications
						
						endpoint = IMMDeviceEnumerator.get_default(eRender, eMultimedia)
						interface = endpoint.Activate(cls._iid_, comtypes.CLSCTX_INPROC_SERVER)
						return ctypes.cast(interface, ctypes.POINTER(cls))
				
				comtypes.CoInitialize()
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.aev = self.VolumeHandler.IAudioEndpointVolume.method()
				
				dBrange = self.aev.GetVolumeRange()
				self.volumeRange = {
					'levelMinDB': dBrange[0],
					'levelMaxDB': dBrange[1],
					'volumeIncrementDB': dBrange[2]
				}
				
				self.use = '''
				\r Clase: Volume
				\r │ 
				\r │ # Descripción: Permite manipular los eventos del
				\r │ teclado. Permite presionar teclas, mantenerlas
				\r │ cuanto tiempo se desee y soltarla cuando se indique.
				\r │ 
				\r + Ejemplos de uso:
				\r |    
				\r |    utils = Utils()
				\r |    vol = utils.Actions.Volume
				\r |    
				\r |  #Control de Silenciado: --------------------------
				\r |    
				\r |    # Nos mostrara el sistema esta silenciado:
				\r |    print(vol.mute)
				\r |    
				\r |    # Para Silenciar o Desilenciar el sistema:
				\r |    vol.mute = True		# True o False
				\r |    
				\r |  #Control de nivel de Volumen: --------------------
				\r |    
				\r |    # Para ver el volumen maestro actual de 0~100:
				\r |    print(vol.volume)
				\r |    
				\r |    # Para poner un nuevo nivel de volumen maestro
				\r |    # puedes usar los siguientes valores:
				\r |    vol.volume = 72      # Entero:   entre 0 y 100
				\r |    vol.volume = 0.72    # Flotante: entre 0 y 1
				\r |    
				\r |  #Ver el Rango de Volumen en Decibeles (dB): ------
				\r |    
				\r |    # Muestra los valores minimos y maximos en dB:
				\r |    print(vol.volumeRange)
				\r |    # Ejemplo de lo permitido por el sistema:
				\r |    #{
				\r |    #  'levelMinDB':        -65.25,
				\r |    #  'levelMaxDB':        0.0,
				\r |    #  'volumeIncrementDB': 0.03125
				\r |    #}
				\r |    # podemos notar que va de -65.25 a 0.0
				\r |    
				\r |  #Control de nivel de Volumen en decibeles (dB): --
				\r |    
				\r |    # Para ver el volumen maestro actual de valores
				\r |    # en decibeles (ver vol.volumeRange):
				\r |    print(vol.volumedB)
				\r |    
				\r |    # Para poner un nuevo nivel de volumen maestro
				\r |    # en decibeles (ver vol.volumeRange):
				\r |    vol.volumeDB = -5   # Entero o Flotante negativo
				\r |    
				\r |  #Control de nivel de Volumen en Saltos:
				\r |    
				\r |    # Para ver la información de posición actual,
				\r |    # mínima y máxima:
				\r |    print(vol.volumeStepInfo)
				\r |    # Ejemplo:
				\r |    #{
				\r |    #  'currentSteps': 36,    # Equivale a 72 de 100
				\r |    #  'minSteps':     0,
				\r |    #  'maxSteps':     50
				\r |    #}
				\r |    
				\r |    # Para subir el volumen un paso a la vez:
				\r |    vol.volumeStepUp()
				\r |    
				\r |    # Para bajar el volumen un paso a la vez:
				\r |    vol.volumeStepDown()
				\r |    
				\r |  #Ver Informacion de disponibilidad del sistema: --
				\r |    
				\r |    print(vol.hardwareSupport)
				\r |    
				\r |    # Obtiene una la lista del hardware soportado
				\r |    # Con los siguientes posibles valores:
				\r |    # [
				\r |    #   'Volume Control',
				\r |    #   'Mute Control',
				\r |    #   'Peak Meter'
				\r |    # ]
				\r |    # Si Volume Control esta presente, será posible
				\r |    # utilizar los controladores de volumen.
				\r |    # Si Mute Control esta presente, será posible
				\r |    # utilizar los controladores de muteo.
				\r |    # Si no esta presente alguno, al querer usar las
				\r |    # funciones dirá que el sistema no lo permite.
				\r |    
				\r |  #Control del los Canales de volumen: --------------
				\r |    # Como ejemplo: Las bocinas izquierda y derecha
				\r |    # de una laptop sería los canales 1 y 2.
				\r |    
				\r |    # Para ver la cantidad de canales disponibles:
				\r |    print(vol.getChannelCount())    # Ejemplo: 2
				\r |    
				\r |    # Para mostrar el volumen del Canal 1 y 2 con
				\r |    # valores de '0~100' 
				\r |    print(vol.getChannelVol())	  # Canal 1: 100
				\r |    print(vol.getChannelVol(2))	  # Canal 2: 100
				\r |    
				\r |    # Para cambiar los niveles de volumen de los
				\r |    # canales por separado:
				\r |    vol.setChannelVol(10)         # Canal 1: 10.
				\r |    vol.setChannelVol(75, 2)      # Canal 2: 75.
				\r |    
				\r |    # El volumen master adoptara la posicion del
				\r |    # canal con mayor volumen, en este caso el 2.
				\r |    
				\r |    print(vol.volume)    # 75.
				\r |    
				\r |    # Si cambiamos el volumen, por ejemplo, de nuevo
				\r |    # a 100 los canales seguiran desfazados.
				\r |    
				\r |    # La solución a este problema es:
				\r |    
				\r |    vol.balanceVolChannels()
				\r |    
				\r |    # Esto balancea el volumen en todos los canales
				\r |    # de audio al nivel de volumen mas alto entre
				\r |    # los canales (en este caso en 75).
				\r |    
				\r |  #Control de los Canales de Volumen en dB: --------
				\r |    
				\r |    # Podemos hacer lo mismo pero con decibeles
				\r |    print(vol.getChannelVoldB())  # Canal 1: 0.0
				\r |    print(vol.getChannelVoldB(2)) # Canal 2: 0.0
				\r |    
				\r |    # -65.25 en este caso equivale al 0% de volumen.
				\r |    # 0.0 equivale al 100% de volumen.
				\r |    # Para ver estos valores vease vol.volumeRange.
				\r |    
				\r |    # Para poner el volumen en decibeles con los
				\r |    # mínimo y máximo visto en vol.volumeRange:
				\r |    vol.setChannelVoldB(-33)   # Equivale a 10%
				\r |    vol.setChannelVoldB(-5, 2) # Equivale a 72%
				\r |    
				\r |    # Igualmente para equilibrar los canales:
				\r |    vol.balanceVolChannels()
				\r \\    
				'''
			
			@property
			def volumeStepInfo(self):
				vsi = self.aev.GetVolumeStepInfo()
				info = {
					'currentSteps': vsi[0],
					'minSteps': 0,
					'maxSteps': vsi[1]-1
				}
				return info 
			
			@property
			def hardwareSupport(self):
				out = []
				value = self.aev.QueryHardwareSupport()
				hardware = {
					1: 'Volume Control',
					2: 'Mute Control',
					4: 'Peak Meter'
				}
				for i in sorted(hardware.keys())[::-1]:
					if i <= value:
						hwi = hardware[i]
						out.append(hwi)
						value -= i
				return out[::-1]
			
			# print(Volume.volume)		# Muestra el nivel de volumen
			@property
			def volume(self) -> int:
				if 'Volume Control' in self.hardwareSupport:
					vol = self.aev.GetMasterVolumeLevelScalar()
					vol = round(vol*100)
					return vol
				else:
					msg = 'El Control de Volumen no es compatible en tu sistema.'
					raise self.VolumeControlIsNotSupported(msg)
			
			# Volume.volume = 100		# Valores de '0~100' o de '0~1'
			@volume.setter
			def volume(self, vol: [int, float]):
				if 'Volume Control' in self.hardwareSupport:
					if   vol < 0:   vol = 0
					elif vol > 100: vol = 100
					elif vol.__class__ == float and 0 <= vol <= 1:
						vol = round(vol*100)
					else:
						vol = round(vol)
					self.aev.SetMasterVolumeLevelScalar(vol/100)
				else:
					msg = 'El Control de Volumen no es compatible en tu sistema.'
					raise self.VolumeControlIsNotSupported(msg)
			
			# print(Volume.volumedB)	# Muestra el nivel de volumen en Decibeles (dB)
			# Ver Volume.volumeRange para saber el valor minimo y maximo de decibeles (dB) permitidos en tu sistema.
			@property
			def volumedB(self) -> float:
				if 'Volume Control' in self.hardwareSupport:
					dB = self.aev.GetMasterVolumeLevel()
					return round(dB, 2)
				else:
					msg = 'El Control de Volumen no es compatible en tu sistema.'
					raise self.VolumeControlIsNotSupported(msg)
			
			# Volume.volumedB = -5		# Muestra el nivel de volumen en Decibeles (dB)
			# Ver Volume.volumeRange para saber el valor minimo y maximo de decibeles (dB) permitidos en tu sistema.
			@volumedB.setter
			def volumedB(self, dB: float):
				if 'Volume Control' in self.hardwareSupport:
					dB = round(dB, 4)
					dBrange = self.volumeRange
					dBmin = dBrange['levelMinDB']
					dBmax = dBrange['levelMaxDB']
					if   dB < dBmin: dB = dBmin
					elif dB > dBmax: dB = dBmax
					self.aev.SetMasterVolumeLevel(dB)
				else:
					msg = 'El Control de Volumen no es compatible en tu sistema.'
					raise self.VolumeControlIsNotSupported(msg)
			
			# print(Volume.mute)		# Muestra si esta mute o no.
			@property
			def mute(self) -> bool:
				if 'Mute Control' in self.hardwareSupport:
					mute = self.aev.GetMute()
					if mute == 0: return False
					else: return True
				else:
					msg = 'El Control de Silenciado (Mute) no es compatible en tu sistema.'
					raise self.MuteControlIsNotSupported(msg)
			
			# Volume.mute = True		# Valores 'True' o 'False' solamente
			@mute.setter
			def mute(self, mute: bool):
				if 'Mute Control' in self.hardwareSupport:
					self.aev.SetMute(mute)
				else:
					msg = 'El Control de Silenciado (Mute) no es compatible en tu sistema.'
					raise self.MuteControlIsNotSupported(msg)
			
			def getChannelCount(self):
				return self.aev.GetChannelCount()
			
			def getChannelVol(self, ch=1):
				if 'Volume Control' in self.hardwareSupport:
					ch_c = self.getChannelCount()
					if 0 < ch <= ch_c:
						vol = self.aev.GetChannelVolumeLevelScalar(ch-1)
						vol = round(vol*100)
						return vol
					else:
						msg = 'El Canal {} no existe. '.format(ch)
						msg += 'El Sistema solo dispone de {} Canales.'.format(ch_c)
						raise self.ChannelDoesNotExists(msg)
				else:
					msg = 'El Control de Volumen no es compatible en tu sistema.'
					raise self.VolumeControlIsNotSupported(msg)
			
			def setChannelVol(self, vol=72, ch=1):
				if 'Volume Control' in self.hardwareSupport:
					ch_c = self.getChannelCount()
					if 0 < ch <= ch_c:
						if   vol < 0:   vol = 0
						elif vol > 100: vol = 100
						elif vol.__class__ == float and 0 <= vol <= 1:
							vol = round(vol*100)
						else:
							vol = round(vol)
						self.aev.SetChannelVolumeLevelScalar(ch-1, vol/100)
					else:
						msg = 'El Canal {} no existe. '.format(ch)
						msg += 'El Sistema solo dispone de {} Canales.'.format(ch_c)
						raise self.ChannelDoesNotExists(msg)
				else:
					msg = 'El Control de Volumen no es compatible en tu sistema.'
					raise self.VolumeControlIsNotSupported(msg)
			
			def getChannelVoldB(self, ch=1):
				if 'Volume Control' in self.hardwareSupport:
					ch_c = self.getChannelCount()
					if 0 < ch <= ch_c:
						dB = self.aev.GetChannelVolumeLevel(ch-1)
						return round(dB, 2)
					else:
						msg = 'El Canal {} no existe. '.format(ch)
						msg += 'El Sistema solo dispone de {} Canales.'.format(ch_c)
						raise self.ChannelDoesNotExists(msg)
				else:
					msg = 'El Control de Volumen no es compatible en tu sistema.'
					raise self.VolumeControlIsNotSupported(msg)
			
			def setChannelVoldB(self, dB=-5, ch=1):
				if 'Volume Control' in self.hardwareSupport:
					ch_c = self.getChannelCount()
					if 0 < ch <= ch_c:
						dB = round(dB, 4)
						dBrange = self.volumeRange
						dBmin = dBrange['levelMinDB']
						dBmax = dBrange['levelMaxDB']
						if   dB < dBmin: dB = dBmin
						elif dB > dBmax: dB = dBmax
						self.aev.SetChannelVolumeLevel(ch-1, dB)
					else:
						msg = 'El Canal {} no existe. '.format(ch)
						msg += 'El Sistema solo dispone de {} Canales.'.format(ch_c)
						raise self.ChannelDoesNotExists(msg)
				else:
					msg = 'El Control de Volumen no es compatible en tu sistema.'
					raise self.VolumeControlIsNotSupported(msg)
			
			def balanceVolChannels(self):
				ch_max_vol = 0
				chs = self.getChannelCount()
				for ch in range(1, chs+1):
					ch_vol = self.getChannelVol(ch)
					if ch_vol > ch_max_vol:
						ch_max_vol = ch_vol
				for ch in range(1, chs+1):
					self.setChannelVol(ch_max_vol, ch)
			
			def volumeStepUp(self):
				self.aev.VolumeStepUp()
			
			def volumeStepDown(self):
				self.aev.VolumeStepDown()
		
		#---------------------------------------------------------------
		
		@property
		def use(self):
			self.load_uses(1)	# Indenta para mostrar en el use general
			use = '''\
			\r Clase: Actions
			\r |
			\r + Lista de usos:
			\r |  
			\r |  utils = Utils()
			\r |  
			\r |  print(utils.Actions.Clipboard.use)
			\r |  ...
			\r |  
			\r |  print(utils.Actions.Explorer.use)
			\r |  ...
			\r |  
			\r |  print(utils.Actions.VBS.use)
			\r |  ...
			\r |  
			\r |  print(utils.Actions.beep_use)
			\r |  
			\r {0}
			\r |  
			\r |  print(utils.Actions.changePasswordCurrentUser_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.cleanRecyclerBin_use)
			\r |  
			\r {1}
			\r |  
			\r |  print(utils.Actions.displaySwitch_use)
			\r |  
			\r {2}
			\r |  
			\r |  print(utils.Actions.exitWindows_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.getPrivileges_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.getProcessPrivileges_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.hideConsole_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.hideCursor_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.killProcess_use)
			\r |  
			\r {3}
			\r |  
			\r |  print(utils.Actions.lockWorkStation_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.messageBox_use)
			\r |  
			\r {4}
			\r |     # For more details use: print(utils.Actions.messageBox_params_use)
			\r |  
			\r |  print(utils.Actions.minimizeWindowCMD_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.screenshot_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.setCursorPos_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.setTopWindow_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.setPriorityPID_use)
			\r |  
			\r ... #Pendiente
			\r |  
			\r |  print(utils.Actions.startApp_use)
			\r |  
			\r {5}
			\r |  
			\r \\\
			'''.format(
				self.beep_use,
				self.cleanRecyclerBin_use,
				self.displaySwitch_use,
				self.killProcess_use,
				self.messageBox_use,
				self.startApp_use
			)
			self.load_uses()	# Vuelve a la normalidad
			return use
		
		def load_uses(self, indent=0):
			pipe = '|    '*indent
			self.beep_use = '''\
			\r {0}Función: beep(tone=5, time=0.5)
			\r {0}|
			\r {0}| Permite generar un sonido de 'beep' por tono y tiempo.
			\r {0}| Nota: Es recomendable NO usar con volumen demasiado alto,
			\r {0}|       podría lastimar los oidos con tonos de 7+.
			\r {0}|
			\r {0}+ Ejemplo de uso:
			\r {0}|    
			\r {0}|    utils = Utils()
			\r {0}|    utils.Actions.VBS.setVolume(32) # Recomendable bajar el volumen.
			\r {0}|    utils.Actions.beep(  6, .5)
			\r {0}|    utils.Actions.beep(5.5, .5)
			\r {0}|    utils.Actions.beep(  6, .5)
			\r {0}|    utils.Actions.beep(5.5, .5)
			\r {0}|    utils.Actions.beep(  5, .5)
			\r {0}\\\
			'''.format(pipe)
			self.cleanRecyclerBin_use = '''\
			\r {0}Función: cleanRecyclerBin(tipo=0, unidad='C:')
			\r {0}|
			\r {0}| Vacia la papelera de reciclaje.
			\r {0}|
			\r {0}+ Tipos de niveles:
			\r {0}|  -------------------------------------------------------------
			\r {0}| | 0 = NORMAL              | 4 = SIN_SONIDO                    |
			\r {0}| | 1 = SIN_CONFIRMACION    | 5 = 4 + 1                         |
			\r {0}| | 2 = SIN_BARRA_PROGRESO  | 6 = 4 + 2                         |
			\r {0}| | 3 = 2 + 1               | 7 = 4 + 2 + 1 = TOTAL_INADVERTIDO |
			\r {0}|  -------------------------------------------------------------
			\r {0}|
			\r {0}+ Ejemplo de uso:
			\r {0}|
			\r {0}|    utils = Utils()
			\r {0}|    # Vaciará la papelera en modo silencioso
			\r {0}|    # Totalmente inadvertido.
			\r {0}|    utils.Actions.cleanRecyclerBin(tipo=7)
			\r {0}\\\
			'''.format(pipe)
			self.displaySwitch_use = '''\
			\r {0}Función: displaySwitch(tipo=0)
			\r {0}|
			\r {0}| Cambia el estilo de pantalla.
			\r {0}|
			\r {0}+ Tipos de cambios:
			\r {0}|  --------------------------------------
			\r {0}| | 0 = internal: Solo pantalla de PC.   |
			\r {0}| | 1 = clone:    Duplicado.             |
			\r {0}| | 2 = extend:   Ampliar.               |
			\r {0}| | 3 = external: Solo segunda pantalla. |
			\r {0}|  --------------------------------------
			\r {0}|
			\r {0}+ Ejemplo de uso:
			\r {0}|
			\r {0}|    utils = Utils()
			\r {0}|    utils.Actions.displaySwitch(2)
			\r {0}\\\
			'''.format(pipe)
			self.killProcess_use = '''\
			\r {0}Función: killProcess(PID)
			\r {0}|
			\r {0}| Termina un proceso utilizando su Process ID.
			\r {0}|
			\r {0}+ Ejemplo de uso:
			\r {0}|
			\r {0}|    utils = Utils()
			\r {0}|
			\r {0}|    # Busca todas las coincidencias con 'notepad':
			\r {0}|    procs = utils.SystemInfo.enumProcess('notepad')
			\r {0}|    for p in procs: print(p)
			\r {0}|
			\r {0}|    # Si solo hubo una coincidencia obtenemos
			\r {0}|    # su ProcessID y terminamos el proceso:
			\r {0}|    if len(procs) == 1:
			\r {0}|        proc = procs.pop()
			\r {0}|        utils.Actions.killProcess(proc['pid'])
			\r {0}\\\
			'''.format(pipe)
			self.messageBox_use = '''\
			\r {0}Función: messageBox(message, title,
			\r {0}|	style = WC.MB_OKCANCEL | WC.MB_ICONINFORMATION | WC.MB_DEFAULT_DESKTOP_ONLY
			\r {0}|    )
			\r {0}|
			\r {0}| Muestra una pequeña ventana con un mensaje.
			\r {0}|
			\r {0}+ Ejemplo de uso:
			\r {0}|    
			\r {0}|    utils = Utils()
			\r {0}|    resp = utils.Actions.messageBox(
			\r {0}|        message = 'Esta función te resulta muy útil?',
			\r {0}|        title = 'Es útil?',
			\r {0}|        style = WC.MB_YESNO | WC.MB_ICONQUESTION
			\r {0}|                | WC.MB_DEFAULT_DESKTOP_ONLY
			\r {0}|                | WC.MB_CANCELTRYCONTINUE
			\r {0}|    )
			\r {0}|    print(resp)
			\r {0}\\\
			'''.format(pipe)
			self.messageBox_params_use = '''
			\r    # URL Ref 1: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messagebox
			\r    # URL Ref 2: http://timgolden.me.uk/pywin32-docs/win32api__MessageBox_meth.html
			\r
			\r    # Botones en Tipo de ventana:
			\r    WC.MB_OK                = 0: Aceptar
			\r    WC.MB_OKCANCEL          = 1: Aceptar - Cancelar
			\r    WC.MB_ABORTRETRYIGNORE  = 2: Anular - Reintentar - Omitir		
			\r    WC.MB_YESNOCANCEL       = 3: Sí - No - Cancelar
			\r    WC.MB_YESNO             = 4: Sí - No
			\r    WC.MB_RETRYCANCEL       = 5: Reintantar - Cancelar
			\r    WC.MB_CANCELTRYCONTINUE = 6: Cancelar - Reintentar - Continuar
			\r    # MB_CANCELTRYCONTINUE Es una constante no definida en WC de forma natural...
			\r
			\r    # Iconos:
			\r    16: Wrong (Red Circle and X)
			\r        WC.MB_ICONSTOP
			\r        WC.MB_ICONERROR
			\r        WC.MB_ICONHAND
			\r    32: Question (Blue Circle)
			\r        WC.MB_ICONQUESTION
			\r    48: Exclamation (Yellow Triangle)
			\r        WC.MB_ICONWARNING
			\r        WC.MB_ICONEXCLAMATION
			\r    64: Information (Blue Circle)
			\r        WC.MB_ICONINFORMATION
			\r        MB_ICONASTERISK
			\r
			\r    # Botón seleccionado por defecto:
			\r    WC.MB_DEFBUTTON1 = 0			# Selecciona por defecto el boton 1
			\r    WC.MB_DEFBUTTON2 = 256		# Selecciona por defecto el boton 2
			\r    WC.MB_DEFBUTTON3 = 512		# Selecciona por defecto el boton 3
			\r    WC.MB_DEFBUTTON4 = 768		# Selecciona por defecto el boton 4
			\r
			\r    # Estilos de ventana:
			\r    WC.MB_APPLMODAL   = 0
			\r    WC.MB_SYSTEMMODAL = 4096
			\r    WC.MB_TASKMODAL   = 8192
			\r
			\r    WC.MB_HELP                 = 16384	# Aceptar - Ayuda (No Funciona el botón Ayuda)
			\r    WC.MB_NOFOCUS              = 32768	# No selecciona la ventana.
			\r
			\r    WC.MB_SETFOREGROUND        = 65536
			\r    WC.MB_DEFAULT_DESKTOP_ONLY = 131072
			\r    WC.MB_TOPMOST              = 262144
			\r    WC.MB_RIGHT                = 524288
			\r    WC.MB_RTLREADING           = 1048576
			\r    WC.MB_SERVICE_NOTIFICATION = 2097152
			\r
			\r    WC.MB_TYPEMASK = 15
			\r    WC.MB_USERICON = 128
			\r    WC.MB_ICONMASK = 240
			\r    WC.MB_DEFMASK  = 3840
			\r    WC.MB_MODEMASK = 12288
			\r    WC.MB_MISCMASK = 49152
			'''
			self.startApp_use = '''\
			\r {0}Función: startApp(name='notepad')
			\r {0}|
			\r {0}| Inicia una aplicación.
			\r {0}| Consultar lista de aplicaciones en el sistema:
			\r {0}| Lista: función pendiente... #Pendiente
			\r {0}|
			\r {0}+ Ejemplo de uso:
			\r {0}|    
			\r {0}|    utils = Utils()
			\r {0}|    utils.Actions.startApp('Notepad')
			\r {0}|    utils.Actions.startApp('Calc')
			\r {0}|    utils.Actions.startApp('Cmd')
			\r {0}\\\
			'''.format(pipe)
		
		def beep(self, tone=5, time=0.5):
			if 1 <= tone <= 10:
				if .1 <= time <= 10: WA.Beep(int(tone*100), int(time*1000))
				else: raise self.BeepError('\n\n\t Duración Seleccionada: {} segundos\n\n\t Rango Valido de Duración: 0.1 a 10 segundos'.format(time))
			else: raise self.BeepError('\n\n\t Tonalidad Seleccionada: {}\n\n\t Rango Valido de Tono: 1 a 10'.format(tone))
		
		def changePasswordCurrentUser(self, oldPwd, newPwd):			# Cambia la contraseña del usuario actual.
			WN.NetUserChangePassword(None, None, oldPwd, newPwd)
		
		def cleanRecyclerBin(self, tipo=0, unidad='C:'): #Use			# int tipo, str unidad. Permite vaciar la papelera de reciclaje, incluso de forma completamente silenciosa
			unidad = unidad.upper()
			if re.search('^[A-Z]{1}:$', str(unidad)) == None:
				return False
			if tipo >= 0 and tipo <= 7:
				try:
					shell.SHEmptyRecycleBin(None, unidad, tipo)
				except pywintypes.com_error:
					raise self.EmptyingTheTrashError('La papelera ya esta vacia.')
		
		def not_closeCMD(self):												# [X] Cierra la consola de comandos
			WCS.FreeConsole()
		
		def displaySwitch(self, tipo=0): #Use							# Cambia la pantalla Solo Primera, Pantalla Duplicada, Extendida o Solo Segunda.
			if not 0 <= tipo <= 3: tipo = 0
			tipos = ['/internal', '/clone', '/extend', '/external']
			cmd = 'displayswitch.exe ' + tipos[tipo]
			# ~ print(cmd)
			self.run_command(cmd)
		
		def exitWindows(self, type_output):								# LogOff = Cierre Total de Sesión, Cierra Todas Las Aplicaciones.
			
			TS = str(type_output).lower()
			
			if   TS == 'logoff'   or TS == '0': WA.ExitWindowsEx(WC.EWX_LOGOFF,   0)	# EWX_LOGOFF	= 0
			elif TS == 'shutdown' or TS == '1':
				self.run_command('shutdown -s -t 0')					# Permisos NO necesarios.
				# ~ WA.ExitWindowsEx(WC.EWX_SHUTDOWN, 0)	# EWX_SHUTDOWN	= 1		Permisos necesarios.
			elif TS == 'reboot'   or TS == '2':
				self.run_command('shutdown -r -t 0')					# Permisos NO necesarios.
				# ~ WA.ExitWindowsEx(WC.EWX_REBOOT,   0)	# EWX_REBOOT	= 2		Permisos necesarios.
			else:
				text =  '\n\n [!] El Tipo de Salida de Windows {} No Es Valido.'.format(repr(TS))
				text += "\n\n [+] Tipos de Salida Validas:\n\n\t 0: 'LogOff'.\n\t 1: 'ShutDown'.\n\t 2: 'ReBoot'."
				raise self.ExitWindowsError(text)
		
		def getActiveWindow(self):										# Obtiene el proceso de la ventana activa
			hWndList = []
			hWndChildList = []
			WG.EnumWindows(lambda hWnd, param: param.append((hWnd, WG.GetWindowText(hWnd), WG.GetClassName(hWnd))), hWndList)
			activeWin = WG.GetWindowText(WG.GetForegroundWindow()) 
			for hwnd, title, classname in hWndList: 
				if title == activeWin:
					# ~ WG.EnumChildWindows(hwnd, lambda hWnd, param: param.append((hWnd, WG.GetWindowText(hWnd), WG.GetClassName(hWnd))), hWndChildList)
					# ~ print(hWndChildList)
					# ~ if hWndChildList:
						# ~ for h in hWndChildList:
							# ~ hWndChildList2 = []
							# ~ WG.EnumChildWindows(h[0], lambda hWnd, param: param.append((hWnd, WG.GetWindowText(hWnd), WG.GetClassName(hWnd))), hWndChildList2)
							# ~ print(hWndChildList2)
					return hwnd
		
		def getNameActiveWindow(self):									# Obtiene el nombre de la ventana activa
			return WG.GetWindowText(WG.GetForegroundWindow())
		
		def getPathFromWinExplorer(self):								# Obtiene la ruta actual del explorador de archivos abierto
			shell = WCM.client.Dispatch("Shell.Application")
			for win in shell.Windows():
				if win.Name == 'Explorador de archivos':
					return (win.LocationURL, win.LocationName, win.ReadyState)
		
		def getPrivileges(self): # IMPORTANTE: Ver el ejemplo de uso.	# Corre de nuevo el programa pero obteniendo permisos de administrador.
			'''
			# if not utils.SystemInfo.isUserAnAdmin: ...
			# Sin esto, el código caera en un bucle de iniciar ventanas
			# con privilegios, ya que se abre a si mismo.
			
			# Ejemplo de uso:
				utils = Utils()
				if not utils.SystemInfo.isUserAnAdmin:
					utils.Actions.getPrivileges()
					sys.exit()
				# todo el demás código aquí ...
			'''
			ctypes.windll.shell32.ShellExecuteW(
				None,
				'runas',
				sys.executable,
				' '.join(sys.argv),
				None,
				1
			)
		
		def getProcessPrivileges(self, PID):							# Devuelve una cadena con los privilegios del proceso.
			'''
			# Ejemplo de uso:
				utils = Utils()
				pid = utils.MemoryInfo.pid
				priv = utils.Actions.getProcessPrivileges(pid)
				print(priv)
			'''
			try:
				# obtain a handle to the target process
				HProc = WA.OpenProcess(WC.PROCESS_QUERY_INFORMATION, False, PID)	# PROCESS_QUERY_INFORMATION = 1024 # (0x0400) or PROCESS_VM_READ (0x0010) or PROCESS_ALL_ACCESS (0x1F0FFF)
				# open the main process token
				HTok = WS.OpenProcessToken(HProc, WC.TOKEN_QUERY)					# TOKEN_QUERY = 8
				# retrieve the list of privileges enabled
				privs = WS.GetTokenInformation(HTok, WS.TokenPrivileges)			# TokenPrivileges = 3
				# iterate over privileges and output the ones that are enabled
				privlist = ''
				
				for inf in privs:
					# check if the privilege is enabled
					if inf[1] == 3: privlist += '{}|'.format(WS.LookupPrivilegeName(None, inf[0]))
				privlist = privlist[:-1]
				
			except: privlist = 'N/A'
			
			return privlist
		
		def getWindowRect(self, hwnd):									# Obtiene las dimensiones y posicion de la ventana
			rect = WG.GetWindowRect(hwnd)
			x, y = rect[:2]
			w = rect[2] - x
			h = rect[3] - y
			return (x, y, w, h)
		
		def hideConsole(self, xD=True):									# Oculta/Desoculta la consola de comandos
			WG.ShowWindow(WCS.GetConsoleWindow(), not xD)
		
		def hideCursor(self, visible=False):							# Oculta/Desoculta el cursor en pantalla.
			
			linux_hide_cursor = '\033[?25l'
			linux_show_cursor = '\033[?25h'
			
			if os.name == 'nt':
				import msvcrt
				import ctypes

				class _CursorInfo(ctypes.Structure):
					_fields_ = [("size", ctypes.c_int),
								("visible", ctypes.c_byte)]
			
			def hide_cursor():
				if os.name == 'nt':
					ci = _CursorInfo()
					handle = ctypes.windll.kernel32.GetStdHandle(-11)
					ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
					ci.visible = False
					ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
				elif os.name == 'posix':
					sys.stdout.write(linux_hide_cursor)
					sys.stdout.flush()

			def show_cursor():
				if os.name == 'nt':
					ci = _CursorInfo()
					handle = ctypes.windll.kernel32.GetStdHandle(-11)
					ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
					ci.visible = True
					ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
				elif os.name == 'posix':
					sys.stdout.write(linux_show_cursor)
					sys.stdout.flush()
			
				
			if visible: hide_cursor()
			else: show_cursor()
		
		def hideWindow(self, hide=True, hwnd=WG.GetForegroundWindow()):	# Oculta/Desoculta la consola de comandos
			WG.ShowWindow(hwnd, not hide)
		
		def killProcess(self, PID): #Use								# Termina un proceso mediante su PID
			if PID != None:
				return (0 != WA.TerminateProcess(WA.OpenProcess(1, 0, int(PID)), 0))
		
		def lockWorkStation(self):										# Bloquea la sesión (Como Win+L)
			#~ run_command('rundll32.exe user32.dll, LockWorkStation')
			ctypes.windll.user32.LockWorkStation()
		
		def messageBox(
				self, message, title,
				style = WC.MB_OKCANCEL
					| WC.MB_ICONINFORMATION
					| WC.MB_DEFAULT_DESKTOP_ONLY
			):
			#Use # Crea una ventana de alerta personalizada y captura la interacción con esta devolviendo la respuesta.
			
			if not 0 <= style%16 <= 6:
				raise self.StyleOfWindowError('Estilo de ventana fuera del rango:  0 <= style%16 <= 6')
			
			resp = WA.MessageBox(0, message, title, style)
			
			type_resp = {
				 10: 'Reintentar', 11: 'Continuar',
				 0: 'Error',  1: 'Aceptar',    2: 'Cancelar',
				 3: 'Anular', 4: 'Reintentar', 5: 'Omitir',
				 6: 'Sí', 7: 'No'
			}
			
			if resp in type_resp:
				return type_resp[resp]
			else:
				return resp
		
		def minimizeWindowCMD(self):									# Minimiza la consola de comandos
			WG.ShowWindow(WG.GetForegroundWindow(), WC.SW_MINIMIZE)
		
		def runAsAdmin(self, show=True, cmd_line=None):					# Abre Una Nueva Ventana Con Permisos De Administrador.
			import traceback, types
			if self.SystemInfo.isUserAnAdmin == False:
				# http://pt.stackoverflow.com/questions/6929/como-rodar-um-subprocess-com-permiss%C3%A3o-de-administrador
				if not self.SystemInfo.isWindows:
					return False
				if cmd_line is None:
					cmd_line = [sys.executable] + sys.argv
				elif cmd_line.__class__.__name__ not in ['list', 'tuple']:
					return False
				#================================================================================================================================
				# Método 1: Abrirá Una Ventana Con Permisos De Administrador
				#           y La Ventana Anterior Continuará La Ejecución Normal Sin Detenerse.
				# Ventana Con Permisos De Admin.
				#procHandle = WA.ShellExecute(
				#	0, 'runas',
				#	'"{}"'.format(cmd_line[0],),							# file
				#	' '.join(['"{}"'.format(x,) for x in cmd_line[1:]]),	# params
				#	'',														# cmd_dir
				#	WC.SW_SHOWNORMAL if show else WC.SW_HIDE
				#)
				#================================================================================================================================
				# ShellExecute() no parece que nos permita obtener el PID o manejar el proceso,
				# por lo que no podemos obtener nada útil de él. Por lo tanto,
				# el más complejo ShellExecuteEx() debe ser utilizado.
				#================================================================================================================================
				# Método 2: Abrira Una Ventana Con Permisos De Administrador
				#           y Pausará La Ventana Anterior Hasta Que Se Cierre La Ventana
				#           Nueva Que Tiene Ya Permisos De Administrador.
				# Ventana Con Permisos De Admin.
				procInfo = shell.ShellExecuteEx(
					nShow  = WC.SW_SHOWNORMAL if show else WC.SW_HIDE,
					fMask  = shellcon.SEE_MASK_NOCLOSEPROCESS,
					lpVerb = 'runas',
					lpFile = '"{}"'.format(cmd_line[0],),
					lpParameters = ' '.join(['"{}"'.format(x,) for x in cmd_line[1:]])
				)
				#================================================================================================================================
				return False
			else: return True
		
		def runProgram(self, program=''):								# Abre Una Nueva Ventana Para Ejecutar Otro Script.
			# http://pt.stackoverflow.com/questions/6929/como-rodar-um-subprocess-com-permiss%C3%A3o-de-administrador
			import traceback, types
			#procInfo = shell.ShellExecuteEx(nShow=WC.SW_SHOWNORMAL, fMask=shellcon.SEE_MASK_NOCLOSEPROCESS, lpVerb='', lpFile=program, lpParameters='')
			procHandle = WA.ShellExecute(0, '', program, '', '', WC.SW_SHOWNORMAL)
		
		def screenshot(self, open_ss=False):							# Toma una captura de pantalla.
			
			screen = mss.mss()
			screen.shot()
			screen_name = 'monitor-1.png'
			
			# Valida el nombre y ruta de guardado para la captura:
			if not os.path.exists('Screenshots'):
				os.mkdir('Screenshots')
			
			data = 0
			scree_new_name = 'Screenshots\\Screenshot_{}.jpg'.format(str(data).zfill(3))
			
			if os.path.isfile(screen_name):
				while os.path.isfile(scree_new_name):
					# ~ print(os.path.isfile(scree_new_name))
					data += 1
					scree_new_name = 'Screenshots\\Screenshot_{}.jpg'.format(str(data).zfill(3))
				os.rename(screen_name, scree_new_name)
			else:
				pass
		
		def setConsoleSize(self, chars=82, lines=55):					# Cambia el tamaño de la consola de comandos por cantidad de caracteres por ancho y cantidad de lineas por alto
			os.system("mode con: cols={} lines={}".format(chars, lines))
		
		def setCursorPos(self, posX, posY):								# Posiciona el cursor en (X, Y)
			WA.SetCursorPos((posX, posY))
		
		def setTopMostConsole(self, topMost=True):						# Coloca al frente la consola de comandos y la fija.
			hwnd = WCS.GetConsoleWindow()
			if topMost:
				WG.SetWindowPos(hwnd, WC.HWND_TOPMOST, *self.getWindowRect(hwnd), 0)
			else:
				WG.SetWindowPos(hwnd, WC.HWND_NOTOPMOST, *self.getWindowRect(hwnd), 0)
		
		def setTopMostWindow(self, topMost=True, hwnd=WG.GetForegroundWindow()):	# Coloca al frente la ventana seleccionada y la fija. Se puede pasar el hwnd para seleccionar una ventana especifica.
			if topMost:
				WG.SetWindowPos(hwnd, WC.HWND_TOPMOST, *self.getWindowRect(hwnd), 0)
			else:
				WG.SetWindowPos(hwnd, WC.HWND_NOTOPMOST, *self.getWindowRect(hwnd), 0)
		
		def not_setTopMostWindowName(targetTitle=''):
			hWndList = []
			WG.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)  
			for hwnd in hWndList:
				clsname = WG.GetClassName(hwnd)
				title = WG.GetWindowText(hwnd)
				print(clsname, [title], ' <--- Here!' if title.endswith('cmd.exe') else '')
				if (title.find(targetTitle) >= 0): #Adjust the target window to coordinates (600,300), the size is set to (600,600)
					WG.SetWindowPos(hwnd, WC.HWND_TOPMOST, 600,300,600,600, WC.SWP_SHOWWINDOW)
		
		def setTopConsole(self):										# Coloca al frente la consola de comandos.
			hwnd   = WCS.GetConsoleWindow()
			title  = WG.GetWindowText(hwnd)
			PyCWnd = WU.FindWindow(None, title)
			PyCWnd.SetForegroundWindow()
			PyCWnd.SetFocus()
		
		def setTopWindow(self, proc_name='Administrador de tareas'):	# Coloca al frente una ventana, la busca por nombre.
			
			def aux(HWND,info):
				
				if WG.IsWindowVisible(HWND) and WG.GetWindowText(HWND) != '':
					info.append((HWND, WG.GetWindowText(HWND)))
			
			info = []
			WG.EnumWindows(aux, info)
			
			for inf in info:
				print(inf)
				if proc_name in inf[1]:
					PyCWnd1 = WU.FindWindow(None, inf[1])
					PyCWnd1.SetForegroundWindow()
					PyCWnd1.SetFocus()
					return True
		
		def not_setDisplayRotation(self, monitor=0):						#[X] Rota la Pantalla 180 graods en el monitor seleccionado.
			# monitor:
			# 0 = Monitor Principal
			# 1 = Segundo Monitor
			display = self.display1_orientation if monitor == 0 else self.display2_orientation
			
			device = WA.EnumDisplayDevices(None, monitor);
			fullName = device.DeviceString
			name = device.DeviceName
			dm = WA.EnumDisplaySettings(name, WC.ENUM_CURRENT_SETTINGS)
			# WC.DMDO_DEFAULT=0, WC.DMDO_90=1, WC.DMDO_180=2, WC.DMDO_270=3
			
			dm.DisplayOrientation = 0 if display == 2 else 2
			if   monitor == 0: self.display1_orientation = dm.DisplayOrientation
			elif monitor == 1: self.display2_orientation = dm.DisplayOrientation
			dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
			dm.Fields = dm.Fields & WC.DM_DISPLAYORIENTATION
			WA.ChangeDisplaySettingsEx(name, dm)
		
		def not_setDisplaySettings(self, xres=None, yres=None, cdepth=32):	#[X] Cambia la resolución.
			"""Changes the display resolution and bit depth on Windows.
			
			From Shane Holloway's post http://aspn.activestate.com/ASPN/Mail/Message/wxPython-users/1684800"""
			
			DM_BITSPERPEL		= 0x00040000
			DM_PELSWIDTH		= 0x00080000
			DM_PELSHEIGHT		= 0x00100000
			CDS_UPDATEREGISTRY	= 0x00000001
			CDS_FULLSCREEN		= 0x00000004
			SIZEOF_DEVMODE		= 148
			
			DevModeData = struct.calcsize("32BHH") * '\x00'.encode()
			DevModeData += struct.pack("H", SIZEOF_DEVMODE)
			DevModeData += struct.calcsize("H") * '\x00'.encode()
			dwFields = (xres and DM_PELSWIDTH or 0) | (yres and DM_PELSHEIGHT or 0) | (cdepth and DM_BITSPERPEL or 0)
			DevModeData += struct.pack("L", dwFields)
			DevModeData += struct.calcsize("l9h32BHL") * '\x00'.encode()
			DevModeData += struct.pack("LLL", cdepth or 0, xres or 0, yres or 0)
			DevModeData += struct.calcsize("8L") * '\x00'.encode()
			result = ctypes.windll.user32.ChangeDisplaySettingsA(DevModeData, CDS_FULLSCREEN | CDS_UPDATEREGISTRY)
			if result != 0: # success if zero, some failure otherwise
				raise WinDesktopError("setDisplaySettings() died, call to ChangeDisplaySettingsA returned" + repr(result))
		
		def setPriorityPID(self, PID=None, priority=1):
			
			""" Setea La Prioridad de un Proceso de Windows.
				El Valor de Prioridad se da entre 0-5 en donde 2 es la Prioridad Normal.
				Pro Defecto se pondra la Prioridad en 1 en el Actual Proceso de Python."""
			
			priorityclasses = [WP.IDLE_PRIORITY_CLASS,
							   WP.BELOW_NORMAL_PRIORITY_CLASS,
							   WP.NORMAL_PRIORITY_CLASS,
							   WP.ABOVE_NORMAL_PRIORITY_CLASS,
							   WP.HIGH_PRIORITY_CLASS,
							   WP.REALTIME_PRIORITY_CLASS]
			
			if PID == None: PID = WA.GetCurrentProcessId()
			
			handle = WA.OpenProcess(WC.PROCESS_ALL_ACCESS, True, PID)
			WP.SetPriorityClass(handle, priorityclasses[priority])
		
		def startApp(self, name='notepad'): #Use						# Abre una aplicación por nombre, ejemplo Notepad (Bloc de notas), Calc (Calculadora), cmd, etc.
			WA.WinExec(name)
	
	class EditRegistry:	# Interacciones con el Registro de Windows (RegEdit)
		# Las Modificaciónes Requieren Permisos de Administrador.
		# Por ejemplo las funciones: enable, disable, show, hide y cleanUp.
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			# Clases Internas:
			self.DropBox = self.DropBox()
			self.Explorer = self.Explorer()
			self.FoldersOnThisPC = self.FoldersOnThisPC()
			self.OneDrive = self.OneDrive()
			self.PhysicalDrivesInWinExplorer = self.PhysicalDrivesInWinExplorer()
			self.Programs = self.Programs()
			self.PowerPlan = self.PowerPlan()
			self.TaskManager = self.TaskManager()
		
		class DropBox:
			# DropBox: {E31EA727-12ED-4702-820C-4B6445F28E1A}
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY  = WR.HKEY_CLASSES_ROOT
				self.PATH  = r'CLSID\{E31EA727-12ED-4702-820C-4B6445F28E1A}'
				self.VALUE   = 'System.IsPinnedToNameSpaceTree'
				self.TRUE  = 0x00000001
				self.FALSE = 0x00000000
				
				self.use = '''
				\r Clase: DropBox
				\r |
				\r + Ejemplo de uso: Requieren Permisos de administrador.
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para ocultar el acceso a la ruta de DropBox (Si se tiene instalado)
				\r |    # que aparece del lado izquierdo en el explorador de archivos:
				\r |    utils.EditRegistry.DropBox.disable()
				\r |    
				\r |    # Para mostrar el acceso a la ruta de DropBox (Si se tiene instalado)
				\r |    # que aparece del lado izquierdo en el explorador de archivos:
				\r |    utils.EditRegistry.DropBox.enable()
				\r \\
				'''
			
			def _keyExists(self):
				try:
					reg = WR.OpenKeyEx(self.HKEY, self.PATH)
					value = WR.QueryValueEx(reg, self.VALUE)[0]
					WR.CloseKey(reg)
					return True, value
				except:
					return False, None
			
			# [HKEY_CLASSES_ROOT\CLSID\{E31EA727-12ED-4702-820C-4B6445F28E1A}]
			# "System.IsPinnedToNameSpaceTree"=dword:00000001
			def enable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo habilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
				elif key_exists and not isDisabled:												# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
			
			# [HKEY_CLASSES_ROOT\CLSID\{E31EA727-12ED-4702-820C-4B6445F28E1A}]
			# "System.IsPinnedToNameSpaceTree"=dword:00000000
			def disable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
				elif key_exists and isDisabled:													# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
		
		class Explorer:
			
			def __init__(self):
				''' Oculta o Desoculta las páginas que se indiquen,
				por ejemplo el contenido en la ventana de
				"Programas y características".'''
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY = WR.HKEY_CURRENT_USER
				self.PATH = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer'
				self.SHOW = 0
				self.HIDE = 1
				
				# Valores para esta ruta:
				self.controlPanel       = 'NoControlPanel'
				self.viewContextMenu    = 'NoViewContextMenu'
				self.clock              = 'HideClock'
				self.SCAHealthVal       = 'HideSCAHealth'
				self.SCANetworkVal      = 'HideSCANetwork'
				self.SCAPowerVal        = 'HideSCAPower'
				self.SCAVolumeVal       = 'HideSCAVolume'
				self.activeDesktop      = 'NoActiveDesktop'
				self.autoTrayNotify     = 'NoAutoTrayNotify'
				self.drivesInSendToMenu = 'NoDrivesInSendToMenu'
				self.favoritesMenu      = 'NoFavoritesMenu'
				self.internetOpenWith   = 'NoInternetOpenWith'
				self.recentDocsMenu     = 'NoRecentDocsMenu'
				self.run                = 'NoRun'
				self.saveSettings       = 'NoSaveSettings'
				self.trayItemsDisplay   = 'NoTrayItemsDisplay'
				self.classicShell       = 'ClassicShell'
				#self.activeDesktopChanges = 'NoActiveDesktopChanges'
				self.propertiesRecycleBin = 'NoPropertiesRecycleBin'
				self.close              = 'NoClose'
				# Modificadas:
				self.windowMinimizingShortcuts = 'NoWindowMinimizingShortcuts'
				
				# Clases Internas:
				self.ControlPanel       = self.ControlPanel(self)
				self.ContextMenu        = self.ContextMenu(self)
				self.Clock              = self.Clock(self)
				self.SCAHealth          = self.SCAHealth(self)
				self.SCANetwork         = self.SCANetwork(self)
				self.SCAPower           = self.SCAPower(self)
				self.SCAVolume          = self.SCAVolume(self)
				self.ActiveDesktop      = self.ActiveDesktop(self)
				self.AutoTrayNotify     = self.AutoTrayNotify(self)
				self.DrivesInSendToMenu = self.DrivesInSendToMenu(self)
				self.FavoritesMenu      = self.FavoritesMenu(self)
				self.InternetOpenWith   = self.InternetOpenWith(self)
				self.RecentDocsMenu     = self.RecentDocsMenu(self)
				self.Run                = self.Run(self)
				self.SaveSettings       = self.SaveSettings(self)
				self.TrayItemsDisplay   = self.TrayItemsDisplay(self)
				self.ClassicShell       = self.ClassicShell(self)
				#self.ActiveDesktopChanges = self.ActiveDesktopChanges(self)
				self.PropertiesRecycleBin = self.PropertiesRecycleBin(self)
				self.Close              = self.Close(self)
				# Modificadas:
				self.WindowMinimizingShortcuts = self.WindowMinimizingShortcuts(self)
				
				self.enumValues = [
					'ControlPanel',
					'ContextMenu',
					'Clock',
					'SCAHealth',
					'SCANetwork',
					'SCAPower',
					'SCAVolume',
					'ActiveDesktop',
					'AutoTrayNotify',
					'DrivesInSendToMenu',
					'FavoritesMenu',
					'InternetOpenWith',
					'RecentDocsMenu',
					'Run',
					'SaveSettings',
					'TrayItemsDisplay',
					'ClassicShell',
					#'ActiveDesktopChanges',
					'PropertiesRecycleBin',
					'Close'
				]
				
				self.use = '''
				\r Clase: Explorer
				\r |
				\r + Ejemplo de uso: Requieren Permisos de administrador.
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para ver los valores que estan disponibles para
				\r |    # ocultar o desocultar:
				\r |    print(utils.EditRegistry.Explorer.enumValues)
				\r |    
				\r |    # Para ocultar el 'Panel de Control':
				\r |    utils.EditRegistry.Explorer.ControlPanel.hide()
				\r |    
				\r |    # Para desocultar el 'Panel de Control':
				\r |    utils.EditRegistry.Explorer.ControlPanel.show()
				\r |    
				\r |    # Es posible utilizar las funciones enable() en
				\r |    # lugar de show() y disable() en lugar de hide()
				\r |    
				\r |    # Para deshacer el cambio realizados en el registro
				\r |    # dejando el valor por defecto del windows:
				\r |    utils.EditRegistry.Explorer.ControlPanel.cleanUp()
				\r |    
				\r |    # Para ver su descripción y características:
				\r |    print(utils.EditRegistry.Explorer.ControlPanel.description)
				\r |    
				\r |    # Se puede aplicar lo mismo que con 'ControlPanel' (Panel
				\r |    # de Control) para cualquier otro valor mostrado en enumValues
				\r |    
				\r |    # Requiere reiniciar el explroador de archivos para aplicar
				\r |    # cambios. Se puede utilizar el siguiente comando desde la
				\r |    # consola de comandos (cmd):
				\r |    #     taskkill /F /IM explorer.exe & start explorer.exe
				\r \\
				'''
			
			def _keyExists(self, VALUE):
				try:
					reg = WR.OpenKeyEx(self.HKEY, self.PATH)
					value = WR.QueryValueEx(reg, VALUE)[0]
					WR.CloseKey(reg)
					return True, value
				except:
					return False, None
			
			def _show(self, VALUE):
				key_exists, isHidden = self._keyExists(VALUE)										# Intenta abrir el key y extraer su valor.
				if not key_exists:																	# Si no existe el key, lo crea y lo habilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, VALUE, 0,  WR.REG_DWORD, self.SHOW)
					WR.CloseKey(reg)
				elif key_exists and isHidden:														# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, VALUE, 0,  WR.REG_DWORD, self.SHOW)
					WR.CloseKey(reg)
			
			def _hide(self, VALUE):
				key_exists, isHidden = self._keyExists(VALUE)										# Intenta abrir el key y extraer su valor.
				if not key_exists:																	# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, VALUE, 0,  WR.REG_DWORD, self.HIDE)
					WR.CloseKey(reg)
				elif key_exists and not isHidden:													# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, VALUE, 0,  WR.REG_DWORD, self.HIDE)
					WR.CloseKey(reg)
			
			def _cleanUp(self, VALUE):
				key_exists, isHidden = self._keyExists(VALUE)
				if key_exists:
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.DeleteValue(reg, VALUE)
					WR.CloseKey(reg)
			
			class Close:
			
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoClose"=dword:00000000
				def show(self): self.parent._show(self.parent.close)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoClose"=dword:00000001
				def hide(self): self.parent._hide(self.parent.close)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoClose"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.close)
			
			class PropertiesRecycleBin:
			
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Quitar Propiedades del menú contextual de
					\r Papelera de reciclaje:
					\r  
					\r  Quita la opción Propiedades del menú contextual
					\r  de Papelera de reciclaje.
					\r  
					\r  Si habilita esta opción, la opción Propiedades
					\r  no aparecerá cuando el usuario haga clic con el botón secundario en Papelera de reciclaje o abra la Papelera de reciclaje y luego haga clic en Archivo. Asimismo, Alt+Entrar no realizará ninguna acción cuando Papelera de reciclaje esté seleccionado.
					\r  
					\r  Si deshabilita esta opción o no la configura, el
					\r  elemento Propiedades se mostrará con normalidad.
					\r  
					\r  URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsDesktop::NoRecycleBinProperties&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoPropertiesRecycleBin"=dword:00000000
				def show(self): self.parent._show(self.parent.propertiesRecycleBin)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoPropertiesRecycleBin"=dword:00000001
				def hide(self): self.parent._hide(self.parent.propertiesRecycleBin)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoPropertiesRecycleBin"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.propertiesRecycleBin)
			
			class WindowMinimizingShortcuts:
			
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Desactivar el gesto del mouse de minimización de
					\r ventanas:
					\r  
					\r  Impide que las ventanas se minimicen o restauren
					\r  cuando se agite la ventana activa hacia delante
					\r  y hacia atrás.
					\r  
					\r  Si habilita esta directiva, no se minimizarán ni
					\r  restaurarán las ventanas de aplicaciones cuando
					\r  se agite la ventana activa hacia delante y hacia
					\r  atrás con el mouse.
					\r  
					\r  Si deshabilita o no configura esta directiva, se
					\r  aplicará el gesto de minimización y restauración
					\r  de ventanas.
					\r  
					\r  URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.WindowsDesktop::NoWindowMinimizingShortcuts&Language=es-es#
					'''
					
					self.parent = parent
					self.PATH = r'SOFTWARE\Policies\Microsoft\Windows\Explorer'
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer]
				# "NoWindowMinimizingShortcuts"=dword:00000000
				def show(self): self.parent._show(self.parent.windowMinimizingShortcuts)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer]
				# "NoWindowMinimizingShortcuts"=dword:00000001
				def hide(self): self.parent._hide(self.parent.windowMinimizingShortcuts)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer]
				# "NoWindowMinimizingShortcuts"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.windowMinimizingShortcuts)
			
			class ControlPanel:
			
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Prohibir el acceso a Configuración de PC y a
					\r Panel de control:
					\r 
					\r  Deshabilita todos los programas del Panel de control y la
					\r  aplicación Configuración de PC.
					\r  
					\r  Esta configuración impide que se ejecuten Control.exe
					\r  y SystemSettings.exe, que son los archivos de programa
					\r  de Panel de control y Configuración de PC. En consecuencia,
					\r  los usuarios no pueden iniciar el Panel de control ni
					\r  Configuración de PC, ni ejecutar ninguno de sus elementos.
					\r  
					\r  Esta configuración quita el Panel de control de:
					\r  La pantalla Inicio
					\r  Explorador de archivos
					\r  
					\r  Esta configuración quita Configuración de PC de:
					\r  La pantalla Inicio
					\r  Acceso a Configuración
					\r  Imagen de cuenta
					\r  Resultados de búsqueda
					\r  
					\r  Si los usuarios intentan seleccionar un elemento del
					\r  Panel de control desde el elemento Propiedades en un
					\r  menú contextual, aparece un mensaje que explica que
					\r  existe una configuración que impide la acción.
					\r  
					\r  URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.ControlPanel::NoControlPanel&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoControlPanel"=dword:00000000
				def show(self): self.parent._show(self.parent.controlPanel)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoControlPanel"=dword:00000001
				def hide(self): self.parent._hide(self.parent.controlPanel)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoControlPanel"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.controlPanel)
			
			class ContextMenu:
			
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Deshabilita el menú contextual en el explorador
					\r de Windows.
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
					
					self.use = '''
					\r Clase: ContextMenu
					\r |
					\r + Ejemplo de uso: Requieren Permisos de administrador.
					\r |    
					\r |    utils = Utils()
					\r |    
					\r |    # Para deshabilitar el uso de el Menu Contextual (dar clic derecho):
					\r |    utils.EditRegistry.Explorer.ContextMenu.hide()
					\r |    
					\r |    # Para habilitar el uso de el Menu Contextual (dar clic derecho):
					\r |    utils.EditRegistry.Explorer.ContextMenu.show()
					\r |    
					\r |    # Para eliminar los cambios realizados en el registro:
					\r |    utils.EditRegistry.Explorer.ContextMenu.cleanUp()
					\r \\
					'''
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoViewContextMenu"=dword:00000000
				def show(self): self.parent._show(self.parent.viewContextMenu)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoViewContextMenu"=dword:00000001
				def hide(self): self.parent._hide(self.parent.viewContextMenu)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoViewContextMenu"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.viewContextMenu)
			
			class Clock:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Oculta el reloj de la barra de tareas
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideClock"=dword:00000000
				def show(self): self.parent._show(self.parent.clock)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideClock"=dword:00000001
				def hide(self): self.parent._hide(self.parent.clock)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideClock"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.clock)
			
			class SCAHealth:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Oculta el estado de x de la barra de tareas
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAHealth"=dword:00000000
				def show(self): self.parent._show(self.parent.SCAHealthVal)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAHealth"=dword:00000001
				def hide(self): self.parent._hide(self.parent.SCAHealthVal)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAHealth"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.SCAHealthVal)
			
			class SCANetwork:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Oculta el estado de red de la barra de tareas
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCANetwork"=dword:00000000
				def show(self): self.parent._show(self.parent.SCANetworkVal)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCANetwork"=dword:00000001
				def hide(self): self.parent._hide(self.parent.SCANetworkVal)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCANetwork"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.SCANetworkVal)
			
			class SCAPower:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Oculta el estado de la batería de la barra de tareas
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAPower"=dword:00000000
				def show(self): self.parent._show(self.parent.SCAPowerVal)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAPower"=dword:00000001
				def hide(self): self.parent._hide(self.parent.SCAPowerVal)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAPower"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.SCAPowerVal)
			
			class SCAVolume:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Oculta el estado del volumen de la barra de tareas
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAVolume"=dword:00000000
				def show(self): self.parent._show(self.parent.SCAVolumeVal)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAVolume"=dword:00000001
				def hide(self): self.parent._hide(self.parent.SCAVolumeVal)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "HideSCAVolume"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.SCAVolumeVal)
			
			class ActiveDesktop:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoActiveDesktop"=dword:00000000
				def show(self): self.parent._show(self.parent.activeDesktop)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoActiveDesktop"=dword:00000001
				def hide(self): self.parent._hide(self.parent.activeDesktop)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoActiveDesktop"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.activeDesktop)
			
			class AutoTrayNotify:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoAutoTrayNotify"=dword:00000000
				def show(self): self.parent._show(self.parent.autoTrayNotify)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoAutoTrayNotify"=dword:00000001
				def hide(self): self.parent._hide(self.parent.autoTrayNotify)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoAutoTrayNotify"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.autoTrayNotify)
			
			class DrivesInSendToMenu:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoDrivesInSendToMenu"=dword:00000000
				def show(self): self.parent._show(self.parent.drivesInSendToMenu)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoDrivesInSendToMenu"=dword:00000001
				def hide(self): self.parent._hide(self.parent.drivesInSendToMenu)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoDrivesInSendToMenu"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.drivesInSendToMenu)
			
			class FavoritesMenu:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoFavoritesMenu"=dword:00000000
				def show(self): self.parent._show(self.parent.favoritesMenu)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoFavoritesMenu"=dword:00000001
				def hide(self): self.parent._hide(self.parent.favoritesMenu)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoFavoritesMenu"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.favoritesMenu)
			
			class InternetOpenWith:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoInternetOpenWith"=dword:00000000
				def show(self): self.parent._show(self.parent.internetOpenWith)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoInternetOpenWith"=dword:00000001
				def hide(self): self.parent._hide(self.parent.internetOpenWith)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoInternetOpenWith"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.internetOpenWith)
			
			class RecentDocsMenu:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoRecentDocsMenu"=dword:00000000
				def show(self): self.parent._show(self.parent.recentDocsMenu)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoRecentDocsMenu"=dword:00000001
				def hide(self): self.parent._hide(self.parent.recentDocsMenu)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoRecentDocsMenu"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.recentDocsMenu)
			
			class Run:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r Deshabilita la ventana de 'Ejecutar...' (Win+R)
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoRun"=dword:00000000
				def show(self): self.parent._show(self.parent.run)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoRun"=dword:00000001
				def hide(self): self.parent._hide(self.parent.run)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoRun"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.run)
			
			class SaveSettings:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoSaveSettings"=dword:00000000
				def show(self): self.parent._show(self.parent.saveSettings)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoSaveSettings"=dword:00000001
				def hide(self): self.parent._hide(self.parent.saveSettings)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoSaveSettings"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.saveSettings)
			
			class TrayItemsDisplay:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoTrayItemsDisplay"=dword:00000000
				def show(self): self.parent._show(self.parent.trayItemsDisplay)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoTrayItemsDisplay"=dword:00000001
				def hide(self): self.parent._hide(self.parent.trayItemsDisplay)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "NoTrayItemsDisplay"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.trayItemsDisplay)
			
			class ClassicShell:
				
				def __init__(self, parent):
					
					self.classes   = ObjectClassNames(self)
					self.functions = None
					self.functions = ObjectFunctionNames(self)
					
					self.description = '''
					\r 
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "ClassicShell"=dword:00000000
				def show(self): self.parent._show(self.parent.classicShell)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "ClassicShell"=dword:00000001
				def hide(self): self.parent._hide(self.parent.classicShell)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
				# "ClassicShell"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.classicShell)
		
		class FoldersOnThisPC:
			
			def __init__(self):
				''' Oculta o Desoculta las carpetas que se muestran en
					la parte izquierda del explorador de archivos en la
					sección de "Este Equipo".'''
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY  = WR.HKEY_LOCAL_MACHINE
				self.PATH  = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions'
				self.VALUE = 'ThisPCPolicy'
				self.SHOW  = 'Show'
				self.HIDE  = 'Hide'
				
				# CLSID of Folders on "This PC":
				self.f3DObjects = r'\{31C0DD25-9439-4F12-BF41-7FF4EDA38722}'
				self.fDesktop   = r'\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}'
				self.fDocuments = r'\{f42ee2d3-909f-4907-8871-4c22fc0bf756}'
				self.fDownloads = r'\{7d83ee9b-2244-4e70-b1f5-5393042af1e4}'
				self.fMusic     = r'\{a0c69a99-21c8-4671-8703-7934162fcf1d}'
				self.fPictures  = r'\{0ddd015d-b06c-45d5-8c4c-f59713854639}'
				self.fVideos    = r'\{35286a68-3c57-41a1-bbb1-0eae73d76c95}'
				
				# Clases Internas:
				self.Folder3DObjects = self.Folder3DObjects(self)
				self.FolderDesktop   = self.FolderDesktop(self)
				self.FolderDocuments = self.FolderDocuments(self)
				self.FolderDownloads = self.FolderDownloads(self)
				self.FolderMusic     = self.FolderMusic(self)
				self.FolderPictures  = self.FolderPictures(self)
				self.FolderVideos    = self.FolderVideos(self)
				
				self.enumFolders = [
					'Folder3DObjects',
					'FolderDesktop',
					'FolderDocuments',
					'FolderDownloads',
					'FolderMusic',
					'FolderPictures',
					'FolderVideos'
				]
				
				self.use = '''
				\r Clase: FoldersOnThisPC
				\r |
				\r + Ejemplo de uso: Requieren Permisos de administrador.
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para ver las carpetas que estan disponibles para
				\r |    # ocultar o desocultar de el apartado 'Este Equipo'
				\r |    # en la parte izquierda del explorador de archivos:
				\r |    print(utils.EditRegistry.FoldersOnThisPC.enumFolders)
				\r |    
				\r |    # Para ocultar el acceso a la carpeta de 'Objectos 3D':
				\r |    utils.EditRegistry.FoldersOnThisPC.Folder3DObjects.hide()
				\r |    
				\r |    # Para desocultar el acceso a la carpeta de 'Objectos 3D':
				\r |    utils.EditRegistry.FoldersOnThisPC.Folder3DObjects.show()
				\r |    
				\r |    # Se puede aplicar lo mismo que con 'Folder3DObjects' para
				\r |    # cualquier otra carpeta mostrada en enumFolders
				\r |    
				\r |    # Requiere reiniciar el explroador de archivos para aplicar
				\r |    # cambios. Se puede utilizar el siguiente comando desde la
				\r |    # consola de comandos (cmd):
				\r |    #     taskkill /F /IM explorer.exe & start explorer.exe
				\r \\
				'''
			
			def _keyExists(self, PATH, withValue=False):
				try:
					value = None
					reg = WR.OpenKeyEx(self.HKEY, PATH)
					if withValue: value = WR.QueryValueEx(reg, self.VALUE)[0]
					WR.CloseKey(reg)
					if withValue:
						return True, value
					else:
						return True
				except:
					if withValue:
						return False, None
					else:
						return False
			
			def _hide(self, FOLDERPATH, PATH):
				key_exists = self._keyExists(FOLDERPATH, withValue=False)						# Intenta abrir el key.
				if key_exists:
					keyExists, value = self._keyExists(PATH, withValue=True)					# Intenta abrir el key y extraer su valor.
					if not keyExists:																# Si no existe el key, lo crea y lo habilita.
						reg = WR.CreateKey(self.HKEY, PATH)
						WR.SetValueEx(reg, self.VALUE, 0, WR.REG_SZ, self.HIDE)
						WR.CloseKey(reg)
					elif keyExists and value == self.SHOW:												# Si existe el key y esta deshabilitado, lo habilita.
						reg = WR.OpenKey(self.HKEY, PATH, 0, WR.KEY_SET_VALUE)
						WR.SetValueEx(reg, self.VALUE, 0, WR.REG_SZ, self.HIDE)
						WR.CloseKey(reg)
			
			def _show(self, FOLDERPATH, PATH):
				key_exists = self._keyExists(FOLDERPATH, withValue=False)						# Intenta abrir el key.
				if key_exists:
					keyExists, value = self._keyExists(PATH, withValue=True)					# Intenta abrir el key y extraer su valor.
					if not keyExists:
						reg = WR.CreateKey(self.HKEY, PATH)
						WR.SetValueEx(reg, self.VALUE, 0, WR.REG_SZ, self.SHOW)
						WR.CloseKey(reg)
					elif keyExists and value == self.HIDE:												# Si existe el key y esta deshabilitado, lo habilita.
						reg = WR.OpenKey(self.HKEY, PATH, 0, WR.KEY_SET_VALUE)
						WR.SetValueEx(reg, self.VALUE, 0, WR.REG_SZ, self.SHOW)
						WR.CloseKey(reg)
			
			class Folder3DObjects:
				
				def __init__(self, parent):
					self.parent = parent
					self.FOLDERPATH = parent.PATH + parent.f3DObjects			# ...\{31C0DD25-9439-4F12-BF41-7FF4EDA38722}
					self.SUBFOLDERPATH = self.FOLDERPATH + r'\PropertyBag'		# ...\{31C0DD25-9439-4F12-BF41-7FF4EDA38722}\PropertyBag
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{31C0DD25-9439-4F12-BF41-7FF4EDA38722}\PropertyBag]
				# "ThisPCPolicy"="Show"
				def show(self): self.parent._show(self.FOLDERPATH, self.SUBFOLDERPATH)
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{31C0DD25-9439-4F12-BF41-7FF4EDA38722}\PropertyBag]
				# "ThisPCPolicy"="Hide"
				def hide(self): self.parent._hide(self.FOLDERPATH, self.SUBFOLDERPATH)
			
			class FolderDesktop:
				
				def __init__(self, parent):
					self.parent = parent
					self.FOLDERPATH = parent.PATH + parent.fDesktop				# ...\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}
					self.SUBFOLDERPATH = self.FOLDERPATH + r'\PropertyBag'		# ...\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}\PropertyBag
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}\PropertyBag]
				# "ThisPCPolicy"="Show"
				def show(self): self.parent._show(self.FOLDERPATH, self.SUBFOLDERPATH)
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{B4BFCC3A-DB2C-424C-B029-7FE99A87C641}\PropertyBag]
				# "ThisPCPolicy"="Hide"
				def hide(self): self.parent._hide(self.FOLDERPATH, self.SUBFOLDERPATH)
			
			class FolderDocuments:
				
				def __init__(self, parent):
					self.parent = parent
					self.FOLDERPATH = parent.PATH + parent.fDocuments			# ...\{f42ee2d3-909f-4907-8871-4c22fc0bf756}
					self.SUBFOLDERPATH = self.FOLDERPATH + r'\PropertyBag'		# ...\{f42ee2d3-909f-4907-8871-4c22fc0bf756}\PropertyBag
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{f42ee2d3-909f-4907-8871-4c22fc0bf756}\PropertyBag]
				# "ThisPCPolicy"="Show"
				def show(self): self.parent._show(self.FOLDERPATH, self.SUBFOLDERPATH)
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{f42ee2d3-909f-4907-8871-4c22fc0bf756}\PropertyBag]
				# "ThisPCPolicy"="Hide"
				def hide(self): self.parent._hide(self.FOLDERPATH, self.SUBFOLDERPATH)
			
			class FolderDownloads:
				
				def __init__(self, parent):
					self.parent = parent
					self.FOLDERPATH = parent.PATH + parent.fDownloads			# ...\{7d83ee9b-2244-4e70-b1f5-5393042af1e4}
					self.SUBFOLDERPATH = self.FOLDERPATH + r'\PropertyBag'		# ...\{7d83ee9b-2244-4e70-b1f5-5393042af1e4}\PropertyBag
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{7d83ee9b-2244-4e70-b1f5-5393042af1e4}\PropertyBag]
				# "ThisPCPolicy"="Show"
				def show(self): self.parent._show(self.FOLDERPATH, self.SUBFOLDERPATH)
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{7d83ee9b-2244-4e70-b1f5-5393042af1e4}\PropertyBag]
				# "ThisPCPolicy"="Hide"
				def hide(self): self.parent._hide(self.FOLDERPATH, self.SUBFOLDERPATH)
			
			class FolderMusic:
				
				def __init__(self, parent):
					self.parent = parent
					self.FOLDERPATH = parent.PATH + parent.fMusic				# ...\{a0c69a99-21c8-4671-8703-7934162fcf1d}
					self.SUBFOLDERPATH = self.FOLDERPATH + r'\PropertyBag'		# ...\{a0c69a99-21c8-4671-8703-7934162fcf1d}\PropertyBag
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{a0c69a99-21c8-4671-8703-7934162fcf1d}\PropertyBag]
				# "ThisPCPolicy"="Show"
				def show(self): self.parent._show(self.FOLDERPATH, self.SUBFOLDERPATH)
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{a0c69a99-21c8-4671-8703-7934162fcf1d}\PropertyBag]
				# "ThisPCPolicy"="Hide"
				def hide(self): self.parent._hide(self.FOLDERPATH, self.SUBFOLDERPATH)
			
			class FolderPictures:
				
				def __init__(self, parent):
					self.parent = parent
					self.FOLDERPATH = parent.PATH + parent.fPictures			# ...\{0ddd015d-b06c-45d5-8c4c-f59713854639}
					self.SUBFOLDERPATH = self.FOLDERPATH + r'\PropertyBag'		# ...\{0ddd015d-b06c-45d5-8c4c-f59713854639}\PropertyBag
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{0ddd015d-b06c-45d5-8c4c-f59713854639}\PropertyBag]
				# "ThisPCPolicy"="Show"
				def show(self): self.parent._show(self.FOLDERPATH, self.SUBFOLDERPATH)
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{0ddd015d-b06c-45d5-8c4c-f59713854639}\PropertyBag]
				# "ThisPCPolicy"="Hide"
				def hide(self): self.parent._hide(self.FOLDERPATH, self.SUBFOLDERPATH)
			
			class FolderVideos:
				
				def __init__(self, parent):
					self.parent = parent
					self.FOLDERPATH = parent.PATH + parent.fVideos				# ...\{35286a68-3c57-41a1-bbb1-0eae73d76c95}
					self.SUBFOLDERPATH = self.FOLDERPATH + r'\PropertyBag'		# ...\{35286a68-3c57-41a1-bbb1-0eae73d76c95}\PropertyBag
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{35286a68-3c57-41a1-bbb1-0eae73d76c95}\PropertyBag]
				# "ThisPCPolicy"="Show"
				def show(self): self.parent._show(self.FOLDERPATH, self.SUBFOLDERPATH)
				
				# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\FolderDescriptions\{35286a68-3c57-41a1-bbb1-0eae73d76c95}\PropertyBag]
				# "ThisPCPolicy"="Hide"
				def hide(self): self.parent._hide(self.FOLDERPATH, self.SUBFOLDERPATH)
		
		class OneDrive:
			# OneDrive: {018D5C66-4533-4307-9B53-224DE2ED1FE6}
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY  = WR.HKEY_CLASSES_ROOT
				self.PATH  = r'CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}'
				self.VALUE   = 'System.IsPinnedToNameSpaceTree'
				self.TRUE  = 0x00000001
				self.FALSE = 0x00000000
				
				self.use = '''
				\r Clase: OneDrive
				\r |
				\r + Ejemplo de uso: Requieren Permisos de administrador.
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para ocultar el acceso a la ruta de OneDrive (Si se tiene instalado)
				\r |    # que aparece del lado izquierdo en el explorador de archivos:
				\r |    utils.EditRegistry.OneDrive.disable()
				\r |    
				\r |    # Para mostrar el acceso a la ruta de OneDrive (Si se tiene instalado)
				\r |    # que aparece del lado izquierdo en el explorador de archivos:
				\r |    utils.EditRegistry.OneDrive.enable()
				\r \\
				'''
			
			def _keyExists(self):
				try:
					reg = WR.OpenKeyEx(self.HKEY, self.PATH)
					value = WR.QueryValueEx(reg, self.VALUE)[0]
					WR.CloseKey(reg)
					return True, value
				except:
					return False, None
			
			# [HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}]
			# "System.IsPinnedToNameSpaceTree"=dword:00000001
			def enable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo habilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
				elif key_exists and not isDisabled:												# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
			
			# [HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}]
			# "System.IsPinnedToNameSpaceTree"=dword:00000000
			def disable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
				elif key_exists and isDisabled:													# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
		
		class PhysicalDrivesInWinExplorer:
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				# ~ self.LETTERS = {
					# ~ 'A': 0x01000000, 'B': 0x02000000, 'C': 0x04000000, 'D': 0x08000000,
					# ~ 'E': 0x10000000, 'F': 0x20000000, 'G': 0x40000000, 'H': 0x80000000,
					# ~ 'I': 0x00010000, 'J': 0x00020000, 'K': 0x00040000, 'L': 0x00080000,
					# ~ 'M': 0x00100000, 'N': 0x00200000, 'O': 0x00400000, 'P': 0x00800000,
					# ~ 'Q': 0x00000100, 'R': 0x00000200, 'S': 0x00000400, 'T': 0x00000800,
					# ~ 'U': 0x00001000, 'V': 0x00002000, 'W': 0x00004000, 'X': 0x00008000,
					# ~ 'Y': 0x00000001, 'Z': 0x00000002
				# ~ }
				
				self.LETTERS = {
					'A': 0x01000000, 'E': 0x10000000, 'I': 0x00010000, 'M': 0x00100000, 'Q': 0x00000100, 'U': 0x00001000, 'Y': 0x00000001,
					'B': 0x02000000, 'F': 0x20000000, 'J': 0x00020000, 'N': 0x00200000, 'R': 0x00000200, 'V': 0x00002000, 'Z': 0x00000002,
					'C': 0x04000000, 'G': 0x40000000, 'K': 0x00040000, 'O': 0x00400000, 'S': 0x00000400, 'W': 0x00004000,
					'D': 0x08000000, 'H': 0x80000000, 'L': 0x00080000, 'P': 0x00800000, 'T': 0x00000800, 'X': 0x00008000
				}
				
				self.HKEY = WR.HKEY_CURRENT_USER
				self.PATH = 'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer'
				self.VALUE = 'NoDrives'
				
				self.use = '''
				\r Clase: PhysicalDrivesInWinExplorer
				\r │
				\r │ # Descripción: Permite ocultar o desocultar los discos físicos
				\r │ que están en el explorador de windows en la parte izquierda en 
				\r │ el apartado de "Este Equipo" indicando la letra o letras de estos.
				\r │
				\r │ # Default params:
				\r │
				\r ├─ enumHiddenDrives()	# No requiere parametros.
				\r │ 
				\r ├─ hide(             # Requiere permisos de administrador.
				\r │      letters		# letters puede ser un caracter de la 'A' a la 'Z' o un conjunto
				\r │  )                 # de ellos (ejemplo: 'ABC', 'A B C' o ['A', 'B', 'C'])
				\r │
				\r ├─ show(             # Requiere permisos de administrador.
				\r │      letters       # letters puede ser un caracter de la 'A' a la 'Z' o un conjunto
				\r │  )                 # de ellos (ejemplo: 'ABC', 'A B C' o ['A', 'B', 'C'])
				\r │
				\r ├─ showAll()         # No requiere parametros.
				\r │
				\r ├─ cleanUp()         # No requiere parametros. Requiere permisos de admin.
				\r |
				\r + Ejemplo de uso:
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para ver las letras de los discos fisicos que estan actualmente ocultos:
				\r |    print(utils.EditRegistry.PhysicalDrivesInWinExplorer.enumHiddenDrives())
				\r |    
				\r |    # Para ocultar uno o varios discos indicamos sus letras:
				\r |    utils.EditRegistry.PhysicalDrivesInWinExplorer.hide('ABCZ')
				\r |    
				\r |    # Para desocultar uno o varios discos indicamos sus letras:
				\r |    utils.EditRegistry.PhysicalDrivesInWinExplorer.show('BZ')
				\r |    
				\r |    # Para desocultar todos los discos:
				\r |    utils.EditRegistry.PhysicalDrivesInWinExplorer.showAll()
				\r |    
				\r |    # Para deshacer los cambios en el registro (desoculta todos):
				\r |    utils.EditRegistry.PhysicalDrivesInWinExplorer.cleanUp()
				\r |    
				\r |    # Requiere reiniciar el explroador de archivos para aplicar
				\r |    # cambios. Se puede utilizar el siguiente comando desde la
				\r |    # consola de comandos (cmd):
				\r |    #     taskkill /F /IM explorer.exe & start explorer.exe
				\r \\
				'''
			
			class DriveLettersError(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			def _keyExists(self):
				try:
					reg = WR.OpenKeyEx(self.HKEY, self.PATH)
					value = WR.QueryValueEx(reg, self.VALUE)[0]
					WR.CloseKey(reg)
					return True, value
				except:
					return False, None
			
			def _int2bytes(self, value):
				value = hex(value)[2:].zfill(8)
				value = [int(value[i*2:(i+1)*2], 16) for i in range(len(value)//2)]
				value = bytes(value)
				return value
			
			def enumHiddenDrives(self):
				
				keyExists, _bytes = self._keyExists()					# Intenta abrir el key y extraer su valor.
				
				if not keyExists: return []
				
				LETTERS_NUMS = {										# Valor a restar (es basado en binario, la suma entre estos representa un valor unico, ejemplo: A=1,B=2,A+B=3,C=4,A+C=5,B+C=6,A+B+C=7,D=8,A+D=9, etc...)
					'A': 1, 'B': 2, 'C': 4, 'D': 8,
					'E': 1, 'F': 2, 'G': 4, 'H': 8,
					'I': 1, 'J': 2, 'K': 4, 'L': 8,
					'M': 1, 'N': 2, 'O': 4, 'P': 8,
					'Q': 1, 'R': 2, 'S': 4, 'T': 8,
					'U': 1, 'V': 2, 'W': 4, 'X': 8,
					'Y': 1, 'Z': 2, ' ': 16
				}
				POS = {													# Posiciones de caracter en la cadena hexadecimal. la cadena consta de 8 caracteres (de 0 al 7)
					1: ['A','B','C','D'],
					0: ['E','F','G','H'],
					3: ['I','J','K','L'],
					2: ['M','N','O','P'],
					5: ['Q','R','S','T'],
					4: ['U','V','W','X'],
					7: ['Y','Z',' ',' '],
					6: [' ',' ',' ',' ']
				}
				value = _bytes.hex()									# Convierte los bytes a hexadecimal
				letters = []
				
				for i, v in enumerate(value):							# i = posicion del caracter hexadecimal extraido. v = el caracter hexadecimal extraido.
					if v == '0': continue								# Si el caracter es 0 entonces se omite
					qty = int(v, 16)									# Convierte a decimal el hexadecimal                # Ejemplo usando i=1 y obteniendo las letras A, B, C y D y el qty de 11 como ejemplo:
					if qty - LETTERS_NUMS[POS[i][3]] >= 0: letters.append(POS[i][3]); qty -= LETTERS_NUMS[POS[i][3]]		# 11 - 8 >= 0:  True.    Se agrega la D. al 10 se le restan los 8 y continuamos con el 2.
					if qty - LETTERS_NUMS[POS[i][2]] >= 0: letters.append(POS[i][2]); qty -= LETTERS_NUMS[POS[i][2]]		#  2 - 4 >= 0: False. No se agrega la C. al  2 no se le resta nada.
					if qty - LETTERS_NUMS[POS[i][1]] >= 0: letters.append(POS[i][1]); qty -= LETTERS_NUMS[POS[i][1]]		#  2 - 2 >= 0:  True.    Se agrega la B. al  2 se le restan los 2 y continuamos con el 0.
					if qty - LETTERS_NUMS[POS[i][0]] >= 0: letters.append(POS[i][0])										#  0 - 2 >= 0: False. No se agrega la A.
																															# El resultado final obtendriamos que las letras B y D si estan en el hexadecimal.
				letters.sort()
				
				return letters
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
			# "NoDrives"=hex:XX,XX,XX,XX 															# Las X representan hexadecimal
			def hide(self, letters):
				
				if not type(letters) in [str, list, tuple, set]:
					raise self.DriveLettersError('Solo se permiten letras de la \'A\' a la \'Z\' o conjunto de letras \'ABC\', \'A B C\' o [\'A\',\'B\',\'C\']')
				
				if type(letters) in [str, list, tuple]:
					letters = set(letters)
					if ' ' in letters: letters.remove(' ')
					if '.' in letters: letters.remove('.')
					if ',' in letters: letters.remove(',')
					if '+' in letters: letters.remove('+')
					if '-' in letters: letters.remove('-')
					if '_' in letters: letters.remove('_')
					
				for letter in letters:
					letter = letter.upper()
					if not letter in self.LETTERS:
						raise self.DriveLettersError('Solo se permiten letras de la \'A\' a la \'Z\' o conjunto de letras \'ABC\', \'A B C\' o [\'A\',\'B\',\'C\']')
				
				value = 0
				for letter in letters:
					letter = letter.upper()
					value += self.LETTERS[letter]
				value = self._int2bytes(value)														# Convierte el entero en bytes
				
				keyExists, hexadecimal = self._keyExists()											# Intenta abrir el key y extraer su valor.
				
				if not keyExists:
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.VALUE, 0, WR.REG_BINARY, value)
					WR.CloseKey(reg)
				elif keyExists:																		# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.VALUE, 0, WR.REG_BINARY, value)
					WR.CloseKey(reg)
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
			# "NoDrives"=hex:XX,XX,XX,XX 															# Las X representan hexadecimal
			def show(self, letters):
				
				res = self.enumHiddenDrives()							# Obtiene la lista de Letras actualmente ocultas
				
				for letter in letters:
					letter = letter.upper()
					if letter in res:
						res.remove(letter)								# Quita la letra de la lista de Letras actualmente ocultas 
				
				self.hide(res)											# Actualiza la lista de letras ocultas
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
			# "NoDrives"=hex:00,00,00,00
			def showAll(self):
				
				keyExists, hexadecimal = self._keyExists()												# Intenta abrir el key y extraer su valor.
				
				if not keyExists:
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.VALUE, 0, WR.REG_BINARY, bytes([0,0,0,0]))
					WR.CloseKey(reg)
				elif keyExists:																		# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.VALUE, 0, WR.REG_BINARY, bytes([0,0,0,0]))
					WR.CloseKey(reg)
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
			# "NoDrives"=-
			def cleanUp(self):
				
				key_exists, _ = self._keyExists()
				
				if key_exists:
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.DeleteValue(reg, self.VALUE)
					WR.CloseKey(reg)
		
		class Programs:
			
			def __init__(self):
				''' Oculta o Desoculta las páginas que se indiquen,
				por ejemplo el contenido en la ventana de
				"Programas y características".'''
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY = WR.HKEY_CURRENT_USER
				self.PATH = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs'
				self.SHOW = 0
				self.HIDE = 1
				
				# Valores para esta ruta:
				self.programsAndFeatures  = 'NoProgramsAndFeatures'
				self.windowsFeatures      = 'NoWindowsFeatures'
				self.windowsMarketplace   = 'NoWindowsMarketplace'
				self.programsControlPanel = 'NoProgramsCPL'
				self.installedUpdates     = 'NoInstalledUpdates'
				self.defaultPrograms      = 'NoDefaultPrograms'
				self.getPrograms          = 'NoGetPrograms'
				
				# Clases Internas:
				self.ProgramsAndFeatures  = self.ProgramsAndFeatures(self)
				self.WindowsFeatures      = self.WindowsFeatures(self)
				self.WindowsMarketplace   = self.WindowsMarketplace(self)
				self.ProgramsControlPanel = self.ProgramsControlPanel(self)
				self.InstalledUpdates     = self.InstalledUpdates(self)
				self.DefaultPrograms      = self.DefaultPrograms(self)
				self.GetPrograms          = self.GetPrograms(self)
				
				self.enumValues = [
					'ProgramsAndFeatures',
					'WindowsFeatures',
					'WindowsMarketplace',
					'ProgramsControlPanel',
					'InstalledUpdates',
					'DefaultPrograms',
					'GetPrograms'
				]
				
				self.use = '''
				\r Clase: Programs
				\r |
				\r + Ejemplo de uso: Requieren Permisos de administrador.
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para ver los valores que estan disponibles para
				\r |    # ocultar o desocultar:
				\r |    print(utils.EditRegistry.Programs.enumValues)
				\r |    
				\r |    # Para ocultar el contenido de 'Programas y características':
				\r |    utils.EditRegistry.Programs.ProgramsAndFeatures.hide()
				\r |    
				\r |    # Para desocultar el contenido de 'Programas y características':
				\r |    utils.EditRegistry.Programs.ProgramsAndFeatures.show()
				\r |    
				\r |    # Para deshacer el cambio realizados en el registro
				\r |    # dejando el valor por defecto del windows:
				\r |    utils.EditRegistry.Programs.ProgramsAndFeatures.cleanUp()
				\r |    
				\r |    # Para ver su descripción y características:
				\r |    print(utils.EditRegistry.Programs.ProgramsAndFeatures.description)
				\r |    
				\r |    # Se puede aplicar lo mismo que con 'ProgramsAndFeatures' (Programas
				\r |    # y características) para cualquier otro valor mostrado en enumValues
				\r |    
				\r |    # Requiere reiniciar el explroador de archivos para aplicar
				\r |    # cambios. Se puede utilizar el siguiente comando desde la
				\r |    # consola de comandos (cmd):
				\r |    #     taskkill /F /IM explorer.exe & start explorer.exe
				\r \\
				'''
			
			def _keyExists(self, VALUE):
				try:
					reg = WR.OpenKeyEx(self.HKEY, self.PATH)
					value = WR.QueryValueEx(reg, VALUE)[0]
					WR.CloseKey(reg)
					return True, value
				except:
					return False, None
			
			def _show(self, VALUE):
				key_exists, isHidden = self._keyExists(VALUE)										# Intenta abrir el key y extraer su valor.
				if not key_exists:																	# Si no existe el key, lo crea y lo habilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, VALUE, 0,  WR.REG_DWORD, self.SHOW)
					WR.CloseKey(reg)
				elif key_exists and isHidden:														# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, VALUE, 0,  WR.REG_DWORD, self.SHOW)
					WR.CloseKey(reg)
			
			def _hide(self, VALUE):
				key_exists, isHidden = self._keyExists(VALUE)										# Intenta abrir el key y extraer su valor.
				if not key_exists:																	# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, VALUE, 0,  WR.REG_DWORD, self.HIDE)
					WR.CloseKey(reg)
				elif key_exists and not isHidden:													# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, VALUE, 0,  WR.REG_DWORD, self.HIDE)
					WR.CloseKey(reg)
			
			def _cleanUp(self, VALUE):
				key_exists, isHidden = self._keyExists(VALUE)
				if key_exists:
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.DeleteValue(reg, VALUE)
					WR.CloseKey(reg)
			
			class ProgramsAndFeatures:
				
				def __init__(self, parent):
					self.description = '''
					\r Ocultar la página "Programas y características":
					\r  
					\r  Esta opción impide a los usuarios obtener acceso a
					\r  "Programas y características" para ver, desinstalar,
					\r  cambiar o reparar programas instalados actualmente
					\r  en el equipo.
					\r  
					\r  Si esta opción está deshabilitada o no está
					\r  configurada, "Programas y características" estará
					\r  disponible para todos los usuarios.
					\r  
					\r  Esta opción no impide que los usuarios usen otros
					\r  métodos y herramientas para ver o desinstalar
					\r  programas. Tampoco impide que los usuarios creen
					\r  vínculos a características relacionadas en el panel
					\r  de control Programas, como Características de
					\r  Windows, Obtener programas o Windows Marketplace.
					\r 
					\r URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.Programs::NoProgramsAndFeatures&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoProgramsAndFeatures"=dword:00000000
				def show(self): self.parent._show(self.parent.programsAndFeatures)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoProgramsAndFeatures"=dword:00000001
				def hide(self): self.parent._hide(self.parent.programsAndFeatures)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoProgramsAndFeatures"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.programsAndFeatures)
			
			class WindowsFeatures:
				
				def __init__(self, parent):
					self.description = '''
					\r Ocultar "Características de Windows":
					\r  
					\r  Esta opción impide a los usuarios obtener acceso
					\r  a la tarea "Activar o desactivar las características
					\r  de Windows" del panel de control Programas de la
					\r  vista por categorías, Programas y características
					\r  de la vista clásica, y Obtener programas. Por
					\r  consiguiente, los usuarios no pueden ver,
					\r  habilitar ni deshabilitar diversas características
					\r  y servicios de Windows.
					\r  
					\r  Si esta opción está deshabilitada o no está
					\r  configurada, la tarea "Activar o desactivar las
					\r  características de Windows" estará disponible
					\r  para todos los usuarios.
					\r  
					\r  Esta opción no impide que los usuarios usen otros
					\r  métodos y herramientas para configurar servicios,
					\r  o bien para habilitar o deshabilitar componentes
					\r  de programa.
					\r  
					\r URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.Programs::NoWindowsFeatures&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoWindowsFeatures"=dword:00000000
				def show(self): self.parent._show(self.parent.windowsFeatures)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoWindowsFeatures"=dword:00000001
				def hide(self): self.parent._hide(self.parent.windowsFeatures)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoWindowsFeatures"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.windowsFeatures)
			
			class WindowsMarketplace:
				
				def __init__(self, parent):
					self.description = '''
					\r Ocultar "Windows Marketplace":
					\r  
					\r  Esta opción impide a los usuarios obtener acceso
					\r  a la tarea "Obtener nuevos programas de Windows
					\r  Marketplace" del panel de control Programas de
					\r  la vista por categorías, Programas y características
					\r  de la vista clásica, y Obtener programas.
					\r  
					\r  Windows Marketplace permite a los usuarios
					\r  comprar o descargar varios programas a su equipo
					\r  para instalarlos.
					\r  
					\r  Habilitar esta característica no impide a los
					\r  usuarios desplazarse hasta Windows Marketplace
					\r  usando otros métodos.
					\r  
					\r  Si esta característica está deshabilitada o no
					\r  está configurada, el vínculo de la tarea "Obtener
					\r  nuevos programas de Windows Marketplace" estará
					\r  disponible para todos los usuarios.
					\r  
					\r  Nota: esta opción se omitirá si "Ocultar el panel
					\r  de control Programas" está habilitada.
					\r  
					\r URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.Programs::NoWindowsMarketplace&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoWindowsMarketplace"=dword:00000000
				def show(self): self.parent._show(self.parent.windowsMarketplace)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoWindowsMarketplace"=dword:00000001
				def hide(self): self.parent._hide(self.parent.windowsMarketplace)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoWindowsMarketplace"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.windowsMarketplace)
			
			class ProgramsControlPanel:
				
				def __init__(self, parent):
					self.description = '''
					\r Ocultar el panel de control Programas:
					\r  
					\r  Esta opción impide a los usuarios usar el panel
					\r  de control Programas de la vista por categorías
					\r  y Programas y características de la vista clásica.
					\r  
					\r  El panel de control Programas permite a los usuarios
					\r  desinstalar, cambiar y reparar programas, habilitar
					\r  y deshabilitar características de Windows,
					\r  establecer los valores predeterminados de los
					\r  programas, ver las actualizaciones instaladas y
					\r  comprar software de Windows Marketplace. Los
					\r  programas publicados o asignados al usuario por
					\r  el administrador del sistema también aparecen en
					\r  el panel de control Programas.
					\r  
					\r  Si esta opción está deshabilitada o no está
					\r  configurada, el panel de control Programas de la
					\r  vista por categorías y Programas y características
					\r  de la vista clásica estarán disponibles para todos
					\r  los usuarios.
					\r  
					\r  Cuando se habilita, esta opción tiene preferencia
					\r  sobre el resto de los valores de esta carpeta.
					\r  
					\r  Esta opción no impide que los usuarios usen otros
					\r  métodos y herramientas para instalar o desinstalar
					\r  programas.
					\r  
					\r URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.Programs::NoProgramsCPL&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoProgramsCPL"=dword:00000000
				def show(self): self.parent._show(self.parent.programsControlPanel)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoProgramsCPL"=dword:00000001
				def hide(self): self.parent._hide(self.parent.programsControlPanel)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoProgramsCPL"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.programsControlPanel)
			
			class InstalledUpdates:
				
				def __init__(self, parent):
					self.description = '''
					\r Ocultar la página "Actualizaciones instaladas":
					\r  
					\r  Esta opción impide a los usuarios obtener acceso
					\r  a la página "Actualizaciones instaladas" desde la
					\r  tarea "Ver actualizaciones instaladas".
					\r  
					\r  "Actualizaciones instaladas" permite a los usuarios
					\r  ver y desinstalar las actualizaciones instaladas
					\r  actualmente en el equipo. Las actualizaciones suelen
					\r  descargarse directamente de Windows Update o de
					\r  varios editores de programas.
					\r  
					\r  Si esta opción está deshabilitada o no está configurada,
					\r  la tarea "Ver actualizaciones instaladas" y la página
					\r  "Actualizaciones instaladas" estarán disponibles para
					\r  todos los usuarios.
					\r  
					\r  Esta opción no impide que los usuarios usen otros
					\r  métodos y herramientas para instalar o desinstalar
					\r  programas.
					\r  
					\r URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.Programs::NoInstalledUpdates&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoInstalledUpdates"=dword:00000000
				def show(self): self.parent._show(self.parent.installedUpdates)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoInstalledUpdates"=dword:00000001
				def hide(self): self.parent._hide(self.parent.installedUpdates)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoInstalledUpdates"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.installedUpdates)
			
			class DefaultPrograms:
				
				def __init__(self, parent):
					self.description = '''
					\r Ocultar la página "Configurar acceso y programas
					\r predeterminados en el equipo":
					\r  
					\r  Esta opción quita la página Configurar acceso y
					\r  programas predeterminados en el equipo del panel
					\r  de control Programas. En consecuencia, los usuarios
					\r  no pueden ver ni cambiar la página asociada.
					\r  
					\r  La página Configurar acceso y programas
					\r  predeterminados en el equipo permite a los
					\r  administradores especificar los programas
					\r  predeterminados para ciertas actividades, como la
					\r  exploración web o el envío de correo electrónico,
					\r  así como especificar los programas a los que se
					\r  tiene acceso desde el menú Inicio, el escritorio
					\r  y otras ubicaciones.
					\r  
					\r  Si esta opción está deshabilitada o no está
					\r  configurada, el botón Configurar acceso y
					\r  programas predeterminados está disponible para
					\r  todos los usuarios.
					\r  
					\r  Esta opción no impide que los usuarios usen otros
					\r  métodos y herramientas para cambiar el acceso o
					\r  las opciones predeterminadas de los programas.
					\r  
					\r  Esta opción no impide que el icono Programas
					\r  predeterminados aparezca en el menú Inicio.
					\r  
					\r URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.Programs::NoDefaultPrograms&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoDefaultPrograms"=dword:00000000
				def show(self): self.parent._show(self.parent.defaultPrograms)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoDefaultPrograms"=dword:00000001
				def hide(self): self.parent._hide(self.parent.defaultPrograms)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoDefaultPrograms"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.defaultPrograms)
			
			class GetPrograms:
				
				def __init__(self, parent):
					self.description = '''
					\r Ocultar la página "Obtener programas":
					\r  
					\r  Impide que los usuarios vean o instalen programas
					\r  publicados desde la red.
					\r  
					\r  Esta opción impide a los usuarios obtener acceso
					\r  a la página "Obtener programas" del panel de
					\r  control Programas de la vista por categorías,
					\r  Programas y características de la vista clásica
					\r  y la tarea "Instalar un programa a partir de la
					\r  red". La página "Obtener programas" incluye los
					\r  programas publicados y ofrece un método sencillo
					\r  para instalarlos.
					\r  
					\r  Los programas publicados son aquellos programas
					\r  que el administrador del sistema ha puesto a
					\r  disposición del usuario explícitamente con una
					\r  herramienta como Windows Installer. Normalmente,
					\r  los administradores del sistema publican programas
					\r  para notificar a los usuarios que están disponibles,
					\r  recomendar su uso o permitirles instalarlos sin
					\r  tener que buscar los archivos de instalación.
					\r  
					\r  Si esta opción está habilitada, los usuarios no
					\r  pueden ver los programas publicados por el
					\r  administrador del sistema, y no pueden usar la
					\r  página "Obtener programas" para instalar programas
					\r  publicados. Habilitar esta característica no impide
					\r  a los usuarios instalar programas usando otros
					\r  métodos. Los usuarios aún pueden ver e instalar
					\r  los programas asignados (parcialmente instalados)
					\r  que se ofrecen en el escritorio o en el menú Inicio.
					\r  
					\r  Si esta opción está deshabilitada o no está
					\r  configurada, la tarea "Instalar un programa a
					\r  partir de la red" de la página "Obtener programas"
					\r  estará disponible para todos los usuarios.
					\r  
					\r  Nota: esta opción se omitirá si "Ocultar el panel
					\r  de control Programas" está habilitada.
					\r  
					\r URL: https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.Programs::NoDefaultPrograms&Language=es-es
					'''
					
					self.parent = parent
					self.enable = self.show
					self.disable = self.hide
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoGetPrograms"=dword:00000000
				def show(self): self.parent._show(self.parent.getPrograms)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoGetPrograms"=dword:00000001
				def hide(self): self.parent._hide(self.parent.getPrograms)
				
				# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Programs]
				# "NoGetPrograms"=-
				def cleanUp(self): self.parent._cleanUp(self.parent.getPrograms)
		
		class PowerPlan:
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY = WR.HKEY_LOCAL_MACHINE
				self.ROOT_PATH = r'SYSTEM\CurrentControlSet\Control\Power\User\PowerSchemes'
				self.BRIGHTNESS_LVL_SUBPATH = r'7516b95f-f776-4464-8c53-06167f40cc99\aded5e82-b909-4619-9949-f5d71dac0bcb'
				self.POWER_SAV_MODE_SUBPATH = r'19cbb8fa-5279-450e-9fac-8a3d5fedd0c1\12bbebe6-58d6-4636-95bb-3217ef867c1a'
				
				self.use = '''
				\r Clase: PowerPlan
				\r │
				\r │ # Default params:
				\r │
				\r ├─ powerSavingMode(      # Para dispositivos con batería.
				\r │      ACDC = 'DC'       # Selecciona entre 'AC' y 'DC'. AC: Conectado. DC: Desconectado.
				\r │  )
				\r │
				\r ├─ setBrightnessLevel(
				\r │      level = 4         # Nivel de brillo. Debe estar entre 0 y 10.
				\r │  )
				\r |
				\r + Ejemplo de uso: 
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para obtener el nivel de brillo actual:
				\r |    print(utils.EditRegistry.PowerPlan.brightnessLevel)
				\r |    
				\r |    # Para obtener el GUID del plan actual de energía:
				\r |    print(utils.EditRegistry.PowerPlan.currentPowerPlanGUID)
				\r |    
				\r |    # Para obtener el Modo de Ahorro de energía:
				\r |    utils.EditRegistry.PowerPlan.powerSavingMode()
				\r |    
				\r |    # Para cambiar el nivel de brillo en la pantalla:
				\r |    utils.EditRegistry.PowerPlan.setBrightnessLevel(5)
				\r \\
				'''
			
			class BrightnessLevelError(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			@property
			def brightnessLevel(self):
				
				PATH = self.ROOT_PATH + '\\' + self.currentPowerPlanGUID + '\\' + self.BRIGHTNESS_SUBPATH
				
				reg = WR.OpenKeyEx(self.HKEY, PATH)
				brightnessValue = WR.QueryValueEx(reg, 'DCSettingIndex')[0]
				WR.CloseKey(reg)
				
				return brightnessValue
			
			@property
			def currentPowerPlanGUID(self):
				# GUID de plan de energía. Se puede obtener desde la cmd con el comando: "powercfg /L"
				reg = WR.OpenKeyEx(self.HKEY, self.ROOT_PATH)
				activePowerScheme = WR.QueryValueEx(reg, 'ActivePowerScheme')[0]
				WR.CloseKey(reg)
				return activePowerScheme
			
			def powerSavingMode(self, ACDC='DC'):
				reg = WR.OpenKeyEx(self.HKEY, self.ROOT_PATH + '\\' + self.currentPowerPlanGUID + '\\' + self.POWER_SAV_MODE_SUBPATH)
				if ACDC.upper() == 'DC':
					value = WR.QueryValueEx(reg, 'DCSettingIndex')[0]
				elif ACDC.upper() == 'AC':
					value = WR.QueryValueEx(reg, 'ACSettingIndex')[0]
				else:
					value = WR.QueryValueEx(reg, 'DCSettingIndex')[0]
				WR.CloseKey(reg)
				if   value == b'\x00\x00\x00\x00': return 'Rendimiento máximo'
				elif value == b'\x01\x00\x00\x00': return 'Ahorro de energía bajo'
				elif value == b'\x02\x00\x00\x00': return 'Ahorro de energía medio'
				elif value == b'\x03\x00\x00\x00': return 'Ahorro de energía máximo'
				else: return None
			
			def setBrightnessLevel(self, value=4):
				if not type(value) == int or not 0 <= value <= 10:
					raise self.BrightnessLevelError('El valor de brillo debe ser entero y estar entre 0 y 10.')
				val = wmi.WMI(namespace='wmi')
				val = val.WmiMonitorBrightnessMethods()[0]
				val.WmiSetBrightness(value*10, 0)
		
		class TaskManager:
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY  = WR.HKEY_CURRENT_USER
				self.PATH  = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
				self.VALUE   = 'DisableTaskMgr'
				self.TRUE  = 0x00000001
				self.FALSE = 0x00000000
				
				self.use = '''
				\r Clase: TaskManager
				\r |
				\r + Ejemplo de uso: Requieren Permisos de administrador.
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para deshabilitar el uso de el Administrador de tareas:
				\r |    utils.EditRegistry.TaskManager.disable()
				\r |    
				\r |    # Para habilitar el uso de el Administrador de tareas:
				\r |    utils.EditRegistry.TaskManager.enable()
				\r |    
				\r |    # Para eliminar los cambios realizados en el registro:
				\r |    utils.EditRegistry.TaskManager.cleanUp()
				\r \\
				'''
			
			def _keyExists(self):
				try:
					reg = WR.OpenKeyEx(self.HKEY, self.PATH)
					value = WR.QueryValueEx(reg, self.VALUE)[0]
					WR.CloseKey(reg)
					return True, value
				except:
					return False, None
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
			# "DisableTaskMgr"=dword:00000000
			def enable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo habilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
				elif key_exists and isDisabled:													# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
			# "DisableTaskMgr"=dword:00000001
			def disable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
				elif key_exists and not isDisabled:												# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.VALUE, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
			# "DisableTaskMgr"=-
			def cleanUp(self):
				key_exists, isDisabled = self._keyExists()
				if key_exists:
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.DeleteValue(reg, self.VALUE)
					WR.CloseKey(reg)
		
	class MemoryInfo:	# Información relacionadas a espacio en disco y demás.
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.pid  = os.getpid()
			self.proc = psutil.Process(self.pid)
			
			# ~ self.proc_dict = self.proc.as_dict()
			self.init_time_raw = self.proc.create_time()
			self.init_time     = datetime.fromtimestamp(self.init_time_raw).strftime('%Y-%m-%d %H:%M:%S')
			
			self.proc_mem_info = self.proc.memory_info()
			self.cpu_percent = psutil.cpu_percent()								# CPU usage percentage
			self.used_memory = self.bytesToString(self.proc_mem_info.rss)		# Used RAM memory
			
			self.memoryStatusUpdate()
		
		def bytesToString(self, nbytes, raw=False):						# Convierte un entero de bytes a formato de cadena en B, KB, MB, GB o TB dependiendo la cantidad, reduciendolo al minimo posible
			
			# ~ if nbytes == 0: return '0 bytes'
			
			# ~ metric = ('bytes', 'KB', 'MB', 'GB', 'TB')
			# ~ nunit = int(math.floor(math.log(nbytes, 1024)))
			# ~ nsize = round(nbytes/(math.pow(1024, nunit)), 2)
			
			# ~ return '{} {}'.format(format(nsize, '.2f'), metric[nunit])
			
			B  = nbytes % 1024
			KB = nbytes / 1024
			MB = nbytes / 1024**2
			GB = nbytes / 1024**3
			TB = nbytes / 1024**4
			
			if raw:
				dB = {'bytes': B}
				if KB > 1: dB = {'KB':int(KB)%1024, **dB}
				if MB > 1: dB = {'MB':int(MB)%1024, **dB}
				if GB > 1: dB = {'GB':int(GB)%1024, **dB}
				if TB > 1: dB = {'TB':int(TB),      **dB}
				return dB
			else:
				if   TB > 1: return '{:.2f} TB'.format(TB)
				elif GB > 1: return '{:.2f} GB'.format(GB)
				elif MB > 1: return '{:.2f} MB'.format(MB)
				elif KB > 1: return '{:.2f} KB'.format(KB)
				else: return '{} bytes'.format(B)
		
		def memoryStatusUpdate(self):									# Actualiza el estado de uso de memoria y cpu del sistema, para poder ver los datos en tiempo real.
			
			self.proc = psutil.Process(self.pid)
			
			self.proc_mem_info = self.proc.memory_info()
			self.cpu_percent = psutil.cpu_percent()										# Porcentaje del CPU utilizado
			self.used_memory = self.bytesToString(self.proc_mem_info.rss)				# Memoria RAM utilizada por el programa.
			
			wagms = WA.GlobalMemoryStatus()
			
			self.global_memory_status = {
				'total':   self.bytesToString(wagms['TotalPhys']),						# RAM Total instalada
				'free':    self.bytesToString(wagms['AvailPhys']),						# RAM disponible
				'used':    self.bytesToString(wagms['TotalPhys']-wagms['AvailPhys']),	# RAM utilizada
				'percent': round(100-(wagms['AvailPhys']/wagms['TotalPhys']*100), 2)	# RAM en porcentaje de uso
			}
		
		def totalFilesInRecyclerBin(self):								# Devuelve la cantidad de archivos que hay en Papelera de Reciclaje
			return shell.SHQueryRecycleBin()[1]
		
		def totalSizeInRecyclerBin(self, raw=False):					# Devuelve la cantidad de memoria que ocupan los archivos en papelera
			B = shell.SHQueryRecycleBin()[0]
			return self.bytesToString(B, raw)
	
	class NetworkInfo:	# Información general sobre la red, wifi, conexión, etc
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.use = '''
			\r / 
			\r + Predeterminado:
			\r | 
			\r |    utils = Utils()
			\r |    nwinf = utils.NetworkInfo
			\r | 
			\r Funciones: ESSIDEnum() y ESSIDPasswd(ESSID)
			\r |
			\r + Ejemplos de uso:
			\r |    
			\r |    utils = Utils()
			\r |    
			\r |    for ESSID in nwinf.ESSIDEnum():
			\r |        pwd = nwinf.ESSIDPasswd(ESSID)
			\r |        print('\\nESSID: ' + ESSID + '\\n  Pwd: ' + pwd)
			\r |
			\r |--------------------------------------------------------
			\r Función: getIPv4(
			\r |            host = socket.gethostname()
			\r |        )
			\r |
			\r + Ejemplos de uso:
			\r |    
			\r |    # Obtiene la IPv4 Local:
			\r |    nwinf.getIPv4()
			\r |    
			\r |    # Obtiene la IPv4 de un Host Remoto:
			\r |    nwinf.getIPv4('www.google.com')
			\r |
			\r |--------------------------------------------------------
			\r Función: packetIPAddress(
			\r |            ipAddress,
			\r |            hexlify  = False,
			\r |            unpacked = False
			\r |        )
			\r |
			\r + Ejemplos de uso:
			\r |    
			\r |    ip = '192.168.1.0'
			\r |    
			\r |    # Empaqueta la IP:
			\r |    packed = nwinf.packetIPAddress(ip)
			\r |    print(packed)    # b'\xc0\xa8\x01\x00'
			\r |    
			\r |    # Desempaqueta la IP:
			\r |    unpacked = nwinf.packetIPAddress(packed, unpacked=True)
			\r |    print(unpacked)  # 192.168.1.0
			\r |    
			\r |    # Empaqueta la IP y la devuelve en hexadecimal:
			\r |    packed = nwinf.packetIPAddress(ip, hexlify=True)
			\r |    print(packed)    # b'c0a80100'
			\r |
			\r |--------------------------------------------------------
			\r Función: findServiceName(
			\r |            port,
			\r |            protocol = 'tcp',   # 'tcp' or 'udp'
			\r |            nones    = False
			\r |        )
			\r |
			\r + Ejemplos de uso:
			\r |    
			\r |    # Obtiene el nombre del servicio.
			\r |    port = 80
			\r |    serv_name = nwinf.findServiceName(port)
			\r |    print(serv_name)
			\r |    
			\r |    # Puertos de ejemplo:
			\r |    ports = [19,21,23,24,25]
			\r |    
			\r |    # Obtiene la lista de puertos (TCP). Ignora los no encontrados:
			\r |    serv_names = nwinf.findServiceName(ports)
			\r |    print(json.dumps(serv_names, indent=4))
			\r |    #{"tcp": {
			\r |    #    "19": "chargen",
			\r |    #    "21": "ftp",
			\r |    #    "23": "telnet",
			\r |    #    "25": "smtp"
			\r |    #}}
			\r |    
			\r |    # Obtiene la lista de puertos (UDP). Ignora los no encontrados:
			\r |    serv_names = nwinf.findServiceName(ports, 'udp')
			\r |    print(json.dumps(serv_names, indent=4))
			\r |    #{"udp": {
			\r |    #    "19": "chargen"
			\r |    #}}
			\r |    
			\r |    # Obtiene la lista de puertos (TCP):
			\r |    serv_names = nwinf.findServiceName(ports, nones=True)
			\r |    print(json.dumps(serv_names, indent=4))
			\r |    #{"tcp": {
			\r |    #    "19": "chargen",
			\r |    #    "21": "ftp",
			\r |    #    "23": "telnet",
			\r |    #    "24": "None",
			\r |    #    "25": "smtp"
			\r |    #}}
			\r |    
			\r |    # Obtiene la lista de puertos (UDP):
			\r |    serv_names = nwinf.findServiceName(ports, 'udp', nones=True)
			\r |    print(json.dumps(serv_names, indent=4))
			\r |    #{"tcp": {
			\r |    #    "19": "chargen",
			\r |    #    "21": "None",
			\r |    #    "23": "None",
			\r |    #    "24": "None",
			\r |    #    "25": "None"
			\r |    #}}
			\r |    
			\r |    # Obtiene la lista de puertos (TCP y UDP). Ignora los no encontrados:
			\r |    port = {'tcp': [19,21,23,24,25], 'udp': [19,21,80,81,88]}
			\r |    serv_name = nwinf.findServiceName(port)
			\r |    print(json.dumps(serv_name, indent=4))
			\r |    #{"tcp": {
			\r |    #    "19": "chargen",
			\r |    #    "21": "ftp",
			\r |    #    "23": "telnet",
			\r |    #    "25": "smtp"
			\r |    # },
			\r |    # "udp": {
			\r |    #    "19": "chargen",
			\r |    #    "81": "hosts2-ns",
			\r |    #    "88": "kerberos"
			\r |    #}}
			\r |
			\r |--------------------------------------------------------
			\r \\
			'''
			
			self.run_command = lambda command: os.popen(command).read()	# Ejecuta cualquier comando en consola
			self.GetIP = self.GetIP()
		
		def __str__(self): return self.use
		
		class GetIP: #Use												# Esta Clase Permite obtener la información sobre la IP Pública y Privada, versión 4 y/o versión 6.
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.use = '''
				\r Clase: GetIP()
				\r |
				\r + Ejemplos de uso:
				\r |
				\r |    utils = Utils()
				\r |
				\r |    # Sirve en el caso de no necesitar las IP públicas.
				\r |    # Evita conectarse a la API de ipify.
				\r |    # Default: utils.GetIP.only_local = True
				\r |
				\r |    print('\\nDatos Locales:\\n')
				\r |    print(' HOST:', utils.GetIP.hostname)
				\r |    print(' IPv4 Privada:', utils.GetIP.local_ipv4)
				\r |    print(' IPv6 Privada:', utils.GetIP.local_ipv6)
				\r |    print(' IPv4 Publica:', utils.GetIP.public_ipv4)
				\r |    print(' IPv6 Publica:', utils.GetIP.public_ipv6)
				\r |
				\r |    # Conecta a la API de ipify para obtener las IP públicas.
				\r |    utils.GetIP.only_local = False
				\r |
				\r |    print('\\nDatos Locales y Públicos:\\n')
				\r |    print(' HOST:', utils.GetIP.hostname)
				\r |    print(' IPv4 Privada:', utils.GetIP.local_ipv4)
				\r |    print(' IPv6 Privada:', utils.GetIP.local_ipv6)
				\r |    print(' IPv4 Publica:', utils.GetIP.public_ipv4)
				\r |    print(' IPv6 Publica:', utils.GetIP.public_ipv6)
				\r \\
				'''
				
				self.only_local_ = True
				self.hostname = socket.gethostname()
				self.local_ipv4 = socket.gethostbyname(self.hostname)
				self.local_ipv6 = socket.getaddrinfo(self.hostname, None, socket.AF_INET6)[0][4][0]
				self.public_ipv4 = None
				self.public_ipv6 = None
			
			def __str__(self): return self.use
			
			@property
			def only_local(self):
				return self.only_local_
			
			@only_local.setter
			def only_local(self, bool_):
				self.only_local_ = bool_
				if not self.only_local_:
					try:
						# Get Public IPv4, commands: nslookup myip.opendns.com resolver1.opendns.com
						self.public_ipv4 = requests.get('https://api.ipify.org').text
						self.public_ipv6 = requests.get('https://api64.ipify.org').text
						if self.public_ipv6 == self.public_ipv4: self.public_ipv6 = None
					except:
						pass
				else:
					self.public_ipv4 = None
					self.public_ipv6 = None
		
		def latin1_encoding(self, res):									# Remplaza los caracteres incorrectos en acentos y puntuaciones por los caracteres correctos al lenguaje español.
			
			# ~ res = res.decode('latin1')
			
			res = res.replace('·','À'); res = res.replace('ú','·'); res = res.replace('¨','¿'); res = res.replace('ù','¨')
			res = res.replace('ï','´'); res = res.replace('­','¡');  res = res.replace('§','º'); res = res.replace('ª','¬')
			res = res.replace('¦','ª'); res = res.replace('ì','ý'); res = res.replace('','ÿ')
			
			res = res.replace('','ù'); res = res.replace('£','ú'); res = res.replace('','ü')
			res = res.replace('ë','Ù');   res = res.replace('é','Ú'); res = res.replace('','Ü')
			
			res = res.replace('','è'); res = res.replace('','é'); res = res.replace('','ë')
			res = res.replace('Ô','È');   res = res.replace('','É'); res = res.replace('Ó','Ë')
			
			res = res.replace('','ì'); res = res.replace('¡','í'); res = res.replace('','ï')
			res = res.replace('Þ','Ì');  res = res.replace('Ö','Í'); res = res.replace('Ø','Ï')
			
			res = res.replace('¶','Â'); res = res.replace('Ò','Ê'); res = res.replace('×','Î')
			res = res.replace('â','Ô'); res = res.replace('ê','Û')
			
			res = res.replace('','ò'); res = res.replace('¢','ó'); res = res.replace('','ö')
			res = res.replace('ã','Ò');  res = res.replace('à','Ó'); res = res.replace('','Ö')
			
			res = res.replace('Ç','Ã');   res = res.replace('å','Õ')
			res = res.replace('Æ','ã');   res = res.replace('ä','õ')
			
			res = res.replace('','à'); res = res.replace(' ','á'); res = res.replace('','ä')
			res = res.replace('µ','Á'); res = res.replace('','Ä')
			
			res = res.replace('','â'); res = res.replace('','ê'); res = res.replace('','î')
			res = res.replace('','ô'); res = res.replace('','û')
			
			res = res.replace('¥','Ñ');   res = res.replace('¤','ñ')
			
			res = res.replace('','ç'); res = res.replace('','Ç')
			
			return res
		
		def ESSIDEnum(self): #Use										# Enumera las redes wifi almacenadas en el sistema.
			
			output = self.run_command('netsh wlan show profiles')
			output = self.latin1_encoding(output).split('\n')
			
			ESSIDs = [
				o.split(': ')[1]
				if ': ' in o else None
				for o in output
			]
			
			while None in ESSIDs: ESSIDs.remove(None)
			
			return ESSIDs
		
		def ESSIDPasswd(self, ESSID): #Use								# Con el nombre de una red wifi obtiene la contraseña almacenada.
			
			output = self.run_command('netsh wlan show profile name="{}" key=clear'.format(ESSID))
			output = self.latin1_encoding(output).split('\n')
			
			Passwd = None
			
			for o in output:
				if 'Contenido de la clave  : ' in o:
					Passwd = o.split(': ')[1]
					break
			
			return Passwd
		
		def findServiceName(self, port, protocol='tcp', nones=False): #Use	# Devuelve el nombre del servicio de uno o varios puertos.
			if port.__class__ == int:
				try:
					out = socket.getservbyport(port, protocol)
				except:
					out = None
			elif port.__class__ in [list, tuple, set]:
				ports = set(port)
				out = {protocol: {}}
				if len(ports) == 1:
					try:
						port = ports.pop()
						serv_name = socket.getservbyport(port, protocol)
						out[protocol][port] = serv_name
					except:
						out[protocol][port] = 'None'
				else:
					for port in ports:
						try:
							serv_name = socket.getservbyport(port, protocol)
							out[protocol][port] = serv_name
						except:
							if nones:
								out[protocol][port] = 'None'
			elif port.__class__ == dict:
				out = {'tcp': {}, 'udp': {}}
				for protocol, ports in port.items():
					ports = set(ports)
					if len(ports) == 1:
						try:
							port = ports.pop()
							serv_name = socket.getservbyport(p, protocol)
							out[protocol][port] = serv_name
						except:
							out[protocol][port] = 'None'
					else:
						for port in ports:
							try:
								serv_name = socket.getservbyport(port, protocol)
								out[protocol][port] = serv_name
							except:
								if nones:
									out[protocol][port] = 'None'
			else:
				out = None
			return out
		
		def getIPv4(self, host=socket.gethostname()): #Use				# Obtiene la IP publica de cualquier pagina.
			try:
				IPv4 = socket.gethostbyname(host)
			except:
				IPv4 = None
			return IPv4
		
		def packetIPAddress(self, ipAddress, hexlify=False, unpacked=False): #Use	# Devuelve empaqueta (Binarios) la IP dada.
			if unpacked:
				try:
					unpackedIPAddr = socket.inet_ntoa(ipAddress)
				except:
					ipAddress = binascii.unhexlify(ipAddress)
					unpackedIPAddr = socket.inet_ntoa(ipAddress)
				return unpackedIPAddr
			else:
				packedIPAddr = socket.inet_aton(ipAddress)
				if hexlify:
					packedIPAddr = binascii.hexlify(packedIPAddr)
				return packedIPAddr
	
	class SystemInfo:	# Información general sobre la PC
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.load_uses()
			
			self.info = self.collectAll
			
			self.run_command = lambda command: os.popen(command).read()	# Ejecuta cualquier comando en consola
		
		def load_uses(self):
			self.enumProcess_use = '''
			\r Función: enumProcess(findstr=None)
			\r |
			\r + Ejemplo de uso:
			\r |
			\r |    utils = Utils()
			\r |
			\r |    # Busca todas las coincidencias con 'note':
			\r |    procs = utils.SystemInfo.enumProcess('note')
			\r |    for p in procs: print(p)
			\r |
			\r |    # Busca todas las coincidencias con 'calc':
			\r |    procs = utils.SystemInfo.enumProcess('calc')
			\r |    for p in procs: print(p)
			\r |
			\r |    # Enumera todos los procesos activos:
			\r |    procs = utils.SystemInfo.enumProcess()
			\r |    for p in procs: print(p)
			\r \\
			'''
		
		def not_enumWindows(self):											# [X] Muestra los hwnd de todas los programas
			class __WindowEnumerator (object):
				'''
				Window enumerator class. Used internally by the window enumeration APIs.
				'''
				def __init__(self):
					self.hwnd = list()

				def __call__(self, hwnd, lParam):
					self.hwnd.append(hwnd)
					return True
			
			class __EnumWndProc (__WindowEnumerator): pass
			
			ERROR_SUCCESS = 0
			ERROR_NO_MORE_FILES = 18
			NULL = None
			PVOID = ctypes.c_void_p
			LPARAM = ctypes.c_void_p
			HWND = ctypes.c_void_p
			BOOL = ctypes.c_int
			WNDENUMPROC = ctypes.WINFUNCTYPE(BOOL, HWND, PVOID)
			
			# DWORD WINAPI GetLastError(void);
			def GetLastError():
				_GetLastError = ctypes.windll.kernel32.GetLastError
				_GetLastError.argtypes = []
				_GetLastError.restype = ctypes.c_uint32
				return _GetLastError()
			
			_EnumWindows = ctypes.windll.user32.EnumWindows
			_EnumWindows.argtypes = [WNDENUMPROC, LPARAM]
			_EnumWindows.restype = bool

			EnumFunc = __EnumWndProc()
			lpEnumFunc = WNDENUMPROC(EnumFunc)
			print(lpEnumFunc)
			if not _EnumWindows(lpEnumFunc, None):
				errcode = GetLastError()
				if errcode not in (ERROR_NO_MORE_FILES, ERROR_SUCCESS):
					raise ctypes.WinError(errcode)
			return EnumFunc.hwnd
		
		def not_isProcessActive(self, process_name):						# [X] Devuelve True si el proceso esta activo.
			
			proc_list = self.run_command('wmic process get name').split('\n')
			
			# ~ print(proc_list)
			
			for proc in proc_list:
				
				proc = proc.strip().split(' ')[0]
				
				if len(proc) == 0: continue
				
				if proc.endswith('.exe'):
					if proc.lower() == process_name.lower():
						return True
			
			return False
		
		def enumComputerSystemInfo(self):								# Muestra información detallada del sistema.
			con = wmi.WMI()
			# ~ print(f'Manufacturer: {computerSystem.Manufacturer}')
			# ~ print(f'Model: {computerSystem.Model}')
			# ~ print(f'Name: {computerSystem.Name}')
			# ~ print(f'NumberOfProcessors: {computerSystem.NumberOfProcessors}')
			# ~ print(f'SystemType: {computerSystem.SystemType}')
			# ~ print(f'SystemFamily: {computerSystem.SystemFamily}')
			return con.Win32_ComputerSystem()[0]
		
		def enumLocalDisk(self):										# Lista todos los discos conectados con información detallada.
			#DriveType	Description
			#		 0	Unknown
			#		 1	No Root Directory
			#		 2	Removable Disk
			#		 3	Local Disk
			#		 4	Network Drive
			#		 5	Compact Disc
			#		 6	RAM Disk
			con = wmi.WMI()
			localDisks = []
			for disk in con.Win32_LogicalDisk():
				if disk.size != None:
					localDisks.append(disk)
					# ~ print(disk)
					# ~ print('Free space on disk \'{}\': {:.2f}%'.format(disk.Caption, 100*float(disk.FreeSpace)/float(disk.Size)))
			
			return localDisks
		
		def enumLocalUsersAndGroups(self):								# Lista todos los grupos y usuarios de cada uno de ellos con información detallada.
			con = wmi.WMI()
			userAndGroups = {}
			for group in con.Win32_Group():
				userAndGroups[group.Caption] = {'users': [], 'group': group}
				for user in group.associators(wmi_result_class="Win32_UserAccount"):
					userAndGroups[group.Caption]['users'].append(user)
			return userAndGroups
		
		def enumProcess(self, findstr=None): #Use						# Enumera todos los procesos o los que coincidan con la cadena 'findstr' y los devuelve.
			
			output = list()
			
			command = 'wmic process get name, processid'
			if findstr: command += ' | findstr "{}"'.format(findstr)
			
			res = self.run_command(command).split('\n\n')
			
			for o in res:
				output.append({
					'name': o[:34].strip(),
					'pid':  o[34:].strip()
				})
			
			if {'name': 'Name', 'pid': 'ProcessId'} in output: output.remove({'name':'Name', 'pid':'ProcessId'})
			while {'name':'', 'pid':''} in output: output.remove({'name':'', 'pid':''})
			
			return output
		
		@property
		def isCapsLockActive(self):										# Devuelve True si el Bloq Mayús está activado o False si no.
			return False if WA.GetKeyState(WC.VK_CAPITAL) == 0 else True
		
		@property
		def isLinux(self):												# Función Que Comprueba si el SO es Linux, Devuelve TRUE/FALSE
			osver = os.popen("ver").read()
			if osver.find("Linux") > 0: return True
			else: return False
		
		@property
		def isMouseInstalled(self):										# Devuelve verdadero si hay controlador de mouse instalado.
			val = WA.GetSystemMetrics(WC.SM_MOUSEPRESENT)	# SM_MOUSEPRESENT = 19
			return val == 1
		
		@property
		def isPythonV2(self):											# Devuelve verdadero si versión de python que corre es 2.X.
			return sys.version[0] == '2'
		
		@property
		def isPythonV3(self):											# Devuelve verdadero si versión de python que corre es 3.X.
			return sys.version[0] == '3'
		
		@property
		def isSlowMachine(self):										# Es 1 si la computadora tiene un procesador de gama baja (lento)
			val = WA.GetSystemMetrics(WC.SM_SLOWMACHINE)				# SM_SLOWMACHINE = 73
			return val == 1
		
		@property
		def isUserAnAdmin(self):										# Devuelve True si el programa tiene permisos de administrador o False si no.
			return shell.IsUserAnAdmin()
		
		
		def isUserPasswordValid(self, userName, passwd):				# Verifica si la contraseña dada es la correcta del usuario.
			'''
			# Aplicanda en un for puede comprobar cientos de palabras en segundos
			# y devuelve True si la contraseña es la correcta.
			# Ejemplo de uso:
			
			utils = Utils()
			
			palabras = ['palabra1','palabra2',...]
			user = 'prueba'
			
			for x in palabras:
				resp = utils.SystemInfo.isUserPasswordValid(user, x)
				if resp:
					print('\n User:', user)
					print('\n Passwd:', x)
					break

			if not resp:
				print('Password Not Found...')
			'''
			try:
				WS.LogonUser(
					userName,
					None,
					passwd,
					WC.LOGON32_LOGON_INTERACTIVE,
					WC.LOGON32_PROVIDER_DEFAULT
				)
				return True
			except:
				return False
		
		@property
		def isWindows(self):											# Función Que Comprueba si el SO es Linux, Devuelve TRUE/FALSE
			osver = os.popen("ver").read()
			if osver.find("Windows") > 0: return True
			else: return False
		
		@property
		def currentProcessId(self):										# Devuelve el ID del proceso actual
			return WA.GetCurrentProcessId()
		
		@property
		def cursorPos(self):											# Devuelve la posición actual del cursor en pantalla en (X, Y) pixeles
			return WA.GetCursorPos()
		
		@property
		def currentSystemMetrics(self):									# Devuelve la resolucion de pantalla (Metricas Actuales)
			xScreen = WA.GetSystemMetrics(WC.SM_CXSCREEN)	# SM_CXSCREEN = 0
			yScreen = WA.GetSystemMetrics(WC.SM_CYSCREEN)	# SM_CYSCREEN = 1
			return (xScreen, yScreen)
		
		@property
		def realSystemMetrics(self):									# Devuelve la resolucion de pantalla (Metricas Reales)
			ctypes.windll.user32.SetProcessDPIAware()
			xScreen = ctypes.windll.user32.GetSystemMetrics(0)
			yScreen = ctypes.windll.user32.GetSystemMetrics(1)
			return (xScreen, yScreen)
		
		@property
		def displaySettings(self):										# Devuelve la resolucion de pantalla y los bits de pixeles (normalmente 32 bits)
			'''return x_resolution, y_resolution, colour_depth'''
			xScreen = WA.GetSystemMetrics(WC.SM_CXSCREEN)	# SM_CXSCREEN = 0
			yScreen = WA.GetSystemMetrics(WC.SM_CYSCREEN)	# SM_CYSCREEN = 1
			bPixels = WU.GetDeviceCaps(WG.GetDC(0), WC.BITSPIXEL)
			return (xScreen, yScreen, bPixels)
		
		@property
		def computerName(self):											# Devuelve el nombre de la Computadora
			return WA.GetComputerName()
		
		@property
		def homeDrive(self):											# Devuelve el nombre del Disco Principal, normalmente 'C:'
			return os.environ.get('HOMEDRIVE')
		
		@property
		def numberOfMonitors(self):										# Devuelve el número de monitores conectados
			return WA.GetSystemMetrics(WC.SM_CMONITORS)	# SM_CMONITORS = 80
		
		@property
		def numberOfProcessors(self):									# Devuelve el número de procesadores lógicos
			# Alternativa: return os.environ.get('NUMBER_OF_PROCESSORS')
			return WA.GetNativeSystemInfo()[5]
		
		@property
		def os(self):													# Devuelve el nombre del sistema operativo. Ejemplo: 'Windows_NT'
			return os.environ.get('OS')
		
		@property
		def processorArchitecture(self):								# Devuelve la aquitectura del sistema. Ejemplo 'AMD64'
			return os.environ.get('PROCESSOR_ARCHITECTURE')
		
		@property
		def processorIdentifier(self):									# Devuelve el nombre del procesador
			return os.environ.get('PROCESSOR_IDENTIFIER')
		
		@property
		def screenSize(self):											# Devuelve la resolución actual de la pantalla en forma de tupla (X, Y)
			user32 = ctypes.windll.user32
			screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
			return screenSize
		
		@property
		def systemDrive(self):											# Devuelve el nombre del Disco Principal, normalmente 'C:'
			return os.environ.get('SYSTEMDRIVE')
		
		@property
		def systemRoot(self):											# Devuelve la ruta predeterminada de la raiz del sistema, normalmente 'C:\WINDOWS'
			return os.environ.get('SYSTEMROOT')
		
		
		def systemUptime(self, raw=False):								# Devuelve el Tiempo de actividad del sistema en formato '0d 00:00:00'
			
			#mili = ctypes.windll.kernel32.GetTickCount64()
			mili = WA.GetTickCount()
			
			secs = (mili // 1000)
			if raw: return str(secs)+'s'
			mins = (secs // 60)
			hrs  = (mins // 60)
			days = (hrs  // 24)
			
			time = ''
			if days > 0: time += str(days)+'d '
			time += str(hrs %24).zfill(2)+':'
			time += str(mins%60).zfill(2)+':'
			time += str(secs%60).zfill(2)
			
			return time
		
		@property
		def userDefaultLanguage(self):									# Devuelve el Idioma por Defecto del Sistema. Ejemplo 'es_ES'.
			langID = ctypes.windll.kernel32.GetUserDefaultUILanguage()
			lang = locale.windows_locale[langID]
			return lang
		
		@property
		def userDowntime(self):											# Devuelve la cantidad de tiempo inactivo del usuario (cuanto tiempo tiene sin presionar una tecla o mover el mouse, por ejemplo)
			
			class LASTINPUTINFO(ctypes.Structure):
				_fields_ = [('cbSize', ctypes.c_uint), ('dwTime', ctypes.c_uint)]
			
			lastInputInfo = LASTINPUTINFO()
			lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
			ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)) 
			millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
			
			return millis / 1000.0
		
		@property
		def userName(self):												# Devuelve el nombre del Usuario
			return os.environ.get('USERNAME')
		
		@property
		def winDir(self):												# Devuelve la ruta predeterminada del Windows, normalmente 'C:\WINDOWS'
			return os.environ.get('WINDIR')
		
		@property
		def collectAll(self):
			
			collected = {
				'winDir':       self.winDir,
				'userName':     self.userName,
				'userDowntime': self.userDowntime,
				'systemUptime': self.systemUptime(),
				'systemRoot':   self.systemRoot,
				'systemDrive':  self.systemDrive,
				'screenSize':   self.screenSize,
				'processorIdentifier':   self.processorIdentifier,
				'processorArchitecture': self.processorArchitecture,
				'os':                 self.os,
				'numberOfProcessors': self.numberOfProcessors,
				'numberOfMonitors':   self.numberOfMonitors,
				'homeDrive':        self.homeDrive,
				'computerName':     self.computerName,
				'displaySettings':  self.displaySettings,
				'cursorPos':        self.cursorPos,
				'currentProcessId': self.currentProcessId,
				'isWindows':        self.isWindows,
				'isUserAnAdmin':    self.isUserAnAdmin,
				'isSlowMachine':    self.isSlowMachine,
				'isMouseInstalled': self.isMouseInstalled,
				'isLinux':          self.isLinux,
				'isCapsLockActive': self.isCapsLockActive
			}
			
			return collected
	
	class Utilities:	# Funciones de utilidad para cosas generales.
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.load_uses()
			
			self.AsciiFont = self.AsciiFont()
			self.DoomsdayRule = self.DoomsdayRule()
			self.Images = self.Images()
			self.NumberSystems = self.NumberSystems()
			self.UBZ2 = self.UBZ2()
		
		class AsciiFont:	# Clase que permite convertir un texto a un tipo de ASCII FONT
			
			class NotSupportedError(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			class TypeError(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.textToAscii = self.not_textToAscii
				
				self.extra = ' '
				self.ascii_lowercase = string.ascii_lowercase+self.extra
				self.ascii_uppercase = string.ascii_uppercase+self.extra
				self.ascii_letters   = string.ascii_letters + self.extra
				
				self.use = '''
				\r Clase: AsciiFont
				\r |
				\r + Ejemplo de uso: 
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para ver todas las fuentes ascii disponibles:
				\r |    print(utils.Utilities.AsciiFont.functions.list)
				\r |    
				\r |    text = 'By LawlietJH'
				\r |    
				\r |    cal = utils.Utilities.AsciiFont.calvinS(text)
				\r |    ans = utils.Utilities.AsciiFont.ansiShadow(text)
				\r |    reg = utils.Utilities.AsciiFont.ansiRegular(text)
				\r |    
				\r |    print(cal + '\\n' + ans + '\\n' + reg)
				\r \\
				'''
			
			def not_textToAscii(self, text, c, rules, width, plus=''):
				
				if c.__class__.__name__ == 'dict':
					height = len(c['l'])
					letters = {
						'lc': {l:None for l in self.ascii_lowercase+plus},
						'uc': {l:None for l in self.ascii_uppercase+plus}
					}
				elif c.__class__.__name__ == 'list':
					height = len(c)
					letters = {l:None for l in self.ascii_uppercase+plus}
				else:
					error_msg = 'must be list or dict, not {}'.format(c.__class__.__name__)
					raise self.NotSupportedError(error_msg) 
				
				for type_ in letters:
					
					start = 0
					end = width
					
					for x in range(len(self.ascii_uppercase+plus)):
						
						if c.__class__.__name__ == 'dict':
							ascii_ = (self.ascii_lowercase+plus)[x] if type_ == 'lc' else (self.ascii_uppercase+plus)[x]
							if ascii_ in self.extra:
								letters[type_][ascii_] = tuple(
									ascii_*(width//2) for i in range(height)
								)
								continue
						elif c.__class__.__name__ == 'list':
							ascii_ = (self.ascii_uppercase+plus)[x]
							if ascii_ in self.extra:
								letters[ascii_] = tuple(
									ascii_*(width//2) for i in range(height)
								)
								continue
						
						for r in rules:
							if ascii_ in r[1]:
								end += r[0]
						
						if c.__class__.__name__ == 'dict':
							letters[type_][ascii_] = tuple(
								c['l'][i][start:end]
								if type_ == 'lc'
								else c['u'][i][start:end]
								for i in range(height)
							)
						elif c.__class__.__name__ == 'list':
							letters[ascii_] = tuple( c[i][start:end] for i in range(height) )
						
						xD = True
						for r in rules:
							if ascii_ in r[1]:
								start += width + r[0]
								xD = False
						
						if xD: start += width
						
						end += width
				
				output = ''
				lets = []
				
				if c.__class__.__name__ == 'dict':
					lets = [letters['lc'][t] if t.islower() else letters['uc'][t] for t in text]
				elif c.__class__.__name__ == 'list':
					lets = [letters[t] for t in text.upper()]
				
				for x in range(height):
					for l in lets:
						output += l[x]
					output += '\n'
				
				return output
			
			def ansiShadow(self, text):
				
				plus = '1234567890.,:;-_[]()!?*^<>@#/&%$'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				# URL: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow
				
				cn = [
					' ██╗██████╗ ██████╗ ██╗  ██╗███████╗ ██████╗ ███████╗ █████╗  █████╗  ██████╗ ',
					'███║╚════██╗╚════██╗██║  ██║██╔════╝██╔════╝ ╚════██║██╔══██╗██╔══██╗██╔═████╗',
					'╚██║ █████╔╝ █████╔╝███████║███████╗███████╗     ██╔╝╚█████╔╝╚██████║██║██╔██║',
					' ██║██╔═══╝  ╚═══██╗╚════██║╚════██║██╔═══██╗   ██╔╝ ██╔══██╗ ╚═══██║████╔╝██║',
					' ██║███████╗██████╔╝     ██║███████║╚██████╔╝   ██║  ╚█████╔╝ █████╔╝╚██████╔╝',
					' ╚═╝╚══════╝╚═════╝      ╚═╝╚══════╝ ╚═════╝    ╚═╝   ╚════╝  ╚════╝  ╚═════╝ '
				]
				
				ce = [
					cn[0] + '                          ███╗███╗ ██╗██╗ ██╗██████╗        ███╗   ██╗██╗   ██████╗  ██╗ ██╗     ██╗  ██╗  ██╗ ██╗▄▄███▄▄·',
					cn[1] + '      ██╗██╗              ██╔╝╚██║██╔╝╚██╗██║╚════██╗▄ ██╗▄██╔██╗ ██╔╝╚██╗ ██╔═══██╗████████╗   ██╔╝  ██║  ╚═╝██╔╝██╔════╝',
					cn[2] + '      ╚═╝╚═╝█████╗        ██║  ██║██║  ██║██║  ▄███╔╝ ████╗╚═╝╚═╝██╔╝  ╚██╗██║██╗██║╚██╔═██╔╝  ██╔╝████████╗ ██╔╝ ███████╗',
					cn[3] + '      ██╗▄█╗╚════╝        ██║  ██║██║  ██║╚═╝  ▀▀══╝ ▀╚██╔▀      ╚██╗  ██╔╝██║██║██║████████╗ ██╔╝ ██╔═██╔═╝██╔╝  ╚════██║',
					cn[4] + '██╗▄█╗╚═╝▀═╝      ███████╗███╗███║╚██╗██╔╝██╗  ██╗     ╚═╝        ╚██╗██╔╝ ╚█║████╔╝╚██╔═██╔╝██╔╝  ██████║ ██╔╝██╗███████║',
					cn[5] + '╚═╝╚═╝            ╚══════╝╚══╝╚══╝ ╚═╝╚═╝ ╚═╝  ╚═╝                 ╚═╝╚═╝   ╚╝╚═══╝  ╚═╝ ╚═╝ ╚═╝   ╚═════╝ ╚═╝ ╚═╝╚═▀▀▀══╝'
				]
				
				c =  [
					' █████╗ ██████╗  ██████╗██████╗ ███████╗███████╗ ██████╗ ██╗  ██╗██╗     ██╗██╗  ██╗██╗     ███╗   ███╗███╗   ██╗ ██████╗ ██████╗  ██████╗ ██████╗ ███████╗████████╗██╗   ██╗██╗   ██╗██╗    ██╗██╗  ██╗██╗   ██╗███████╗' + ce[0],
					'██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝ ██║  ██║██║     ██║██║ ██╔╝██║     ████╗ ████║████╗  ██║██╔═══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝╚══██╔══╝██║   ██║██║   ██║██║    ██║╚██╗██╔╝╚██╗ ██╔╝╚══███╔╝' + ce[1],
					'███████║██████╔╝██║     ██║  ██║█████╗  █████╗  ██║  ███╗███████║██║     ██║█████╔╝ ██║     ██╔████╔██║██╔██╗ ██║██║   ██║██████╔╝██║   ██║██████╔╝███████╗   ██║   ██║   ██║██║   ██║██║ █╗ ██║ ╚███╔╝  ╚████╔╝   ███╔╝ ' + ce[2],
					'██╔══██║██╔══██╗██║     ██║  ██║██╔══╝  ██╔══╝  ██║   ██║██╔══██║██║██   ██║██╔═██╗ ██║     ██║╚██╔╝██║██║╚██╗██║██║   ██║██╔═══╝ ██║▄▄ ██║██╔══██╗╚════██║   ██║   ██║   ██║╚██╗ ██╔╝██║███╗██║ ██╔██╗   ╚██╔╝   ███╔╝  ' + ce[3],
					'██║  ██║██████╔╝╚██████╗██████╔╝███████╗██║     ╚██████╔╝██║  ██║██║╚█████╔╝██║  ██╗███████╗██║ ╚═╝ ██║██║ ╚████║╚██████╔╝██║     ╚██████╔╝██║  ██║███████║   ██║   ╚██████╔╝ ╚████╔╝ ╚███╔███╔╝██╔╝ ██╗   ██║   ███████╗' + ce[4],
					'╚═╝  ╚═╝╚═════╝  ╚═════╝╚═════╝ ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝      ╚══▀▀═╝ ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝   ╚═══╝   ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝' + ce[5]
				]
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-5, ['i','I','.',',',':',';','!']),
					(-4, ['1','[',']','(',')']),
					(-2, ['-']),
					( 1, ['g','o','q','t','u','v','y','G','O','Q','T','U','V','Y','6','0']),
					( 2, ['n','w','N','W']),
					( 3, ['m','M'])
				]
				
				return self.textToAscii(text, c, rules, width=8, plus=plus)
			
			def ansiRegular(self, text):
				
				plus = '1234567890.,:;-_[]()!?*^<>@#/&%$'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				# URL: http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular
				cn = [
					' ██ ██████  ██████  ██   ██ ███████  ██████  ███████  █████   █████   ██████  ',
					'███      ██      ██ ██   ██ ██      ██            ██ ██   ██ ██   ██ ██  ████ ',
					' ██  █████   █████  ███████ ███████ ███████      ██   █████   ██████ ██ ██ ██ ',
					' ██ ██           ██      ██      ██ ██    ██    ██   ██   ██      ██ ████  ██ ',
					' ██ ███████ ██████       ██ ███████  ██████     ██    █████   █████   ██████  ',
					'                                                                              '
				]
				
				ce = [
					cn[0] + '                          ███ ███  ██ ██  ██ ██████          ███    ██ ██    ██████   ██  ██      ██   ██   ██  ██ ▄▄███▄▄·',
					cn[1] + '      ██ ██               ██   ██ ██   ██ ██      ██ ▄ ██ ▄ ██ ██  ██   ██  ██    ██ ████████    ██    ██      ██  ██      ',
					cn[2] + '            █████         ██   ██ ██   ██ ██   ▄███   ████        ██     ██ ██ ██ ██  ██  ██    ██  ████████  ██   ███████ ',
					cn[3] + '      ██ ▄█               ██   ██ ██   ██      ▀▀    ▀ ██ ▀        ██   ██  ██ ██ ██ ████████  ██   ██  ██   ██         ██ ',
					cn[4] + '██ ▄█    ▀        ███████ ███ ███  ██ ██  ██   ██                   ██ ██    █ ████   ██  ██  ██    ██████  ██  ██ ███████ ',
					cn[5] + '                                                                                                               ▀▀▀         '
				]
				
				c =  [
					' █████  ██████   ██████ ██████  ███████ ███████  ██████  ██   ██ ██      ██ ██   ██ ██      ███    ███ ███    ██  ██████  ██████   ██████  ██████  ███████ ████████ ██    ██ ██    ██ ██     ██ ██   ██ ██    ██ ███████ ' + ce[0],
					'██   ██ ██   ██ ██      ██   ██ ██      ██      ██       ██   ██ ██      ██ ██  ██  ██      ████  ████ ████   ██ ██    ██ ██   ██ ██    ██ ██   ██ ██         ██    ██    ██ ██    ██ ██     ██  ██ ██   ██  ██     ███  ' + ce[1],
					'███████ ██████  ██      ██   ██ █████   █████   ██   ███ ███████ ██      ██ █████   ██      ██ ████ ██ ██ ██  ██ ██    ██ ██████  ██    ██ ██████  ███████    ██    ██    ██ ██    ██ ██  █  ██   ███     ████     ███   ' + ce[2],
					'██   ██ ██   ██ ██      ██   ██ ██      ██      ██    ██ ██   ██ ██ ██   ██ ██  ██  ██      ██  ██  ██ ██  ██ ██ ██    ██ ██      ██ ▄▄ ██ ██   ██      ██    ██    ██    ██  ██  ██  ██ ███ ██  ██ ██     ██     ███    ' + ce[3],
					'██   ██ ██████   ██████ ██████  ███████ ██       ██████  ██   ██ ██  █████  ██   ██ ███████ ██      ██ ██   ████  ██████  ██       ██████  ██   ██ ███████    ██     ██████    ████    ███ ███  ██   ██    ██    ███████ ' + ce[4],
					'                                                                                                                                      ▀▀                                                                                 ' + ce[5]
				]
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				
				rules = [
					(-5, ['i','I','.',',',':',';','!']),
					(-4, ['1','[',']','(',')']),
					(-2, ['-']),
					( 1, ['g','o','q','t','u','v','y','G','O','Q','T','U','V','Y','6','0']),
					( 2, ['n','w','N','W']),
					( 3, ['m','M'])
				]
				
				return self.textToAscii(text, c, rules, width=8, plus=plus)
			
			def calvinS(self, text):
				
				plus = '.,-_[]!?*^@#&%$'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Calvin%20S
				ce = [
					'         ┌──┐┬┌─┐\│//\┌─┐─┼─┼─ ┬ O┬┌┼┐',
					'  ───    │  ││ ┌┘─ ─  │└┘─┼─┼─┌┼─┌┘└┼┐',
					'o┘   ────└──┘o o /│\  └──     └┘ ┴O└┼┘',
				]
				
				c = {
					'l': [
						'┌─┐┌┐ ┌─┐┌┬┐┌─┐┌─┐┌─┐┬ ┬┬ ┬┬┌─┬  ┌┬┐┌┐┌┌─┐┌─┐┌─┐ ┬─┐┌─┐┌┬┐┬ ┬┬  ┬┬ ┬─┐ ┬┬ ┬┌─┐' + ce[0],
						'├─┤├┴┐│   ││├┤ ├┤ │ ┬├─┤│ │├┴┐│  │││││││ │├─┘│─┼┐├┬┘└─┐ │ │ │└┐┌┘│││┌┴┬┘└┬┘┌─┘' + ce[1],
						'┴ ┴└─┘└─┘─┴┘└─┘└  └─┘┴ ┴┴└┘┴ ┴┴─┘┴ ┴┘└┘└─┘┴  └─┘└┴└─└─┘ ┴ └─┘ └┘ └┴┘┴ └─ ┴ └─┘' + ce[2]
					],
					'u': [
						'╔═╗╔╗ ╔═╗╔╦╗╔═╗╔═╗╔═╗╦ ╦╦ ╦╦╔═╦  ╔╦╗╔╗╔╔═╗╔═╗╔═╗ ╦═╗╔═╗╔╦╗╦ ╦╦  ╦╦ ╦═╗ ╦╦ ╦╔═╗' + ce[0],
						'╠═╣╠╩╗║   ║║║╣ ╠╣ ║ ╦╠═╣║ ║╠╩╗║  ║║║║║║║ ║╠═╝║═╬╗╠╦╝╚═╗ ║ ║ ║╚╗╔╝║║║╔╩╦╝╚╦╝╔═╝' + ce[1],
						'╩ ╩╚═╝╚═╝═╩╝╚═╝╚  ╚═╝╩ ╩╩╚╝╩ ╩╩═╝╩ ╩╝╚╝╚═╝╩  ╚═╝╚╩╚═╚═╝ ╩ ╚═╝ ╚╝ ╚╩╝╩ ╚═ ╩ ╚═╝' + ce[2]
					]
				}
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-2, ['i','I','.',',','!']),
					(-1, ['j','J','[',']','^','%']),
					( 1, ['q','v','x','Q','V','X','_']),
					( 2, ['#'])
				]
				
				return self.textToAscii(text, c, rules, width=3, plus=plus)
			
			def deltaCorpsPriest(self, text):
				
				for t in text:
					if not t in self.ascii_letters:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Delta%20Corps%20Priest%201
				c = [
					'   ▄████████ ▀█████████▄   ▄████████ ████████▄     ▄████████    ▄████████    ▄██████▄     ▄█    █▄     ▄█       ▄█    ▄█   ▄█▄  ▄█         ▄▄▄▄███▄▄▄▄   ███▄▄▄▄    ▄██████▄     ▄███████▄ ████████▄      ▄████████    ▄████████     ███     ███    █▄   ▄█    █▄   ▄█     █▄  ▀████    ▐████▀ ▄██   ▄    ▄███████▄  ',
					'  ███    ███   ███    ███ ███    ███ ███   ▀███   ███    ███   ███    ███   ███    ███   ███    ███   ███      ███   ███ ▄███▀ ███       ▄██▀▀▀███▀▀▀██▄ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███    ███   ███    ███ ▀█████████▄ ███    ███ ███    ███ ███     ███   ███▌   ████▀  ███   ██▄ ██▀     ▄██ ',
					'  ███    ███   ███    ███ ███    █▀  ███    ███   ███    █▀    ███    █▀    ███    █▀    ███    ███   ███▌     ███   ███▐██▀   ███       ███   ███   ███ ███   ███ ███    ███   ███    ███ ███    ███    ███    ███   ███    █▀     ▀███▀▀██ ███    ███ ███    ███ ███     ███    ███  ▐███    ███▄▄▄███       ▄███▀ ',
					'  ███    ███  ▄███▄▄▄██▀  ███        ███    ███  ▄███▄▄▄      ▄███▄▄▄      ▄███         ▄███▄▄▄▄███▄▄ ███▌     ███  ▄█████▀    ███       ███   ███   ███ ███   ███ ███    ███   ███    ███ ███    ███   ▄███▄▄▄▄██▀   ███            ███   ▀ ███    ███ ███    ███ ███     ███    ▀███▄███▀    ▀▀▀▀▀▀███  ▀█▀▄███▀▄▄ ',
					'▀███████████ ▀▀███▀▀▀██▄  ███        ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███ ████▄  ▀▀███▀▀▀▀███▀  ███▌     ███ ▀▀█████▄    ███       ███   ███   ███ ███   ███ ███    ███ ▀█████████▀  ███    ███  ▀▀███▀▀▀▀▀   ▀███████████     ███     ███    ███ ███    ███ ███     ███    ████▀██▄     ▄██   ███   ▄███▀   ▀ ',
					'  ███    ███   ███    ██▄ ███    █▄  ███    ███   ███    █▄    ███          ███    ███   ███    ███   ███      ███   ███▐██▄   ███       ███   ███   ███ ███   ███ ███    ███   ███        ███    ███  ▀███████████          ███     ███     ███    ███ ███    ███ ███     ███   ▐███  ▀███    ███   ███ ▄███▀       ',
					'  ███    ███   ███    ███ ███    ███ ███   ▄███   ███    ███   ███          ███    ███   ███    ███   ███      ███   ███ ▀███▄ ███▌    ▄ ███   ███   ███ ███   ███ ███    ███   ███        ███  ▀ ███    ███    ███    ▄█    ███     ███     ███    ███ ███    ███ ███ ▄█▄ ███  ▄███     ███▄  ███   ███ ███▄     ▄█ ',
					'  ███    █▀  ▄█████████▀  ████████▀  ████████▀    ██████████   ███          ████████▀    ███    █▀    █▀   █▄ ▄███   ███   ▀█▀ █████▄▄██  ▀█   ███   █▀   ▀█   █▀   ▀██████▀   ▄████▀       ▀██████▀▄█   ███    ███  ▄████████▀     ▄████▀   ████████▀   ▀██████▀   ▀███▀███▀  ████       ███▄  ▀█████▀   ▀████████▀ ',
					'                                                                                                           ▀▀▀▀▀▀    ▀         ▀                                                                         ███    ███                                                                                                  '
				]
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-8, ['I']),
					(-5, ['J']),
					(-3, ['L','N','Y']),
					(-2, ['C','D','O','U','V']),
					(-1, ['K','Q','T','W','Z']),
					( 2, ['H']),
					( 3, ['M','X'])
				]
				
				return self.textToAscii(text, c, rules, width=13)
			
			def block(self, text):
				
				plus  = '1234567890'
				plus += '.,:;-_[](){}¡!¿?ç'
				plus += '+*^"\'<>@#/\\|&%$ºª~¬'
				plus += 'äëïöüâêîôûáéíóúàèìòù'
				plus += 'ÄËÏÖÜÂÊÎÔÛÁÉÍÓÚÀÈÌÒÙ'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				cn = [
					'                                                                                                ',
					'   _|    _|_|    _|_|_|    _|  _|    _|_|_|_|    _|_|_|  _|_|_|_|_|    _|_|      _|_|      _|   ',
					' _|_|  _|    _|        _|  _|  _|    _|        _|                _|  _|    _|  _|    _|  _|  _| ',
					'   _|      _|      _|_|    _|_|_|_|  _|_|_|    _|_|_|          _|      _|_|      _|_|_|  _|  _| ',
					'   _|    _|            _|      _|          _|  _|    _|      _|      _|    _|        _|  _|  _| ',
					'   _|  _|_|_|_|  _|_|_|        _|    _|_|_|      _|_|      _|          _|_|    _|_|_|      _|   ',
					'                                                                                                ',
					'                                                                                                '
				]
				
				ce = [
					cn[0] + '                                             _|_|  _|_|    _|  _|        _|  _|                                                                  _|    _| _|    _|                      _|_|_|_|_|                                        _|                                                                           ',
					cn[1] + '                                             _|      _|  _|      _|    _|      _|    _|  _|      _|  _|_|      _|_|_|      _|      _|  _|  _|  _|  _|  _| _|  _|        _|  _|        _|          _|    _|  _|            _|  _|          _|    _|        _|_|    _|    _|      _|_|      _|_|_|                       ',
					cn[2] + '           _|    _|                          _|      _|  _|      _|    _|      _|        _|              _|  _|            _|        _|_|_|                           _|      _|    _|    _|_|_|  _|  _|_|_|_|_|        _|      _|        _|  _|  _|      _|_|  _|    _|_|_|  _|    _|  _|    _|    _|  _|             ',
					cn[3] + '                     _|_|_|_|_|              _|      _|  _|      _|  _|          _|  _|  _|    _|_|  _|_|    _|        _|_|_|_|_|  _|_|_|_|_|                       _|          _|  _|  _|    _|  _|    _|  _|        _|          _|      _|    _|_|  _|      _|      _|_|      _|_|      _|_|_|  _|  _|    _|_|_|_|_| ',
					cn[4] + '                                             _|      _|  _|      _|    _|      _|    _|      _|                _|_|_|      _|        _|_|_|                           _|      _|    _|    _|_|_|_|    _|_|_|_|_|    _|              _|    _|  _|    _|      _|  _|_|    _|_|                                        _| ',
					cn[5] + ' _|    _|  _|    _|                          _|      _|  _|      _|    _|      _|    _|  _|    _|_|  _|          _|        _|      _|  _|  _|                           _|  _|        _|                _|  _|    _|                  _|  _|    _|_|  _|  _|    _|_|  _|_|_|  _|_|_|_|  _|_|_|_|                       ',
					cn[6] + '     _|        _|                _|_|_|_|_|  _|_|  _|_|    _|  _|        _|  _|                                _|_|                                                                     _|_|_|_|_|_|                                      _|                            _|                                             ',
					cn[7] + '                                                                                                                                                                                                                                                                                                                       '
				]
				
				cel = [
					ce[0] + ' _|    _|  _|    _|  _|  _|  _|    _|  _|    _|      _|      _|_|      _|      _|_|      _|_|          _|        _|    _|     _|          _|    _|        _|      _|      _|        _|     ',
					ce[1] + '                                                   _|  _|  _|    _|  _|  _|  _|    _|  _|    _|      _|        _|    _|     _|          _|        _|        _|      _|      _|        _|   ',
					ce[2] + '   _|_|_|    _|_|      _|      _|_|    _|    _|              _|_|                                            _|_|                                         _|_|                             ',
					ce[3] + ' _|    _|  _|_|_|_|    _|    _|    _|  _|    _|    _|_|_|  _|_|_|_|    _|      _|_|    _|    _|    _|_|_|  _|_|_|_|  _|     _|_|    _|    _|    _|_|_|  _|_|_|_|    _|    _|_|    _|    _| ',
					ce[4] + ' _|    _|  _|          _|    _|    _|  _|    _|  _|    _|  _|          _|    _|    _|  _|    _|  _|    _|  _|        _|   _|    _|  _|    _|  _|    _|  _|          _|  _|    _|  _|    _| ',
					ce[5] + '   _|_|_|    _|_|_|    _|      _|_|      _|_|_|    _|_|_|    _|_|_|    _|      _|_|      _|_|_|    _|_|_|    _|_|_|  _|     _|_|      _|_|_|    _|_|_|    _|_|_|    _|    _|_|      _|_|_| ',
					ce[6] + '                                                                                                                                                                                           ',
					ce[7] + '                                                                                                                                                                                           '
				]
				
				ceu = [
					cel[0] + ' _|    _|  _|    _|  _|  _|  _|    _|  _|    _|    _|_|      _|_|      _|      _|_|      _|_|        _|        _|        _|      _|        _|      _|        _|      _|        _|        _|     ',
					cel[1] + '                                                 _|    _|  _|    _|  _|  _|  _|    _|  _|    _|    _|        _|        _|      _|        _|          _|        _|      _|        _|        _|   ',
					cel[2] + '   _|_|    _|_|_|_|  _|_|_|    _|_|    _|    _|            _|_|_|_|  _|_|_|    _|_|                _|_|    _|_|_|_|  _|_|_|    _|_|                _|_|    _|_|_|_|  _|_|_|    _|_|             ',
					cel[3] + ' _|    _|  _|_|_|      _|    _|    _|  _|    _|    _|_|    _|_|_|      _|    _|    _|  _|    _|  _|    _|  _|_|_|      _|    _|    _|  _|    _|  _|    _|  _|_|_|      _|    _|    _|  _|    _| ',
					cel[4] + ' _|_|_|_|  _|          _|    _|    _|  _|    _|  _|_|_|_|  _|          _|    _|    _|  _|    _|  _|_|_|_|  _|          _|    _|    _|  _|    _|  _|_|_|_|  _|          _|    _|    _|  _|    _| ',
					cel[5] + ' _|    _|  _|_|_|_|  _|_|_|    _|_|      _|_|    _|    _|  _|_|_|_|  _|_|_|    _|_|      _|_|    _|    _|  _|_|_|_|  _|_|_|    _|_|      _|_|    _|    _|  _|_|_|_|  _|_|_|    _|_|      _|_|   ',
					cel[6] + '                                                                                                                                                                                                ',
					cel[7] + '                                                                                                                                                                                                '
				]
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Block
				c = {
					'l': [
						'                                                                                                                                                                                                                                                                     ' + ceu[0],
						'           _|                        _|                _|_|            _|        _|   _|  _|        _|                                                                                _|                                                                             ' + ceu[1],
						'   _|_|_|  _|_|_|      _|_|_|    _|_|_|    _|_|      _|        _|_|_|  _|_|_|             _|  _|    _|  _|_|_|  _|_|    _|_|_|      _|_|    _|_|_|      _|_|_|  _|  _|_|    _|_|_|  _|_|_|_|  _|    _|  _|      _|  _|      _|      _|  _|    _|  _|    _|  _|_|_|_| ' + ceu[2],
						' _|    _|  _|    _|  _|        _|    _|  _|_|_|_|  _|_|_|_|  _|    _|  _|    _|  _|   _|  _|_|      _|  _|    _|    _|  _|    _|  _|    _|  _|    _|  _|    _|  _|_|      _|_|        _|      _|    _|  _|      _|  _|      _|      _|    _|_|    _|    _|      _|   ' + ceu[3],
						' _|    _|  _|    _|  _|        _|    _|  _|          _|      _|    _|  _|    _|  _|   _|  _|  _|    _|  _|    _|    _|  _|    _|  _|    _|  _|    _|  _|    _|  _|            _|_|    _|      _|    _|    _|  _|      _|  _|  _|  _|    _|    _|  _|    _|    _|     ' + ceu[4],
						'   _|_|_|  _|_|_|      _|_|_|    _|_|_|    _|_|_|    _|        _|_|_|  _|    _|  _|   _|  _|    _|  _|  _|    _|    _|  _|    _|    _|_|    _|_|_|      _|_|_|  _|        _|_|_|        _|_|    _|_|_|      _|          _|      _|      _|    _|    _|_|_|  _|_|_|_| ' + ceu[5],
						'                                                                   _|                 _|                                                    _|              _|                                                                                          _|           ' + ceu[6],
						'                                                               _|_|                 _|                                                      _|              _|                                                                                      _|_|             ' + ceu[7]
					],
					'u': [
						'                                                                                                                                                                                                                                                                                        ' + ceu[0],
						'   _|_|    _|_|_|      _|_|_|  _|_|_|    _|_|_|_|  _|_|_|_|    _|_|_|  _|    _|  _|_|_|        _|  _|    _|  _|        _|      _|  _|      _|    _|_|    _|_|_|      _|_|      _|_|_|      _|_|_|  _|_|_|_|_|  _|    _|  _|      _|  _|          _|  _|      _|  _|      _|  _|_|_|_|_| ' + ceu[1],
						' _|    _|  _|    _|  _|        _|    _|  _|        _|        _|        _|    _|    _|          _|  _|  _|    _|        _|_|  _|_|  _|_|    _|  _|    _|  _|    _|  _|    _|    _|    _|  _|            _|      _|    _|  _|      _|  _|          _|    _|  _|      _|  _|          _|   ' + ceu[2],
						' _|_|_|_|  _|_|_|    _|        _|    _|  _|_|_|    _|_|_|    _|  _|_|  _|_|_|_|    _|          _|  _|_|      _|        _|  _|  _|  _|  _|  _|  _|    _|  _|_|_|    _|  _|_|    _|_|_|      _|_|        _|      _|    _|  _|      _|  _|    _|    _|      _|          _|          _|     ' + ceu[3],
						' _|    _|  _|    _|  _|        _|    _|  _|        _|        _|    _|  _|    _|    _|    _|    _|  _|  _|    _|        _|      _|  _|    _|_|  _|    _|  _|        _|    _|    _|    _|        _|      _|      _|    _|    _|  _|      _|  _|  _|      _|  _|        _|        _|       ' + ceu[4],
						' _|    _|  _|_|_|      _|_|_|  _|_|_|    _|_|_|_|  _|          _|_|_|  _|    _|  _|_|_|    _|_|    _|    _|  _|_|_|_|  _|      _|  _|      _|    _|_|    _|          _|_|  _|  _|    _|  _|_|_|        _|        _|_|        _|          _|  _|      _|      _|      _|      _|_|_|_|_| ' + ceu[5],
						'                                                                                                                                                                                                                                                                                        ' + ceu[6],
						'                                                                                                                                                                                                                                                                                        ' + ceu[7]
					]
				}
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-6, ['i','l','.',':','¡','!','|']),
					(-5, ['j','í']),
					(-4, [',',';','[',']','(',')','\'','1','ì']),
					(-3, ['"']),
					(-2, ['I','{','}','¿','?','^','<','>','$','0','ï','î','Ï','Î','Í','Ì']),
					( 2, ['v','M','N','Q','T','V','X','Y','Z','-','_','+','*','#','/','\\','&','%','¬','7']),
					( 6, ['m','W']),
					( 8, ['@']),
					(10, ['w'])
				]
				
				return self.textToAscii(text, c, rules, width=10, plus=plus)
			
			def alligator(self, text):
				
				plus  = '1234567890'
				plus += '.,:;-_[](){}!?'
				plus += '+*^"\'<>@#/\\|&%$~'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Alligator2
				cn = [
					'  :::    ::::::::   ::::::::      :::     ::::::::::  ::::::::  :::::::::::  ::::::::   ::::::::   :::::::  ',
					':+:+:   :+:    :+: :+:    :+:    :+:      :+:    :+: :+:    :+: :+:     :+: :+:    :+: :+:    :+: :+:   :+: ',
					'  +:+         +:+         +:+   +:+ +:+   +:+        +:+               +:+  +:+    +:+ +:+    +:+ +:+  :+:+ ',
					'  +#+       +#+        +#++:   +#+  +:+   +#++:++#+  +#++:++#+        +#+    +#++:++#   +#++:++#+ +#+ + +:+ ',
					'  +#+     +#+             +#+ +#+#+#+#+#+        +#+ +#+    +#+      +#+    +#+    +#+        +#+ +#+#  +#+ ',
					'  #+#    #+#       #+#    #+#       #+#   #+#    #+# #+#    #+#     #+#     #+#    #+# #+#    #+# #+#   #+# ',
					'####### ##########  ########        ###    ########   ########      ###      ########   ########   #######  '
				]
				
				ce = [
					cn[0] + '                                         :::::: ::::::   ::: :::      :::: ::::    :::  :::::::::  ',
					cn[1] + '        :+: :+:                          :+:       :+:  :+:   :+:    :+:     :+:   :+: :+:     :+: ',
					cn[2] + '                                         +:+       +:+ +:+     +:+   +:+     +:+   +:+        +:+  ',
					cn[3] + '                +#++:++#++:++            +#+       +#+ +#+     +#+ +#+         +#+ +#+       +#+   ',
					cn[4] + '                                         +#+       +#+ +#+     +#+   +#+     +#+   +#+     +#+     ',
					cn[5] + '#+# #+# #+# #+#                          #+#       #+#  #+#   #+#    #+#     #+#                   ',
					cn[6] + '### ##      ##                ########## ###### ######   ### ###      #### ####    ###     ###     '
				]
				
				ce2 = [
					ce[0] + '                                :::     :: :: :::    ::: :::       :::::::::::       :::   :::          ::: :::       :::  :::::::     :::   :::      :::                   ',
					ce[1] + '     :+:       :+:     :+:    :+: :+:   :+ +: :+    :+:   :+:    :+: :+:+:+:+:+:     :+:   :+:         :+:   :+:      :+: :+:   :+:    :+:  :+:    :+:+:+:+:                ',
					ce[2] + '     +:+         +:+ +:+    +:+     +:+            +:+     +:+  +:+ +:+   +:+ +:+ +:+:+:+:+:+:+:+     +:+     +:+     +:+  +:+ +:+         +:+   +:+  +:+       :::::   ::: ',
					ce[3] + '+#++:++#++:++ +#++:++#++:++                       +#+       +#+ +#+ +:+   +#+ +:+    +#+   +:+       +#+       +#+    +#+   +#++:  ++#    +#+      +#++:++#+  :+:   :+:+:   ',
					ce[4] + '     +#+         +#+ +#+                           +#+     +#+  +#+ +#+   +#+ +#+ +#+#+#+#+#+#+#+   +#+         +#+   +#+  +#+ +#+#+#    +#+          +#+ +#+               ',
					ce[5] + '     #+#       #+#     #+#                          #+#   #+#    #+# #+#+#+#+#+      #+#   #+#     #+#           #+#  #+# #+#   #+#+    #+#  #+#   #+#+#+#+#                ',
					ce[6] + '                                                     ### ###       #####             ###   ###    ###             ### ###  ##########  ###   ###      ###                   '
				]
				
				c = [
					'    :::     :::::::::   ::::::::  :::::::::  :::::::::: ::::::::::  ::::::::  :::    ::: ::::::::::: :::::::::: :::    ::: :::        ::::     :::: ::::    :::  ::::::::  :::::::::   ::::::::   :::::::::   ::::::::  ::::::::::: :::    ::: :::     ::: :::       ::: :::    ::: :::   ::: ::::::::: ' + ce2[0],
					'  :+: :+:   :+:    :+: :+:    :+: :+:    :+: :+:        :+:        :+:    :+: :+:    :+:     :+:         :+:    :+:   :+:  :+:        +:+:+: :+:+:+ :+:+:   :+: :+:    :+: :+:    :+: :+:    :+:  :+:    :+: :+:    :+:     :+:     :+:    :+: :+:     :+: :+:       :+: :+:    :+: :+:   :+:      :+:  ' + ce2[1],
					' +:+   +:+  +:+    +:+ +:+        +:+    +:+ +:+        +:+        +:+        +:+    +:+     +:+         +:+    +:+  +:+   +:+        +:+ +:+:+ +:+ :+:+:+  +:+ +:+    +:+ +:+    +:+ +:+    +:+  +:+    +:+ +:+            +:+     +:+    +:+ +:+     +:+ +:+       +:+  +:+  +:+   +:+ +:+      +:+   ' + ce2[2],
					'+#++:++#++: +#++:++#+  +#+        +#+    +:+ +#++:++#   :#::+::#   :#:        +#++:++#++     +#+         +#+    +#++:++    +#+        +#+  +:+  +#+ +#+ +:+ +#+ +#+    +:+ +#++:++#+  +#+    +:+  +#++:++#:  +#++:++#++     +#+     +#+    +:+ +#+     +:+ +#+  +:+  +#+   +#++:+     +#++:      +#+    ' + ce2[3],
					'+#+     +#+ +#+    +#+ +#+        +#+    +#+ +#+        +#+        +#+   +#+# +#+    +#+     +#+         +#+    +#+  +#+   +#+        +#+       +#+ +#+  +#+#+# +#+    +#+ +#+        +#+  # +#+  +#+    +#+        +#+     +#+     +#+    +#+  +#+   +#+  +#+ +#+#+ +#+  +#+  +#+     +#+      +#+     ' + ce2[4],
					'#+#     #+# #+#    #+# #+#    #+# #+#    #+# #+#        #+#        #+#    #+# #+#    #+#     #+#     #+# #+#    #+#   #+#  #+#        #+#       #+# #+#   #+#+# #+#    #+# #+#        #+#   +#+   #+#    #+# #+#    #+#     #+#     #+#    #+#   #+#+#+#    #+#+# #+#+#  #+#    #+#    #+#     #+#      ' + ce2[5],
					'###     ### #########   ########  #########  ########## ###         ########  ###    ### ###########  #####     ###    ### ########## ###       ### ###    ####  ########  ###         ###### ### ###    ###  ########      ###      ########      ###       ###   ###   ###    ###    ###    ######### ' + ce2[6]
				]
				
				# 12 11 11 11 11 11 11 11 12 11 11 11 14
				#  A  B  C  D  E  F  G  H  I  J  K  L  M
				# 12 11 11 12 11 11 12 11 12 14 11 10 10
				#  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-7, ['.',',',':',';','!','\'','|']),
					(-5, ['(',')','"']),
					(-4, ['[',']','<','>']),
					(-3, ['1','{','}']),
					(-1, ['y','z','Y','Z','0','/','\\','%']),
					( 1, ['a','i','n','q','t','v','A','I','N','Q','T','V','4','7','?','^']),
					( 2, ['&','$']),
					( 3, ['m','w','M','W','-','+','*','~']),
					( 5, ['#']),
					( 7, ['@'])
				]
				
				return self.textToAscii(text, c, rules, width=11, plus=plus)
			
			def cybermedium(self, text):
				
				plus  = '.,:;-_!?"\'/\\|'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				ce = [
					'            | __....   / \\   | ',
					"   ..__     |  _]'''  /   \\  | ",
					'.. .,   ___ .  .     /     \\ | ',
					" '                           | "
				]
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Cybermedium
				c = [
					'____ ___  ____ ___  ____ ____ ____ _  _ _  _ _  _ _    _  _ _  _ ____ ___  ____ ____ ____ ___ _  _ _  _ _ _ _ _  _ _   _ ___  ' + ce[0],
					'|__| |__] |    |  \ |___ |___ | __ |__| |  | |_/  |    |\/| |\ | |  | |__] |  | |__/ [__   |  |  | |  | | | |  \/   \_/    /  ' + ce[1],
					'|  | |__] |___ |__/ |___ |    |__] |  | | _| | \_ |___ |  | | \| |__| |    |_\| |  \ ___]  |  |__|  \/  |_|_| _/\_   |    /__ ' + ce[2],
					'                                                                                                                              ' + ce[3]
				]
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-4, ['.',':',';']),
					(-3, ['i','I',',','!','"','\'','|']),
					(-2, ['j','J','-','?']),
					(-1, ['t','T','_','/','\\']),
					( 1, ['w','y','W','Y'])
				]
				
				return self.textToAscii(text, c, rules, width=5, plus=plus)
			
			def dobleShorts(self, text):
				
				plus = '.,()!?"\'#%'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				ce = [
					'       _   _  __ ____    //  __ __     _  ',
					"      ((   )) || '_// //    =||=||= O //  ",
					'|| //  \\\\ //  ..  ||         || ||   // O '
				]
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Double%20Shorts
				c = [
					' ___  ____   ____ _____  _____ _____  ____  __  __ __    __ __ __ __    ___  __ __  __  _____  _____  _____  _____   __ ____ __ __ __ __ __    __ _  _ _  _ ____  ' + ce[0],
					'||=|| ||=)  ((    ||  )) ||==  ||==  (( ___ ||==|| ||    || ||<<  ||    || \\/ | ||\\\\|| ((   )) ||_// ((   )) ||_//  ((   ||  || || \\\\ // \\\\ /\\ // \\\\// \\\\//   //  ' + ce[1],
					'|| || ||_))  \\\\__ ||_//  ||___ ||     \\\\_|| ||  || || |__|| || \\\\ ||__| ||    | || \\||  \\\\_//  ||     \\\\_/X| || \\\\ \\_))  ||  \\\\_//  \\V/   \\V/\\V/  //\\\\  //   //__ ' + ce[2]
				]
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-3, ['i','I','.',',','!','"','\'']),
					(-2, ['(',')']),
					(-1, ['s','t','x','y','S','T','X','Y','?']),
					( 1, ['d','g','h','n','D','G','H','N']),
					( 2, ['m','o','q','M','O','Q','#']),
					( 3, ['w','W'])
				]
				
				return self.textToAscii(text, c, rules, width=6, plus=plus)
			
			def doble(self, text):
				
				plus = '.,()!?"\'#%'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				ce = [
					'        _ _   __ ____   _ //  __ __     _ ',
					'       // \\\\  || |  \\\\ //     || ||  O // ',
					'      ((   )) ||   _//       =||=||=  //  ',
					'|| //  \\\\ //  ..   ||         || ||  // O ',
					'                                          '
				]
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Double
				c = [
					'  ___  ____    ___ ____    ____  ____   ___  __  __ __    __ __ __ __    ___  ___ __  __   ___   ____    ___   ____   __  ______ __ __ __ __ __    __ _   _ _  _ ____ ' + ce[0],
					' // \\\\ || ))  //   || \\\\  ||    ||     // \\\\ ||  || ||    || || // ||    ||\\\\//|| ||\\ ||  // \\\\  || \\\\  // \\\\  || \\\\ (( \\ | || | || || || || ||    || \\\\ // \\\\//   // ' + ce[1],
					' ||=|| ||=)  ((    ||  )) ||==  ||==  (( ___ ||==|| ||    || ||<<  ||    || \\/ || ||\\\\|| ((   )) ||_// ((   )) ||_//  \\\\    ||   || || \\\\ // \\\\ /\\ //  )X(   )/   //  ' + ce[2],
					' || || ||_))  \\\\__ ||_//  ||___ ||     \\\\_|| ||  || || |__|| || \\\\ ||__| ||    || || \\||  \\\\_//  ||     \\\\_/X| || \\\\ \\_))   ||   \\\\_//  \\V/   \\V/\\V/  // \\\\ //   //__ ' + ce[3],
					'                                                                                                                                                                     ' + ce[4]
				]
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-3, ['i','I','.',',','!','"','\'']),
					(-2, ['(',')']),
					(-1, ['s','y','z','S','Y','Z','%']),
					( 1, ['a','d','g','h','n','t','A','D','G','H','N','T']),
					( 2, ['o','q','O','Q','#']),
					( 3, ['m','w','M','W'])
				]
				
				return self.textToAscii(text, c, rules, width=6, plus=plus)
			
			def not_lean(self, text):
				
				plus = '.,()!?"\'#%'
				
				for t in text:
					if not t in self.ascii_letters+plus:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				ce = [
					'        _ _   __ ____   _ //  __ __     _ ',
					'       // \\\\  || |  \\\\ //     || ||  O // ',
					'      ((   )) ||   _//       =||=||=  //  ',
					'|| //  \\\\ //  ..   ||         || ||  // O ',
					'                                          '
				]
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Double
				c = {
					'l': [
						'                                                                                                                                                                                                                                                                       ',
						'             _/                        _/                _/_/            _/        _/  _/  _/        _/                                                                                _/                                                                              ',
						'    _/_/_/  _/_/_/      _/_/_/    _/_/_/    _/_/      _/        _/_/_/  _/_/_/            _/  _/    _/  _/_/_/  _/_/    _/_/_/      _/_/    _/_/_/      _/_/_/  _/  _/_/    _/_/_/  _/_/_/_/  _/    _/  _/      _/  _/      _/      _/  _/    _/  _/    _/  _/_/_/_/   ',
						' _/    _/  _/    _/  _/        _/    _/  _/_/_/_/  _/_/_/_/  _/    _/  _/    _/  _/  _/  _/_/      _/  _/    _/    _/  _/    _/  _/    _/  _/    _/  _/    _/  _/_/      _/_/        _/      _/    _/  _/      _/  _/      _/      _/    _/_/    _/    _/      _/      ',
						'_/    _/  _/    _/  _/        _/    _/  _/          _/      _/    _/  _/    _/  _/  _/  _/  _/    _/  _/    _/    _/  _/    _/  _/    _/  _/    _/  _/    _/  _/            _/_/    _/      _/    _/    _/  _/      _/  _/  _/  _/    _/    _/  _/    _/    _/         ',
						' _/_/_/  _/_/_/      _/_/_/    _/_/_/    _/_/_/    _/        _/_/_/  _/    _/  _/  _/  _/    _/  _/  _/    _/    _/  _/    _/    _/_/    _/_/_/      _/_/_/  _/        _/_/_/        _/_/    _/_/_/      _/          _/      _/      _/    _/    _/_/_/  _/_/_/_/      ',
						'                                                                _/                _/                                                    _/              _/                                                                                          _/                 ',
						'                                                           _/_/                _/                                                      _/              _/                                                                                      _/_/                    '
					],
					'u': [
						'                                                                                                                                                                                                                                                                                             ',
						'      _/_/    _/_/_/      _/_/_/  _/_/_/    _/_/_/_/  _/_/_/_/    _/_/_/  _/    _/  _/_/_/        _/  _/    _/  _/        _/      _/  _/      _/    _/_/    _/_/_/      _/_/      _/_/_/      _/_/_/  _/_/_/_/_/  _/    _/  _/      _/  _/          _/  _/      _/  _/      _/  _/_/_/_/_/   ',
						'   _/    _/  _/    _/  _/        _/    _/  _/        _/        _/        _/    _/    _/          _/  _/  _/    _/        _/_/  _/_/  _/_/    _/  _/    _/  _/    _/  _/    _/    _/    _/  _/            _/      _/    _/  _/      _/  _/          _/    _/  _/      _/  _/          _/      ',
						'  _/_/_/_/  _/_/_/    _/        _/    _/  _/_/_/    _/_/_/    _/  _/_/  _/_/_/_/    _/          _/  _/_/      _/        _/  _/  _/  _/  _/  _/  _/    _/  _/_/_/    _/  _/_/    _/_/_/      _/_/        _/      _/    _/  _/      _/  _/    _/    _/      _/          _/          _/         ',
						' _/    _/  _/    _/  _/        _/    _/  _/        _/        _/    _/  _/    _/    _/    _/    _/  _/  _/    _/        _/      _/  _/    _/_/  _/    _/  _/        _/    _/    _/    _/        _/      _/      _/    _/    _/  _/      _/  _/  _/      _/  _/        _/        _/            ',
						'_/    _/  _/_/_/      _/_/_/  _/_/_/    _/_/_/_/  _/          _/_/_/  _/    _/  _/_/_/    _/_/    _/    _/  _/_/_/_/  _/      _/  _/      _/    _/_/    _/          _/_/  _/  _/    _/  _/_/_/        _/        _/_/        _/          _/  _/      _/      _/      _/      _/_/_/_/_/       ',
						'                                                                                                                                                                                                                                                                                             ',
						'                                                                                                                                                                                                                                                                                             '
					]
				}
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					
				]
			
			def morse(self, text): pass
			
			def rammstein(self, text):
				
				for t in text:
					if not t in self.ascii_letters:
						error_msg = repr(text) + ' --> ' + t
						raise self.NotSupportedError(error_msg) 
				
				# URL: http://patorjk.com/software/taag/#p=display&f=Rammstein
				c = {
					'l': [
						'                                                                                                                                                                                                                    ',
						' ____    ______  ______  _____   ______  ______  ______  __   _  ____    ____  __  __  ____    ____    __  ____   _  _____  _____  _____   _____   ______    __    __   _  __    _ __  __  __  __ __ __    _ ______ ',
						'|    \  |      >|   ___||     \ |   ___||   ___||   ___||  |_| ||    |  |    ||  |/ / |    |  |    \  /  ||    \ | |/     \|     |/     \ |     | |   ___| _|  |_ |  | | |\  \  //|  \/  \|  | \ ` / \ \  //|___   |',
						'|     \ |     < |   |__ |      \|   ___||   ___||   |  ||   _  ||    | _|    ||     \ |    |_ |     \/   ||     \| ||     ||    _||     | |     \  `-.`-. |_    _||  |_| | \  \// |     /\   | /   \  \ \//  .-`.-` ',
						'|__|\__\|______>|______||______/|______||___|   |______||__| |_||____||______||__|\__\|______||__/\__/|__||__/\____|\_____/|___|  \___/\_\|__|\__\|______|  |__|  |______|  \__/  |____/  \__|/__/\_\ /__/  |______|',
						'                                                                                                                                                                                                                    ',
						'                                                                                                                                                                                                                    '
					],
					'u': [
						'    _____        _____        _____        _____        _____        _____        _____        _____        _____          _____        _____        _____         _____         _____        _____        _____        _____        _____        _____         _____        _____        _____         _____        _____        _____        _____    ',
						' __|_    |__  __|___  |__  __|___  |__  __|__   |__  __|___  |__  __|___  |__  __|___  |__  __|  _  |__  __|_    |__    __|_    |__  __| __  |__  __|_    |__  ___|    _|__  ___|   _ |__  __|__   |__  __|__   |__  __|__   |__  __|__   |__  __|___  |__  ___|__   |__  __|  _  |__  __|   _ |__  ___|__  _|__  __|__   |__ ___|  _  |__  __|___  |__ ',
						'|    \      ||      >    ||   ___|    ||     \     ||   ___|    ||   ___|    ||   ___|    ||  |_| |    ||    |      |  |    |      ||  |/ /     ||    |      ||    \  /  | ||    \ | |   |/     \     ||     |     |/     \     ||     |     ||   ___|    ||_    _|     ||  | | |    |\  \  //    ||  \/  \|  | | \ ` /      |\ \  //     ||___   |    |',
						'|     \     ||     <     ||   |__     ||      \    ||   ___|    ||   ___|    ||   |  |    ||   _  |    ||    |      | _|    |      ||     \     ||    |_     ||     \/   | ||     \| |   ||     |     ||    _|     ||     |     ||     \     | `-.`-.     | |    |      ||  |_| |    ||\  \//     ||     /\   | | /   \      ||\ \//      | .-`.-`     |',
						'|__|\__\  __||______>  __||______|  __||______/  __||______|  __||___|     __||______|  __||__| |_|  __||____|    __||______|    __||__|\__\  __||______|  __||__/\__/|__|_||__/\____| __|\_____/   __||___|     __|\___/\_\  __||__|\__\  __||______|  __| |____|    __||______|  __||_\__/    __||____/  \__|_|/__/\_\   __||/__/     __||______|  __|',
						'   |_____|      |_____|      |_____|      |_____|      |_____|      |_____|      |_____|      |_____|      |_____|        |_____|      |_____|      |_____|       |_____|       |_____|      |_____|      |_____|      |_____|      |_____|      |_____|       |_____|      |_____|      |_____|       |_____|      |_____|      |_____|      |_____|   ',
						'                                                                                                                                                                                                                                                                                                                                                        '
					]
				}
				
				# Reglas de desplazamiento para letras que no tienen el ancho por defecto
				rules = [
					(-2, ['i']),
					(-1, ['o','p','x','y']),
					( 2, ['n']),
					( 4, ['m','w']),
					( 5, ['A','B','C','D','E','F','G','H','I','K','L','O','P','Q','R','S','U','V','X','Y','Z']),
					( 6, ['M','N','T','W']),
					( 7, ['J'])
				]
				
				return self.textToAscii(text, c, rules, width=8)
		
		class DoomsdayRule:		# Algoritmo de doomsday. Permite saber de cualquier fecha (pasado o futuro) en que día de la semana caerá. Permite crear un calendario de cualquier año con cuentas mentales simples de aritmetica. Esto se puede realizar mentalmente, es fantástico.
			#
			#  ██████╗  ██████╗  ██████╗ ███╗   ███╗███████╗██████╗ ██╗  ██╗██╗   ██╗
			#  ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║██╔════╝██╔══██╗██║  ██║╚██╗ ██╔╝
			#  ██║  ██║██║   ██║██║   ██║██╔████╔██║███████╗██║  ██║███████║ ╚████╔╝ 
			#  ██║  ██║██║   ██║██║   ██║██║╚██╔╝██║╚════██║██║  ██║╚════██║  ╚██╔╝  
			#  ██████╔╝╚██████╔╝╚██████╔╝██║ ╚═╝ ██║███████║██████╔╝     ██║   ██║   
			#  ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═════╝      ╚═╝   ╚═╝   
			#                                                         By: LawlietJH
			#                                                               v1.0.6
			# Fuente: 'ANSI Shadow' - Desde: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Doomsd4y

			class MonthDoesNotExist(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			class InvalidDate(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			def __init__(self):
				self.weekdays = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
				self.msgError  = 'La Fecha {} no es valida. Modo de Uso: Día/Mes/Año o Día-Mes-Año.'
				
				self.learnToDoItMentally = '''
				\r # Regla del fin del mundo (Doomsday Rule):
				
				Algoritmo de Doomsday.					Domingo, 29 de Septiembre del 2019
													Por: LawlietJH

				--------------------------------------------------------------------------------------------
				El Algoritmo de Doomsday fue creado por el Matematico John Horton Conway
				(Creador tambien del Juego de la Vida).

				Este algoritmo nos permite saber en que día de la semana cae cualquier día de cualquier
				año del pasado o del futuro.

				Primeramente aprenderemos con este tutorial a hacerlo de forma mental, aunque
				parece complicado, es demasiado sencillo.

				Primero Aprenderemos a saber en que día de la semana cae cualquier fecha de 1 solo año,
				en este caso nos basaremos en el actual escrito esto, 2019.

				Sección 1: Aprendiendo a Desplazarnos en el año actual para ya
				no necesitar ver un calendario jamas.

				--------------------------------------------------------------------------------------------

				Parte 1: El Doomsday es el ultimo día de febrero, si el ultimo día de febrero
				(supongamos que es el 28) fue Jueves, entonces todos los Jueves de ese mismo
				año son Doomsday.

				El Doomsday de este año, 2019, es Jueves.

				-----------------------------------------------
				Calendario de Doomsdays -----------------------
				-----------------------------------------------
					Mes		| Día
				 1- Enero	| 3  o  4 en bisiesto
				 2- Febrero	| 28 o 29 en bisiesto <- Base
				 3- Marzo	| 7
				 4- Abril	| 4
				 5- Mayo	| 9
				 6- Junio	| 6
				 7- Julio	| 11
				 8- Agosto	| 8
				 9- Septiembre	| 5
				10- Octubre	| 10
				11- Noviembre	| 7
				12- Diciembre	| 12
				------------------------------------------------

				Para comprenderlo mejor lo dividimos en 3 secciones:

				Sección 1: Primeros 3 meses --------------------

				 1 - Enero	| 3   o  4 en bisiesto
				 2 - Febrero	| 28  o 29 en bisiesto <- Base
				 3 - Marzo	| 7

				Sección 2: Pares -------------------------------

				 4 - Abril	| 4
				 6 - Junio	| 6
				 8 - Agosto	| 8
				10 - Octubre	| 10
				12 - Diciembre	| 12

				Sección 3: Impares -----------------------------
				5 -> 9, 7 -> 11 y viceversa 9 -> 5 y 11 -> 7. O sea:
				Mes  5 -> Día 9
				Mes  7 -> Día 11
				Mes  9 -> Día 5
				Mes 11 -> Día 7

				 5 - Mayo	| 9
				 7 - Julio	| 11
				 9 - Septiembre	| 5
				11 - Noviembre	| 7

				------------------------------------------------

				Todos los días registrados a la derecha del mes, son Doomsday, para saber cualquier día
				del mes, solo basta recordar el día de doomsday base de cada mes y desplazarse.

				------------------------------------------------------------------------------------------------

				Parte 2: Días del Mes.

				Los meses tienen 31, 30, 31, 30, 31, 30 días...

				Enero   31
				Febrero 28 o 29    <- Siguiendo la secuencia febrero seria 30 pero se pone el correspondiente.
				Marzo   31
				Abril   30
				Mayo    31
				Junio   30
				Julio   31
				---------- <- Reinicio, Ahora se inicia de nuevo con 31.
				Agosto  31
				Septiem 30
				Octubre 31
				Noviemb 30
				Diciemb 31

				--------------------------------------------------------------------------------------------

				Parte 3: Qué años son bisiestos?

				Si el año es multiplo de 4 entonces es bisiesto.
				Los multiplos de 100 no lo son pero de 400 si.

				Entones:

				Los años 4 8 12 16 20... etc., son bisiestos
				Los años 100, 200, 300, 500, 600, 700, 900, 1000... etc., no lo son.
				Los años 400, 800, 1200, 1600, 2000, 2400... etc., si son bisiestos.

				por lo tanto como ejemplos los años 2020, 1996, 2012 son bisiestos.

				--------------------------------------------------------------------------------------------

				Una vez dominada esta seccion que es fundamental. Pasaremos a saber cual es el Doomsday 
				de cualquier año ya sea del pasado o del futuro.

				Practiquemos un poco, estamos en el año 2019 y su Doomsday es Jueves,
				entoneces la fecha 29 de Septiembre se sacaría de la siguiente manera:

				Sabemos que el día doomsday base de Semptiembre (el mes número 9) es
				el día 5, lo que significa que el día 5 fue Jueves y los días 12, 19 y 26
				también lo son, ahora solo nos desplazamos y encontramos que el día 29 es Domingo.

				Ahora que lo comprendemos mejor, hagamos otros.

				* El día 19 de Julio de 2019.
				Doomsdays de Julio: 4, 11 (Base), 18, 25.
				Entonces el 19 de Julio fue un día Viernes.

				* El día 23 de Diciembre de 2019.
				Doomsdays de Abril: 5, 12 (Base), 19, 26.
				Entonces el 23 de Abril fue un día Lunes.

				* El día 9 de Enero de 2019. No es bisiesto.
				Doomsdays de Enero: 3 (Base), 10, 17, 24, 31.
				Entonces el 9 de Enero fue un día Miércoles.

				--------------------------------------------------------------------------------------------

				Sección 2: Como saber el doomsday de cualquier año del pasado o futuro.

				Parte 1: -------------------------------------------

				Se debe tomar el año que se desea analizar, tomemos como ejemplo este año, el 2019.

				lo dividimos en 2 partes, la parte de los siglos y la parte de las décadas por decirlo así.

				Siglo-1  Décadas
				  20       19

				Tomamos la primera parte (el numero 20) y aplicamos modulo 4 (el modulo es el residuo de una división).

				por ejemplo 13 % 4 (13 modulo 4) su resultado es 1, porque 13 / 4 es = 3 y sobra 1.
				entones: 20 % 4 (20 modulo 4) su resultado es 0, porque 20 / 4 es = 5 y sobran 0.

				Entonces observemos lo siguiente:
				Si el modulo da como resultado lo siguiente se tomará como base el día indicado.
				A esto el podemos llamar Doomsday base del Siglo.

				0 - Martes.
				1 - Domingo.
				2 - Viernes.
				3 - Miércoles.

				Entonces del siglo, obtenemos que su base es Martes.

				Parte 2: -------------------------------------------

				Ahora sacamos el Doomsday base de la década, en este caso es el año 19.

				Primero dividimos el año entre 12 y el resultado se acumula.
				Segundo acumulamos el residuo.
				Tercero al residuo le hacemos una división entre 4 y se acumula. 

				Y al resultado de todo lo acumulado le aplicamos modulo 7.

				Ejemplo:

				19 / 12 = 1
				19 % 12 = 7
				 7 /  4 = 1
				Total   = 9

				 9 %  7 = 2

				Ahora que tenemos el resultado 2, este se lo sumamos a el Doomsday base del siglo:

				Base del siglo-1: Martes.

				Martes + 2 días = Jueves.

				Entonces el último día de Febrero del año 2019 fue Jueves.

				Ahora tenemos el Doomsday base del año 2019 para sacar cualquier fecha de ese año.

				--------------------------------------------------------------------------------------------
				--------------------------------------------------------------------------------------------
				--------------------------------------------------------------------------------------------

				Ahora veremos ejemplos prácticos utilizando todo el algoritmo:

				--------------------------------------------------
				* Fecha: 23 de Octubre de 1993.

				19 % 4 = 3 = Miércoles.

				93 / 12 = 7
				93 % 12 = 9
				 9 /  4 = 2
				 Total  = 18
				18 %  7 = 4

				Miércoles + 4 días = Domingo.

				Doomsday del año 1993: Domingo.
				Doomsdays de Octubre: 3, 10 (Base), 17, 24, 31.

				El Día 23 de Octubre de 1993 fue Sábado.
				--------------------------------------------------
				--------------------------------------------------
				--------------------------------------------------
				* Fecha: 5 de Mayo de 2055.

				20 % 4 = 0 = Martes.

				55 / 12 = 4
				55 % 12 = 7
				 7 /  4 = 1
				 Total  = 12
				12 %  7 = 5

				Martes + 5 días = Domingo.

				Doomsday del año 2055: Domingo.
				Doomsdays de Mayo: 2, 9 (Base), 16, 23, 30.

				El Día 5 de Mayo de 2055 será Miercoles.
				--------------------------------------------------

				Así de simple. El Algoritmo Jamás Falla, Haz la prueba. Happy Huntig!

				--------------------------------------------------------------------------------------------
				'''
				
				self.learnToDoItMentally = self.learnToDoItMentally.replace('				', ' ')
				
				self.use = '''
				\r Clase: DoomsdayRule          # Algoritmo de Doomsday (Doomsday Rule)
				\r |
				\r + Descripción: 
				\r |    
				\r |    Regla del fin del mundo (Doomsday Rule):
				\r |    
				\r |    La regla del día del juicio final (Doomsday rule
				\r |    o Doomsday algorithm, en inglés) es un método
				\r |    para el cálculo del día de la semana en el que
				\r |    cae una fecha determinada, optimizado para el
				\r |    cálculo mental. Se basa principalmente en el
				\r |    hecho de que ciertos conjuntos de fechas comparten,
				\r |    dentro de un mismo año, el día de la semana en
				\r |    el que caen.
				\r |    
				\r |    El algoritmo fue creado por el matemático inglés
				\r |    John Conway y publicado en 1982.
				\r |    
				\r |    Este código lo hice en homenaje a 'John Horton Conway'
				\r |    creador del mismo.
				\r |    
				\r |    John Horton Conway ​​​fue un prolífico matemático
				\r |    británico, especialista en la teoría de grupos,
				\r |    teoría de nudos, teoría de números, teoría de
				\r |    juegos y teoría de códigos.
				\r |    
				\r |    El 11 de abril de 2020, a los 82 años, murió de
				\r |    complicaciones por COVID-19.
				\r |    
				\r |    Dato curioso: El algoritmo es lo suficientemente
				\r |    simple como para poder calcularlo mentalmente.
				\r |    Conway normalmente podía dar la respuesta correcta
				\r |    en menos de dos segundos. Para mejorar su velocidad,
				\r |    practicó sus cálculos de calendario en su computadora,
				\r |    que estaba programada para hacerle preguntas con
				\r |    fechas aleatorias cada vez que se conectaba. Por
				\r |    ello y en forma de homenaje replique el algoritmo.
				\r |    
				\r + Ejemplo de uso: 
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    date = '22/07/2050'
				\r |    weekday = utils.Utilities.DoomsdayRule.getWeekday(date)
				\r |    print(date + ': ' + weekday)
				\r |    
				\r |    # El resultado es: '22/07/2050: Viernes'
				\r |    
				\r |    # Si deseas replicar el algoritmo de forma mental, es
				\r |    # muy simple, las instrucciones las puedes ver
				\r |    # con la siguiente función:
				\r |    utils.Utilities.DoomsdayRule.learnToDoItMentally()
				\r |    
				\r |    # Para obtener una fecha aleatoria y prácticar:
				\r |    utils.Utilities.DoomsdayRule.getRandomDate()
				\r \\
				'''
			
			def isLeapYear(self, year):									# Analiza si el año es bisiesto.
				if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
					return True
				return False
			
			def getCenturyBaseDay(self, year):							# Obtiene el día base del siglo.
				century = year // 100
				if   century % 4 == 0: return 2
				elif century % 4 == 1: return 0
				elif century % 4 == 2: return 5
				elif century % 4 == 3: return 3
			
			def getBaseDayOfDecade(self, year):							# Obtiene el día base de la decada.
				baseDay = year % 100
				part1 = baseDay // 12
				part2 = baseDay % 12
				part3 = part2 // 4
				parts = part1 + part2 + part3
				return parts % 7
			
			def isValidDate(self, day, month, isLeapYear):					# Comprobamos si la fecha solicitada es valida.
				if (month == 1  and day >= 1 and day <= 31)\
				or (month == 2  and day >= 1 and day <=(28 if not isLeapYear else 29))\
				or (month == 3  and day >= 1 and day <= 31)\
				or (month == 4  and day >= 1 and day <= 30)\
				or (month == 5  and day >= 1 and day <= 31)\
				or (month == 6  and day >= 1 and day <= 30)\
				or (month == 7  and day >= 1 and day <= 31)\
				or (month == 8  and day >= 1 and day <= 31)\
				or (month == 9  and day >= 1 and day <= 30)\
				or (month == 10 and day >= 1 and day <= 31)\
				or (month == 11 and day >= 1 and day <= 30)\
				or (month == 12 and day >= 1 and day <= 31):
					return True
				return False
			
			def getDateValues(self, date):
				date = date.replace(' ', '')
				date = date.replace('-', '/')
				date = date.replace('.', '/')
				date = date.replace('_', '/')
				date = date.replace(',', '/')
				date = date.replace('|', '/')
				date = date.replace('\\', '/')
				date = date.split('/')
				if len(date) == 3:
					day, month, year = date
					return int(day), month, int(year)
				else:
					return None, None, None
			
			def getMonthValue(self, month):
				month = month.lower()
				try:
					month = int(month)
					if 1 <= month <= 12:
						return month
					else:
						raise self.MonthDoesNotExist('El mes ' + repr(month) + ' no existe.')
				except:
					if   month == 'enero'      or mes == 'ene': return 1
					elif month == 'febrero'    or mes == 'feb': return 2
					elif month == 'marzo'      or mes == 'mar': return 3
					elif month == 'abril'      or mes == 'abr': return 4
					elif month == 'mayo'       or mes == 'may': return 5
					elif month == 'junio'      or mes == 'jun': return 6
					elif month == 'julio'      or mes == 'jul': return 7
					elif month == 'agosto'     or mes == 'ago': return 8
					elif month == 'septiembre' or mes == 'sep': return 9
					elif month == 'octubre'    or mes == 'oct': return 10
					elif month == 'noviembre'  or mes == 'nov': return 11
					elif month == 'diciembre'  or mes == 'dic': return 12
					else:
						raise self.MonthDoesNotExist('El mes ' + repr(month) + ' no existe.')
			
			def calculateWeekday(self, day, month, isLeapYear, doomsday):
				# Estos dias son doomsdays base de cada mes:
				# Ene = 3/4		May = 9		Sep = 5
				# Feb = 28/29	Jun = 6		Oct = 10
				# Mar = 7		Jul = 11	Nov = 7
				# Abr = 4		Ago = 8		Dic = 12
				
				months = [3, 28, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
				m_pos  = months[month-1] + (1 if isLeapYear and month in [1, 2] else 0)
				d_sum  = (day - (m_pos))
				res    = (28 + d_sum)
				return (doomsday + res) % 7
			
			def getWeekday(self, date='31/12/2050', raw=False):
				
				day, month, year = self.getDateValues(date)
				if day == None:
					raise self.InvalidDate(self.msgError.format(repr(date)))
				
				month = self.getMonthValue(month)
				isLeapYear = self.isLeapYear(year)
				isValidDate = self.isValidDate(day, month, isLeapYear)
				
				if not isValidDate:
					raise self.InvalidDate(self.msgError.format(repr(date)))
				
				BaseC = self.getCenturyBaseDay(year)
				BaseD = self.getBaseDayOfDecade(year)
				doomsday = (BaseC + BaseD) % 7
				weekday = self.calculateWeekday(day, month, isLeapYear, doomsday)
				
				if raw:
					return weekday
				else:
					return self.weekdays[weekday]
			
			def getRandomDate(self, lvl=0):
				
				if lvl == 0: yi, ye = 1900, 2050
				if lvl == 1: yi, ye = 1800, 2100
				if lvl == 2: yi, ye = 1500, 2200
				if lvl == 3: yi, ye = 1000, 2300
				if lvl == 4: yi, ye =  500, 2500
				if lvl == 5: yi, ye =    0, 3000
				
				day   = random.randint(1, 31)
				month = random.randint(1, 12)
				year  = random.randint(yi, ye)
				isLeapYear = self.isLeapYear(year)
				
				while not self.isValidDate(day, month, isLeapYear):
					day -= 1
				
				date = '{:02d}/{:02d}/{:04d}'.format(day, month, year)
				weekday = self.getWeekday(date, raw=True)
				response = ''
				
				t_init = time.perf_counter()
				qty = 0
				weekdays = {
					'd':0, 'l':1, 'm':2, 'x':3, 'j':4, 'v':5, 's':6,
					0:'d', 1:'l', 2:'m', 3:'x', 4:'j', 5:'v', 6:'s',
					'domingo':0, 'lunes':1, 'martes':2, 'miercoles':3, 'miércoles':3,
					'jueves':4, 'viernes':5, 'sabado':6, 'sábado':6
				}
				
				while True:
					
					t = time.perf_counter()
					
					if qty == 5:
						s = self.weekdays[weekday]
						l = weekdays[weekday]
						print(' La respuesta era: {} ({})'.format(s, l))
						print(' Tardaste en responder: {:.2f}'.format(t-t_init))
						break
					
					print(' Fecha: {} Día: '.format(date), end='')
					res = input().lower()
					
					try:
						wd = weekdays[res]
					except:
						qty += 1
						continue
					
					if wd == weekday:
						print(' Tardaste en responder: {:.2f}'.format(t-t_init))
						break
					else:
						qty += 1
		
		class Images:
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
			
			def convertFromCv2ToImage(self, img):
				# return PIL.Image.fromarray(img)
				return PIL.Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
			
			def convertFromImageToCv2(self, img):
				# return numpy.asarray(img)
				return cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
			
			def screenshot(self, img_type=''):
				ss = PIL.ImageGrab.grab()
				if img_type.lower() in ['cv2', 'numpy', 'np', 'array', 'cv']:
					return self.convertFromImageToCv2(ss)
				else:
					return ss
			
			def cropImage(self, img, pos: dict):
				# pos = {
				#	 'x': (340, 420),
				#	 'y': (810, 840)
				# }
				if img.__class__.__name__ == 'Image':
					return img.crop((
						pos['x'][0],
						pos['y'][0],
						pos['x'][1],
						pos['y'][1]
					))
				elif img.__class__.__name__ == 'ndarray':
					return img[
						pos['y'][0] : pos['y'][1],
						pos['x'][0] : pos['x'][1]
					]
			
			# Devuelve el porcentaje de similitud entre 2 imagenes del mismo tamaño y tipo
			def compare(self, cv2img1, cv2img2):
				
				img1 = self.convertFromCv2ToImage(cv2img1)
				img2 = self.convertFromCv2ToImage(cv2img2)
				
				assert img1.mode == img2.mode, "Different kinds of images."
				assert img1.size == img2.size, "Different sizes."
				
				pairs = zip(img1.getdata(), img2.getdata())
				
				if len(img1.getbands()) == 1:
					# for gray-scale jpegs
					dif = sum(abs(p1-p2) for p1,p2 in pairs)
				else:
					dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
				
				ncomponents = img1.size[0] * img1.size[1] * 3
				
				return round(100 - ((dif / 255.0 * 100) / ncomponents), 2)
			
			# get grayscale image
			def get_grayscale(self, image):
				return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			
			# noise removal
			def remove_noise(self, image):
				return cv2.medianBlur(image,5)
			
			# thresholding:
			def thresholding(self, gray_image):
				return cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
			
			# Finding histogram
			def histogram(self, gray_image):
				return cv2.calcHist([gray_image], [0],
									None, [256], [0, 256])
			
			#dilation
			def dilate(self, image):
				kernel = numpy.ones((5,5),numpy.uint8)
				return cv2.dilate(image, kernel, iterations = 1)
			
			#erosion
			def erode(self, image):
				kernel = numpy.ones((5,5),numpy.uint8)
				return cv2.erode(image, kernel, iterations = 1)
			
			#opening - erosion followed by dilation
			def opening(self, image):
				kernel = numpy.ones((5,5),numpy.uint8)
				return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
			
			#canny edge detection
			def canny(self, image):
				return cv2.Canny(image, 100, 200)
		
		class NumberSystems:	# Permite hacer conversiones entre distintos sistemas numericos.
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
			
			def decimalToBinary(self, decimal, raw=False):
				#------------------------
				# Método Manual:
				#out = ''
				#res = decimal
				#while res > 0:
				#	bit  = res%2
				#	out += str(bit)
				#	res  = (res//2)
				#if not out: out = '0'
				#return out[::-1]
				#------------------------
				# Método Python:
				binary = bin(decimal)
				if raw: binary = str(binary)[2:]
				return binary
			
			def binaryToDecimal(self, binary):
				#------------------------
				# Método Manual:
				# ~ print(binary.__class__.__name__)
				# ~ if binary.__class__.__name__:
					
				# ~ for bit in binary:
					
				#------------------------
				# Método Python:
				try:
					decimal = int(binary, 2)
				except:
					decimal = int(str(binary), 2)
				return decimal
		
		class UBZ2:			# Algoritmo de compresión y descompresión de archivos bz2. El nombre se refiere a Utils BZ2.
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				# Icono de Navi de Zelda en Pixel Art (de mi autoria). Esta en bz2.
				self.iconFile = b'BZh91AY&SY\xc8z\xbe\x10\x00\x01\x9d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x18?\x01\xb1\x8b\xd8\xd5}\xbe\x1d-\x88\xbb\xba\xe1\xabmv}\xef\xbd\xae,\xe9M4\x07\xbbti\xa0\x03@\xd0P\xdf\x03\xdc\xf3{\x8e\x80|\xa0\x00\xed\xee\x0ct{}\xf7\xc0dI\x91\t\x93 \xa7\xa4\xda\x8c5\r\x0fS\xd3(\x1az\x8c\x86F&\xd1<(\xd0\xc9\xeaa6\xa6\xd4i\x91\xe8M\xa8\xf4h\x10z\x8c4&@\r=OI\xe8\x9a\x19\x06\x9e\xa0\xd04i\xea2\x06\x9e\x88\xd3A\xa6\x86\x9a4\xd3@4\xd0\xc43\xca\x83D\x93#S\xc0\x98\x86\x99\x00\xd0\x10\xd2zh\x9am\x13(z\x9a\x06\x9e\xa3\xd42\x9b"a\x94\xf4= \x9bDd\xd3&\x9a<\x91\xa3\x00\x00\x00\x00OP=CA\x89\xeaf\xd4\x04z\x80\xc2\x06\x9a\x19\xa0\x13&\x8cLLF\x12\x88\xd0\x93D\x9a\x04z\x9ai\xa3&\x8d6\x90\x18\x81\xa6F\x11\x88\xda@\xd0a\x03\x11\xa1\xa6\x80\x03@\x00\x1a\x00\x03&CFF\xd4\r\r\x18OS@i\xa6\x81\x91\xa3F\xd4hd\xd1\x81\r\x0c\x8d2c\xd5\x02MTI\xa9\xb4\t\x8ax(\xc9\x91\xa0\xf5\x00\x00\x00\x03\xd4\x00\x00\x01\xeah\xd0\xd1\xea\x19\x00\x00h\xd1\xa0\x00\x00\x00h\x00\x00\r\x00\xc9\xa0\x00\x00\x00\x00\x00\x00\r\x04RB\x9aH\xf0\rS&@hyCF\x9e\xa0=@\xd3F\x8d\x1bP\xf5\x00\xf4\x83F\x83OP\x06\x9ah\x0fP\x00\x01\x90i\xa0\xd0z\x9ah\x01\xa3@\x07\xa8\x07\xa8\x03j\x00\x01\xea\x00\x00\x1a\x00\x00\x08\x94"\x00"i\x90\x1a\xa6i\x92\x9e\x98\xa7\x8az\x8fP\xc4\xf5<Q\x99M\x19=54z\x9bS\xd4\xd3h\x9e\x9a\x9a=#2\x9e\xa7\xa9\xe5\x1eS\xc4\x9e\xa3h\xd4z\x9e\x9a\x8fM6\xa6\x86\xa7\xa6\x90\xf2 6\x93j\r\x07\xa3&\xa0\xd0\xf15\x1e\xa7\xa8\x01\xa6\xd4i\xa01\x91\x93=T\xeag\x0b\xe5Z.\xee\xc1\xba\xe2h\x06\xd0\x8a\xaf\x81\x11\x83\x08O\x93<\xa9\xfd\xb3\xe5@\x11<\xb8\n\x9853h\xa8\x02\x83H\xc6h\x94\xf8\xbe\xcb\x009!\xf4 /\xce\x8c\x9e<<\x88\x03\xf3\xe0\x9e\\C\xca\x8a\xe1\xfa473\x04\x1dX9-C\xcc\x86(\xdf\x03jj\x01\x03\x16Z\x88\x81\xf4\xd0\r\xe4\xd9\x9c\x87\tKp\xdcMN\x06\xea\x88\x18`\x82\x15\x82\xb2&\xfe\x08\xd6\x95\x02\xaa2\x02I \x92 E\xbf\rT\x15\xbe&(\xef\xe1\x8e\xb4LR\xd0\x90\xdeC\x90\x88qp8x<l\xe3!\xf57P\xac\xdf\xc5\r\x1cm\x17m0\xc5\n\xc48\xadK\xf8\xcf\xaa\xb8\x94\x92\x04\x04D\x08\x10 B\xadX\xbf\xf8\x8a*4\xa9\xa9Z\xb1\xdfWVBi-%\x90fT\x1a!\xc0f\x0b\xe6\x05y\xbb\xe2\x90\xbd\x1f;\x81\xc2T\xd3W\xc4\xc4\xb6\xad\x94\x8b\x83\x97Z\x97\x81\'\x19\x8e\xc2\xe4&I\x02o\x15\nj+\xd5\x8f\xf3\xd8823\x0f\xe1"\x13]pP_H\x95\xf8\xd5\x96\x9d\x9dv!\xd9\x19\x0c\xc5\x0cc2\xb9*\xe5\x85\x04\xd5u\\\x89\xa9\x80+\xa4\x12\x02\xcd!\x8d\x12Z\xf0)(\x12\x80]\xf9|\xb9 f\xb4\x19\xbe\xe3Ed@\xd0\xa1\xcegs\xd0\x9a\xfe\x19\xf3\xa0\xd0ht>\xde\xe0OU\'\x06\x8f\xb7\x94\x8c\x9e\xd3\xaf\xa5\xc2\xb0m\xd9\xd1\x00P\xec\xa0\x01\xb1\xd8S\'gD\x04\xf6\xba\x94\x07bm\xa7i\x00\x1d\x13$@\xcb\x1bE\x11\xba\x08N\r\x04\x14\xde\xbe\xb0\xe7\'\nx\xdc1\x7f\xb9\r\xff\xa8\xbc\xc39\x99)\xe8=\xd3\xe9K\x83/\xad(r\x08K\x0bK\x07aT\xd1\xc0\x7f\x12\x91s\x16\x85\xe0+\xdfjU\x91\x19\xdaR\xce\xab,\x82\x8e\x9a\x01\x02\tz1iZ\x82\xbf\x00B\x15e\\U\x02\x8b\x00\xa3#\x91\xa7\x16\xd2\x0c\xb62\xc9\xd5\x14\x1dO\xaf\xb85b\x1e\xb6 b\x89Z\xd0S\xf1a"\x03&\x84)\xc3{\x02\xc5\x90\x8aG\xf0I\xc3P\xee:\x03\xab*\x17\xa4\xe8e\xc7NXzA\xb8\xa0\xb1P\x90\x80PzN\xe4\xbe\\\x9dAk\xc4\xda\x82\xc2\x08I\xb7\xbf\xdfZ\xd6\x9b[P7T\x85F~\xc1\xc2tJ\x9c\xb5\n\xf0b\x04\x95\x11n5\xfe\xb6nPNY}\x08cV"f\x8b\x07\xd5r\x81+\xe7\x0e\xee\xcf\xb5\xd96\xa3ju\x18\x02\xdd\x91F\x07\xed\x80P\xdd\x87\x85b\x95I6\xa4\x80\xf5\xd4IK7\xbb\xe9JJ\xcf?mh[\xe0Y\xc9hUM3d\xc6\xb2\xf0\xb5\xc0\x0e4X\x17\x9f\xa7G\x17\xc24P\x84_6U\xaa\xf9\x80N\xaa\xd7\x01\xb5\x00;\xf6\x87\\\xab[\x11\xaf\xea\xea%vO\x9a,\xeb\xb5"y\xa0\x88)\xc0\xb89\xbc\xc6|\xdd\x0f\x9bi&\x9c*\x12\x816\x0f\xa6\xa9\x81e2\xc9\x11\xea*\x19H\x82\xe7\xe1\x84V\x81\x14<\xa4\x8d\x91\x1f\xad\xac\x94M\x98{\xd1$\x1cnY\xa6.\x14\xd7A\xe5S7\x9f\xac\x10\x92U\xb3\xb2[\x95}\x7f\x9b\xee\xc7\xc5\xc5\x012\x05r\xa0*\\T\xcdE*\xf2\xae\xa8"S2\x03?D g3\x80\x83YB\x9f\xde,\x06\x04\x0e\xe15\xf9\xba\xe5\x90\xc7\xcb\x13/\xa3YSK)\x97h\xd3\xd2\xfeA\x95\xcc\xcd\x12\xe0\x02a\xa8 #\xa8\n\xe4\x04T\x00\x99 o\x02\xd3v\x98s\xd1\xea+\xb6\xa7\xdd\x1bN\xf4\xec.\xb4\xd5\xb0~\xd8D\xceD\x18Z\xf6\xa7\xaa\x0e\xf0\xab_\x08\xf9D\xe4\xad\xf3>?\xcb/\x9d\xf8\\q\xde\x1a\x01L*\x05 \x81\x11$\x85\xe6L\xf4D\x82 \x9a\x1a\x7f\x1e\xb1\x86e]\x02\x95\xc6\xb6\x9ai\x82\xf8\xe8\x9a\xd7WN\x904sk\x96\x9a\x99\xea\xc8\x12\xaa\xa4X\x80Z\xb5X\xffh\xeb\xec\x87\n\x0f\xd7\xbcz0\xfb>w;\x02\xb1K~\x8f\xc8<\xc3\x95\xe07\x9ed\xebO\x00\xef\xd4*\xff\x89f\x80\x9e2\x1eO\x92U\xba\xeb\n\xa4\x99>\xf50pu\xe5\xa4+\x97r@\xe7\xf8/\x9b\xfe\xd1H\n\x188[&\xb6\x9d\x04\x94\x01\x06\xe0E\xdf\xe2 \xc3\x85\x07\x95\xee\xd4<\xbd\xc8\x88h\x0c\xfa\xacBH\x10\x10%\x9f\x99\x90\x83\x0b5N{\x0bb\x1e"\xe6\xe6\x0f\xe1I\xf4\xfb:\xcdk\x14-\xd2\x9do\x13\x96\x84z\xcd\x98\x1ek\xb7\n\xc7f\x06"\x12@AM\xd5\xc2\x08\xe1\xe7\xf5\x94\x1c\x85\xbbF[\xf2o"\xfe\xda\xb5k/\xb0\xa1\xabW\x05\xec\xc1h\x01\x1b\x81?\x18+m 9\x9a3\xa3`\x8c\xc1j\x94\xa4\xbc\x06\xdd8N\rg\xe1\xd0\xf7\x81\x8fh\x82\xdf\x95\\N\x14d7\xc2\x96\x9a\xc7w\x010\xcf\xdfB3\xac\x9c\x99p\xed\xd0@\x03H\xd8\xa2\x81\x00\n\x00\xbc\xb6\x1b1m\xca\xb7w\x86\xb6\x90\x06Q\xdd#\xfb\xf8meH\xe0\x00\x95\xa1\x86\xaa\x01\x8fa rn\xacJ\x80\x05\x0b\xa5C\x02\xe9\xf1\x1a\xb3\xbd5!H\xa0M\xcc \xfc\x0b\xc7\x06\x01\xdb\x11m\x14\x1fv\x8e\xack\xc9@\r\xc8\xa2rn:R\x04X\x845\x0c\xcc\xb6\x8ct\n\xd2+g\x14\x02\x88\x14\x03\xb1\xc2\x07\x01`&OdPS\x9a\x8a\xaf\x05a\xcea6\xe8\x1e\x9c\xcc\xd7\x88\xc6]:\x85\xf03\xabHy\x14\xe2\xa1\x92&Q#*\xbaes\xd8\x00\x1a\xf2\x1f\xcd\xddC\xaf\xad\x9b\x88\xf5\xee@9\xcd\xe7M\xb9\xcb\x8e\xf4\xa1:\xfar\x05\x9b\xb9\xd0\xb3\xd5\xa0\x80\x85\x8c\xc0[M\x00\xf48\x17\x9f\xa94\xc5\xb0\xa1\xa5\\K\xc4p\x96\xd0]\x92r\xd0d\xb4\xc3q\xb3\x1d\x8d$\xc6Y\xee\xd2\xa2\xafB\xe0]\xd0\xb3>\xf4o\xd0\x13\x1a\xa8\x89-\x91\x85l\xea]L\xadP\x93UX\x95g&\xc3\x9c\x18\xc1\x10\xe1\xe0\x84Q\xce\xdb\xf0H_\xd3\xd8 D\xa0\xd9\x18\xb2\x0b\x91\xe5\x1b\xfe\x85\xb7\x0eMF\x07\'\x12\x8b\x0eu\xf2%\x15\x95h\x04xZ ?\xce)\x951.>\x84L\x9a0!S\x87\xa2\xac\x03e\x15\x8c1\x89y\xf7TqH\x8b-.\xc3k\xab/\xdb\xd64"u\xcd\r\xe9\xfd@\x14ej\xa3\x800W\x11\x0cS\xf0\xd0\xae\xe2\xe61\xd3\x8eD\xa9\x19/h\xb0\xa78(\r*\xa8!\xef[\xe8\xc8\\]\xfc\xc9E; \'\x93\x96\xc1\x84\xb0;4\xc8\xfb\\9$6\xf7\x00F\xb1\xf8\xa1\x16\xb5R\xfbT,h\x9a=\xd0@\x81R P\xa3[\xbe\xcd48j\x07_[<~\x0c\x01\xea3\x1c\xf8z\x95\xe8\xb0\xd0\x1a\x90\x1c\x17\x185R\x87rC\x8f\xe8\xe5\xe1\xfc\xf2X3\xe2\x8a\xf1\xe6\xb2c\x84\xdc\xd0\xb9\x14\xaad\x83\xbe\x0e\xdc$\xb8\xc9}\x04\x8a\xdcR\x14T`l\x1c\x1b\x88W-\xc3h]**\xe9\'\xdfq\xf9\x9a\xeb\x8b\xef(\x03,\x9ap\xe5 d\xc0\x1b\xa6Q}+aa\x11\x81\xbbu\x15\xc5\x10\xadcH:\x94]\xd5\xad\xe7A\x10\x80\x9f\xbdAoD\xeer\xa6\x0c\x8b\xed7\xa4\x00Q\x10\x81\x02N@\x8e\xa7\x02O\x02\x81\x08\x99\x8b\xfa\xfbO+\x11xN~\xdc\x8c\xb1{&S\x86\xca\x9dm\xf5p\x1b0\xb0\x85\xe7\x0e\xbc\x1f\xa1u\x99\x95\xc3?\x13\xd9\xa3\x873\x17\x05v\xd9\x0b\xa9\xba\x02\xf0 \x84B\x82\xa1\x11\x02e\xb7%\x00!\xa8A G\xb6\x9c\xbeF\xf1\xe6,t\x98^&\xb6\x92X\x9d\x879\xdad\xf4\xf7LWz $\xeb\xe5\xa6\xae]\x06\xa3\x86\x0c\xfad2H\x01<\x19\x00=LZ\x81\x96/\xa6\xc2\x9fW\xb0\xf0\xd3\xca\n\xb0\xc7\x84\x0e\x86t\x94\x12f\x0b\xa2\x17\xfd_\xa2\xd4\xe5\xad\xbe\xdea\xe8\xfd\xc1\x98\x00\x00\xe2\x15\x031\x15\xe0\xb0Q+q\x85\xf7\xfd\x93\xf13\xe2\x01\xcf3\x18^\xc8(\x97\xa8fv&+u\xc8\x06W8\xbe\xf2q\xd5\xafpVWA\x87\x8c\x1b\xa3\x06\x11V\x1cD\xf2Zwv!\xfa\xebt\x17]W\x07T\x93\x05T\x17P6\xde\x9ez\xca\xc7u\xdba\xe6\xe0\xe4L\x85\t\x10\xe9\xf9\x9d\xbf/\xc9\xeb\xf4\xdc\x1az\x0fFg\xfat\x1d\x91CG\x8a\xb4\xe3\xce\x06\xc2eCs\xa4\x80f\xf09\xaev\xe6\xcb!m.1kq\x92A\x0eOo\xc7_l\xb2\xe3\xf5\x938l\xc5\xc5\x12\x00\xbf5\xd9\xfa7\x88\x9dy\xe3!\xb0\xeei$\x0b\xd0\xd7e\xe5\xfe\x0f\x02@\xb2\xa8X\x8c\x88X\x06@\x9d\x1c\xe6p\xd2\x8e\xa1\xab\x7fK\xcd\xf1\xa6\xde\\\x967\xc4b\x01\xa0\x1a\x03 \x18\xdd?\x1ad\x07\x8b\x9e\xf7\x9ds\xf8\xe5\xe6uRe\x9b\r\xb5\x01\xa5\xd0\xa7T\x82\x814\x19\x82gP.v\xbek\xea\xfd\xc14\x87\x96\xb8\xf6H$*\xb2\x10E\xf27\xbe\xef\x18\xb8\xbd\xd8\xea\xf2ha\x11*\xca\xa3\'0\xa9`J\xd6e\x00\xd0o\xf4\xac\x84\xc6\x1d\\\x8e\x89NH\x8717\x1f\'pi>fwJ\x89"I (\xa0\x1b\xf1\x85\xa8:\xdf\xf9\xca\x1a;-\xc6\xbf\xbfLpwQ)\x06Tr(\x80\x84C}MJ\xab\xaf0\xb5\xd8\x9b\xca\x97\x85\xa6\x81\x81\x94\xdb\xf3+\x0b^\xdc\x16,X\x80\xc9_\x83\x98\x16\xc0P\\QU\xa5;\xee/\xfe\xfe7K}\xf9\x14>\x01\x15$\x08D{:\xe3\xd0\xf3\xdcV\x15\xc1g>\xf6X\xe5l;\x97k\xbe\xe8:+\x8d!\xf0`\x9a\x89\x89\xcf\x92\x8c\x83\x93\xfd\xe7\xa9\xfc\xffw\x8c\x13\x17a\xb2\x99\x1b\x194+:\x92\xec\xa9M\xcd@?\x1d\x16\xff%\x8e\xde\xf8\x1f\x1a\xc6\xb5\x8eJ\xdd \x0b\x14\x15T\x85vO9}\x0e\x13R\xadC\x9b\xf5_vb\xee\xc8\x92I#\t=\xde\xb9oK\x94\xc6`\xd1\x9a\xa6\x03\xeb\xf8\x19\x0eq\x90\x84be\xc5\xda\x90\xfbnDsd\x1bTSn*\xa8\x04#\x04(\x96X_\xeb_\xab1h\xef\xff\x8e\x181&3(\x9f\xc6\nAr]\xe9u\xe5Z\xbb\x0c\x02\xbb\xf7`\xf7[\x81\xdc\x08\x16(\xc4\xd8\xea\x0ew\xe4\xddv5d\xed\xf8n\xf7)y\x93|\xc8I##"+uHe\xd8\xeaLq$XN\x1c\xbc\xc0\x9a\x82\xd5\xa5\x86\x0b\xedp\x9b\x05n\xfa\xc1\x04H\x08\xaf@\xc9+L\x1d\x8dV""E"\xd4\x00\x04\x0f\x17\x87*_\xdd\x11\x84\x94\xd5\x0b\xc00\xf9\x05\x83$\t\x01H\r\xc9p\t\x10\xf1\xfa\xff\xb4\xea\xf9\x9fm\xf1\xa6\xe7\xa2\xc4h\x07\xb8\x9b\xbc\xc6\x9d\x08j\xa4!QP\xb7\x17\xf8\x80&\x19\x1d\x84.S\x0e#\x08\x10$Y$\x16E$dU\xa8-\x90\xe2\xc0\xf2,{\\P\r\x87\x06+\x80kTc\x01\x18\xbb\'S\xcc{s\xf8}&>\xdc\x91$\x92\x04\xd6\x0ci\x972\xa5\x10j\x1e\'C\xe7~\xba\xfe\x9b\xb4\x03\x1b\x10\x8c\x87\xbc\xa3h\xa1\xb8r&dR"Q\xdbuE\xc8k\x8a\x1e\xc6\xf3Q\xc2\x19\x05\xb8,\x88\x11"$$\x91\x8d\x85\xcd!!\x01\xcc\xf8\x8a\x0eD_\x89\xbf\xddg\xfdQ#\xb1\x9f\xdaE\x919\xe6\x07\xd0\x1d\x10@t\xcd\xcfT8\x15\x98\xa4!\x04+\x103\x13"A\x82\x85\xcc\xe1rV\xb5v<V\x9f\\\x8b]\x17>\\\xc1\xe5\x8e\x86\xf8\xb0\n\xa0>\xe2\xec\x9fY\x8b\xf0\x89\rl\x89\x85\x13&0*\xb1\x8b)$\xa8\x0cd+\xf3\x1e\x93}\xc4{]\xde\x16\xfb\r\xb1[D`\xf4B\xf6X{S.5PL\x04HIS\xa8\x9d.Oh\xf0\xf1\xac(Y\x13x@!\xaf\xa7\xa2\xecP\xd4\x08\xa9\x9a#\xa9J;\xa3N\x90\xbe\x10\x892!h\xa4s\xf04\xf7V\xcf\x86\x98\xc0\xf6\x10\x908\xdc\xc9\x90\x132\xe0\xcc(^Yn\xc9\xaa\xebh\x97\n\x14\x03\x9d\xfd\xfe_\x9b1\x95\xb1\xc8\x96*V\xd7\xcb\x9b\t;\x05aM\xa7H)DBOg\x02\xd2C\x1f\xcf\xef{m\xc7\x83\xbb\xf8b\x06X\x01\xf7\x903\xe4\xca\xba4\x06\x04*;\xf0\xdd\xfa2\xa8\xb8]L\xf3\xad\xcaFFI\xc6d\x0c\x01\x93/\x92\xb7\xa2\xd6\x00\x16$\x12\xe2J\xf2\xf4\xc4\x18\xec\x85\xa5k<{\x15Y\x8fh\xa6\xc3h\xb2\x96r\xba,\x14\xb8\xa6\x86\x05V\x06s\x98\xf3*cT?\x0ee\x82\x13\x1aa\x1a\xa0\x18\xa4\x8aB\t\xdb\xea\x16\xe2\xa8\x14\x118X&\x08\x10s\x1f3\xfe~F\xc6w>t\xc49\xc47\x10\x0b\xa4J\xed\xa27&G\x9c\xe7x\xfd\x7fq\x83\x00c#\xeb\x9c\x91$\x1a\xd6\x85\x15\x1b\x19V\xe5\xb2\x04"\x84 \x87H%\xa2$P\xd6\x8d\xe2\x11\x08\x88\x9a\xf9\xf2\xf3\xda|\x88(w\x9d)\xbe5\xf3p\x04\xf7%\r\xb7\'\x9b\x8b\xebO7\xcb\xdb\xd4mk\xeb\xf4\x01\xb9\x82\x12\x05"n\x92\xdb\xb2\xe0\xa0\xd8\x8aX\r\xbf)\xab\xe3{\xcc\x07\xad\x90\x89\x89q8\xea\x01\xc4\xec>h\x85"R\xee\x12"\x17\x12\x90\xc0&\xa9\xf0\xfa\xcc5\xdde\x0ez\x07E2\x0e1\xdd\xe8\xb2\xaekP\xc1\x12\xbb\xde\x16\xe5p\x89O=\xb7\xf7\xff\xb1\xde\xf1\xd9E9\x98\x8b\x99\xe52\x86\x8f,.[\xe4\x85\x8d\x11\x17LL.\xb7\xfdja\x04\xc27\xb8\xabH\xa0\xc1\xb4l\x9a\xb00jM\xc7s\x84\xf4\x8c\x81\xc9L\x10\xac\xfb\xebTq\x8eR\xea\x10+\x16\x10i\xbb6|\xd0J\x1e\x9d\xac\xdbQ\xb5\x8b\xad\x01oi\r\x13\x12k\rR\x96\xf7\xde\xee\x94\xa96\xf9\xf3\x08\xb5\xb3I\t\xa2\x07I\xa1T\x00\xae\x0bZ!\xa7E\xd2+\xb1,\x17\r\xa3\xa3\xc88\xday\xfeG\x00\x13=\x134\xac\x03g"&p\xb1aB\xb9`\x1b\x7f;\x82\xb7\x8bx\x14\x14!\x91\xed\xb59/R`^*\x0e\xfeR2\x1d<C\x18:\x02\x8d\x1d\x1a4C\xf7l\xb8B\xf8\x0cR\xfa\x99aP\xcf\xd7r\xbc\xd9_\xad\xe8:\x0c\x82\x89\xc8\xe3\x13MZ\x06i\xa6\x9b5^\x1d\x02\xe8H\xb2\x08H\x80D\xfb*\x9bk\xef\xad\xc6k\x1c\r8\x84\xb0\x10ys\x00\x1cA\xb7\xc0\xc2\x91\xa1\x0fClY\xe9\x9a*8\x80\xe1"\xdf}\x96\xa1\x90\xdf\\\xf6\xc6&\xba\xb4\x04\x10\x12\xe1\xa0/Z\'\xfbD\xcdB\xc6\x11T\xcb?\x80\x96\xe4\x1b\x80)\xa6i\xd5\xd4\xae\xe3\x02`x\xffm\xd6_rp/\x84H\x12\x04\x84\x8e\xac\x06\x8c\t\x04\x90$JA\xa8\x86\x83Fm\xed\xae\x14w-\x1cR\xeaP\xcd\x14\x0b\x8c\xf7\xf5\xd7\xd2\xb451a0\xa6\x10\xca@\x90\x08\x11\x93Z\x94\x90\x90\x89PO$\x98s\xd2\xc0H\x1b\xbf\x9d\xb7\xa5\x82\xc7Y\xa7_N\xae\x9c\xb8\x89\x8e\xd8\xd4\xc6\x1d\\\x0e\x9aV\x12*\xcf\'\xe6\xf8\xe7\xc13\n\x01\xd2vT\x0e\x8fKCw\x17k\xec\xfa)\xaeR\xf3\x1bI\xe1T(\x8b:\xd7\x9ae\xda)\x7f\xa5Q%\x9a\xba\xad\x14@ f\x13{\x00z-R\xd5_\xc7\x83\x9a!!\x824"R\t\r\xa7\x9d\xe2\x0b 7@W<P>\x8c\x04\x07e\x10U\x12\'\xd2P\xb8\xae\xadD\xf0\xaf\xb6\xda\xf2\x99)B\xf4I!\xb6\xad\x1a\xaa\xd0\xe9T+PF\x1f\xaa}\xccJr\xda<\x02\xa7=\xeb\r\xcf5k\xf1\xaaR\x08\x90~$\xcd\x1a\xc3\xb0\xf9\x7f\xcbc\xbb\xb8\xf7\xb1\xceN\x92\x85\xf9-2\xfaD\xe24B\xa5\xb5U\x96\x1b\xc7\xae\xfb\xeaj@49\xc9\n2\x85G=QE\x14\xe0\x15\xc2".\xa6\xda\xe2\xa9\xa4\xfbVY\xb6\x1a\x87B\nQ|\x95^\x16\xcb%\t\xda\x00D@v\xd2.\xb8\xe2\x1d\xce\xdb\xe9\x03\xec\xb8\xba/aj\\\xfaN`A\xeah\xaf\x10\x9e\xe5\x8e"\x88\xd3\x08\xe1AD7|{\x8f\xce\x8cR\xf5\x89\x86\xd1\xa0\xaf5\\\xdb\x0c\xd8\xfb\xce\xf5\x08P\xf9$\xf4_.\xc2\xec$\xaci\xb6\xecnn\xb5m\xdb\xb2\xd2%[@\xc2\xab\x00R/rl\xcd|\xda\x19O\x1b\xe4\xf9\xfe%\xc9\x10.\x99\x07d\xfd\xc9\xf3\xb7:Dh+\x99\xd0\xbcl)`mt%\x8f\xe9\xa8\xb4\xfb\xa5\xa1\x9a\xe5\x92\xb1\xceB\x05Z\xdf<vD\x08\x16{5D\xacjEU\xe0N\xbb9\xd9\xfe\xcb\xb3\x8aU\xaf\x1d\n\x81\xf3\xbfI\x11\x8b\x13e\xba\xdaX\x14\xf3$e"h\xd9a\xc5\xac\xf6\xfe/\x7ff\xd1\t\x13{\xbdQ\xe9Y\xc8u\xebm\xae}\xe4@ID@\xd9\xed\xe5\xbbKe\xc2\xf8\x92\x87)B\x9f\x1f\xc1\xa8\x88<\xb4\x14:9\xea\xe0\x82\x1dT\xf3\xd1\x1aG\xd3AN\x93\xd9\xd180\x03~\x8cqR\xea\xbc\x8cNN{\xee3\x05Q\x03&Z\x08y\x90\x97\xec\n\xcc\x92\x17H\x12E$`\xa2\xa1\x06\x00\xc5E@\x14R,\x08@\xb6\xde-\xfd\xca\x863Y\xa0/\x0f\xe3d\xa4\x94\x95\xde\xc71wk\xc5d\xe0\xd8\xd5i_\xda\xed\xa2\xe5\xe0\xfd\xe3,\xdc\xea\x81vUf\xeb\xfa\xc5\xc3\xe8\xac\xee\xba\x9a\x0f6\xc5\xfc\xfe>;\x00&\x95\x08 X@\xa9\x7f\x97\xbc&\x02x\\T=\x94-\xbdd\xa8\x87\x01\x0f\xa1\xe9H\x05\xa2\x04\xbd\xbc\xa0\x19\x89#\x8a\xb4\xcb.\x829\xa2\x05\xe6\n d\x89H\xf7\x8ew\xe1?o\xc7y\xfb^\x8e(\xfa\xf8\x1f\xd1\x11\x0c,\r=\xf7kT\xe7\xfe\xe8\xa0_\x14\x90SN:z\xb8\x08\x14\x81\x8e\ttOE\ny}\xfd4\x07\x06\x8b\x86\xfd\xde\xdf\x9b\xdeY\xf15O\xe3\xa9U\xb2h\x12\xe5\x81\x84\xf0\xc3\xa8iFTTE\xb3\xa0\xc3\xe3Y\x80%9\xa3iMZ\xc5\x82\x14\xdbP\xe1\xa2\x1a\xb0+\x00\xd5\x88\x98<m\x15BO\x17%\x107\x91d\x04\xdf\xc9J+h\na\x88\x8d"\x96\x88\x88\xe9\xf4\xd4\x03\xffc\xba\xba\x8a\xe9\x8dH\x18\x08jCE\xf4\xba"H\xa6\xea\x05\ti\xddEjC_\xc0\xa5M\xe9\xe6\xeall\xd8\xa8b!{\x0b@\xdbh\xde\xd9\xb4\x80Z\x12\x04\xb5=\xec\xd3\x1dk\xa8\x95\x9a\xb0MX\xdd\x0eGm\xb3S\x9a\xc9G\x17\xb3\xa6\x18@\x8an\xe3h&\xb4r\xcd\xee|\xb7\xe5\xdeL\x16\xa6\\$\xf9\xb4\\\x10\xa8D\xe1 \xb5\x81\x8a\x05\rID\x84\x00\r\x88\xc8\x029`g\x88\x83\xfe\x91D\xcf\x11\\PQp\xc5\x14tO\xea\x17k\xd1\x7f\x16\xae\rl\xb8\xa5rq\x17]\xad\x95\x04HjL`\x04\x0fb\xc6\x8c3\xbd/\xd1\x89M\xb6\x17\x80*\x0b\xbd\xf0HI\xb7D$@$x \xc8\x9b \xff\xcd\x9a\x12\xb2k\x06\r\x00\xc8\xcc\x89G\xd9HzZ\xaeob\x80]\xd6\x14\x95\xe8\xec\x9ed0\xc1\x07p\xa5a\xc4\xb4\xb3\x06\x18\x1e\xaenK\xb6*c\xc1Fy\xae?\xc1\xd6+\xde\xfc]S\x853j\xd5s\x90\x0c\xe4\xccI\x02\x10\xd9\x90\x1c\xf6\xa3\xb8\xed\x11\x89\x82\xbc\xca\xb9v\xc5{L\x00\x94h\xd2 L5\x02\x05\xd1\xab\xa1v\x16k-\n\xa2\xdd\xd8\xbf\xf5\xc8\xfbqsB]5\xd7\xe3]\xdb\x10\x13\xcc\x8a\xda\xe0ZU\x16\x82V\xd2\x02\xca\xe8\x0b\x80\x00\xbfr\x9e\x01\xe0\x8c-#6\xd5\x15\x81\x88\xf5Q\x1bk\xb4\xaf\xc8\xee8;,V\xc5\xa6+P\xb0 vL\x00\xfcJ\xf5\x92,Wos\xbf\xa7jN\xd9j\x89\x96\x14\xb6\xefFA\xd82u\xb2\x00V\x89\x02\x9a\x02#i]\xa4\x08\x0f\x07\x17\x1d\xed\xaa\x04\x16\x10\xde;\x01\xab\x97\x1b\xe2\x1bM:O\xc1!\x99\xc6\x91\x07\xcc\x97&/\x9a\xd1[\xb8\xe4\x0e\x85t)\xe3\xd8R\x15)\x0eqCtd\xc4\xe4|{\xedmK72\xc1\x16\xcf\xd8\x9dE\xa9\xac\xb3+E^\xa5\xe0\x80/E\x1c\x11\x0bB\xc0G\xd3\xcc\xd0b\x96>=6\xe2J\xd3tE\x8b\x1a\ri\xf8\x9c8\xb9\xdc+\x98\x0bf\x88\xcd\xc9\xa3R\xe81z\xa5\xe4\xafFES|\xee\xd6\x10\x14RO\x1bh\x7f\xae\xb5*vX\xbf\xecX\x85vM\x86(\xd6\xdb3\x04p\xd8\xb1\x0eB\xc2\xbe\x9bc\x8d\x99\x1f)\x8c\x8b \x86\xf8eT\xdb\x04\x06^YZ\xa2\xf2\xf5hO\x11e\xc0\xd4\x10fl\xbc,;\xb9\xce\xcd\xc3[*i\xd9\xd2Q\x81\xfcY\x9a==\xfe\x9a;\xf7 \x0e\x18\xac1Q&\xa8\x14\x15\x98\xdb\xce\xd4%\xf0\xe9_\'\xe8j\\~\xe4\x88j\xcc\xaf\x8dGs\xa4\xea\x83G+\x9a\xb5\xf4^p\xe6\x15#w%\x19*#\x0eV\xea\xf4\xa8\xa7\x02*a\xc4Ln=\xee`\xcbZ\x97\x86\x16i\x9c\xed\xcdh\xf6C;\x96\x92\x8b"\x13\x92\x1a\xaaW\xe7\xba\x18\x1b\xc3\x90O\x9f\x84\xa6\x13\x8f\xc2D\xe4\x87-K\xb3;y\xdbE3D\xc5\xfb\x13WX\xf7o\xc98z\xfc\xaa\xbd\xdb\x0b2\xb9\x92FL\x98\xc8\x9d6L\x034\xa1<\x93.\xab\x05Ct\x81\x10\x03\xe4\xfc?S\xa9\x1b?\x82\xa2\xee\x05\x8f\xb2J\x0e\x85\x170\x03\x9d\xe1d\r\xe7\x9f ow\t\x18\xfc|\x83\x96\x08\x14N+-?\xd6\x0f\xd2\xc1\xf0\xcf\xd6\xbb!\xf6\xa3\x86\xd7\x82\xd6\x01$\rLT*\xaa\xc8C\xc7\xf0\xfb\t\xbf\x86\xa1\xc3\xebJ\x1b\xbd\x02\xd0\xde\x05\r\xfb\x0fD\xf5e\xf7\x90\x85z\xd4b#\xc7>\xdb\x14k\xd3S%\x8c\xb7\xda\xda\xeb\x7f\xef\x963oL{N%os\xca~\xbf}HO1\xab\x1b\xbe\xb5"\x04\xb1\x12\xbc\n%\x81\xfdt68\x17\xf4\xc1\xccb\xd3\x8foMV\xd4\xbe\xee\xa9)\xda\xb9\xfeE^\xf37\x88\xf7\x7f\x97S.P;\x8eI\xa9\xbf\xca\xf9O\xe3jfg\xf0\xbe\xe5\xbd\xb7\x7f\xa4\xef\x9c\xaa\x06\xb9\x08\xbaa\xb3EL\xf0\x90\x94a{\xa9\xe2qDDP\xce}9t$9\x17y\xfb=^\xf4\xc1x\xbf\xe3\xb3\xe4\xa1\xe3\x1cpe9\x14\x13E\x0cH2\xa7\x9f!\xaf\x92\x0b\xa5\xe2\xearIJ\xd2\x8d\x15\x8c)OL\x8c\x00\x98re;\x9a\xfai\xdb#0A\xfa\xefd>\x13\x1d\x04\x88`\xc1E\r\x9d\xf4\xdbP\xfb,\'\xac\xf7\xbcp\x1d\x8d\xb0\xdcQ\xb1\x90t`yXBQ\xd2\xacZf\xe9\xdf\x04A\x15;>_\x84\xdep\x0b\xbe"\xa0\x12 #\xdc@\x13\xb9\x82\xf4\xd1U\x04\xf0b"\x10~\x05\x10;\x18\x08~\xbcD\x01;\xc8"({\x18\xaa\x07\xb6\x89\xeb\xa5Q\xc9(\xbdl\x11\xfe\x08\xaf\xe4\xc1P\x02\xa6\x05U2\xd0+\xdf\xc0\x02\\B*\xdfJG\xbb\x1dG!\xd2\xcc\xdd\xd4+\x96\x81\xc9\xc6\xda\xd1\xecrPO\xcd\x80\n\xd6\x07\x87\x14E\xd4\x8fi\x11;Z\xd1\x14\xa4P\r\xe4O\x9b\x01d\x8b\xf5\x1d\xf7_c\xe1MM\xbd\x1e\x96\x1b\xe8\xa8\'i\x00\x00\xc9\xbe\x83\xb3So\x17\x0cpG\x81)\x03V-\xd0\x17\xa1\x8aG\x95M\xe52i\x00\x0b$\tt>\xa3\xd2\xa6Q\x80B\xd5 zFW\rL\xa2\x10\x00\xad\x81\xb3\x85D4[EAMb\xd4\xc4\x92\xb7\xdb%uk\x8d\x8b\x8cnK\x15\x80\'(\xcfwi>,\xc4\xfc\x15\xf9\xee\xbf*\x8f\xbdY\x13\x1d\x80\xc1=\xe6Y\x02\xb1^=GAZiM\x81\xac\xa5\x8f\x19\x93J\xaa$G\x002e\xa0\x86\xcc\x02\xf3!\x98\xc1\xf3\n\x9c\x01G\x8e\xb6\xc6\xb1\xe4\x9bU\xc4p\xfbU\x9f\x801-\xd7\xf5\x9c%4\xa3\x91Bo*\xaa\xaaK\x9a\xa4E \x93\x8e`\xa7-\xf5SjX\x0b/L\x90\x12-Q\xa8t\xf6\x86\x83\xe3\xa1\x8d\xb7\xf7u\xd4!k\xdf\xbeUe\x1cm\xb2\x93f\xbc\xc3\xe0\xd4F\x05\x95hC:\x95)\xd9\xf3\x02R\x82\x08m\xccK\'\x83W\xe1\x87\xa2\x04EH\x8d\xec\x06\x80S=\xf0\xb0R\r\xf8q\xb3\x10`\xcc\x84\xe5\xb6Y\xf30\xe6\xeb\xa9\xd1\x82>$\xf8\xffiA\xc6\x06u\x03y\xf8\xc5\xdc\x91N\x14$2\x1e\xaf\x84\x00'
				
				# Datos para agregar al registro al añadir el icono a los archivos con la extension .ubz2
				self.iconFileName = 'ubz2file.ico'
				self.fileName = 'ubz2file'
				self.fileExt = '.ubz2'
				
				self.use = '''
				\r Clase: UBZ2 (v1.0)
				\r │
				\r │ # Descripción: Permite comprimir archivos de manera individual con
				\r │ el algoritmo de compresión 'bz2' con el método 'compress()' generando
				\r │ un nuevo archivo con extensión .ubz2 (utils bz2) los cuales puede
				\r │ descomprimirse con el método de descompresión 'decompress()'.
				\r │ Al Generar los archivos comprimidos (.ubz2) se generara en cada
				\r │ uno de ellos un flujo de datos alterno llamado 'Info' (.ubz2:Info)
				\r │ en el cual se almacenan metadatos con información de la compresión.
				\r │ Estos metadatos podran obtenerse con el método 'getDataFromUBZ2File()'.
				\r │ También es posible generar un icono para agregar al tipo de
				\r │ archivo .ubz2 utilizando el método 'addIconToFileExtension()'
				\r │ pero requerira permisos de administrador para esta acción.
				\r │ También es posible solo generar el icono para su visualización
				\r │ con el método 'generateIcon()'
				\r │ 
				\r │ # Default params:
				\r │
				\r ├─ compress(
				\r │      fileName,             # Nombre del archivo
				\r │      verb = False          # Muestra texto para ver progreso
				\r │  )
				\r ├─ decompress(
				\r │      fileNameUbz2,         # Nombre del archivo comprimido
				\r │      verb = False          # Muestra texto para ver progreso
				\r │  )
				\r ├─ getDataFromUBZ2File(
				\r │      fileNameUbz2,         # Nombre del archivo comprimido
				\r │  )
				\r ├─ addIconToFileExtension()  # No requiere parametros. Requiere permisos.
				\r ├─ generateIcon()            # No requiere parametros
				\r |
				\r + Ejemplo de uso:
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para comprimir un archivo:
				\r |    fileName = utils.Actions.Explorer.getFileName(topmost=False)
				\r |    if fileName:
				\r |        utils.Utilities.UBZ2.compress(fileName)
				\r |    
				\r |    # Para descomprimir un archivo:
				\r |    fileNameUbz2 = utils.Actions.Explorer.getFileName(topmost=False)
				\r |    if fileNameUbz2:
				\r |        utils.Utilities.UBZ2.decompress(fileNameUbz2)
				\r |    
				\r |    # Para extraer los metadatos generados en algún archivo comprimido:
				\r |    fileNameUbz2 = utils.Actions.Explorer.getFileName(topmost=False)
				\r |    if fileNameUbz2:
				\r |        data = utils.Utilities.UBZ2.getDataFromUBZ2File(fileNameUbz2)
				\r |        print(data)
				\r |    
				\r |    # Utilizar la función addIconToFileExtension() para añadir el icono
				\r |    # de navi a los archivos con extensión .ubz2
				\r |    utils.Utilities.UBZ2.addIconToFileExtension()   # Requiere permisos de admin
				\r |    
				\r |    # Se puede crear solo el icono de navi con:
				\r |    utils.Utilities.UBZ2.generateIcon()             # No requiere permisos
				\r \\
				'''
			
			def _keyExists(self, HKEY, PATH, VALUE=''):
				try:
					reg = WR.OpenKeyEx(HKEY, PATH)
					value = WR.QueryValueEx(reg, VALUE)[0]
					WR.CloseKey(reg)
					return True, value
				except:
					return False, None
			
			def _originalCode(self):
				
				xD = open('xD diccionary.txt', 'rb')
				
				original_data = xD.read()
				print('\nOriginal     :', len(original_data))#, binascii.hexlify(original_data))
				
				compressed = bz2.compress(original_data)
				print('Compressed   :', len(compressed))#, binascii.hexlify(compressed))
				xD = open('xD Compress'+self.fileExt, 'wb')
				xD.write(compressed)
				
				xD = open('xD Compress'+self.fileExt, 'rb')
				compressedData = xD.read()
				decompressed = bz2.decompress(compressedData)
				print('Decompressed :', len(decompressed))#, decompressed)
				xD = open('xD diccionary-decompress.txt', 'wb')
				xD.write(decompressed)
				
				print('Porcentaje Compresion: ', 100-round(len(compressed)/len(original_data), 3)*100, '%')
			
			def _saveInfoData(self, fileName, lenCompressed, lenOriginalData):
				
				prevData = self.getDataFromUBZ2File(fileName)
				
				if prevData == {}:
					rounded = round(lenCompressed/lenOriginalData, 3)
				else:
					rounded = round(lenCompressed/prevData['originalFileLength'], 3)
				data = {
					'author':   __author__,
					'software': __title__,
					'version':  __version__,
					'originalFileLength': lenOriginalData if prevData == {} else prevData['originalFileLength'],
					'compressedFileLength': lenCompressed,
					'compressionPercentage': str(100 - rounded*100) + '%',
					'timesCompressed': 1 if prevData == {} else prevData['timesCompressed'] + 1
				}
				infoFile = open(fileName+':Info', 'w')
				infoFile.write(json.dumps(data))
			
			def addIconToFileExtension(self):							# Agrega un icono pixel art (de mi autoria) de Navi de Zelda a los archivos con extensión .ubz2 pero Requiere permisos de admin
				
				if not os.path.exists(self.iconFileName): self._generateIcon()
				
				# [HKEY_CLASSES_ROOT\.ubz2]
				# @="ubz2file"
				reg = WR.CreateKey(WR.HKEY_CLASSES_ROOT, self.fileExt)
				WR.SetValueEx(reg, '', 0, WR.REG_SZ, self.fileName)
				WR.CloseKey(reg)
				
				# [HKEY_CLASSES_ROOT\ubz2file\DefaultIcon]
				# @="C:\Users\etc...\ubz2file.ico"
				reg = WR.CreateKey(WR.HKEY_CLASSES_ROOT, self.fileName+r'\DefaultIcon')
				WR.SetValueEx(reg, '', 0, WR.REG_SZ, os.path.abspath(self.iconFileName))
				WR.CloseKey(reg)
				
				# [HKEY_CLASSES_ROOT\ubz2file\shell\edit\command]
				# @="notepad.exe %1"
				reg = WR.CreateKey(WR.HKEY_CLASSES_ROOT, self.fileName+r'\shell\edit\command')
				WR.SetValueEx(reg, '', 0, WR.REG_SZ, 'notepad.exe %1')
				WR.CloseKey(reg)
				
				# [HKEY_CLASSES_ROOT\ubz2file\shell\edit]
				# @="Editar"
				reg = WR.OpenKey(WR.HKEY_CLASSES_ROOT, self.fileName+r'\shell\edit', 0, WR.KEY_SET_VALUE)
				WR.SetValueEx(reg, '', 0, WR.REG_SZ, 'Editar')
				WR.CloseKey(reg)
				
				# [HKEY_CLASSES_ROOT\ubz2file\shell\open\command]
				# @="notepad.exe %1"
				reg = WR.CreateKey(WR.HKEY_CLASSES_ROOT, self.fileName+r'\shell\open\command')
				WR.SetValueEx(reg, '', 0, WR.REG_SZ, 'notepad.exe %1')
				WR.CloseKey(reg)
				
				# [HKEY_CLASSES_ROOT\ubz2file\shell\open]
				# @="Abrir"
				reg = WR.OpenKey(WR.HKEY_CLASSES_ROOT, self.fileName+r'\shell\open', 0, WR.KEY_SET_VALUE)
				WR.SetValueEx(reg, '', 0, WR.REG_SZ, 'Abrir')
				WR.CloseKey(reg)
			
			def generateIcon(self):										# Genera el icono de Navi en la carpeta del código.
				xD = open(self.iconFileName, 'wb')
				iconData = bz2.decompress(self.iconFile)
				xD.write(iconData)
				xD.close()
			
			def compress(self, fileName='file.txt', verb=False):		# Compresión de un archivo con el algoritmo bz2 genera un archivo con extension .ubz2
				
				if verb: print('Extracting the uncompressed data...')
				xD = open(fileName, 'rb')
				originalData = xD.read()
				xD.close()
				
				if verb: print('Compressing...')
				compressed = bz2.compress(originalData)
				
				if verb: print('Saving compressed file...')
				xD = open(fileName+self.fileExt, 'wb')
				xD.write(compressed)
				xD.close()
				
				self._saveInfoData(fileName+self.fileExt, len(compressed), len(originalData))
				
				if verb: print('Done!')
			
			def decompress(self, fileNameUbz2='file.ubz2', verb=False):	# Descompresión de un archivo con el algoritmo bz2
				
				if verb: print('Extracting the compressed data...')
				xD = open(fileNameUbz2, 'rb')
				compressedData = xD.read()
				xD.close()
				
				if verb: print('Decompressing...')
				decompressed = bz2.decompress(compressedData)
				
				if verb: print('Saving decompressed file...')
				xD = open(fileNameUbz2[:-len(self.fileExt)], 'wb')
				xD.write(decompressed)
				xD.close()
				
				if verb: print('Done!')
			
			def getDataFromUBZ2File(self, fileNameUbz2):
				try:
					infoFile = open(fileNameUbz2+':Info', 'r')
					data = json.loads(infoFile.read())
					return data
				except FileNotFoundError:
					return {}
		
		class Hash:			# Convierte un texto a algun tipo de hash seleccionado.
			
			class HashNotAvailableError(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
				
			def __init__(self, hash_, text, type_):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.types_avail = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'md5']
				if not type_ in self.types_avail:
					error_msg  = 'El hash {} no esta disponible.\n Disponibles: '.format(repr(type_))
					error_msg += 'sha1 (Default), sha224, sha256, sha384, sha512, md5'
					self.HashNotAvailableError(error_msg)
				
				self.hash = hash_
				self.text = text
				self.type = type_
			
			def __str__(self):			# Permite mostrar el hash al usar el objeto
				return self.hash
			
			def __add__(self, val):		# Permite concatenar hash + str
				return self.hash + val
			
			def __radd__(self, val):	# Permite concatenar str + hash
				return val + self.hash
			
			def __len__(self):			# Permite usar len(hash)
				return len(self.hash)
			
			def __mul__(self, val):		# Permite multiplicar el hash: hash * 2
				return self.hash * val
				
			def __rmul__(self, val):	# Permite multiplicar el hash: 2 * hash
				return val * self.hash
			
			def update(self, type_hash):	# Permite cambiar el hash a otro tipo
				if not type_hash in self.types_avail:
					error_msg  = 'El hash {} no esta disponible.\n Disponibles: '.format(repr(type_))
					error_msg += 'sha1 (Default), sha224, sha256, sha384, sha512, md5'
					self.HashNotAvailableError(error_msg)
				if not type_hash == self.type:
					self.hash = self.f_hash(self.text, type_hash)
					self.type = type_hash
			
			def f_hash(self, text, algo='sha1'):
				algo = algo.lower()
				# ~ exec('hash_ = hashlib.'+algo+'(text.encode())')
				hash_ = text.encode()
				if   algo == 'sha1':   hash_ = hashlib.sha1(hash_)
				elif algo == 'sha224': hash_ = hashlib.sha224(hash_)
				elif algo == 'sha256': hash_ = hashlib.sha256(hash_)
				elif algo == 'sha384': hash_ = hashlib.sha384(hash_)
				elif algo == 'sha512': hash_ = hashlib.sha512(hash_)
				elif algo == 'md5':    hash_ = hashlib.md5(hash_)
				return hash_.hexdigest()
			
			'''
			'__mul__', '__reversed__', '__rmul__', '__setitem__', '__setslice__', 
			'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
			'sort', '__imul__')): <class 'tags_file_module.BaseListProxy'>, 
			('PoolProxy', ('apply', 'apply_async', 'close', 'imap', 'imap_unordered', 
			'join', 'map', 'map_async', 'terminate')): <class 'tags_file_module.PoolProxy'>}
			'''
		
		def load_uses(self):											# Función que carga todos los 'use'.
			self.hash_use = '''
			\r Función: hash(text, algo='sha1')
			\r |
			\r + Ejemplo de uso:
			\r |    
			\r |    utils = Utils()
			\r |    
			\r |    # Available: sha1 (Default), sha224, sha256, sha384, sha512, md5.
			\r |    
			\r |    h = utils.Utilities.hash('hello world!', 'sha256')
			\r |    print('Hash: ' + h)
			\r |    print('Type: ' + h.type)
			\r |    print('Text: ' + h.text)
			\r |    
			\r |    h.update('sha1')
			\r |    print('\\nActualizado a sha1:')
			\r |    print('Hash: ' + h)
			\r |    print('Type: ' + h.type)
			\r |    print('Text: ' + h.text)
			\r \\
			'''
		
		# Math -------------------------------------------------------
		def cos(self, deg=45):											# Obtiene el Coseno de X grados
			rad = math.radians(deg)
			return math.cos(rad)
		
		def sin(self, deg=45):											# Obtiene el Seno de X grados
			rad = math.radians(deg)
			return math.sin(rad)
		
		def diagonal(self, h, deg=45, rounded=True):					# Obtiene los catetos (cateto opuesto y adyacente) usando la hipotenusa y un angulo
			
			inv = True if deg//90 in [1,-1,3,-3] else False 
			deg = deg%90
			
			if inv:
				co = h * self.cos(deg)
				ca = h * self.sin(deg)
			else:
				ca = h * self.cos(deg)
				co = h * self.sin(deg)
			
			if rounded:
				if str(rounded).isnumeric():
					return {'x': round(ca, rounded), 'y': round(co, rounded)}
				else:
					return {'x': round(ca, 2), 'y': round(co, 2)}
			else:
				return {'x': ca, 'y': co}
		
		def euclideanDistance(self, A, B):								# Obtiene la distancia entre 2 putnos del plano cartesiano.
			''' Formula: d(A,B) = sqrt( (Xb-Xa)^2 + (Yb-Ya)^2 )
			Donde: A=(Xa,Ya), B=(Xb,Yb)
			'''
			Xa, Ya = A
			Xb, Yb = B
			X = (Xb-Xa)**2
			Y = (Yb-Ya)**2
			d = math.sqrt(X+Y)
			return d
		
		def getAngle(self, A, B):										# Obtiene el angulo que genera una linea entre 2 puntos del plano cartesiano.
			''' Donde: A=(Xa,Ya), B=(Xb,Yb) '''
			Xa, Ya = A
			Xb, Yb = B
			X = (Xb-Xa)
			Y = (Yb-Ya)
			atan2 = math.atan2(Y, X)
			angle = math.degrees(atan2)
			return angle
		
		# Pygame -------------------------------------------------------
		def moveWindow(self, win_x, win_y, win_w, win_h):
			from ctypes import windll
			hwnd = pygame.display.get_wm_info()['window']
			windll.user32.MoveWindow(hwnd, win_x, win_y, win_w, win_h, False)
		
		@property
		def curWinRect(self):
			from ctypes import POINTER, WINFUNCTYPE, windll
			from ctypes.wintypes import BOOL, HWND, RECT
			
			hwnd = pygame.display.get_wm_info()['window']
			prototype = WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
			paramflags = (1, 'hwnd'), (2, 'lprect')
			GetWindowRect = prototype(('GetWindowRect', windll.user32), paramflags)
			rect = GetWindowRect(hwnd)
			return [rect.left, rect.top, rect.right, rect.bottom]
		
		@property
		def curWinSize(self):
			info = pygame.display.Info()
			return [info.current_w, info.current_h]
		
		# Bluetooth ----------------------------------------------------
		# Reference: Baseband (Complete) - https://btprodspecificationrefs.blob.core.windows.net/assigned-numbers/Assigned%20Number%20Types/Baseband.pdf
		# Other Reference (Incomplete Info): Class of Device/Service fields: https://www.ampedrftech.com/datasheets/cod_definition.pdf
		
		def getMajorServiceClass(self, CoD: [hex, int]) -> str:			# Devuelve el "Major Service Class" de un formato CoD (Class of Device/Service) de Bluetooth.
			# Assigned Numbers for Baseband
			if CoD.__class__ == int:
				binary = str(CoD).zfill(24)
			elif CoD.__class__ == str and not CoD.startswith('0x'):
				CoD = CoD.replace('0b', '')
				binary = CoD.zfill(24)
			else:
				binary = bin(int(CoD, 16))[2:].zfill(24)
			
			binary = binary[::-1]
			s_ini = 13
			s_end = 23
			
			section = binary[s_ini:s_end+1]
			section = section[::-1]
			
			masc = ''
			
			if section[10] == '1': masc += 'Limited Discoverable Mode, '
			if section[9]  == '1': masc += 'LE audio, '
			if section[8]  == '1': masc += '(reserved), '
			if section[7]  == '1': masc += 'Positioning (Location identification), '
			if section[6]  == '1': masc += 'Networking, '
			if section[5]  == '1': masc += 'Rendering, '
			if section[4]  == '1': masc += 'Capturing, '
			if section[3]  == '1': masc += 'Object Transfer, '
			if section[2]  == '1': masc += 'Audio, '
			if section[1]  == '1': masc += 'Telephony, '
			if section[0]  == '1': masc += 'Information'
			if masc.endswith(', '): masc = masc[:-2]
			
			return masc
			
		def getMajorDeviceClass(self, CoD: [hex, int]) -> str:			# Devuelve el "Major Device Class" de un formato CoD (Class of Device/Service) de Bluetooth.
			# Assigned Numbers for Baseband
			if CoD.__class__ == int:
				binary = str(CoD).zfill(24)
			elif CoD.__class__ == str and not CoD.startswith('0x'):
				CoD = CoD.replace('0b', '')
				binary = CoD.zfill(24)
			else:
				binary = bin(int(CoD, 16))[2:]
			
			binary = binary[::-1]
			s_ini = 8
			s_end = 12
			
			section = binary[s_ini:s_end+1]
			section = section[::-1]
			
			major_device_class = {
				'00000': 'Miscellaneous',
				'00001': 'Computer',
				'00010': 'Phone',
				'00011': 'LAN/Network Access Point',
				'00100': 'Audio', #Audio/Video
				'00101': 'Peripheral',
				'00110': 'Imaging',
				'00111': 'Wearable',
				'01000': 'Toy',
				'01001': 'Health',
				'11111': 'Uncategorized: device code not specified'
				#XXXXX#: 'All other values reserved'
			}
			
			madc = major_device_class.get(section)
			
			if not madc:
				madc = 'Uncategorized'
			
			return madc
		
		def getMinorDeviceClass(self, CoD: [hex, int], ret_madc=False) -> str:	# Devuelve el "Minor Device Class" de un formato CoD (Class of Device/Service) de Bluetooth.
			# Assigned Numbers for Baseband
			madc = self.getMajorDeviceClass(CoD)
			
			if CoD.__class__ == int:
				binary = str(CoD).zfill(24)
			elif CoD.__class__ == str and not CoD.startswith('0x'):
				CoD = CoD.replace('0b', '')
				binary = CoD.zfill(24)
			else:
				binary = bin(int(CoD, 16))[2:]
			
			binary = binary[::-1]
			s_ini = 2
			s_end = 7
			
			section = binary[s_ini:s_end+1]
			section = section[::-1]
			
			if madc == 'Computer':						#Sub Device Class field for the 'Computer' Major Class
				minor_device_class = {
					'000000': 'Uncategorized, code for device not assigned',
					'000001': 'Desktop Workstation',
					'000010': 'Server-class Computer',
					'000011': 'Laptop',
					'000100': 'Handheld PC/PDA (Clamshell)',
					'000101': 'Palm-sized PC/PDA',
					'000110': 'Wearable Computer (Watch Size)',
					'000111': 'Tablet'
					#XXXXXX#: 'All other values reserved'
				}
				midc = minor_device_class.get(section)
			elif madc == 'Phone':						#Sub Device Classes for the 'Phone' Major Class
				minor_device_class = {
					'000000': 'Uncategorized, code for device not assigned',
					'000001': 'Cellular',
					'000010': 'Cordless',
					'000011': 'Smart Phone',
					'000100': 'Wired Modem or Voice Gateway',
					'000101': 'Common ISDN Access'
					#XXXXXX#: 'All other values reserved'
				}
				midc = minor_device_class.get(section)
			elif madc == 'LAN/Network Access Point':	#The LAN/Network Access Point Load Factor field
				minor_device_class = {
					'000000': 'Fully available',
					'001000': '1 - 17% utilized',
					'010000': '17 - 33% utilized',
					'011000': '33 - 50% utilized',
					'100000': '50 - 67% utilized',
					'101000': '67 - 83% utilized',
					'110000': '83 - 99% utilized',
					'111000': 'No service available'
					#XXXXXX#: 'All other values reserved'
				}
				midc = minor_device_class.get(section)
			elif madc == 'Audio':						#Sub Device Classes for the 'Audio/Video' Major Class
				minor_device_class = {
					'000000': 'Uncategorized, code not assigned',
					'000001': 'Wearable Headset Device',
					'000010': 'Hands-free Device',
					'000011': '(Reserved)',
					'000100': 'Microphone',
					'000101': 'Loudspeaker',
					'000110': 'Headphones',
					'000111': 'Portable Audio',
					'001000': 'Car Audio',
					'001001': 'Set-top Box',
					'001010': 'HiFi Audio Device',
					'001011': 'VCR',
					'001100': 'Video Camera',
					'001101': 'Camcorder',
					'001110': 'Video Monitor',
					'001111': 'Video Display and Loudspeaker',
					'010000': 'Video Conferencing',
					'010001': '(Reserved)',
					'010010': 'Gaming/Toy'
					#XXXXXX#: 'All other values reserved'
				}
				midc = minor_device_class.get(section)
			elif madc == 'Peripheral':					#The Peripheral Major Class keyboard/pointing device field
				minor_device_class = {
					'00': 'Not Keyboard/Not Pointing Device',
					'01': 'Keyboard',
					'10': 'Pointing Device',
					'11': 'Combo Keyboard/Pointing Device'
					#XXXXXX#: 'All other values reserved'
				}
				device_type = {							#Reserved sub-field for the device type
					'0000': 'Uncategorized device',
					'0001': 'Joystick',
					'0010': 'Gamepad',
					'0011': 'Remote Control',
					'0100': 'Sensing Device',
					'0101': 'Digitizer Tablet',
					'0110': 'Card Reader',
					'0111': 'Digital Pen',
					'1000': 'Handheld scanner for bar-codes, RFID, etc.',
					'1001': 'Handheld gestural input device'
					#XXXX#: 'All other values reserved'
				}
				midc = minor_device_class.get(section[:2])
				if device_type.get(section[2:]):
					midc += ': ' + device_type.get(section[2:])
				else:
					midc += ': Uncategorized'
			elif madc == 'Imaging':						#The Imaging Major Class
				midc = ''
				if section[2] == '1':
					midc += 'Display, '
				if section[3] == '1':
					midc += 'Camera, '
				if section[4] == '1':
					midc += 'Scanner, '
				if section[5] == '1':
					midc += 'Printer'
				if midc.endswith(', '):
					midc = midc[:-2]
			elif madc == 'Wearable':					#Minor Device Class field - Wearable Major Class
				minor_device_class = {
					'000001': 'Wrist Watch',
					'000010': 'Pager',
					'000011': 'Jacket',
					'000100': 'Helmet',
					'000101': 'Glasses'
					#XXXXXX#: 'All other values reserved'
				}
				midc = minor_device_class.get(section)
			elif madc == 'Toy':							#Minor Device Class field - Toy Major Class
				minor_device_class = {
					'000001': 'Robot',
					'000010': 'Vehicle',
					'000011': 'Doll / Action Figure',
					'000100': 'Controller',
					'000101': 'Game'
					#XXXXXX#: 'All other values reserved'
				}
				midc = minor_device_class.get(section)
			elif madc == 'Health':						#Minor Device Class field - Health
				minor_device_class = {
					'000000': 'Undefined',
					'000001': 'Blood Pressure Monitor',
					'000010': 'Thermometer',
					'000011': 'Weighing Scale',
					'000100': 'Glucose Meter',
					'000101': 'Pulse Oximeter',
					'000110': 'Heart/Pulse Rate Monitor',
					'000111': 'Health Data Display',
					'001000': 'Step Counter',
					'001001': 'Body Composition Analyzer',
					'001010': 'Peak Flow Monitor',
					'001011': 'Medication Monitor',
					'001100': 'Knee Prosthesis',
					'001101': 'Ankle Prosthesis',
					'001110': 'Generic Health Manager',
					'001111': 'Personal Mobility Device'
					#XXXXXX#: 'All other values reserved'
				}
				midc = minor_device_class.get(section)
			else:
				midc = None
			
			if not midc:
				midc = 'Uncategorized'
			
			if ret_madc:
				return midc, madc
			else:
				return midc
		
		def getSavedBTHDevices(self, jsonify=False) -> dict:			# Devuelve un diccionario con la información de los Dispositivos Bluetooth que estan vinculados.
			
			aReg = WR.ConnectRegistry(None, WR.HKEY_LOCAL_MACHINE)
			aKey = WR.OpenKey(aReg, r'SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Devices')
			
			devices = {}
			
			for i in range(128):
				try:
					keyname = WR.EnumKey(aKey, i).upper()
					asubkey = WR.OpenKey(aKey, keyname)
					name = WR.QueryValueEx(asubkey, 'Name')[0][:-1].decode()
					lastConn = WR.QueryValueEx(asubkey, 'LastConnected')[0]
					lastSeen = WR.QueryValueEx(asubkey, 'lastSeen')[0]
					CoD = hex(WR.QueryValueEx(asubkey, 'COD')[0])
					masc = self.getMajorServiceClass(CoD)
					midc, madc = self.getMinorDeviceClass(CoD, ret_madc=True)
					devices[i] = {
						'name': name,
						'address': self.splitBytes(keyname, ':'),
						'lastConnected': str(self.getFiletime(lastConn)),
						'lastSeen': str(self.getFiletime(lastSeen)),
						'majorServiceClass': masc,
						'majorDeviceClass': madc,
						'minorDeviceClass': midc
					}
				except WindowsError:
					print(i, False)
					break
			
			if jsonify:
				devices = json.dumps(devices, indent=4)
			
			return devices
		
		# Otros --------------------------------------------------------
		def splitBytes(self, hexa, char=':'):							# Divide un hexadecimal en bytes añadiendo el caracter deseado.
			_bytes = []
			for x, h in enumerate(hexa):
				if x % 2 == 0:
					_bytes.append(h)
				else:
					_bytes[int(x/2)] += h
			return char.join(_bytes)
		
		def splitText(self, text, chunk_size=32):						# Divide un texto por palabras en lineas de tamaño limite indicado.
			
			output = []
			chunks  = len(text)//chunk_size
			chunks += 1 if len(text)%chunk_size > 0 else 1
			
			while text:
				
				p = chunk_size
				br = 1
				
				try:
					while not text[p] == ' ':
						p -= 1
						if p == 0:
							br = 0
							p = chunk_size
							break
				except: pass
				
				chunk = text[:p]
				text = text[p+br:]
				output.append(chunk)
			
			return output
		
		def hash(self, text, algo='sha1'): #Use							# Devuelve el Hash del texto con el algoritmo seleccionado.
			algo = algo.lower()
			hash_ = text.encode()
			if   algo == 'sha1':   hash_ = hashlib.sha1(hash_)
			elif algo == 'sha224': hash_ = hashlib.sha224(hash_)
			elif algo == 'sha256': hash_ = hashlib.sha256(hash_)
			elif algo == 'sha384': hash_ = hashlib.sha384(hash_)
			elif algo == 'sha512': hash_ = hashlib.sha512(hash_)
			elif algo == 'md5':    hash_ = hashlib.md5(hash_)
			else: return None
			hash_ = hash_.hexdigest()
			return self.Hash(hash_, text, algo)
		
		def getFiletime(self, time: [hex, int]) -> datetime:			# Convierte de formato Filetime (Win 64-bit value) a Datetime
			'''
				Win32 FILETIME:
					Contains a 64-bit value representing the number of
					100-nanosecond intervals since January 1, 1601 (UTC).
				Example:
					time = '0x1d7d7583c54c000' (hex) or 132811488000000000 (int)
					Return: '2021-11-12 00:00:00' (datetime)
			'''
			if time.__class__ in [int, float]:
				microsecs = int(time)/10
			else:
				microsecs = int(time, 16)/10
			secs, microsecs = divmod(microsecs, 1000000)
			days, secs = divmod(secs, 86400)
			dt = datetime(1601, 1, 1) + timedelta(days, secs, microsecs)
			return dt
		
		def getLastError(self) -> int:									# DWORD WINAPI GetLastError(void);
			DWORD = ctypes.c_uint32
			_GetLastError = ctypes.windll.kernel32.GetLastError
			_GetLastError.argtypes = []
			_GetLastError.restype = DWORD
			return _GetLastError()
		
		def writeHiddenText(self, text_to_print):						# Muestra el text_to_print en pantalla y pide capturar texto, el texto capturado no se mostraá pero será devuelto por la función.
			''' passwd = utils.Utilities.writeHiddenText('Password: ')
				print(f'La contraseña escrita fue: {passwd}') '''
			from getpass import getpass
			return getpass(text_to_print)
		
		def flushBuffer(self):											# Vacia el Buffer (Flush)
			# Limpia el Buffer (Flush) para que los input aparescan vacios.
			# Si se escribe a la 'Nada' antes de un input, todo lo escrito aparecera en el input.
			try:
				import msvcrt
				while msvcrt.kbhit(): msvcrt.getch()
			except ImportError:
				import sys, termios
				termios.tcflush(sys.stdin, termios.TCIOFLUSH)

#=======================================================================
#=======================================================================
#=======================================================================

# ~ ┌───┬───┐   ╔═══╦═══╗   ▄▄▄▄▄▄▄▄▄
# ~ │   │   │   ║   ║   ║   █   █   █
# ~ ├───┼───┤   ╠═══╬═══╣   █■■■█■■■█
# ~ │   │   │   ║   ║   ║   █   █   █
# ~ └───┴───┘   ╚═══╩═══╝   ▀▀▀▀▀▀▀▀▀

STRUCT = '''\
   
■■■ Class Utils ({})
    ║
    ║ - Main Classes:
    ╠══ Class Actions
    ║   ║
    ║   ║ - Error Classes: ───────────────────
    ║   ╠══ Class BeepError
    ║   ╠══ Class EmptyingTheTrashError
    ║   ╠══ Class ExitWindowsError
    ║   ╠══ Class StyleOfWindowError
    ║   ║
    ║   ║ - Classes: ─────────────────────────
    ║   ╠══ Class Clipboard
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    └── property text (get, set, delete)
    ║   ║
    ║   ╠══ Class Explorer
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function getFileName
    ║   ║    ├── function getFolderName
    ║   ║    └── function getFileNameSave
    ║   ║
    ║   ╠══ Class Keyboard
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function getVK
    ║   ║    ├── function getKeyState
    ║   ║    ├── function getAsyncKeyState
    ║   ║    ├── function press
    ║   ║    ├── function pressAndHold
    ║   ║    ├── function release
    ║   ║    ├── function pressHoldRelease
    ║   ║    ├── function typeWithShift
    ║   ║    └── function typer
    ║   ║
    ║   ╠══ Class Mouse
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── property position (get, set)
    ║   ║    ├── function leftClick
    ║   ║    ├── function leftClickDown
    ║   ║    ├── function leftClickUp
    ║   ║    ├── function rightClick
    ║   ║    ├── function rightClickDown
    ║   ║    ├── function rightClickUp
    ║   ║    ├── function middleClick
    ║   ║    ├── function middleClickDown
    ║   ║    └── function middleClickUp
    ║   ║
    ║   ╠══ Class VBS
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function runScriptVBS
    ║   ║    ├── function minimizeAll
    ║   ║    ├── function ejectCDROM
    ║   ║    ├── function getWindowsProductKey
    ║   ║    └── function setVolume
    ║   ║
    ║   ╠══ Class Volume
    ║   │    ║
    ║   │    ║ - Error Classes: ──────────────
    ║   │    ╠══ Class VolumeControlIsNotSupported
    ║   │    ╠══ Class MuteControlIsNotSupported
    ║   │    ╠══ Class ChannelDoesNotExists
    ║   │    ║
    ║   │    ║ - Classes: ────────────────────
    ║   │    ╠══ Class VolumeHandler
    ║   │    │
    ║   │    │ - Functions: ──────────────────
    ║   │    ├── property volumeRange        (get)
    ║   │    ├── property volumeStepInfo     (get)
    ║   │    ├── property hardwareSupport    (get)
    ║   │    ├── property volume             (get, set)
    ║   │    ├── property volumedB           (get, set)
    ║   │    ├── property mute               (get, set)
    ║   │    ├── function getChannelCount
    ║   │    ├── function getChannelVol
    ║   │    ├── function setChannelVol
    ║   │    ├── function getChannelVoldB
    ║   │    ├── function setChannelVoldB
    ║   │    ├── function balanceVolChannels
    ║   │    ├── function volumeStepUp
    ║   │    └── function volumeStepDown
    ║   │
    ║   │ - Functions: ───────────────────────
    ║   ├── function beep
    ║   ├── function changePasswordCurrentUser
    ║   ├── function cleanRecyclerBin
    ║   ├── function displaySwitch
    ║   ├── function exitWindows
    ║   ├── function getActiveWindow
    ║   ├── function getNameActiveWindow
    ║   ├── function getPathFromWinExplorer
    ║   ├── function getPrivileges
    ║   ├── function getProcessPrivileges
    ║   ├── function getWindowRect
    ║   ├── function hideConsole
    ║   ├── function hideCursor
    ║   ├── function hideWindow
    ║   ├── function killProcess
    ║   ├── function lockWorkStation
    ║   ├── function messageBox
    ║   ├── function minimizeWindowCMD
    ║   ├── function runAsAdmin
    ║   ├── function runProgram
    ║   ├── function screenshot
    ║   ├── function setConsoleSize
    ║   ├── function setCursorPos
    ║   ├── function setTopMostConsole
    ║   ├── function setTopMostWindow
    ║   ├── function setTopConsole
    ║   ├── function setTopWindow
    ║   ├── function setPriorityPID
    ║   └── function startApp
    ║
    ╠═ EditRegistry
    ║   ║
    ║   ║ - Classes: ─────────────────────────
    ║   ╠══ Class DropBox
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function enable
    ║   ║    └── function disable
    ║   ║
    ║   ╠══ Class Explorer
    ║   ║    ║
    ║   ║    ║ - Classes: ────────────────────
    ║   ║    ╠══ Class Close
    ║   ║    ╠══ Class PropertiesRecycleBin
    ║   ║    ╠══ Class ControlPanel
    ║   ║    ╠══ Class ContextMenu
    ║   ║    ╠══ Class Clock
    ║   ║    ╠══ Class SCAHealth
    ║   ║    ╠══ Class SCANetwork
    ║   ║    ╠══ Class SCAPower
    ║   ║    ╠══ Class SCAVolume
    ║   ║    ╠══ Class ActiveDesktop
    ║   ║    ╠══ Class AutoTrayNotify
    ║   ║    ╠══ Class DrivesInSendToMenu
    ║   ║    ╠══ Class FavoritesMenu
    ║   ║    ╠══ Class InternetOpenWith
    ║   ║    ╠══ Class RecentDocsMenu
    ║   ║    ╠══ Class Run
    ║   ║    ╠══ Class SaveSettings
    ║   ║    ╠══ Class TrayItemsDisplay
    ║   ║    ╠══ Class ClassicShell
    ║   ║    ║ #Modificadas:
    ║   ║    ╚══ Class WindowMinimizingShortcuts
    ║   ║
    ║   ╠══ Class FoldersOnThisPC
    ║   ║    ║
    ║   ║    ║ - Classes: ────────────────────
    ║   ║    ╠══ Class Folder3DObjects
    ║   ║    ╠══ Class FolderDesktop
    ║   ║    ╠══ Class FolderDocuments
    ║   ║    ╠══ Class FolderDownloads
    ║   ║    ╠══ Class FolderMusic
    ║   ║    ╠══ Class FolderPictures
    ║   ║    ╚══ Class FolderVideos
    ║   ║
    ║   ╠══ Class OneDrive
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function enable
    ║   ║    └── function disable
    ║   ║
    ║   ╠══ Class PhysicalDrivesInWinExplorer
    ║   ║    ║
    ║   ║    ║ - Error Classes: ──────────────
    ║   ║    ╠══ Class DriveLettersError
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function enumHiddenDrives
    ║   ║    ├── function hide
    ║   ║    ├── function show
    ║   ║    ├── function showAll
    ║   ║    └── function cleanUp
    ║   ║
    ║   ╠══ Class Programs
    ║   ║    ║
    ║   ║    ║ - Classes: ────────────────────
    ║   ║    ╠══ Class ProgramsAndFeatures
    ║   ║    ╠══ Class WindowsFeatures
    ║   ║    ╠══ Class WindowsMarketplace
    ║   ║    ╠══ Class ProgramsControlPanel
    ║   ║    ╠══ Class InstalledUpdates
    ║   ║    ╠══ Class DefaultPrograms
    ║   ║    ╚══ Class GetPrograms
    ║   ║
    ║   ╠══ Class PowerPlan
    ║   ║    ║
    ║   ║    ║ - Error Classes: ──────────────
    ║   ║    ╠══ Class BrightnessLevelError
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── property brightnessLevel      (get)
    ║   ║    ├── property currentPowerPlanGUID (get)
    ║   ║    ├── function powerSavingMode
    ║   ║    └── function setBrightnessLevel
    ║   ║
    ║   ╚══ Class TaskManager
    ║        │
    ║        │ - Functions: ──────────────────
    ║        ├── function enable
    ║        ├── function disable
    ║        └── function cleanUp
    ║
    ╠═ Class MemoryInfo
    ║   │
    ║   │ - Functions: ───────────────────────
    ║   ├── function bytesToString
    ║   ├── function memoryStatusUpdate
    ║   ├── function totalFilesInRecyclerBin
    ║   └── function totalSizeInRecyclerBin
    ║
    ╠═ Class NetworkInfo
    ║   ║
    ║   ║ - Classes: ─────────────────────────
    ║   ╠══ Class GetIP
    ║   │    │
    ║   │    │ - Functions: ──────────────────
    ║   │    └── property only_local (get, set)
    ║   │
    ║   │ - Functions: ───────────────────────
    ║   ├── function latin1_encoding
    ║   ├── function ESSIDEnum
    ║   ├── function ESSIDPasswd
    ║   ├── function findServiceName
    ║   ├── function getIPv4
    ║   └── function packetIPAddress
    ║
    ╠═ Class SystemInfo
    ║   │
    ║   │ - Functions: ───────────────────────
    ║   ├── function enumComputerSystemInfo
    ║   ├── function enumLocalDisk
    ║   ├── function enumLocalUsersAndGroups
    ║   ├── function enumProcess
    ║   ├── property isCapsLockActive      (get)
    ║   ├── property isLinux               (get)
    ║   ├── property isMouseInstalled      (get)
    ║   ├── property isPythonV2            (get)
    ║   ├── property isPythonV3            (get)
    ║   ├── property isSlowMachine         (get)
    ║   ├── property isUserAnAdmin         (get)
    ║   ├── function isUserPasswordValid
    ║   ├── property isWindows             (get)
    ║   ├── property currentProcessId      (get)
    ║   ├── property cursorPos             (get)
    ║   ├── property currentSystemMetrics  (get)
    ║   ├── property realSystemMetrics     (get)
    ║   ├── property displaySettings       (get)
    ║   ├── property computerName          (get)
    ║   ├── property homeDrive             (get)
    ║   ├── property numberOfMonitors      (get)
    ║   ├── property numberOfProcessors    (get)
    ║   ├── property os                    (get)
    ║   ├── property processorArchitecture (get)
    ║   ├── property processorIdentifier   (get)
    ║   ├── property screenSize            (get)
    ║   ├── property systemDrive           (get)
    ║   ├── property systemRoot            (get)
    ║   ├── function systemUptime
    ║   ├── property userDefaultLanguage   (get)
    ║   ├── property userDowntime          (get)
    ║   ├── property userName              (get)
    ║   ├── property winDir                (get)
    ║   └── property collectAll            (get)
    ║
    ╚═ Class Utilities
        ║
        ║ - Classes: ─────────────────────────
        ╠══ Class AsciiFont
        ║    ║
        ║    ║ - Error Classes: ──────────────
        ║    ╠══ Class NotSupportedError
        ║    ╠══ Class TypeError
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function ansiShadow
        ║    ├── function ansiRegular
        ║    ├── function calvinS
        ║    ├── function deltaCorpsPriest
        ║    ├── function block
        ║    ├── function alligator
        ║    ├── function cybermedium
        ║    ├── function dobleShorts
        ║    ├── function doble
        ║    └── function rammstein
        ║
        ╠══ Class DoomsdayRule
        ║    ║
        ║    ║ - Error Classes: ──────────────
        ║    ╠══ Class MonthDoesNotExist
        ║    ╠══ Class InvalidDate
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function getWeekday (Principal)
        ║    ├── function getRandomDate
        ║    ├── function isLeapYear
        ║    ├── function getCenturyBaseDay
        ║    ├── function getBaseDayOfDecade
        ║    ├── function isValidDate
        ║    ├── function getDateValues
        ║    ├── function getMonthValue
        ║    └── function calculateWeekday
        ║
        ╠══ Class Images
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function convertFromCv2ToImage
        ║    ├── function convertFromImageToCv2
        ║    ├── function screenshot
        ║    ├── function cropImage
        ║    ├── function compare
        ║    ├── function get_grayscale
        ║    ├── function remove_noise
        ║    ├── function thresholding
        ║    ├── function histogram
        ║    ├── function dilate
        ║    ├── function erode
        ║    ├── function opening
        ║    └── function canny
        ║
        ╠══ Class NumberSystems
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function decimalToBinary
        ║    └── function binaryToDecimal
        ║
        ╠══ Class UBZ2
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function addIconToFileExtension
        ║    ├── function generateIcon
        ║    ├── function compress
        ║    ├── function decompress
        ║    └── function getDataFromUBZ2File
        ║
        ╠══ Class Hash
        │    ║
        │    ║ - Error Classes: ──────────────
        │    ╠══ Class HashNotAvailableError
        │    │
        │    │ - Functions: ──────────────────
        │    ├── function update
        │    └── function f_hash
        │
        │ - Functions: ───────────────────────
        │ #Math:
        ├── function cos
        ├── function sin
        ├── function diagonal
        ├── function euclideanDistance
        ├── function getAngle
        │ #Pygame:
        ├── function moveWindow
        ├── function curWinRect
        ├── function curWinSize
        │ #Bluetooth:
        ├── function getMajorServiceClass
        ├── function getMajorDeviceClass
        ├── function getMinorDeviceClass
        ├── function getSavedBTHDevices
        │ #Otros:
        ├── function splitBytes
        ├── function splitText
        ├── function hash
        ├── function getFiletime
        ├── function getLastError
        ├── function writeHiddenText
        └── function flushBuffer

 All Classes Have a 'use', 'classes' and 'functions' variables.

 *Classes:    71
 *Functions:  141
 *Properties: 32

'''.format(__version__)



# Ejecuta esto despues de terminar la ejecución del programa.
@atexit.register
def close():
	time.sleep(.1)

#=======================================================================

if __name__ == '__main__':
	
	# Pruebas:
	
	# ~ print(STRUCT)
	
	utils = Utils()
	# ~ utils.Actions.setTopMostWindow()
	# ~ name = utils.Utilities.AsciiFont.deltaCorpsPriest(__title__)
	# ~ ver = utils.Utilities.AsciiFont.ansiRegular(__version__)
	# ~ print('\n\n Delta Corps Priest:\n\n' + name + '\n\n Ansi Regular:\n\n' + ver)
	
	#-------------------------------------------------------------------
	
	nwinf = utils.NetworkInfo
	sysinf = utils.SystemInfo
	actions = utils.Actions
	
	#-------------------------------------------------------------------
	
	lang = sysinf.userDefaultLanguage
	print(lang)
	
	#-------------------------------------------------------------------
	
	port = 80
	serv_name = nwinf.findServiceName(port)
	print(serv_name)
	
	ports = [19,21,23,24,25]
	
	serv_names = nwinf.findServiceName(ports)
	print(json.dumps(serv_names, indent=4))
	
	serv_names = nwinf.findServiceName(ports, 'udp')
	print(json.dumps(serv_names, indent=4))
	
	serv_names = nwinf.findServiceName(ports, nones=True)
	print(json.dumps(serv_names, indent=4))
	
	serv_names = nwinf.findServiceName(ports, 'udp', nones=True)
	print(json.dumps(serv_names, indent=4))
	
	port = {'tcp': [19,21,23,24,25], 'udp': [19,21,80,81,88]}
	serv_name = nwinf.findServiceName(port)
	print(json.dumps(serv_name, indent=4))
	
	#-------------------------------------------------------------------
	
	ip = '192.168.1.0'
	
	# Empaqueta la IP:
	packed = nwinf.packetIPAddress(ip)
	print(packed)    # b'\xc0\xa8\x01\x00'
	
	# Desempaqueta la IP:
	unpacked = nwinf.packetIPAddress(packed, unpacked=True)
	print(unpacked)  # 192.168.1.0
	
	# Empaqueta la IP y la devuelve en hexadecimal:
	packed = nwinf.packetIPAddress(ip, hexlify=True)
	print(packed)    # b'c0a80100'
	
	#-------------------------------------------------------------------
	
	# Obtiene la IPv4 Local:
	ip = nwinf.getIPv4()
	print(ip)
	
	# Obtiene la IPv4 de un Host Remoto:
	ip = nwinf.getIPv4('www.google.com')
	print(ip)
	
	#-------------------------------------------------------------------
	# Control de Volumen del Sistema (Muy Eficiente)
	
	vol = actions.Volume
	
	#-----------------------------------
	
	#Control de silenciado:
	print(vol.mute)					# Nos mostrara el estado del sistema (Si esta silenciado o no)
	vol.mute = True					# Silencia el sistema.
	print(vol.mute)					# Ahora el sistema estará silenciado (hasta que se cambie el valor del volumen o se desmutea)
	vol.mute = False				# Quita el silenciado del sistema.
	print(vol.mute)					# Ahora el sistema ya no estará silenciado.
	
	#-----------------------------------
	
	#Control de nivel de Volumen:
	print(vol.volume)				# Obtiene el nivel de volumen de 0~100
	vol.volume = 72					# Pone un nuevo nivel de volumen.
	print(vol.volume)				# Obtiene el nuevo nivel de volumen de 0~100
	
	#Control de nivel de Volumen en decibeles (dB):
	print(vol.volumeDB)				# Obtiene el nivel de volumen en Decibeles (dB en positivos) de aprox. 'Volume.volumeRange['levelMinDB']~Volume.volumeRange['levelMaxDB']' donde el limite es aprox. '-65.254~0' dB
	vol.volumeDB = -5				# Pone un nuevo nivel de volumen en decibeles.
	print(vol.volumeDB)				# Obtiene el nuevo nivel de volumen de 0~100
	
	print(vol.volumeRange)			# Obtiene el rango de volumen en Decibeles (dB) 'levelMinDB, levelMaxDB y volumeIncrementDB'.
	
	#-----------------------------------
	
	#Control de nivel de Volumen en Saltos (Como al presionar teclas de volumen):
	print(vol.volumeStepInfo)		#Actual posicion del audio.
	vol.volumeStepUp()				#Sube el volumen, como presionar 1 vez para subir volumen.
	print(vol.volumeStepInfo)		#Nueva posicion del audio.
	vol.volumeStepDown()			#Baja el volumen, como presionar 1 vez para bajar volumen.
	print(vol.volumeStepInfo)		#Regresando una posicion.
	
	#-----------------------------------
	
	#Informacion de disponibilidad del sistema:
	print(vol.hardwareSupport)		# Obtiene la lista del hardware soportado: ['Volume Control', 'Mute Control', 'Peak Meter']
	
	#-----------------------------------
	
	#Control de los canales de volumen (por ejemplo las bocinas izquierda y derecha de tu laptop):
	print(vol.getChannelCount())	# Muestra la cantidad de canales, Ejemplo: 2 (Bocina Izquierda y Derecha respectivamente).
	
	print(vol.getChannelVol())		# Muestra el volumen del Canal 1 con valores de '0~100' (Ejemplo: Bocina Izquierda)
	print(vol.getChannelVol(2))		# Muestra el volumen del Canal 2 con valores de '0~100' (Ejemplo: Bocina Derecha)
	vol.setChannelVol(10)			# Cambia el volumen del Canal 1 (Izq) a 10.
	vol.setChannelVol(75, 2)		# Cambia el volumen del Canal 2 (Der) a 75.
	print(vol.getChannelVol())		# Muestra el nuevo volumen en el Canal 1 con valores de '0~100'
	print(vol.getChannelVol(2))		# Muestra el nuevo volumen en el Canal 2 con valores de '0~100'
	
	vol.balanceVolChannels()		# Esto balancea el volumen en todos los canales de audio al nivel de volumen mas alto entre los canales (en este ejemplo tomara el 75 del canal 2).
	
	#Control de los canales de volumen en decibeles (por ejemplo las bocinas izquierda y derecha de tu laptop):
	print(vol.getChannelVoldB())	# Muestra el volumen del Canal 1 con valores de 'Volume.volumeRange['levelMinDB']~Volume.volumeRange['levelMaxDB']' (Ejemplo: Bocina Izquierda)
	print(vol.getChannelVoldB(2))	# Muestra el volumen del Canal 2 con valores de 'Volume.volumeRange['levelMinDB']~Volume.volumeRange['levelMaxDB']' (Ejemplo: Bocina Derecha)
	vol.setChannelVoldB(-33)		# Cambia el volumen del Canal 1 (Izq) a -33 decibeles (dB).
	vol.setChannelVoldB(-5, 2)		# Cambia el volumen del Canal 2 (Der) a -5  decibeles (dB).
	print(vol.getChannelVoldB())	# Muestra el nuevo volumen en el Canal 1 con valores de 'Volume.volumeRange['levelMinDB']~Volume.volumeRange['levelMaxDB']'
	print(vol.getChannelVoldB(2))	# Muestra el nuevo volumen en el Canal 2 con valores de 'Volume.volumeRange['levelMinDB']~Volume.volumeRange['levelMaxDB']'
	
	vol.balanceVolChannels()		# Esto balancea el volumen en todos los canales de audio al nivel de volumen mas alto entre los canales (en este ejemplo tomara el -5 del canal 2).
	
	#-------------------------------------------------------------------
	
	# Bluetooth: Obtiene los dispositivos que estan vinculados e información sobre estos:
	devices = utils.Utilities.getSavedBTHDevices(jsonify=True)
	print(devices)
	
	#-------------------------------------------------------------------
	
	# Cortador de cadenas, limita las lineas a un maximo de caracteres pero sin cortar las palabras.
	text = 'Hola mundo! xD Soy el creador de estas hermosas funciones.'
	text_list = utils.Utilities.splitText(text, 20)
	print(text_list)
	
	#-------------------------------------------------------------------
	
	# Conversiones de Sistemas Numericos
	out = utils.Utilities.NumberSystems.decimalToBinary(128, True)
	print(out)
	out = utils.Utilities.NumberSystems.binaryToDecimal(out)
	print(out)
	
	#===================================================================
	
	# ~ for a in utils.Actions.classes.list:
		# ~ try:
			# ~ print(a, isinstance(eval('utils.Actions.'+a+'("")'), Exception))
		# ~ except: pass
	
	# ~ print(utils.Actions.classes)
	# ~ list_ = [
		# ~ a for a in dir(utils.Actions)
		# ~ if a[0] == a[0].upper()
		# ~ and not a[0] == '_'
		# ~ and not a.startswith('not_')
	# ~ ]
	# ~ print(list_)
	# ~ print(utils.Actions.classes)
	# ~ print(utils.Actions.functions)
	
	#-------------------------------------------------------------------
	'''
	def bucle(base='utils', deep=0, spa2='', data=False):
		print()
		print(base, deep)
		out_main = ''
		
		cls_list = '.classes.list'
		cls_list_err = '.classes.error_list'
		fn_list = '.functions.list'
		
		spa  = spa2 if deep > 0 else '    '
		swb  = ' ║  '
		sbg  = ' ║ -'
		swb2 = ' │  '
		sbg2 = ' │ -'
		brk  = '\n'
		
		# ~ if deep == 0:
		values = eval(base+cls_list)[:1]
		# ~ else:
			# ~ values = eval(base+cls_list)
		
		for i1, cls in enumerate(values):
			
			sub_cls = base+'.'+cls
			print(sub_cls)
			sub_cls_list    = cls+'_list'
			sub_errcls_list = cls+'_list_err'
			sub_fn_list     = cls+'fn_list'
			
			exec(sub_cls_list    + ' = ' + sub_cls + cls_list)
			exec(sub_errcls_list + ' = ' + sub_cls + cls_list_err)
			exec(sub_fn_list     + ' = ' + sub_cls + fn_list)
			
			out_main_class = ''
			
			if deep == 0:
				if i1 == len(values)-1:
					if not i1 == 0:
						out_main_class += spa + swb*(deep+1) + brk
					out_main_class += spa + swb*deep + ' ╚══ Class ' + cls + brk
					spa = spa*2
					deep -= 1
				elif i1 == 0:
					out_main_class += spa + swb*deep + ' ╠══ Class ' + cls + brk
				else:
					out_main_class += spa + swb*deep + brk
					out_main_class += spa + swb*deep + ' ╠══ Class ' + cls + brk
			else:
				deep -= 1
				if i1 == len(values)-1:
					if not i1 == 0:
						out_main_class += spa + swb*(deep+1) + brk
					if data:
						out_main_class += spa + swb*deep + ' ╠══ Class ' + cls + brk
					else:
						out_main_class += spa + swb*deep + ' ╚══ Class ' + cls + brk
					spa = spa2 + '    '*2
					deep -= 1
				elif i1 == 0:
					out_main_class += spa + swb*deep + ' ╠══ Class ' + cls + brk
				else:
					out_main_class += spa + swb*deep + brk
					out_main_class += spa + swb*deep + ' ╠══ Class ' + cls + brk
				
			
			
			deep += 1
			
			methods = []
			others = []
			
			for cls in eval(sub_fn_list):
				sub_cls2 = sub_cls+'.'+cls
				type_obj = type(eval(sub_cls2)).__name__
				if type_obj == 'method':
					methods.append(cls)
				else:
					others.append((cls, type_obj))
			
			others_data = False
			out_others = ''
			if others:
				print(others)
				out_others += spa + swb*deep + swb2 + brk
				out_others += spa + swb*deep + sbg2 + ' Others:' + brk
				for i5, (name, _type) in enumerate(others):
					others_data = True
					if i5 == len(others)-1:
						out_others += spa + swb*deep + ' └── ' + _type + ' ' + name + brk
					else:
						out_others += spa + swb*deep + ' ├── ' + _type + ' ' + name + brk
			
			methods_data = False
			out_methods = ''
			if methods:
				out_methods += spa + swb*deep + swb2 + brk
				out_methods += spa + swb*deep + sbg2 + ' Methods:' + brk
				for i4, name in enumerate(methods):
					methods_data = True
					if others_data:
						out_methods += spa + swb*deep + ' ├── Function ' +  name + brk
					else:
						if i4 == len(methods)-1:
							out_methods += spa + swb*deep + ' └── Function ' +  name + brk
						else:
							out_methods += spa + swb*deep + ' ├── Function ' +  name + brk
			
			classes_data = False
			val = eval(sub_cls_list)
			out_classes = ''
			if val:
				out_classes += spa + swb*deep + swb + brk
				out_classes += spa + swb*deep + sbg + ' Classes:' + brk
				# ~ for i3, cls in enumerate(val):
					# ~ classes_data = True
					# ~ if methods_data or others_data:
						# ~ out_classes += spa + swb*deep + ' ╠══ Class ' + cls + brk
					# ~ else:
						# ~ if i3 == len(val)-1:
							# ~ out_classes += spa + swb*deep + ' ╚══ Class ' + cls + brk
						# ~ else:
							# ~ out_classes += spa + swb*deep + ' ╠══ Class ' + cls + brk
				classes_data = True
				data = methods_data or others_data
				out_classes += bucle(sub_cls, deep+1, spa + swb*deep, data)
			
			val = eval(sub_errcls_list)
			out_error_classes = ''
			if val:
				out_error_classes += spa + swb*deep + swb + brk
				out_error_classes += spa + swb*deep + sbg + ' Error Classes:' + brk
				for i2, cls in enumerate(val):
					if classes_data or methods_data or others_data:
						out_error_classes += spa + swb*deep + ' ╠══ Class ' + cls + brk
					else:
						if i2 == len(val)-1:
							out_error_classes += spa + swb*deep + ' ╚══ Class ' + cls + brk
						else:
							out_error_classes += spa + swb*deep + ' ╠══ Class ' + cls + brk
			
			deep -= 1
			
			out_main += out_main_class + out_error_classes + out_classes + out_methods + out_others
		
		return out_main
	
	spa  = '    '
	swb  = ' ║  '
	sbg  = ' ║ -'
	brk  = '\n'
	
	out_main  = '■■■ Class Utils ({})'.format(__version__) + brk
	out_main += spa + swb + brk
	out_main += spa + sbg + ' Main Classes:' + brk
	out_main += bucle()
	
	print('\n\n',out_main)
	'''
	#-------------------------------------------------------------------
	#-------------------------------------------------------------------
	#-------------------------------------------------------------------
	
	# Algoritmo de Doomsday (Doomsday Rule)
	# ~ date = '22/07/2050'
	# ~ weekday = utils.Utilities.DoomsdayRule.getWeekday(date)
	# ~ print(date + ': ' + weekday)
	
	
	# ~ time.sleep(3)
	# ~ utils.Actions.Keyboard.typer('Hola Mundo!', sleep=.01)
	
	
	# ~ print(utils.Utilities.DoomsdayRule.learnToDoItMentally)
	
	# ~ for x in range(3):
		# ~ utils.Utilities.DoomsdayRule.getRandomDate()
	
	# ~ print(utils.EditRegistry.Programs.use)
	# ~ print(utils.EditRegistry.Programs.enumValues)
	# ~ utils.EditRegistry.Programs.ProgramsAndFeatures.hide()
	# ~ utils.EditRegistry.Programs.ProgramsAndFeatures.show()
	# ~ utils.EditRegistry.Programs.ProgramsAndFeatures.cleanUp()
	
	# ~ print(utils.EditRegistry.Explorer.use)
	# ~ utils.EditRegistry.Explorer.ControlPanel.disable()
	# ~ utils.EditRegistry.Explorer.ControlPanel.enable()
	# ~ utils.EditRegistry.Explorer.ControlPanel.cleanUp()
	
	
	# toma una captura de pantalla despues de 5 segundos de inactividad del usuario
	# ~ while True:
		# ~ if utils.SystemInfo.userDowntime > 5:
			# ~ utils.Actions.screenshot()
			# ~ utils.Actions.beep()
			# ~ break
		# ~ time.sleep(.1)
	
	# ~ utils.Actions.Mouse.position = (150, 200)
	# ~ utils.Actions.Mouse.leftClickDown()
	# ~ utils.Actions.Mouse.position = (150, 300)
	# ~ utils.Actions.Mouse.leftClickUp()
	
	# ~ print(utils.Actions.Mouse.position)
	# ~ utils.Actions.Mouse.position = (105, 205)
	# ~ print(utils.Actions.Mouse.position)
	
	# ~ utils.Actions.Mouse.leftClick()		# clic
	# ~ utils.Actions.Mouse.leftClick(2)	# doble clic
	
	# ~ utils.Actions.Mouse.rightClick()	# clic derecho
	
	# ~ utils.EditRegistry.PhysicalDrivesInWinExplorer.hide('ABCDEFGH')
	# ~ utils.EditRegistry.PhysicalDrivesInWinExplorer.show('CFB')
	# ~ print(utils.EditRegistry.PhysicalDrivesInWinExplorer.enumHiddenDrives())
	# ~ utils.EditRegistry.PhysicalDrivesInWinExplorer.showAll()
	# ~ utils.EditRegistry.PhysicalDrivesInWinExplorer.cleanUp()
	
	# UBZ2 -------------------------------------------------------------
	# ~ print(utils.Utilities.UBZ2.use)
	# ~ utils.Utilities.UBZ2.addIconToFileExtension()
	
	# ~ fileName = utils.Actions.Explorer.getFileName(topmost=False)
	# ~ if fileName:
		# ~ utils.Utilities.UBZ2.compress(fileName)
		# ~ utils.Utilities.UBZ2.decompress(fileName)
		# ~ print(utils.Utilities.UBZ2.getDataFromUBZ2File(fileName))
	#-------------------------------------------------------------------
	
	# ~ utils.EditRegistry.ContextMenu.disable()
	# ~ utils.EditRegistry.TaskManager.disable()
	# ~ utils.EditRegistry.OneDrive.disable()
	# ~ utils.EditRegistry.DropBox.disable()
	# ~ utils.EditRegistry.FoldersOnThisPC.Folder3DObjects.hide()
	
	# ~ print(utils.EditRegistry.PowerPlan.currentPowerPlanGUID)
	# ~ print(utils.EditRegistry.PowerPlan.brightnessLevel)
	# ~ print(utils.EditRegistry.PowerPlan.powerSavingMode())
	# ~ utils.EditRegistry.PowerPlan.setBrightnessLevel(3)
	
	# ~ print(utils.SystemInfo.enumLocalDisk())
	
	# ~ groups = utils.SystemInfo.enumLocalUsersAndGroups()
	# ~ for name, group in groups.items():
		# ~ print(name, group['group'])
		# ~ for user in group['users']:
			# ~ print(user)
	
	# ~ print(utils.SystemInfo.enumComputerSystemInfo())
	
	# ~ utils.Actions.setCursorPos(700,400)
	
	#-------------------------------------------------------------------
	# Buscando la contraseña de usuario 'prueba'.
	# Contraseña de prueba propuesta: 'xD'.
	# ~ palabras = [
		# ~ 'ab',    'cd',    'ef',    'fg',    'hi',
		# ~ 'jk',    'lasd',  'lasd1', 'lasd3', 'lasd2',
		# ~ 'lasd4', 'lasd5', 'lasd6', 'xD',    'XDD',
		# ~ 'xD3',   'xD4',   'lasx1', 'laxd3', 'xasd2'
	# ~ ]
	
	# ~ user = 'prueba'
	
	# ~ for x in palabras:
		# ~ resp = utils.SystemInfo.isUserPasswordValid(user, x)
		# ~ if resp:
			# ~ print('\n User:', user)
			# ~ print('\n Passwd:', x)
			# ~ break

	# ~ if not resp:
		# ~ print('Password Not Found...')
	#-------------------------------------------------------------------
	
	# ~ if utils.Actions.runAsAdmin():
		# ~ print(True)
		# ~ time.sleep(10)
	
	# ~ passwd = utils.Utilities.writeHiddenText('Password: ')
	# ~ print(f'La contraseña escrita fue: {passwd}')
	
	# ~ print('\n\n Ascii Font functions availables: '+utils.Utilities.AsciiFont.functions.list)
	
	# ~ text = 'By: LawlietJH'
	
	# ~ cal = utils.Utilities.AsciiFont.calvinS(text)
	# ~ sha = utils.Utilities.AsciiFont.ansiShadow(text)
	# ~ reg = utils.Utilities.AsciiFont.ansiRegular(text)
	# ~ dcp = utils.Utilities.AsciiFont.deltaCorpsPriest(text)
	# ~ blo = utils.Utilities.AsciiFont.block(text)
	# ~ alg = utils.Utilities.AsciiFont.alligator(text)
	# ~ cyb = utils.Utilities.AsciiFont.cybermedium(text)
	# ~ dsh = utils.Utilities.AsciiFont.dobleShorts(text)
	# ~ dob = utils.Utilities.AsciiFont.doble(text)
	# ~ ram = utils.Utilities.AsciiFont.rammstein(text)
	
	# ~ print('calvinS:\n'          + cal)
	# ~ print('ansiShadow:\n'       + sha)
	# ~ print('ansiRegular:\n'      + reg)
	# ~ print('deltaCorpsPriest:\n' + dcp)
	# ~ print('block:\n'            + blo)
	# ~ print('alligator:\n'        + alg)
	# ~ print('cybermedium:\n'      + cyb)
	# ~ print('dobleShorts:\n'      + dsh)
	# ~ print('doble:\n'            + dob)
	# ~ print('rammstein:\n'        + ram)
	
	# ~ collected = utils.SystemInfo.collectAll
	
	# ~ for key, val in collected.items():
		# ~ print(key.ljust(24), val)
	
	# ~ print(utils.Utilities.hash_use)
	
	# ~ print(utils.Actions.functions)
	
	# ~ key = utils.Actions.VBS.getWindowsProductKey()
	# ~ print('\nClave de Producto de Windows:', key)
	
	# ~ print(utils.Actions.messageBox_use)
	
	# ~ resp = utils.Actions.messageBox(
		# ~ message = 'Esta función te resulta muy útil?',
		# ~ title = 'Es útil?',
		# ~ style = WC.MB_YESNO | WC.MB_ICONQUESTION
				# ~ | WC.MB_DEFAULT_DESKTOP_ONLY
				# ~ | WC.MB_CANCELTRYCONTINUE
	# ~ )
	# ~ print('Respuesta: ' + resp)
	
	# ~ utils.Actions.screenshot()
	# ~ utils.Actions.VBS.setVolume(72)
	# ~ utils.Actions.startApp('Notepad')
	# ~ utils.Actions.startApp('Calc')
	
	# ~ procs = utils.SystemInfo.enumProcess('notepad')
	# ~ for p in procs: print(p)
	
	# ~ if len(procs) == 1:
		# ~ proc = procs.pop()
		# ~ resp = utils.Actions.killProcess(proc['pid'])
		# ~ print('Proceso Terminado: '+str(proc) if resp else 'Permiso Denegado: '+str(proc))
	
	# ~ print(utils.Actions.use)
	# ~ print(utils.Actions.Clipboard.use)
	# ~ print(utils.Actions.Explorer.use)
	# ~ print(utils.Actions.VBS.use)
	# ~ print(utils.Actions.VBS.getWindowsProductKey_use)
	# ~ print(utils.Actions.VBS.getWindowsProductKey_use)
	
	# ~ print(utils.Actions.cleanRecyclerBin_use)
	# ~ print(utils.Actions.displaySwitch_use)
	# ~ print(utils.Actions.messageBox_use)
	# ~ print(utils.Actions.startApp_use)

#=======================================================================






