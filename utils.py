
# Tested in: Python 3.8.8
# By: LawlietJH
# Utils v1.0.1

from datetime import datetime
import pywintypes
import requests						# python -m pip install requests
import hashlib
import atexit
import psutil						# python -m pip install psutil
import socket
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
import win32con			as WC
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
__version__ = 'v1.0.1'		# Version

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

class ObjectClassNames:    # Obtiene todos los nombres de las clases en los objetos de 'Utils' y la cantidad.    Detecta Clases con Formato de primer letra Mayúscula. Ejemplo: 'PrimeroSegundoTercero'
	
	def __init__(self, obj):
		self.use = '''
		\r Ejemplo de uso:
		\r	utils = Utils()
		
		\r	# utils.classes --> str: <'list':[...], 'qty':0>
		\r	print(utils.classes)
		
		\r	# utils.classes.list + list--> list
		\r	# utils.classes.list --> list
		\r	print('Classes list:', utils.classes.list)
		
		\r	# utils.classes.qty + int --> int
		\r	# utils.classes.qty --> int
		\r	print('Classes qty:', utils.classes.qty)
		
		\r	# Al sumar con string se convierte en string, sino, seguira siendo una lista.
		\r	# utils.classes.list + str --> str
		\r	print('Classes str(list): ' + utils.classes.list)
		
		\r	# Al sumar con string se convierte en string, sino, seguira siendo un entero.
		\r	# utils.classes.qty + str --> str
		\r	print('Classes str(qty): ' + utils.classes.qty)
		'''
		list_ = [
			a for a in dir(obj) 
			if a[0] == a[0].upper()
			and not a[0] == '_'
			and not a.startswith('not_')
		]
		self.list = ObjectList(list_)
		self.qty  = ObjectInt(len(list_))
	
	def __str__(self):
		output = '<{}: '+str(self.list) + ', {}: '+str(self.qty) + '>'
		return output.format(repr('list'), repr('qty'))

class ObjectFunctionNames: # Obtiene todos los nombres de las funciones en los objetos de 'Utils' y la cantidad. Detecta funciones con Formato de primer letra minúscula. Ejemplo: 'primeroSegundoTercero'
	
	def __init__(self, obj):
		self.use = '''
		\r Ejemplos de uso:
		
		\r	utils = Utils()
		
		\r	# utils.functions --> str: <'list':[...], 'qty':0>
		\r	print(utils.functions)
		
		\r	# utils.functions.list + list --> list
		\r	# utils.functions.list --> list
		\r	print('Functions list:', utils.functions.list)
		
		\r	# utils.functions.qty + int --> int
		\r	# utils.functions.qty --> int
		\r	print('Functions qty:', utils.functions.qty)
		
		\r	# Al sumar con string se convierte en string, sino, seguira siendo una lista.
		\r	# utils.functions.list + str --> str
		\r	print('Functions str(list): ' + utils.functions.list)
		
		\r	# Al sumar con string se convierte en string, sino, seguira siendo un entero.
		\r	# utils.functions.qty + str --> str
		\r	print('Functions str(qty): ' + utils.functions.qty)
		'''
		list_ = [
			a for a in dir(obj) 
			if  not a[0] == a[0].upper()
			and not a[0] == '_'
			and not a.startswith('not_')
		]
		self.list = ObjectList(list_)
		self.qty  = ObjectInt(len(list_))
	
	def __str__(self):
		output = '<{}: '+str(self.list) + ', {}: '+str(self.qty) + '>'
		return output.format(repr('list'), repr('qty'))

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
	
	class Actions:	# Interacciones con el Systema (Mayormente Windows)
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
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
		
		class Explorer:													# Permite controlar las ventanas 'Abrir', 'Seleccionar carpeta' y 'Guardar como' para obtener las rutas seleccionadas.
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.use = '''\
					\r Ejemplo de Uso:
					
					\r	utils = Utils()
					
					\r	# Obtiene la ruta completa y el nombre del archivo para 'Abrir':
					\r	file_name = utils.Actions.Explorer.getFileName()
					\r	print(file_name)
					
					\r	# Obtiene la ruta completa de la Carpeta Seleccionada para 'Seleccionar Carpeta':
					\r	folder_path = utils.Actions.Explorer.getFolderName()
					\r	print(folder_path)
					
					\r	# Obtiene la ruta completa y el nombre de Archivo indicado para 'Guardar como':
					\r	file_name_save = utils.Actions.Explorer.getFileNameSave()
					\r	print(file_name_save)
				'''
				self.root = Tk()
				self.root.withdraw()
			
			def __str__(self): return self.use
			
			def getFileName(self, title='Abrir', file_types=[ 
						['Archivos de Texto','.txt'], ['Todos los Archivos','.*']
					], init_dir=os.getcwd(), encima=True):
				
				if encima == True:
					self.root.wm_attributes('-topmost', True)
				else:
					self.root.wm_attributes('-topmost', False)
				
				f_name = filedialog.askopenfile(title = title,
												initialdir = init_dir,
												filetypes = file_types)
				if not f_name == None:
					return f_name.name
			
			def getFolderName(self, title='Seleccionar Carpeta', init_dir=os.getcwd(), encima=True):
				
				if encima == True:
					self.root.wm_attributes('-topmost', True)
				else:
					self.root.wm_attributes('-topmost', False)
				
				d_path = filedialog.askdirectory(title = title, initialdir = init_dir)
				
				if not d_path == '':
					return d_path
			
			def getFileNameSave(self, title='Guardar como', file_types=[
							['Archivos de Texto','.txt'], ['Todos los Archivos','.*']
						], init_dir=os.getcwd(), encima=True):
				
				if encima == True:
					self.root.wm_attributes('-topmost', True)
				else:
					self.root.wm_attributes('-topmost', False)
				
				f_name = filedialog.asksaveasfilename(title = title,
													  initialdir = init_dir,
													  filetypes = file_types)
				if not f_name == '':
					return f_name
		
		class VBS:														# Ejecuta Scripts VBS
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.run_command = lambda command: os.popen(command).read()	# Ejecuta cualquier comando en consola
			
			def runScriptVBS(self, name, payload, rm):						# Ejecuta el script VBS
				
				temp_path = os.getenv('TEMP') + '\\_odin_\\'				# Obtiene la ruta de la carpeta de archivos temporales en windows
				name = temp_path + name										# Indica la ruta y nombre del archivo
				
				if not os.path.isdir(temp_path):							# Crea la carpeta _odin_ en los archivos temporales si no existe
					os.mkdir(temp_path)
				
				if not os.path.isfile(name):								# Crea el archivo si no existe en la carpeta %temp%\_odin_
					with open(name,'w') as File:
						File.write(payload)									# Añade el código dentro del archivo
						File.close()
				
				self.run_command('cscript ' + name)							# Ejecuta el código del script
				
				if rm: os.remove(name)										# Elimina el archivo min.vbs
				
				if len(os.listdir(temp_path)) == 0:							# Elimina la carpeta _odin_ si esta vacia 
					os.rmdir(temp_path)
			
			def minimizeAll(self, rm=True):									# Minimiza todas las ventanas
				name = 'minimizeAll.vbs'									# Indica el nombre del archivo
				payload = '''\
					\r ' VBS Script para Minimizar todas las ventanas.
					\r Set var = CreateObject("Shell.Application")
					\r var.MinimizeAll
				'''
				self.runScriptVBS(name, payload, rm)
			
			def ejectCDROM(self, rm=True):									# Expulsa la bandeja de disco.
				name = 'ejectCDROM.vbs'										# Indica el nombre del archivo
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
		
		def beep(self, t=5, d=0.5):
			
			if t >= 1 and t <= 10:
				if d >= .1 and d <= 10: WA.Beep(int(t*100), int(d*1000))
				else: raise self.BeepError('\n\n\t Duración Seleccionada: {} segundos\n\n\t Rango Valido de Duración: 0.3 a 10 segundos'.format(d))
			else: raise self.BeepError('\n\n\t Tonalidad Seleccionada: {}\n\n\t Rango Valido de Tono: 3 a 10'.format(t))
		
		def changePasswordCurrentUser(self, oldPwd, newPwd):			# Cambia la contraseña del usuario actual.
			WN.NetUserChangePassword(None, None, oldPwd, newPwd)
		
		def cleanRecyclerBin(self, tipo=0, unidad='C:'):				# int tipo, str unidad. Permite vaciar la papelera de reciclaje, incluso de forma completamente silenciosa
			''' Tipos:
			 -------------------------------------------------------------
			| 0 = NORMAL			  | 4 = SIN_SONIDO					  |
			| 1 = SIN_CONFIRMACION	  | 5 = 4 + 1						  |
			| 2 = SIN_BARRA_PROGRESO  | 6 = 4 + 2						  |
			| 3 = 2 + 1				  | 7 = 4 + 2 + 1 = TOTAL_INADVERTIDO |
			 -------------------------------------------------------------
			'''
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
		
		def displaySwitch(self, tipo=0):								# Cambia la pantalla Solo Primera, Pantalla Duplicada, Extendida o Solo Segunda.
			'''
			0 = internal: Solo pantalla de PC.
			1 = clone:    Duplicado.
			2 = extend:   Ampliar.
			3 = external: Solo segunda pantalla.
			'''
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
		
		def lockWorkStation(self):
			#~ run_command('rundll32.exe user32.dll, LockWorkStation')
			ctypes.windll.user32.LockWorkStation()
		
		def minimizeWindowCMD(self):									# Minimiza la consola de comandos
			WG.ShowWindow(WG.GetForegroundWindow(), WC.SW_MINIMIZE)
		
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
	
	class MemoryInfo:
		
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
	
	class NetworkInfo:
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.use = '''\
			\r Ejemplo de uso:
			
			\r	utils = Utils()
			
			\r	for ESSID in utils.NetworkInfo.ESSIDEnum():
			\r	    pwd = utils.NetworkInfo.ESSIDPasswd(ESSID)
			\r	    print('\\nESSID: ' + ESSID + '\\n  Pwd: ' + pwd)
			'''
			
			self.run_command = lambda command: os.popen(command).read()	# Ejecuta cualquier comando en consola
			self.GetIP = self.GetIP()
		
		def __str__(self): return self.use
		
		class GetIP:
			
			def __init__(self):
				
				self.classes   = ObjectClassNames(self)
				self.functions = None
				self.functions = ObjectFunctionNames(self)
				
				self.use = '''
				\r Ejemplos de uso:
				
				\r	utils = Utils()
				
				\r	# Sirve en el caso de no necesitar las IP públicas.
				\r	# Evita conectarse a la API de ipify.
				\r	# Default: utils.GetIP.only_local = True
				
				\r	print('\\nDatos Locales:\\n')
				\r	print(' HOST:', utils.GetIP.hostname)
				\r	print(' IPv4 Privada:', utils.GetIP.local_ipv4)
				\r	print(' IPv6 Privada:', utils.GetIP.local_ipv6)
				\r	print(' IPv4 Publica:', utils.GetIP.public_ipv4)
				\r	print(' IPv6 Publica:', utils.GetIP.public_ipv6)
				
				\r	# Conecta a la API de ipify para obtener las IP públicas.
				\r	utils.GetIP.only_local = False
				
				\r	print('\\nDatos Locales y Públicos:\\n')
				\r	print(' HOST:', utils.GetIP.hostname)
				\r	print(' IPv4 Privada:', utils.GetIP.local_ipv4)
				\r	print(' IPv6 Privada:', utils.GetIP.local_ipv6)
				\r	print(' IPv4 Publica:', utils.GetIP.public_ipv4)
				\r	print(' IPv6 Publica:', utils.GetIP.public_ipv6)
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
		
		def latin1_encoding(self, res):
			
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
		
		def ESSIDEnum(self):
			
			output = self.run_command('netsh wlan show profiles')
			output = self.latin1_encoding(output).split('\n')
			
			ESSIDs = [
				o.split(': ')[1]
				if ': ' in o else None
				for o in output
			]
			
			while None in ESSIDs: ESSIDs.remove(None)
			
			return ESSIDs
		
		def ESSIDPasswd(self, ESSID):
			
			output = self.run_command('netsh wlan show profile name="{}" key=clear'.format(ESSID))
			output = self.latin1_encoding(output).split('\n')
			
			Passwd = None
			
			for o in output:
				if 'Contenido de la clave  : ' in o:
					Passwd = o.split(': ')[1]
					break
			
			return Passwd
	
	class SystemInfo:
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.run_command = lambda command: os.popen(command).read()	# Ejecuta cualquier comando en consola
		
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
		
		@property
		def isCapsLockActive(self):										# Devuelve True si el Bloq Mayús está activado o False si no.
			return False if WA.GetKeyState(WC.VK_CAPITAL) == 0 else True
		
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
		
		@property
		def isSlowMachine(self):										# Es 1 si la computadora tiene un procesador de gama baja (lento)
			val = WA.GetSystemMetrics(WC.SM_SLOWMACHINE)				# SM_SLOWMACHINE = 73
			return val == 1
		
		@property
		def isUserAnAdmin(self):										# Devuelve True si el programa tiene permisos de administrador o False si no.
			return shell.IsUserAnAdmin()
		
		def getComputerName(self):										# Devuelve el nombre de la Computadora
			return WA.GetComputerName()
		
		def getCurrentProcess(self):									# Devuelve el ID del proceso actual
			return WA.GetCurrentProcessId()
		
		def getCursorPos(self):
			return WA.GetCursorPos()
		
		def getDisplaySettings(self):
			'''return x_resolution, y_resolution, colour_depth'''
			xScreen = WA.GetSystemMetrics(WC.SM_CXSCREEN)	# SM_CXSCREEN = 0
			yScreen = WA.GetSystemMetrics(WC.SM_CYSCREEN)	# SM_CYSCREEN = 1
			bPixels = WU.GetDeviceCaps(WG.GetDC(0), WC.BITSPIXEL)
			return [xScreen, yScreen, bPixels]
		
		def getNumberOfProcessors(self):
			return WA.GetNativeSystemInfo()[5]
		
		def getNumberOfMonitors(self):
			return WA.GetSystemMetrics(WC.SM_CMONITORS)	# SM_CMONITORS = 80
		
		@property
		def screenSize(self):											# Devuelve la resolución actual de la pantalla en forma de tupla (X, Y)
			user32 = ctypes.windll.user32
			screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
			return screenSize
		
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
	
	class Utilities:
		
		def __init__(self):
			
			self.classes   = ObjectClassNames(self)
			self.functions = None
			self.functions = ObjectFunctionNames(self)
			
			self.use_hash = '''
			\r Ejemplo de uso:
			
			\r	utils = Utils()
			
			\r	# Available: sha1 (Default), sha224, sha256, sha384, sha512, md5.
			
			\r	h = utils.Utilities.hash('hello world!', 'sha256')
			\r	print('Hash: ' + h)
			\r	print('Type: ' + h.type)
			\r	print('Text: ' + h.text)
			
			\r	h.update('sha1')
			\r	print('\\nActualizado a sha1:')
			\r	print('Hash: ' + h)
			\r	print('Type: ' + h.type)
			\r	print('Text: ' + h.text)
			'''
		
		class Hash:
			
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
		
		def hash(self, text, algo='sha1'):								# Devuelve un Hash.
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
	time.sleep(3)

#=======================================================================

if __name__ == '__main__':
	
	# Pruebas:
	
	utils = Utils()
	
	print(utils.Utilities.use_hash)
	
	# Available: sha1 (Default), sha224, sha256, sha384, sha512, md5.
	
	h = utils.Utilities.hash('hello world!', 'sha256')
	print('Hash: ' + h)
	print('Type: ' + h.type)
	print('Text: ' + h.text)
	
	h.update('sha1')
	print('\nActualizado a sha1:')
	print('Hash: ' + h)
	print('Type: ' + h.type)
	print('Text: ' + h.text)

#=======================================================================






