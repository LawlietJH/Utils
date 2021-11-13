# Utilidades
 Un módulo recopilatorio con decenas de funciones que he hecho a lo largo del tiempo, utilidades de todo tipo, desde usar funciones simples como hash o comprimir archivos de texto plano con hasta 99% de compresión en algunos casos, editar los registros de Windows para personalizar el sistema o manejar la API de Windows para manipular el mouse, la pantalla, el teclado, vaciar la papelera de forma silenciosa o esconderle archivos dentro y que sean imborrables, obtener información de dispositivos bluetooth previamente vinculados o de conexiones wi-fi y mucho, mucho más...
```
███    █▄      ███      ▄█   ▄█          ▄████████    
███    ███ ▀█████████▄ ███  ███         ███    ███    █▄▄ █▄█ ▀   █   ▄▀█ █ █ █ █   █ █▀▀ ▀█▀   █ █ █
███    ███    ▀███▀▀██ ███▌ ███         ███    █▀     █▄█  █  ▄   █▄▄ █▀█ ▀▄▀▄▀ █▄▄ █ ██▄  █  █▄█ █▀█
███    ███     ███   ▀ ███▌ ███         ███           
███    ███     ███     ███▌ ███       ▀███████████    ██    ██  ██     ██████      █████
███    ███     ███     ███  ███                ███    ██    ██ ███    ██  ████    ██   ██
███    ███     ███     ███  ███▌    ▄    ▄█    ███    ██    ██  ██    ██ ██ ██     █████
████████▀     ▄████▀   █▀   █████▄▄██  ▄████████▀      ██  ██   ██    ████  ██    ██   ██
                            ▀                           ████    ██ ██  ██████  ██  █████
```
## Tested in: Python 3.8.8
## By: LawlietJH
## Utils v1.0.8

![Icon](ubz2file.ico "Icono de archivos ubz2")

```php
■■■ Class Utils (v1.0.8)
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
    ║   │    │
    ║   │    │ - Functions: ──────────────────
    ║   │    ├── function runScriptVBS
    ║   │    ├── function minimizeAll
    ║   │    ├── function ejectCDROM
    ║   │    ├── function getWindowsProductKey
    ║   │    └── function setVolume
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
    ║   └── function ESSIDPasswd
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

```
