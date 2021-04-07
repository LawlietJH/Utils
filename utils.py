
# Tested in: Python 3.8.8
# By: LawlietJH
# Utils v1.0.4

# Banner:
# ███    █▄      ███      ▄█   ▄█          ▄████████ 
# ███    ███ ▀█████████▄ ███  ███         ███    ███ 
# ███    ███    ▀███▀▀██ ███▌ ███         ███    █▀  
# ███    ███     ███   ▀ ███▌ ███         ███        
# ███    ███     ███     ███▌ ███       ▀███████████    ██    ██  ██     ██████     ██   ██
# ███    ███     ███     ███  ███                ███    ██    ██ ███    ██  ████    ██   ██
# ███    ███     ███     ███  ███▌    ▄    ▄█    ███    ██    ██  ██    ██ ██ ██    ███████
# ████████▀     ▄████▀   █▀   █████▄▄██  ▄████████▀      ██  ██   ██    ████  ██         ██
#                             ▀                           ████    ██ ██  ██████  ██      ██

from datetime import datetime
import pywintypes
import requests						# python -m pip install requests
import hashlib
import atexit
import psutil						# python -m pip install psutil
import socket
import string
import json
import math
import time
import mss							# python -m pip install mss
import sys
import re
import os

# Interfaz en Utils.Actions.Explorer ===================================
try:
	from Tkinter import Tk
	from Tkinter import filedialog
except:
	from tkinter import Tk
	from tkinter import filedialog

# Manipulacion de DLLs de Windows ======================================
import ctypes
#=======================================================================

# pip install pywin32 ==================================================
from win32com.shell import shell
import win32api			as WA
import win32con			as WC		# All Constants
import win32gui			as WG
import win32console		as WCS
import win32ui			as WU
import win32security	as WS
import win32clipboard	as WCB
import win32net			as WN
# ~ import win32com			as WCM
# ~ import win32process		as WP
#=======================================================================

__author__  = 'LawlietJH'	# Desarrollador
__title__   = 'Utils'		# Nombre
__version__ = 'v1.0.4'		# Version

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
		\r \
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
		\r \
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
		
		self.Actions     = self.Actions()
		self.MemoryInfo  = self.MemoryInfo()
		self.NetworkInfo = self.NetworkInfo()
		self.SystemInfo  = self.SystemInfo()
		self.Utilities   = self.Utilities()
	
	class Actions:		# Interacciones con el Systema (Mayormente Windows)
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.load_uses()
			self.run_command = lambda command: os.popen(command).read()	# Ejecuta cualquier comando en consola
			self.Clipboard = self.Clipboard()
			self.Explorer  = self.Explorer()
			self.VBS       = self.VBS()
		
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
		
		#---------------------------------------------------------------
		
		class Clipboard:												# Manipula el clipboard (Copiar/Pegar)
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
			
			# print(Clipboard.text)										# Pegar: Devuelve el contenido que se haya copiado.
			@property
			def text(self):
				WCB.OpenClipboard()
				text = WCB.GetClipboardData()
				WCB.CloseClipboard()
				return text
			
			# Clipboard.text = 'Texto'									# Copiar: Remplaza el contenido para poder Pegarlo.
			@text.setter
			def text(self, text):
				WCB.OpenClipboard()
				WCB.EmptyClipboard()
				WCB.SetClipboardText(text.encode(), WCB.CF_TEXT)
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
				\r \    
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
			
			def load_uses(self):
				self.getWindowsProductKey_use = '''
				\r Función: getWindowsProductKey(return_key=True, save_key=False, rm=True)
				\r |
				\r + Ejemplo de uso: 
				\r |
				\r |    # save_key=True Permite guardar la clave en un archivo
				\r |    key = utils.Actions.VBS.getWindowsProductKey(save_key=True)
				\r |    print('\nClave de Producto de Windows:', key)
				\r \
				'''
			
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
			
			def getWindowsProductKey(self, save_key=False, rm=True):	# Obtiene la Clave de Producto de Windows y la muestra en pantalla.
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
			
			def setVolume(self, percent=72, rm=True):
				percent = percent//2
				name = 'vol.vbs'
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
		
		def load_uses(self):
			self.cleanRecyclerBin_use = '''
			\r Función: cleanRecyclerBin(tipo=0, unidad='C:')
			\r |
			\r + Tipos de niveles:
			\r |  -------------------------------------------------------------
			\r | | 0 = NORMAL              | 4 = SIN_SONIDO                    |
			\r | | 1 = SIN_CONFIRMACION    | 5 = 4 + 1                         |
			\r | | 2 = SIN_BARRA_PROGRESO  | 6 = 4 + 2                         |
			\r | | 3 = 2 + 1               | 7 = 4 + 2 + 1 = TOTAL_INADVERTIDO |
			\r |  -------------------------------------------------------------
			\r |
			\r + Ejemplo de uso:
			\r |
			\r |    utils = Utils()
			\r |    # Vaciará la papelera en modo silencioso
			\r |    # Totalmente inadvertido.
			\r |    utils.Actions.cleanRecyclerBin(tipo=7)
			\r \
			'''
			self.displaySwitch_use = '''
			\r Función: displaySwitch(tipo=0)
			\r |
			\r + Tipos de cambios:
			\r |  --------------------------------------
			\r | | 0 = internal: Solo pantalla de PC.   |
			\r | | 1 = clone:    Duplicado.             |
			\r | | 2 = extend:   Ampliar.               |
			\r | | 3 = external: Solo segunda pantalla. |
			\r |  --------------------------------------
			\r |
			\r + Ejemplo de uso:
			\r |
			\r |    utils = Utils()
			\r |    utils.Actions.displaySwitch(2)
			\r \
			'''
			self.killProcess_use = '''
			\r Función: killProcess(PID)
			\r |
			\r + Ejemplo de uso:
			\r |
			\r |    utils = Utils()
			\r |
			\r |    # Busca todas las coincidencias con 'notepad':
			\r |    procs = utils.SystemInfo.enumProcess('notepad')
			\r |    for p in procs: print(p)
			\r |
			\r |    # Si solo hubo una coincidencia obtenemos
			\r |    # su ProcessID y terminamos el proceso:
			\r |    if len(procs) == 1:
			\r |        proc = procs.pop()
			\r |        utils.Actions.killProcess(proc['pid'])
			\r \
			'''
			self.messageBox_use = '''
			\r Función: messageBox(message, title,
			\r |	style = WC.MB_OKCANCEL | WC.MB_ICONINFORMATION | WC.MB_DEFAULT_DESKTOP_ONLY
			\r |    )
			\r |
			\r + Ejemplo de uso:
			\r |
			\r |    utils = Utils()
			\r |    resp = utils.Actions.messageBox(
			\r |        message = 'Esta función te resulta muy útil?',
			\r |        title = 'Es útil?',
			\r |        style = WC.MB_YESNO | WC.MB_ICONQUESTION | WC.MB_DEFAULT_DESKTOP_ONLY
			\r |    )
			\r |    print(resp)
			\r \
			'''
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
			self.startApp_use = '''
			\r Función: startApp(name='notepad')
			\r |
			\r + Ejemplo de uso:
			\r |
			\r |    utils = Utils()
			\r |    utils.Actions.startApp('Notepad')
			\r |    utils.Actions.startApp('Calc')
			\r |    utils.Actions.startApp('Cmd')
			\r \
			'''
		
		def beep(self, t=5, d=0.5):
			
			if t >= 1 and t <= 10:
				if d >= .1 and d <= 10: WA.Beep(int(t*100), int(d*1000))
				else: raise self.BeepError('\n\n\t Duración Seleccionada: {} segundos\n\n\t Rango Valido de Duración: 0.3 a 10 segundos'.format(d))
			else: raise self.BeepError('\n\n\t Tonalidad Seleccionada: {}\n\n\t Rango Valido de Tono: 3 a 10'.format(t))
		
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
		
		def hideConsole(xD=True):										# Oculta/Desoculta la consola de comandos
			WG.ShowWindow(WCS.GetConsoleWindow(), not xD)
		
		def hideCursor(visible=False):									# Oculta/Desoculta el cursor en pantalla.
			
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
		
		def messageBox(self, message, title, style = WC.MB_OKCANCEL | WC.MB_ICONINFORMATION | WC.MB_DEFAULT_DESKTOP_ONLY
		): #Use # Crea una ventana de alerta personalizada y captura la interacción con esta devolviendo la respuesta.
			
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
		
		def screenshot(self, open_ss=False): 
			
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
			\r \
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
				\r \
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
			\r \
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
		def isSlowMachine(self):										# Es 1 si la computadora tiene un procesador de gama baja (lento)
			val = WA.GetSystemMetrics(WC.SM_SLOWMACHINE)				# SM_SLOWMACHINE = 73
			return val == 1
		
		@property
		def isUserAnAdmin(self):										# Devuelve True si el programa tiene permisos de administrador o False si no.
			return shell.IsUserAnAdmin()
		
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
				\r \
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
			
			def update(self, type_hash):	# Permite cambiar el hash a otro typo
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
		
		def load_uses(self):	# Función que carga todos los 'use'.
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
			\r \
			'''
		
		def hash(self, text, algo='sha1'): #Use						# Devuelve el Hash del texto con el algoritmo seleccionado.
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

#=======================================================================
#=======================================================================
#=======================================================================



# Ejecuta esto despues de terminar la ejecución del programa.
@atexit.register
def close():
	time.sleep(1)

#=======================================================================

if __name__ == '__main__':
	
	# Pruebas:
	
	utils = Utils()
	
	print('\n\n Ascii Font functions availables: ' + utils.Utilities.AsciiFont.functions.list)
	
	text = 'v1.0.4'
	
	# ~ cal = utils.Utilities.AsciiFont.calvinS(text)
	# ~ sha = utils.Utilities.AsciiFont.ansiShadow(text)
	reg = utils.Utilities.AsciiFont.ansiRegular(text)
	# ~ dcp = utils.Utilities.AsciiFont.deltaCorpsPriest(text)
	# ~ blo = utils.Utilities.AsciiFont.block(text)
	# ~ alg = utils.Utilities.AsciiFont.alligator(text)
	# ~ cyb = utils.Utilities.AsciiFont.cybermedium(text)
	# ~ dsh = utils.Utilities.AsciiFont.dobleShorts(text)
	# ~ dob = utils.Utilities.AsciiFont.doble(text)
	# ~ ram = utils.Utilities.AsciiFont.rammstein(text)
	
	# ~ print('calvinS:\n'          + cal)
	# ~ print('ansiShadow:\n'       + sha)
	print('ansiRegular:\n'      + reg)
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
		# ~ style = WC.MB_YESNO | WC.MB_ICONQUESTION | WC.MB_DEFAULT_DESKTOP_ONLY
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
	
	# ~ print(utils.Actions.cleanRecyclerBin_use)
	# ~ print(utils.Actions.displaySwitch_use)
	# ~ print(utils.Actions.messageBox_use)
	# ~ print(utils.Actions.startApp_use)

#=======================================================================






