# Utilidades
 Un módulo recopilatorio con decenas de funciones que he hecho a lo largo del tiempo, utilidades de todo tipo, desde usar funciones simples como hash o comprimir archivos de texto plano con hasta 99% de compresión en algunos casos, editar los registros de Windows para personalizar el sistema o manejar la API de Windows para manipular el mouse, la pantalla, el teclado, vaciar la papelera de forma silenciosa o esconderle archivos dentro y que sean imborrables, obtener información de dispositivos bluetooth previamente vinculados o de conexiones wi-fi y mucho, mucho más...
```
███    █▄      ███      ▄█   ▄█          ▄████████
███    ███ ▀█████████▄ ███  ███         ███    ███    █▄▄ █▄█ ▀   █   ▄▀█ █ █ █ █   █ █▀▀ ▀█▀   █ █ █
███    ███    ▀███▀▀██ ███▌ ███         ███    █▀     █▄█  █  ▄   █▄▄ █▀█ ▀▄▀▄▀ █▄▄ █ ██▄  █  █▄█ █▀█
███    ███     ███   ▀ ███▌ ███         ███
███    ███     ███     ███▌ ███       ▀███████████    ██    ██  ██     ██    ██   ██
███    ███     ███     ███  ███                ███    ██    ██ ███    ███    ██   ██
███    ███     ███     ███  ███▌    ▄    ▄█    ███    ██    ██  ██     ██    ███████
████████▀     ▄████▀   █▀   █████▄▄██  ▄████████▀      ██  ██   ██     ██         ██
                            ▀                           ████    ██ ██  ██ ██      ██
```
## Tested in: Python 3.8.8
## By: LawlietJH
## Utils v1.1.4

![Icon](ubz2file.ico "Icono de archivos ubz2")

```php
■■■ Class Utils (v1.1.4)
    ║
    ║ - Functions: ───────────────────────────
    ╠══ function getBanner
    ╠══ function getClassAndFuncs
    ║
    ║ - Properties: ──────────────────────────
    ╠══ property tree
    ╠══ property raw_tree
    ║
    ║ - Main Classes: ────────────────────────
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
    ║   ║    ├── property text  (get, set, delete)
    ║   ║    └── property files (get)                           (+New)
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
    ║   ║    ├── function isActive                              (+New)
    ║   ║    ├── function isPressed                             (+New)
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
    ║   ║    ├── function confineCursor                         (+New)
    ║   ║    ├── function confineCursorCoords                   (+New)
    ║   ║    ├── function cursorInfo                            (+New)
    ║   ║    ├── function freezeCursor                          (+New)
    ║   ║    ├── function leftClick
    ║   ║    ├── function leftClickDown
    ║   ║    ├── function leftClickUp
    ║   ║    ├── function rightClick
    ║   ║    ├── function rightClickDown
    ║   ║    ├── function rightClickUp
    ║   ║    ├── function middleClick
    ║   ║    ├── function middleClickDown
    ║   ║    ├── function middleClickUp
    ║   ║    ├── function move                                  (+New)
    ║   ║    ├── function scrollUp
    ║   ║    ├── function scrollDown
    ║   ║    ├── function scrollRight
    ║   ║    ├── function scrollLeft
    ║   ║    └── function swapMouseButtons                      (+New)
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
    ║   │    ├── function toggleMute
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
    ║   ├── function disableMouseOnWindow                       (+New)
    ║   ├── function displaySwitch
    ║   ├── function dragAcceptFiles                            (+New)
    ║   ├── function exitWindows
    ║   ├── function getActiveWindow
    ║   ├── function getShortcutTargetPath                      (+New)
    ║   ├── function getNameActiveWindow
    ║   ├── function getPathFromWinExplorer
    ║   ├── function getPrivileges
    ║   ├── function getProcessPrivileges
    ║   ├── function getPosWindowToScreen                       (+New)
    ║   ├── function getPosScreenToWindow                       (+New)
    ║   ├── function getWindowPixelColor                        (+New)
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
    ║   ├── function getHwnds                                   (+New)
    ║   ├── function getPIDs                                    (+New)
    ║   ├── function getProcessName                             (+New)
    ║   ├── function getWindowsVersionStr                       (+New)
    ║   ├── function isUserPasswordValid
    ║   ├── function isWindowEnabled                            (+New)
    ║   │ #
    ║   ├── property isCapsLockActive      (get)
    ║   ├── property isLinux               (get)
    ║   ├── property isMouseInstalled      (get)
    ║   ├── property isPythonV2            (get)
    ║   ├── property isPythonV3            (get)
    ║   ├── property isSlowMachine         (get)
    ║   ├── property isUserAnAdmin         (get)
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
    ║   │ #
    ║   └── property collectAll            (get)
    ║
    ╚═ Class Utilities
        ║
        ║ - Classes: ─────────────────────────
        ╠══ Class ArgParser                                     (+New)
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function pairsUnion
        ║    ├── function pairsVals
        ║    ├── function singleVals
        ║    ├── function unitedVals
        ║    └── function parser
        ║
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
        ╠══ Class ContentOnImage
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function asc2Bin
        ║    ├── function bin2Asc
        ║    ├── function bin2Dec
        ║    ├── function dec2Bin
        ║    ├── function dec2Hex
        ║    ├── function hex2Dec
        ║    ├── function getMaxChars
        ║    ├── function getMaxCharsVal
        ║    ├── function checksumFixed
        ║    ├── function checksumNormal
        ║    ├── function listGenerator
        ║    ├── function testRules
        ║    ├── function extractData
        ║    ├── function insertData
        ║    ├── function insertContent
        ║    └── function extractContent
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
        ╠══ Class FileTimeChanger
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function toTimestamp (Lambda)
        ║    ├── function toFileTime  (Lambda)
        ║    ├── function timeToDate  (Lambda)
        ║    ├── function dateToTime  (Lambda)
        ║    ├── function strToDate   (Lambda)
        ║    ├── function toDatetime  (Lambda)
        ║    ├── function getFileTimes
        ║    └── function changeFileTimes
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
        ╠══ Class JSONToTree
        ║    │
        ║    │ - Functions: ──────────────────
        ║    └── function tree
        ║
        ╠══ Class NumberSystems
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function binToChr (Lambda)
        ║    ├── function binToHex (Lambda)
        ║    ├── function binToDec (Lambda)
        ║    ├── function binToOct (Lambda)
        ║    ├── function chrToBin (Lambda)
        ║    ├── function chrToHex (Lambda)
        ║    ├── function chrToDec (Lambda)
        ║    ├── function chrToOct (Lambda)
        ║    ├── function hexToBin (Lambda)
        ║    ├── function hexToChr (Lambda)
        ║    ├── function hexToDec (Lambda)
        ║    ├── function hexToOct (Lambda)
        ║    ├── function decToBin (Lambda)
        ║    ├── function decToChr (Lambda)
        ║    ├── function decToHex (Lambda)
        ║    ├── function decToOct (Lambda)
        ║    ├── function octToBin (Lambda)
        ║    ├── function octToChr (Lambda)
        ║    ├── function octToHex (Lambda)
        ║    └── function octToDec (Lambda)
        ║
        ╠══ Class Splitmix64
        ║    │
        ║    │ - Functions: ──────────────────
        ║    ├── function asc2Bin
        ║    ├── function bin2Asc
        ║    ├── function bin2Dec
        ║    ├── function dec2Bin
        ║    ├── property seed_text        (get)
        ║    ├── property seed             (get, set)
        ║    ├── function reset
        ║    ├── function nextInt
        ║    ├── function nextFloat
        ║    ├── function nextIntInRange
        ║    └── function nextFloatInRange
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
        ├── function getNumWords (Lambda)
        ├── function getNumChars (Lambda)
        ├── function getFileSize (Lambda)
        │ #Temperature Conversions:
        ├── function tempCtoF (Lambda)                          (+New)
        ├── function tempCtoK (Lambda)                          (+New)
        ├── function tempFtoC (Lambda)                          (+New)
        ├── function tempFtoK (Lambda)                          (+New)
        ├── function tempKtoC (Lambda)                          (+New)
        ├── function tempKtoF (Lambda)                          (+New)
        │ #Math:
        ├── function cos
        ├── function sin
        ├── function diagonal
        ├── function euclideanDistance
        ├── function fibonacci
        ├── function factorial
        ├── function getAngle
        ├── function isPrime
        │ #Combinatoria:
        ├── function nCr
        ├── function nVr
        ├── function nP
        ├── function nCRr
        ├── function nVRr
        ├── function nPR
        ├── function wordGenerator
        ├── function listGenerator
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
        ├── function getPasswd                                  (+New)
        ├── function getUncrackablePasswords                    (+New)
        ├── function writeHiddenText
        └── function flushBuffer

■■■ Class ObjTyList
■■■ Class ObjTyInt
■■■ Class ObjTyClassNames
■■■ Class ObjTyFunctionNames
■■■ Class SuperInheritance                                      (+New)
 
 All Classes Have Properties Called 'use', 'classes', and 'functions'.
 
 *Classes:    86
 *Functions:  258
 *Properties: 44
 
```
