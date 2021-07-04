
# Tested in: Python 3.8.8 - Windows
# By: LawlietJH
# Utils v1.0.6

# Banner:
# ███    █▄      ███      ▄█   ▄█          ▄████████ 
# ███    ███ ▀█████████▄ ███  ███         ███    ███ 
# ███    ███    ▀███▀▀██ ███▌ ███         ███    █▀  
# ███    ███     ███   ▀ ███▌ ███         ███        
# ███    ███     ███     ███▌ ███       ▀███████████    ██    ██  ██     ██████      ██████
# ███    ███     ███     ███  ███                ███    ██    ██ ███    ██  ████    ██
# ███    ███     ███     ███  ███▌    ▄    ▄█    ███    ██    ██  ██    ██ ██ ██    ███████
# ████████▀     ▄████▀   █▀   █████▄▄██  ▄████████▀      ██  ██   ██    ████  ██    ██    ██
#                             ▀                           ████    ██ ██  ██████  ██  ██████

from datetime import datetime
import pywintypes
import binascii
import requests						# python -m pip install requests
import hashlib
import atexit
import psutil						# python -m pip install psutil
import socket
import string
import json
import math
import time
import bz2
import mss							# python -m pip install mss
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
#=======================================================================

# pip install pywin32 ==================================================
from win32com.shell import shell, shellcon
import win32api			as WA
import win32con			as WC		# All Constants
import win32gui			as WG
import win32console		as WCS
import win32ui			as WU
import win32security	as WS
import win32clipboard	as WCB
import win32net			as WN
import winreg			as WR
# ~ import win32com			as WCM
# ~ import win32process		as WP
#=======================================================================
#=======================================================================
#=======================================================================
__author__  = 'LawlietJH'	# Desarrollador
__title__   = 'Utils'		# Nombre
__version__ = 'v1.0.6'		# Version
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
			self.VBS       = self.VBS()
			
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
			
			def setVolume(self, percent=72, rm=True): # use				# Permite ajustar el volumen del sistema.
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
			print(cmd)
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
					print(os.path.isfile(scree_new_name))
					data += 1
					scree_new_name = 'Screenshots\\Screenshot_{}.jpg'.format(str(data).zfill(3))
				os.rename(screen_name, scree_new_name)
			else:
				pass
		
		def setConsoleSize(self, chars=82, lines=55):					# Cambia el tamaño de la consola de comandos por cantidad de caracteres por ancho y cantidad de lineas por alto
			os.system("mode con: cols={} lines={}".format(chars, lines))
		
		def setCursorPos(self, posX, posY):								# Posiciona el cursor en (X, Y)
			WA.SetCursorPos((posX, posY))
		
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
		# Requiere Permisos de Administrador
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			# Clases Internas:
			self.ContextMenu = self.ContextMenu()
			self.DropBox = self.DropBox()
			self.FoldersOnThisPC = self.FoldersOnThisPC()
			self.OneDrive = self.OneDrive()
			self.PowerPlan = self.PowerPlan()
			self.TaskManager = self.TaskManager()
		
		class ContextMenu:
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY = WR.HKEY_CURRENT_USER
				self.PATH = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer'
				self.KEY  = 'NoViewContextMenu'
				self.HIDE = 0x00000001
				self.SHOW = 0x00000000
				
				self.use = '''
				\r Clase: ContextMenu
				\r |
				\r + Ejemplo de uso: Requieren Permisos de administrador.
				\r |    
				\r |    utils = Utils()
				\r |    
				\r |    # Para deshabilitar el uso de el Menu Contextual (dar clic derecho):
				\r |    utils.EditRegistry.ContextMenu.disable()
				\r |    
				\r |    # Para habilitar el uso de el Menu Contextual (dar clic derecho):
				\r |    utils.EditRegistry.ContextMenu.enable()
				\r |    
				\r |    # Para eliminar los cambios realizados en el registro:
				\r |    utils.EditRegistry.ContextMenu.cleanUp()
				\r \\
				'''
			
			def _keyExists(self):
				try:
					reg = WR.OpenKeyEx(self.HKEY, self.PATH)
					value = WR.QueryValueEx(reg, self.KEY)[0]
					WR.CloseKey(reg)
					return True, value
				except:
					return False, None
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
			# "NoViewContextMenu"=dword:00000000
			def enable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo habilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.SHOW)
					WR.CloseKey(reg)
				elif key_exists and isDisabled:													# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.SHOW)
					WR.CloseKey(reg)
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer]
			# "NoViewContextMenu"=dword:00000001
			def disable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.HIDE)
					WR.CloseKey(reg)
				elif key_exists and not isDisabled:												# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.HIDE)
					WR.CloseKey(reg)
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
			# "DisableTaskMgr"=-
			def cleanUp(self):
				key_exists, isDisabled = self._keyExists()
				if key_exists:
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.DeleteValue(reg, self.KEY)
					WR.CloseKey(reg)
		
		class DropBox:
			# DropBox: {E31EA727-12ED-4702-820C-4B6445F28E1A}
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY  = WR.HKEY_CLASSES_ROOT
				self.PATH  = r'CLSID\{E31EA727-12ED-4702-820C-4B6445F28E1A}'
				self.KEY   = 'System.IsPinnedToNameSpaceTree'
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
					value = WR.QueryValueEx(reg, self.KEY)[0]
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
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
				elif key_exists and not isDisabled:												# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
			
			# [HKEY_CLASSES_ROOT\CLSID\{E31EA727-12ED-4702-820C-4B6445F28E1A}]
			# "System.IsPinnedToNameSpaceTree"=dword:00000000
			def disable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
				elif key_exists and isDisabled:													# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
		
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
					elif keyExists and value == 'Show':												# Si existe el key y esta deshabilitado, lo habilita.
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
					elif keyExists and value == 'Hide':												# Si existe el key y esta deshabilitado, lo habilita.
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
			# DropBox: {E31EA727-12ED-4702-820C-4B6445F28E1A}
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.HKEY  = WR.HKEY_CLASSES_ROOT
				self.PATH  = r'CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}'
				self.KEY   = 'System.IsPinnedToNameSpaceTree'
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
					value = WR.QueryValueEx(reg, self.KEY)[0]
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
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
				elif key_exists and not isDisabled:												# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
			
			# [HKEY_CLASSES_ROOT\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}]
			# "System.IsPinnedToNameSpaceTree"=dword:00000000
			def disable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
				elif key_exists and isDisabled:													# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
		
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
				self.KEY   = 'DisableTaskMgr'
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
					value = WR.QueryValueEx(reg, self.KEY)[0]
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
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
				elif key_exists and isDisabled:													# Si existe el key y esta deshabilitado, lo habilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.FALSE)
					WR.CloseKey(reg)
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
			# "DisableTaskMgr"=dword:00000001
			def disable(self):
				key_exists, isDisabled = self._keyExists()										# Intenta abrir el key y extraer su valor.
				if not key_exists:																# Si no existe el key, lo crea y lo deshabilita.
					reg = WR.CreateKey(self.HKEY, self.PATH)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
				elif key_exists and not isDisabled:												# Si existe el key y esta habilitado, lo deshabilita.
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.SetValueEx(reg, self.KEY, 0,  WR.REG_DWORD, self.TRUE)
					WR.CloseKey(reg)
			
			# [HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
			# "DisableTaskMgr"=-
			def cleanUp(self):
				key_exists, isDisabled = self._keyExists()
				if key_exists:
					reg = WR.OpenKey(self.HKEY, self.PATH, 0, WR.KEY_SET_VALUE)
					WR.DeleteValue(reg, self.KEY)
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
			\r Funciones: ESSIDEnum() y ESSIDPasswd(ESSID)
			\r |
			\r + Ejemplos de uso:
			\r |
			\r |    utils = Utils()
			\r |
			\r |    for ESSID in utils.NetworkInfo.ESSIDEnum():
			\r |        pwd = utils.NetworkInfo.ESSIDPasswd(ESSID)
			\r |        print('\\nESSID: ' + ESSID + '\\n  Pwd: ' + pwd)
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
	
	class SystemInfo:	# Información general sobre la PC
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.load_uses()
			
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
		def displaySettings(self):										# Devuelve la resolucion de pantalla y los bits de pixeles (normalmente 32 bits)
			'''return x_resolution, y_resolution, colour_depth'''
			xScreen = WA.GetSystemMetrics(WC.SM_CXSCREEN)	# SM_CXSCREEN = 0
			yScreen = WA.GetSystemMetrics(WC.SM_CYSCREEN)	# SM_CYSCREEN = 1
			bPixels = WU.GetDeviceCaps(WG.GetDC(0), WC.BITSPIXEL)
			return [xScreen, yScreen, bPixels]
		
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
			self.UBZ2 = self.UBZ2()
		
		class AsciiFont:	# Clase que permite convertir un texto a un tipo de ASCII FONT
			
			class NotSupportedError(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			class TypeError(Exception):
				def __init__(self, error_msg): self.error_msg = error_msg
				def __str__(self): return repr(self.error_msg)
			
			def __init__(self):
				
				self.functions = ObjectFunctionNames(self)
				self.classes   = ObjectClassNames(self)
				
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
		
		class UBZ2:			# Algoritmo de compresión y descompresión de archivos bz2. El nombre se refiere a Utils BZ2.
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				# Icono de Navi de Zelda en Pixel Art (de mi autoria). Esta en bz2.
				self.iconFile = b''
				
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
		
		def getLastError(self) -> int:									# DWORD WINAPI GetLastError(void);
			DWORD = ctypes.c_uint32
			_GetLastError = ctypes.windll.kernel32.GetLastError
			_GetLastError.argtypes = []
			_GetLastError.restype = DWORD
			return _GetLastError()
		
		def writeHiddenText(self, text_to_print):						# Muestra el text_to_print en pantalla y pide capturar texto, el texto capturado no se mostraá pero será devuelto por la función.
			'''
				passwd = utils.Utilities.writeHiddenText('Password: ')
				print(f'La contraseña escrita fue: {passwd}')
			'''
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
    ║   ╠══ Class VBS
    ║   │    │
    ║   │    │ - Functions: ──────────────────
    ║   │    ├── function ejectCDROM
    ║   │    ├── function getWindowsProductKey
    ║   │    ├── function minimizeAll
    ║   │    ├── function runScriptVBS
    ║   │    └── function setVolume
    ║   │
    ║   │ - Functions: ───────────────────────
    ║   ├── function beep
    ║   ├── function changePasswordCurrentUser
    ║   ├── function cleanRecyclerBin
    ║   ├── function displaySwitch
    ║   ├── function exitWindows
    ║   ├── function getPrivileges
    ║   ├── function getProcessPrivileges
    ║   ├── function hideConsole
    ║   ├── function hideCursor
    ║   ├── function killProcess
    ║   ├── function lockWorkStation
    ║   ├── function messageBox
    ║   ├── function minimizeWindowCMD
    ║   ├── function screenshot
    ║   ├── function setCursorPos
    ║   ├── function setTopWindow
    ║   ├── function setPriorityPID
    ║   └── function startApp
    ║
    ╠═ EditRegistry
    ║   ║
    ║   ║ - Classes: ─────────────────────────
    ║   ╠══ Class ContextMenu
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function enable
    ║   ║    ├── function disable
    ║   ║    └── function cleanUp
    ║   ║
    ║   ╠══ Class DropBox
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function enable
    ║   ║    └── function disable
    ║   ║
    ║   ╠══ Class FoldersOnThisPC
    ║   ║    ║
    ║   ║    ║ - Classes: ────────────────────
    ║   ║    ╠══ Class Folder3DObjects
    ║   ║    ║    │
    ║   ║    ║    │ - Functions: ─────────────
    ║   ║    ║    ├── function show
    ║   ║    ║    └── function hide
    ║   ║    ║
    ║   ║    ╠══ Class FolderDesktop
    ║   ║    ║    │
    ║   ║    ║    │ - Functions: ─────────────
    ║   ║    ║    ├── function show
    ║   ║    ║    └── function hide
    ║   ║    ║
    ║   ║    ╠══ Class FolderDocuments
    ║   ║    ║    │
    ║   ║    ║    │ - Functions: ─────────────
    ║   ║    ║    ├── function show
    ║   ║    ║    └── function hide
    ║   ║    ║
    ║   ║    ╠══ Class FolderDownloads
    ║   ║    ║    │
    ║   ║    ║    │ - Functions: ─────────────
    ║   ║    ║    ├── function show
    ║   ║    ║    └── function hide
    ║   ║    ║
    ║   ║    ╠══ Class FolderMusic
    ║   ║    ║    │
    ║   ║    ║    │ - Functions: ─────────────
    ║   ║    ║    ├── function show
    ║   ║    ║    └── function hide
    ║   ║    ║
    ║   ║    ╠══ Class FolderPictures
    ║   ║    ║    │
    ║   ║    ║    │ - Functions: ─────────────
    ║   ║    ║    ├── function show
    ║   ║    ║    └── function hide
    ║   ║    ║
    ║   ║    ╚══ Class FolderVideos
    ║   ║         │
    ║   ║         │ - Functions: ─────────────
    ║   ║         ├── function show
    ║   ║         └── function hide
    ║   ║
    ║   ╠══ Class OneDrive
    ║   ║    │
    ║   ║    │ - Functions: ──────────────────
    ║   ║    ├── function enable
    ║   ║    └── function disable
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
    ║   │
    ║   │ - Functions: ───────────────────────
    ║   ├── function latin1_encoding
    ║   ├── function ESSIDEnum
    ║   └── function ESSIDPasswd
    ║
    ╠═ Class SystemInfo
    ║   │
    ║   │ - Functions: ───────────────────────
    ║   ├── function enumComputerSystemInfo
    ║   ├── function enumLocalDisk
    ║   ├── function enumLocalUsersAndGroups
    ║   ├── function enumProcess
    ║   ├── function isCapsLockActive
    ║   ├── function isLinux
    ║   ├── function isMouseInstalled
    ║   ├── function isPythonV2
    ║   ├── function isPythonV3
    ║   ├── function isSlowMachine
    ║   ├── function isUserAnAdmin
    ║   ├── function isUserPasswordValid
    ║   ├── function isWindows
    ║   ├── function currentProcessId
    ║   ├── function cursorPos
    ║   ├── function displaySettings
    ║   ├── function computerName
    ║   ├── function homeDrive
    ║   ├── function numberOfMonitors
    ║   ├── function numberOfProcessors
    ║   ├── function os
    ║   ├── function processorArchitecture
    ║   ├── function processorIdentifier
    ║   ├── function screenSize
    ║   ├── function systemDrive
    ║   ├── function systemRoot
    ║   ├── function systemUptime
    ║   ├── function userName
    ║   ├── function winDir
    ║   └── function collectAll
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
        ╠══ Class UBZ2
        ║    ║
        ║    ║ - Error Classes: ──────────────
        ║    ╠══ Class NotSupportedError
        ║    ╠══ Class TypeError
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function addIconToFileExtension
        ║    ├── function generateIcon
        ║    ├── function compress
        ║    ├── function decompress
        ║    └── function getDataFromUBZ2File
        ║
        ╠══ Class Hash
        │
        │ - Functions: ───────────────────────
        ├── function hash
        ├── function getLastError
        ├── function writeHiddenText
        └── function flushBuffer

 All Classes Have a 'use', 'classes' and 'functions' variables.

'''.format(__version__)



# Ejecuta esto despues de terminar la ejecución del programa.
@atexit.register
def close():
	time.sleep(.1)

#=======================================================================

if __name__ == '__main__':
	
	# Pruebas:
	
	# ~ print(struct)
	
	utils = Utils()
	# ~ reg = utils.Utilities.AsciiFont.ansiRegular(__version__)
	# ~ print('ansiShadow:\n' + reg)
	
	print(utils.Utilities.UBZ2.use)
	
	# ~ utils.Utilities.UBZ2.addIconToFileExtension()
	
	# ~ fileName = utils.Actions.Explorer.getFileName(topmost=False)
	# ~ if fileName:
		# ~ utils.Utilities.UBZ2.compress(fileName)
		# ~ utils.Utilities.UBZ2.decompress(fileName)
		# ~ print(utils.Utilities.UBZ2.getDataFromUBZ2File(fileName))
	
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
	
	# ~ text = 'By LawlietJH'
	
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






