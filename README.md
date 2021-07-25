# Utilidades
 Un módulo recopilatorio con decenas de funciones que he hecho a lo largo del tiempo, utilidades de todo tipo, desde usar funciones simples como hash o comprimir archivos de texto plano con hasta 99% de compresión en algunos casos, editar los registros de windows para personalizar el sistema o manejar la API de windows para manipular el mouse, la pantalla, vaciar la papelera de forma silenciosa y mucho más...
```
 ███    █▄      ███      ▄█   ▄█          ▄████████ 
 ███    ███ ▀█████████▄ ███  ███         ███    ███ 
 ███    ███    ▀███▀▀██ ███▌ ███         ███    █▀  
 ███    ███     ███   ▀ ███▌ ███         ███        
 ███    ███     ███     ███▌ ███       ▀███████████    ██    ██  ██     ██████     ███████
 ███    ███     ███     ███  ███                ███    ██    ██ ███    ██  ████         ██
 ███    ███     ███     ███  ███▌    ▄    ▄█    ███    ██    ██  ██    ██ ██ ██        ██
 ████████▀     ▄████▀   █▀   █████▄▄██  ▄████████▀      ██  ██   ██    ████  ██       ██
                             ▀                           ████    ██ ██  ██████  ██    ██
```
## Tested in: Python 3.8.8
## By: LawlietJH
## Utils v1.0.7

![Icon](ubz2file.ico "Icono de archivos ubz2")

```
■■■ Class Utils (v1.0.7)
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
    ║   ╠══ Class Mouse
    ║   ║
    ║   ╠══ Class Keyboard
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
    ║   ├── function getWindowRect
    ║   ├── function hideConsole
    ║   ├── function hideCursor
    ║   ├── function killProcess
    ║   ├── function lockWorkStation
    ║   ├── function messageBox
    ║   ├── function minimizeWindowCMD
    ║   ├── function screenshot
    ║   ├── function setCursorPos
    ║   ├── function setTopMostWindow
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
    ║   ║    ╠══ Class PropertiesRecycleBin
    ║   ║    ╚══ Class Close
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
    ║   ├── function currentSystemMetrics
    ║   ├── function realSystemMetrics
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
    ║   ├── function userDowntime
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
        ║    ║
        ║    ║ - Error Classes: ──────────────
        ║    ╠══ Class MonthDoesNotExist
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
```
