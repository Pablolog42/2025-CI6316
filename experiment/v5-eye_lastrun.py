#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on noviembre 10, 2025, at 19:05
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware, iohub
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
block_number = 1



# 1. Definir las listas de coordenadas
x_coords = [-0.4, 0.08541666667, 0.5645833333]
y_coords = [0.3518518519, 0.1296296296, -0.09259259259, -0.3148148148, -0.537037037, -0.7592592593]

# 2. Crear la matriz anidada usando una lista de comprensión
# La estructura es positions[indice_x][indice_y]
positions = [[(x, y) for y in y_coords] for x in x_coords]

position_boton_caminata = [-0.4895833333,0.8518518519]
position_boton_metro = [-0.01041666667,0.8518518519]
position_boton_uber = [0.4583333333,0.8518518519]

box_size = [0.08854166667, 0.09259259259]
double_box_size = [0.08854166667, 2*0.09259259259]
size_boton = [0.2239583333,0.1666666667]

# 3. Rescatar los atributos desde los csv #########
import pandas as pd

# Cargar el archivo CSV
file_path = f'Atributos-Bloque-{block_number}.csv'
df = pd.read_csv(file_path)

# Establecer 'task' como el índice (la "llave" para buscar)
df_params = df.set_index('task')





# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'v5-eye'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\CI6316 - Grupo 1\\Desktop\\2025-CI6316\\Experiment\\v5-eye_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    # setup eyetracking
    ioConfig['eyetracker.hw.tobii.EyeTracker'] = {
        'name': 'tracker',
        'runtime_settings': {
            'sampling_rate': '60',
            'track_eyes': 'BINOCULAR',
        },
    }
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    deviceManager.devices['eyetracker'] = ioServer.getDevice('tracker')
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('respuesta') is None:
        # initialise respuesta
        respuesta = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='respuesta',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "wait" ---
    text = visual.TextStim(win=win, name='text',
        text='Registrando\nEspere un segundo...',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from code
    # partimos con la task 1, la idea es ir aumentandolo
    task_number = 0
    
    # 1. Definir las listas de coordenadas
    x_coords = [-0.4, 0.08541666667, 0.5645833333]
    y_coords = [0.3518518519, 0.1296296296, -0.09259259259, -0.3148148148, -0.537037037, -0.7592592593]
    
    # 2. Crear la matriz anidada usando una lista de comprensión
    # La estructura es positions[indice_x][indice_y]
    positions = [[(x, y) for y in y_coords] for x in x_coords]
    
    position_boton_caminata = [-0.4895833333,0.8518518519]
    position_boton_metro = [-0.01041666667,0.8518518519]
    position_boton_uber = [0.4583333333,0.8518518519]
    
    box_size = [0.08854166667, 0.09259259259]
    double_box_size = [0.08854166667, 2*0.09259259259]
    size_boton = [0.2239583333,0.1666666667]
    
    # 3. Rescatar los atributos desde los csv #########
    import pandas as pd
    
    # Cargar el archivo CSV
    file_path = f'Atributos-Bloque-{block_number}.csv'
    df = pd.read_csv(file_path)
    
    # Establecer 'task' como el índice (la "llave" para buscar)
    df_params = df.set_index('task')
    
    
    
    
    
    
    
    # --- Initialize components for Routine "trial" ---
    fondo = visual.ImageStim(
        win=win,
        name='fondo', units='norm', 
        image='fondo_eleccion.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    cam_inicio_viaje = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][0]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cam_inicio_viaje',
         depth=-2, autoLog=True,
    )
    cam_travel_time_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][1]], draggable=False, units='norm',     letterHeight=0.05,
         size=[0.08854166667 ,0.09259259259], borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cam_travel_time_text',
         depth=-3, autoLog=True,
    )
    cam_cost_text = visual.TextBox2(
         win, text='-', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][2]], draggable=False, units='norm',     letterHeight=0.05,
         size=[0.08854166667 ,0.09259259259], borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cam_cost_text',
         depth=-4, autoLog=True,
    )
    cam_dens_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][3]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cam_dens_text',
         depth=-5, autoLog=True,
    )
    cam_sec_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][4]], draggable=False, units='norm',     letterHeight=0.05,
         size=double_box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='cam_sec_text',
         depth=-6, autoLog=True,
    )
    metro_inicio_viaje_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[1][0]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='metro_inicio_viaje_text',
         depth=-7, autoLog=True,
    )
    metro_travel_time_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[1][1]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='metro_travel_time_text',
         depth=-8, autoLog=True,
    )
    metro_cost_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[1][2]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='metro_cost_text',
         depth=-9, autoLog=True,
    )
    metro_dens_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[1][3]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='metro_dens_text',
         depth=-10, autoLog=True,
    )
    metro_users_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[1][4]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='metro_users_text',
         depth=-11, autoLog=True,
    )
    uber_inicio_viaje_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[2][0]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='uber_inicio_viaje_text',
         depth=-12, autoLog=True,
    )
    uber_travel_time_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[2][1]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='uber_travel_time_text',
         depth=-13, autoLog=True,
    )
    uber_cost_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[2][2]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='uber_cost_text',
         depth=-14, autoLog=True,
    )
    uber_stars_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[2][3]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='uber_stars_text',
         depth=-15, autoLog=True,
    )
    uber_gender_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[2][4]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='uber_gender_text',
         depth=-16, autoLog=True,
    )
    uber_record_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[2][5]], draggable=False, units='norm',     letterHeight=0.05,
         size=box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='uber_record_text',
         depth=-17, autoLog=True,
    )
    cam_inicio_viaje_roi = visual.ROI(win, name='cam_inicio_viaje_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][0]], size=box_size, 
        anchor='center', ori=0.0, depth=-18
        )
    cam_travel_time_roi = visual.ROI(win, name='cam_travel_time_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][1]], size=box_size, 
        anchor='center', ori=0.0, depth=-19
        )
    cam_cost_roi = visual.ROI(win, name='cam_cost_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][2]], size=box_size, 
        anchor='center', ori=0.0, depth=-20
        )
    cam_dens_roi = visual.ROI(win, name='cam_dens_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][3]], size=box_size, 
        anchor='center', ori=0.0, depth=-21
        )
    cam_sec_roi = visual.ROI(win, name='cam_sec_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][4]], size=box_size, 
        anchor='center', ori=0.0, depth=-22
        )
    metro_inicio_viaje_roi = visual.ROI(win, name='metro_inicio_viaje_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][0]], size=box_size, 
        anchor='center', ori=0.0, depth=-23
        )
    metro_travel_time_roi = visual.ROI(win, name='metro_travel_time_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][1]], size=box_size, 
        anchor='center', ori=0.0, depth=-24
        )
    metro_cost_roi = visual.ROI(win, name='metro_cost_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][2]], size=box_size, 
        anchor='center', ori=0.0, depth=-25
        )
    metro_dens_roi = visual.ROI(win, name='metro_dens_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][3]], size=box_size, 
        anchor='center', ori=0.0, depth=-26
        )
    metro_users_roi = visual.ROI(win, name='metro_users_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][4]], size=box_size, 
        anchor='center', ori=0.0, depth=-27
        )
    uber_inicio_viaje_roi = visual.ROI(win, name='uber_inicio_viaje_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[2][0]], size=box_size, 
        anchor='center', ori=0.0, depth=-28
        )
    uber_travel_time_roi = visual.ROI(win, name='uber_travel_time_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[2][1]], size=box_size, 
        anchor='center', ori=0.0, depth=-29
        )
    uber_cost_roi = visual.ROI(win, name='uber_cost_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[2][2]], size=box_size, 
        anchor='center', ori=0.0, depth=-30
        )
    uber_stars_roi = visual.ROI(win, name='uber_stars_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[2][3]], size=box_size, 
        anchor='center', ori=0.0, depth=-31
        )
    uber_gender_roi = visual.ROI(win, name='uber_gender_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[2][4]], size=box_size, 
        anchor='center', ori=0.0, depth=-32
        )
    uber_record_roi = visual.ROI(win, name='uber_record_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[2][5]], size=box_size, 
        anchor='center', ori=0.0, depth=-33
        )
    respuesta = keyboard.Keyboard(deviceName='respuesta')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # set up handler to look after randomisation of conditions etc
    task = data.TrialHandler2(
        name='task',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('Atributos-Bloque-1.csv'), 
        seed=None, 
    )
    thisExp.addLoop(task)  # add the loop to the experiment
    thisTask = task.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
    if thisTask != None:
        for paramName in thisTask:
            globals()[paramName] = thisTask[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTask in task:
        task.status = STARTED
        if hasattr(thisTask, 'status'):
            thisTask.status = STARTED
        currentLoop = task
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTask.rgb)
        if thisTask != None:
            for paramName in thisTask:
                globals()[paramName] = thisTask[paramName]
        
        # --- Prepare to start Routine "wait" ---
        # create an object to store info about Routine wait
        wait = data.Routine(
            name='wait',
            components=[text],
        )
        wait.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for wait
        wait.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        wait.tStart = globalClock.getTime(format='float')
        wait.status = STARTED
        thisExp.addData('wait.started', wait.tStart)
        wait.maxDuration = None
        # keep track of which components have finished
        waitComponents = wait.components
        for thisComponent in wait.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "wait" ---
        wait.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # if trial has changed, end Routine now
            if hasattr(thisTask, 'status') and thisTask.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=wait,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                wait.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wait.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "wait" ---
        for thisComponent in wait.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for wait
        wait.tStop = globalClock.getTime(format='float')
        wait.tStopRefresh = tThisFlipGlobal
        thisExp.addData('wait.stopped', wait.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if wait.maxDurationReached:
            routineTimer.addTime(-wait.maxDuration)
        elif wait.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "trial" ---
        # create an object to store info about Routine trial
        trial = data.Routine(
            name='trial',
            components=[fondo, cam_inicio_viaje, cam_travel_time_text, cam_cost_text, cam_dens_text, cam_sec_text, metro_inicio_viaje_text, metro_travel_time_text, metro_cost_text, metro_dens_text, metro_users_text, uber_inicio_viaje_text, uber_travel_time_text, uber_cost_text, uber_stars_text, uber_gender_text, uber_record_text, cam_inicio_viaje_roi, cam_travel_time_roi, cam_cost_roi, cam_dens_roi, cam_sec_roi, metro_inicio_viaje_roi, metro_travel_time_roi, metro_cost_roi, metro_dens_roi, metro_users_roi, uber_inicio_viaje_roi, uber_travel_time_roi, uber_cost_roi, uber_stars_roi, uber_gender_roi, uber_record_roi, respuesta],
        )
        trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_1
        # En cada rutina, rescatamos los atributos y aumentamos el task en 1
        
        # Rescatamos atributos caminata
        #cam_light = df_params.loc[task_number, "cam_light"]
        #cam_travel_time = df_params.loc[task_number, "cam_travel_time"]
        #cam_cost = df_params.loc[task_number, "cam_cost"]
        #cam_dens = df_params.loc[task_number, "cam_dens"]
        #cam_sec = df_params.loc[task_number, "cam_sec"]
        
        cam_inicio_viaje.reset()
        cam_inicio_viaje.setText(hora)
        cam_travel_time_text.reset()
        cam_travel_time_text.setText(cam_travel_time)
        cam_cost_text.reset()
        cam_dens_text.reset()
        cam_dens_text.setText(cam_dens)
        cam_sec_text.reset()
        cam_sec_text.setText(cam_sec)
        metro_inicio_viaje_text.reset()
        metro_inicio_viaje_text.setText(hora)
        metro_travel_time_text.reset()
        metro_travel_time_text.setText(metro_travel_time)
        metro_cost_text.reset()
        metro_cost_text.setText(metro_cost)
        metro_dens_text.reset()
        metro_dens_text.setText(metro_dens)
        metro_users_text.reset()
        metro_users_text.setText(metro_users)
        uber_inicio_viaje_text.reset()
        uber_inicio_viaje_text.setText(hora)
        uber_travel_time_text.reset()
        uber_travel_time_text.setText(uber_travel_time)
        uber_cost_text.reset()
        uber_cost_text.setText(uber_cost)
        uber_stars_text.reset()
        uber_stars_text.setText(uber_stars)
        uber_gender_text.reset()
        uber_gender_text.setText(uber_driver_gender)
        uber_record_text.reset()
        uber_record_text.setText(uber_record)
        # clear any previous roi data
        cam_inicio_viaje_roi.reset()
        # clear any previous roi data
        cam_travel_time_roi.reset()
        # clear any previous roi data
        cam_cost_roi.reset()
        # clear any previous roi data
        cam_dens_roi.reset()
        # clear any previous roi data
        cam_sec_roi.reset()
        # clear any previous roi data
        metro_inicio_viaje_roi.reset()
        # clear any previous roi data
        metro_travel_time_roi.reset()
        # clear any previous roi data
        metro_cost_roi.reset()
        # clear any previous roi data
        metro_dens_roi.reset()
        # clear any previous roi data
        metro_users_roi.reset()
        # clear any previous roi data
        uber_inicio_viaje_roi.reset()
        # clear any previous roi data
        uber_travel_time_roi.reset()
        # clear any previous roi data
        uber_cost_roi.reset()
        # clear any previous roi data
        uber_stars_roi.reset()
        # clear any previous roi data
        uber_gender_roi.reset()
        # clear any previous roi data
        uber_record_roi.reset()
        # create starting attributes for respuesta
        respuesta.keys = []
        respuesta.rt = []
        _respuesta_allKeys = []
        # store start times for trial
        trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial.tStart = globalClock.getTime(format='float')
        trial.status = STARTED
        thisExp.addData('trial.started', trial.tStart)
        trial.maxDuration = None
        # keep track of which components have finished
        trialComponents = trial.components
        for thisComponent in trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTask, 'status') and thisTask.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fondo* updates
            
            # if fondo is starting this frame...
            if fondo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fondo.frameNStart = frameN  # exact frame index
                fondo.tStart = t  # local t and not account for scr refresh
                fondo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fondo, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fondo.started')
                # update status
                fondo.status = STARTED
                fondo.setAutoDraw(True)
            
            # if fondo is active this frame...
            if fondo.status == STARTED:
                # update params
                pass
            
            # *cam_inicio_viaje* updates
            
            # if cam_inicio_viaje is starting this frame...
            if cam_inicio_viaje.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_inicio_viaje.frameNStart = frameN  # exact frame index
                cam_inicio_viaje.tStart = t  # local t and not account for scr refresh
                cam_inicio_viaje.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_inicio_viaje, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_inicio_viaje.started')
                # update status
                cam_inicio_viaje.status = STARTED
                cam_inicio_viaje.setAutoDraw(True)
            
            # if cam_inicio_viaje is active this frame...
            if cam_inicio_viaje.status == STARTED:
                # update params
                pass
            
            # *cam_travel_time_text* updates
            
            # if cam_travel_time_text is starting this frame...
            if cam_travel_time_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_travel_time_text.frameNStart = frameN  # exact frame index
                cam_travel_time_text.tStart = t  # local t and not account for scr refresh
                cam_travel_time_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_travel_time_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_travel_time_text.started')
                # update status
                cam_travel_time_text.status = STARTED
                cam_travel_time_text.setAutoDraw(True)
            
            # if cam_travel_time_text is active this frame...
            if cam_travel_time_text.status == STARTED:
                # update params
                pass
            
            # *cam_cost_text* updates
            
            # if cam_cost_text is starting this frame...
            if cam_cost_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_cost_text.frameNStart = frameN  # exact frame index
                cam_cost_text.tStart = t  # local t and not account for scr refresh
                cam_cost_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_cost_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_cost_text.started')
                # update status
                cam_cost_text.status = STARTED
                cam_cost_text.setAutoDraw(True)
            
            # if cam_cost_text is active this frame...
            if cam_cost_text.status == STARTED:
                # update params
                pass
            
            # *cam_dens_text* updates
            
            # if cam_dens_text is starting this frame...
            if cam_dens_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_dens_text.frameNStart = frameN  # exact frame index
                cam_dens_text.tStart = t  # local t and not account for scr refresh
                cam_dens_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_dens_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_dens_text.started')
                # update status
                cam_dens_text.status = STARTED
                cam_dens_text.setAutoDraw(True)
            
            # if cam_dens_text is active this frame...
            if cam_dens_text.status == STARTED:
                # update params
                pass
            
            # *cam_sec_text* updates
            
            # if cam_sec_text is starting this frame...
            if cam_sec_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_sec_text.frameNStart = frameN  # exact frame index
                cam_sec_text.tStart = t  # local t and not account for scr refresh
                cam_sec_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_sec_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_sec_text.started')
                # update status
                cam_sec_text.status = STARTED
                cam_sec_text.setAutoDraw(True)
            
            # if cam_sec_text is active this frame...
            if cam_sec_text.status == STARTED:
                # update params
                pass
            
            # *metro_inicio_viaje_text* updates
            
            # if metro_inicio_viaje_text is starting this frame...
            if metro_inicio_viaje_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_inicio_viaje_text.frameNStart = frameN  # exact frame index
                metro_inicio_viaje_text.tStart = t  # local t and not account for scr refresh
                metro_inicio_viaje_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_inicio_viaje_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_inicio_viaje_text.started')
                # update status
                metro_inicio_viaje_text.status = STARTED
                metro_inicio_viaje_text.setAutoDraw(True)
            
            # if metro_inicio_viaje_text is active this frame...
            if metro_inicio_viaje_text.status == STARTED:
                # update params
                pass
            
            # *metro_travel_time_text* updates
            
            # if metro_travel_time_text is starting this frame...
            if metro_travel_time_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_travel_time_text.frameNStart = frameN  # exact frame index
                metro_travel_time_text.tStart = t  # local t and not account for scr refresh
                metro_travel_time_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_travel_time_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_travel_time_text.started')
                # update status
                metro_travel_time_text.status = STARTED
                metro_travel_time_text.setAutoDraw(True)
            
            # if metro_travel_time_text is active this frame...
            if metro_travel_time_text.status == STARTED:
                # update params
                pass
            
            # *metro_cost_text* updates
            
            # if metro_cost_text is starting this frame...
            if metro_cost_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_cost_text.frameNStart = frameN  # exact frame index
                metro_cost_text.tStart = t  # local t and not account for scr refresh
                metro_cost_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_cost_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_cost_text.started')
                # update status
                metro_cost_text.status = STARTED
                metro_cost_text.setAutoDraw(True)
            
            # if metro_cost_text is active this frame...
            if metro_cost_text.status == STARTED:
                # update params
                pass
            
            # *metro_dens_text* updates
            
            # if metro_dens_text is starting this frame...
            if metro_dens_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_dens_text.frameNStart = frameN  # exact frame index
                metro_dens_text.tStart = t  # local t and not account for scr refresh
                metro_dens_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_dens_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_dens_text.started')
                # update status
                metro_dens_text.status = STARTED
                metro_dens_text.setAutoDraw(True)
            
            # if metro_dens_text is active this frame...
            if metro_dens_text.status == STARTED:
                # update params
                pass
            
            # *metro_users_text* updates
            
            # if metro_users_text is starting this frame...
            if metro_users_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_users_text.frameNStart = frameN  # exact frame index
                metro_users_text.tStart = t  # local t and not account for scr refresh
                metro_users_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_users_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_users_text.started')
                # update status
                metro_users_text.status = STARTED
                metro_users_text.setAutoDraw(True)
            
            # if metro_users_text is active this frame...
            if metro_users_text.status == STARTED:
                # update params
                pass
            
            # *uber_inicio_viaje_text* updates
            
            # if uber_inicio_viaje_text is starting this frame...
            if uber_inicio_viaje_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_inicio_viaje_text.frameNStart = frameN  # exact frame index
                uber_inicio_viaje_text.tStart = t  # local t and not account for scr refresh
                uber_inicio_viaje_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_inicio_viaje_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_inicio_viaje_text.started')
                # update status
                uber_inicio_viaje_text.status = STARTED
                uber_inicio_viaje_text.setAutoDraw(True)
            
            # if uber_inicio_viaje_text is active this frame...
            if uber_inicio_viaje_text.status == STARTED:
                # update params
                pass
            
            # *uber_travel_time_text* updates
            
            # if uber_travel_time_text is starting this frame...
            if uber_travel_time_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_travel_time_text.frameNStart = frameN  # exact frame index
                uber_travel_time_text.tStart = t  # local t and not account for scr refresh
                uber_travel_time_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_travel_time_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_travel_time_text.started')
                # update status
                uber_travel_time_text.status = STARTED
                uber_travel_time_text.setAutoDraw(True)
            
            # if uber_travel_time_text is active this frame...
            if uber_travel_time_text.status == STARTED:
                # update params
                pass
            
            # *uber_cost_text* updates
            
            # if uber_cost_text is starting this frame...
            if uber_cost_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_cost_text.frameNStart = frameN  # exact frame index
                uber_cost_text.tStart = t  # local t and not account for scr refresh
                uber_cost_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_cost_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_cost_text.started')
                # update status
                uber_cost_text.status = STARTED
                uber_cost_text.setAutoDraw(True)
            
            # if uber_cost_text is active this frame...
            if uber_cost_text.status == STARTED:
                # update params
                pass
            
            # *uber_stars_text* updates
            
            # if uber_stars_text is starting this frame...
            if uber_stars_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_stars_text.frameNStart = frameN  # exact frame index
                uber_stars_text.tStart = t  # local t and not account for scr refresh
                uber_stars_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_stars_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_stars_text.started')
                # update status
                uber_stars_text.status = STARTED
                uber_stars_text.setAutoDraw(True)
            
            # if uber_stars_text is active this frame...
            if uber_stars_text.status == STARTED:
                # update params
                pass
            
            # *uber_gender_text* updates
            
            # if uber_gender_text is starting this frame...
            if uber_gender_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_gender_text.frameNStart = frameN  # exact frame index
                uber_gender_text.tStart = t  # local t and not account for scr refresh
                uber_gender_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_gender_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_gender_text.started')
                # update status
                uber_gender_text.status = STARTED
                uber_gender_text.setAutoDraw(True)
            
            # if uber_gender_text is active this frame...
            if uber_gender_text.status == STARTED:
                # update params
                pass
            
            # *uber_record_text* updates
            
            # if uber_record_text is starting this frame...
            if uber_record_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_record_text.frameNStart = frameN  # exact frame index
                uber_record_text.tStart = t  # local t and not account for scr refresh
                uber_record_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_record_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_record_text.started')
                # update status
                uber_record_text.status = STARTED
                uber_record_text.setAutoDraw(True)
            
            # if uber_record_text is active this frame...
            if uber_record_text.status == STARTED:
                # update params
                pass
            
            # if cam_inicio_viaje_roi is starting this frame...
            if cam_inicio_viaje_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_inicio_viaje_roi.frameNStart = frameN  # exact frame index
                cam_inicio_viaje_roi.tStart = t  # local t and not account for scr refresh
                cam_inicio_viaje_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_inicio_viaje_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_inicio_viaje_roi.started')
                # update status
                cam_inicio_viaje_roi.status = STARTED
                cam_inicio_viaje_roi.setAutoDraw(True)
            
            # if cam_inicio_viaje_roi is active this frame...
            if cam_inicio_viaje_roi.status == STARTED:
                # update params
                pass
                # check whether cam_inicio_viaje_roi has been looked in
                if cam_inicio_viaje_roi.isLookedIn:
                    if not cam_inicio_viaje_roi.wasLookedIn:
                        cam_inicio_viaje_roi.timesOn.append(cam_inicio_viaje_roi.clock.getTime()) # store time of first look
                        cam_inicio_viaje_roi.timesOff.append(cam_inicio_viaje_roi.clock.getTime()) # store time looked until
                    else:
                        cam_inicio_viaje_roi.timesOff[-1] = cam_inicio_viaje_roi.clock.getTime() # update time looked until
                    cam_inicio_viaje_roi.wasLookedIn = True  # if cam_inicio_viaje_roi is still looked at next frame, it is not a new look
                else:
                    if cam_inicio_viaje_roi.wasLookedIn:
                        cam_inicio_viaje_roi.timesOff[-1] = cam_inicio_viaje_roi.clock.getTime() # update time looked until
                    cam_inicio_viaje_roi.wasLookedIn = False  # if cam_inicio_viaje_roi is looked at next frame, it is a new look
            else:
                cam_inicio_viaje_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                cam_inicio_viaje_roi.wasLookedIn = False  # if cam_inicio_viaje_roi is looked at next frame, it is a new look
            
            # if cam_travel_time_roi is starting this frame...
            if cam_travel_time_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_travel_time_roi.frameNStart = frameN  # exact frame index
                cam_travel_time_roi.tStart = t  # local t and not account for scr refresh
                cam_travel_time_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_travel_time_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_travel_time_roi.started')
                # update status
                cam_travel_time_roi.status = STARTED
                cam_travel_time_roi.setAutoDraw(True)
            
            # if cam_travel_time_roi is active this frame...
            if cam_travel_time_roi.status == STARTED:
                # update params
                pass
                # check whether cam_travel_time_roi has been looked in
                if cam_travel_time_roi.isLookedIn:
                    if not cam_travel_time_roi.wasLookedIn:
                        cam_travel_time_roi.timesOn.append(cam_travel_time_roi.clock.getTime()) # store time of first look
                        cam_travel_time_roi.timesOff.append(cam_travel_time_roi.clock.getTime()) # store time looked until
                    else:
                        cam_travel_time_roi.timesOff[-1] = cam_travel_time_roi.clock.getTime() # update time looked until
                    cam_travel_time_roi.wasLookedIn = True  # if cam_travel_time_roi is still looked at next frame, it is not a new look
                else:
                    if cam_travel_time_roi.wasLookedIn:
                        cam_travel_time_roi.timesOff[-1] = cam_travel_time_roi.clock.getTime() # update time looked until
                    cam_travel_time_roi.wasLookedIn = False  # if cam_travel_time_roi is looked at next frame, it is a new look
            else:
                cam_travel_time_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                cam_travel_time_roi.wasLookedIn = False  # if cam_travel_time_roi is looked at next frame, it is a new look
            
            # if cam_cost_roi is starting this frame...
            if cam_cost_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_cost_roi.frameNStart = frameN  # exact frame index
                cam_cost_roi.tStart = t  # local t and not account for scr refresh
                cam_cost_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_cost_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_cost_roi.started')
                # update status
                cam_cost_roi.status = STARTED
                cam_cost_roi.setAutoDraw(True)
            
            # if cam_cost_roi is active this frame...
            if cam_cost_roi.status == STARTED:
                # update params
                pass
                # check whether cam_cost_roi has been looked in
                if cam_cost_roi.isLookedIn:
                    if not cam_cost_roi.wasLookedIn:
                        cam_cost_roi.timesOn.append(cam_cost_roi.clock.getTime()) # store time of first look
                        cam_cost_roi.timesOff.append(cam_cost_roi.clock.getTime()) # store time looked until
                    else:
                        cam_cost_roi.timesOff[-1] = cam_cost_roi.clock.getTime() # update time looked until
                    cam_cost_roi.wasLookedIn = True  # if cam_cost_roi is still looked at next frame, it is not a new look
                else:
                    if cam_cost_roi.wasLookedIn:
                        cam_cost_roi.timesOff[-1] = cam_cost_roi.clock.getTime() # update time looked until
                    cam_cost_roi.wasLookedIn = False  # if cam_cost_roi is looked at next frame, it is a new look
            else:
                cam_cost_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                cam_cost_roi.wasLookedIn = False  # if cam_cost_roi is looked at next frame, it is a new look
            
            # if cam_dens_roi is starting this frame...
            if cam_dens_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_dens_roi.frameNStart = frameN  # exact frame index
                cam_dens_roi.tStart = t  # local t and not account for scr refresh
                cam_dens_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_dens_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_dens_roi.started')
                # update status
                cam_dens_roi.status = STARTED
                cam_dens_roi.setAutoDraw(True)
            
            # if cam_dens_roi is active this frame...
            if cam_dens_roi.status == STARTED:
                # update params
                pass
                # check whether cam_dens_roi has been looked in
                if cam_dens_roi.isLookedIn:
                    if not cam_dens_roi.wasLookedIn:
                        cam_dens_roi.timesOn.append(cam_dens_roi.clock.getTime()) # store time of first look
                        cam_dens_roi.timesOff.append(cam_dens_roi.clock.getTime()) # store time looked until
                    else:
                        cam_dens_roi.timesOff[-1] = cam_dens_roi.clock.getTime() # update time looked until
                    cam_dens_roi.wasLookedIn = True  # if cam_dens_roi is still looked at next frame, it is not a new look
                else:
                    if cam_dens_roi.wasLookedIn:
                        cam_dens_roi.timesOff[-1] = cam_dens_roi.clock.getTime() # update time looked until
                    cam_dens_roi.wasLookedIn = False  # if cam_dens_roi is looked at next frame, it is a new look
            else:
                cam_dens_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                cam_dens_roi.wasLookedIn = False  # if cam_dens_roi is looked at next frame, it is a new look
            
            # if cam_sec_roi is starting this frame...
            if cam_sec_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cam_sec_roi.frameNStart = frameN  # exact frame index
                cam_sec_roi.tStart = t  # local t and not account for scr refresh
                cam_sec_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cam_sec_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cam_sec_roi.started')
                # update status
                cam_sec_roi.status = STARTED
                cam_sec_roi.setAutoDraw(True)
            
            # if cam_sec_roi is active this frame...
            if cam_sec_roi.status == STARTED:
                # update params
                pass
                # check whether cam_sec_roi has been looked in
                if cam_sec_roi.isLookedIn:
                    if not cam_sec_roi.wasLookedIn:
                        cam_sec_roi.timesOn.append(cam_sec_roi.clock.getTime()) # store time of first look
                        cam_sec_roi.timesOff.append(cam_sec_roi.clock.getTime()) # store time looked until
                    else:
                        cam_sec_roi.timesOff[-1] = cam_sec_roi.clock.getTime() # update time looked until
                    cam_sec_roi.wasLookedIn = True  # if cam_sec_roi is still looked at next frame, it is not a new look
                else:
                    if cam_sec_roi.wasLookedIn:
                        cam_sec_roi.timesOff[-1] = cam_sec_roi.clock.getTime() # update time looked until
                    cam_sec_roi.wasLookedIn = False  # if cam_sec_roi is looked at next frame, it is a new look
            else:
                cam_sec_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                cam_sec_roi.wasLookedIn = False  # if cam_sec_roi is looked at next frame, it is a new look
            
            # if metro_inicio_viaje_roi is starting this frame...
            if metro_inicio_viaje_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_inicio_viaje_roi.frameNStart = frameN  # exact frame index
                metro_inicio_viaje_roi.tStart = t  # local t and not account for scr refresh
                metro_inicio_viaje_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_inicio_viaje_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_inicio_viaje_roi.started')
                # update status
                metro_inicio_viaje_roi.status = STARTED
                metro_inicio_viaje_roi.setAutoDraw(True)
            
            # if metro_inicio_viaje_roi is active this frame...
            if metro_inicio_viaje_roi.status == STARTED:
                # update params
                pass
                # check whether metro_inicio_viaje_roi has been looked in
                if metro_inicio_viaje_roi.isLookedIn:
                    if not metro_inicio_viaje_roi.wasLookedIn:
                        metro_inicio_viaje_roi.timesOn.append(metro_inicio_viaje_roi.clock.getTime()) # store time of first look
                        metro_inicio_viaje_roi.timesOff.append(metro_inicio_viaje_roi.clock.getTime()) # store time looked until
                    else:
                        metro_inicio_viaje_roi.timesOff[-1] = metro_inicio_viaje_roi.clock.getTime() # update time looked until
                    metro_inicio_viaje_roi.wasLookedIn = True  # if metro_inicio_viaje_roi is still looked at next frame, it is not a new look
                else:
                    if metro_inicio_viaje_roi.wasLookedIn:
                        metro_inicio_viaje_roi.timesOff[-1] = metro_inicio_viaje_roi.clock.getTime() # update time looked until
                    metro_inicio_viaje_roi.wasLookedIn = False  # if metro_inicio_viaje_roi is looked at next frame, it is a new look
            else:
                metro_inicio_viaje_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                metro_inicio_viaje_roi.wasLookedIn = False  # if metro_inicio_viaje_roi is looked at next frame, it is a new look
            
            # if metro_travel_time_roi is starting this frame...
            if metro_travel_time_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_travel_time_roi.frameNStart = frameN  # exact frame index
                metro_travel_time_roi.tStart = t  # local t and not account for scr refresh
                metro_travel_time_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_travel_time_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_travel_time_roi.started')
                # update status
                metro_travel_time_roi.status = STARTED
                metro_travel_time_roi.setAutoDraw(True)
            
            # if metro_travel_time_roi is active this frame...
            if metro_travel_time_roi.status == STARTED:
                # update params
                pass
                # check whether metro_travel_time_roi has been looked in
                if metro_travel_time_roi.isLookedIn:
                    if not metro_travel_time_roi.wasLookedIn:
                        metro_travel_time_roi.timesOn.append(metro_travel_time_roi.clock.getTime()) # store time of first look
                        metro_travel_time_roi.timesOff.append(metro_travel_time_roi.clock.getTime()) # store time looked until
                    else:
                        metro_travel_time_roi.timesOff[-1] = metro_travel_time_roi.clock.getTime() # update time looked until
                    metro_travel_time_roi.wasLookedIn = True  # if metro_travel_time_roi is still looked at next frame, it is not a new look
                else:
                    if metro_travel_time_roi.wasLookedIn:
                        metro_travel_time_roi.timesOff[-1] = metro_travel_time_roi.clock.getTime() # update time looked until
                    metro_travel_time_roi.wasLookedIn = False  # if metro_travel_time_roi is looked at next frame, it is a new look
            else:
                metro_travel_time_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                metro_travel_time_roi.wasLookedIn = False  # if metro_travel_time_roi is looked at next frame, it is a new look
            
            # if metro_cost_roi is starting this frame...
            if metro_cost_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_cost_roi.frameNStart = frameN  # exact frame index
                metro_cost_roi.tStart = t  # local t and not account for scr refresh
                metro_cost_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_cost_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_cost_roi.started')
                # update status
                metro_cost_roi.status = STARTED
                metro_cost_roi.setAutoDraw(True)
            
            # if metro_cost_roi is active this frame...
            if metro_cost_roi.status == STARTED:
                # update params
                pass
                # check whether metro_cost_roi has been looked in
                if metro_cost_roi.isLookedIn:
                    if not metro_cost_roi.wasLookedIn:
                        metro_cost_roi.timesOn.append(metro_cost_roi.clock.getTime()) # store time of first look
                        metro_cost_roi.timesOff.append(metro_cost_roi.clock.getTime()) # store time looked until
                    else:
                        metro_cost_roi.timesOff[-1] = metro_cost_roi.clock.getTime() # update time looked until
                    metro_cost_roi.wasLookedIn = True  # if metro_cost_roi is still looked at next frame, it is not a new look
                else:
                    if metro_cost_roi.wasLookedIn:
                        metro_cost_roi.timesOff[-1] = metro_cost_roi.clock.getTime() # update time looked until
                    metro_cost_roi.wasLookedIn = False  # if metro_cost_roi is looked at next frame, it is a new look
            else:
                metro_cost_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                metro_cost_roi.wasLookedIn = False  # if metro_cost_roi is looked at next frame, it is a new look
            
            # if metro_dens_roi is starting this frame...
            if metro_dens_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_dens_roi.frameNStart = frameN  # exact frame index
                metro_dens_roi.tStart = t  # local t and not account for scr refresh
                metro_dens_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_dens_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_dens_roi.started')
                # update status
                metro_dens_roi.status = STARTED
                metro_dens_roi.setAutoDraw(True)
            
            # if metro_dens_roi is active this frame...
            if metro_dens_roi.status == STARTED:
                # update params
                pass
                # check whether metro_dens_roi has been looked in
                if metro_dens_roi.isLookedIn:
                    if not metro_dens_roi.wasLookedIn:
                        metro_dens_roi.timesOn.append(metro_dens_roi.clock.getTime()) # store time of first look
                        metro_dens_roi.timesOff.append(metro_dens_roi.clock.getTime()) # store time looked until
                    else:
                        metro_dens_roi.timesOff[-1] = metro_dens_roi.clock.getTime() # update time looked until
                    metro_dens_roi.wasLookedIn = True  # if metro_dens_roi is still looked at next frame, it is not a new look
                else:
                    if metro_dens_roi.wasLookedIn:
                        metro_dens_roi.timesOff[-1] = metro_dens_roi.clock.getTime() # update time looked until
                    metro_dens_roi.wasLookedIn = False  # if metro_dens_roi is looked at next frame, it is a new look
            else:
                metro_dens_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                metro_dens_roi.wasLookedIn = False  # if metro_dens_roi is looked at next frame, it is a new look
            
            # if metro_users_roi is starting this frame...
            if metro_users_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_users_roi.frameNStart = frameN  # exact frame index
                metro_users_roi.tStart = t  # local t and not account for scr refresh
                metro_users_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_users_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_users_roi.started')
                # update status
                metro_users_roi.status = STARTED
                metro_users_roi.setAutoDraw(True)
            
            # if metro_users_roi is active this frame...
            if metro_users_roi.status == STARTED:
                # update params
                pass
                # check whether metro_users_roi has been looked in
                if metro_users_roi.isLookedIn:
                    if not metro_users_roi.wasLookedIn:
                        metro_users_roi.timesOn.append(metro_users_roi.clock.getTime()) # store time of first look
                        metro_users_roi.timesOff.append(metro_users_roi.clock.getTime()) # store time looked until
                    else:
                        metro_users_roi.timesOff[-1] = metro_users_roi.clock.getTime() # update time looked until
                    metro_users_roi.wasLookedIn = True  # if metro_users_roi is still looked at next frame, it is not a new look
                else:
                    if metro_users_roi.wasLookedIn:
                        metro_users_roi.timesOff[-1] = metro_users_roi.clock.getTime() # update time looked until
                    metro_users_roi.wasLookedIn = False  # if metro_users_roi is looked at next frame, it is a new look
            else:
                metro_users_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                metro_users_roi.wasLookedIn = False  # if metro_users_roi is looked at next frame, it is a new look
            
            # if uber_inicio_viaje_roi is starting this frame...
            if uber_inicio_viaje_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_inicio_viaje_roi.frameNStart = frameN  # exact frame index
                uber_inicio_viaje_roi.tStart = t  # local t and not account for scr refresh
                uber_inicio_viaje_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_inicio_viaje_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_inicio_viaje_roi.started')
                # update status
                uber_inicio_viaje_roi.status = STARTED
                uber_inicio_viaje_roi.setAutoDraw(True)
            
            # if uber_inicio_viaje_roi is active this frame...
            if uber_inicio_viaje_roi.status == STARTED:
                # update params
                pass
                # check whether uber_inicio_viaje_roi has been looked in
                if uber_inicio_viaje_roi.isLookedIn:
                    if not uber_inicio_viaje_roi.wasLookedIn:
                        uber_inicio_viaje_roi.timesOn.append(uber_inicio_viaje_roi.clock.getTime()) # store time of first look
                        uber_inicio_viaje_roi.timesOff.append(uber_inicio_viaje_roi.clock.getTime()) # store time looked until
                    else:
                        uber_inicio_viaje_roi.timesOff[-1] = uber_inicio_viaje_roi.clock.getTime() # update time looked until
                    uber_inicio_viaje_roi.wasLookedIn = True  # if uber_inicio_viaje_roi is still looked at next frame, it is not a new look
                else:
                    if uber_inicio_viaje_roi.wasLookedIn:
                        uber_inicio_viaje_roi.timesOff[-1] = uber_inicio_viaje_roi.clock.getTime() # update time looked until
                    uber_inicio_viaje_roi.wasLookedIn = False  # if uber_inicio_viaje_roi is looked at next frame, it is a new look
            else:
                uber_inicio_viaje_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                uber_inicio_viaje_roi.wasLookedIn = False  # if uber_inicio_viaje_roi is looked at next frame, it is a new look
            
            # if uber_travel_time_roi is starting this frame...
            if uber_travel_time_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_travel_time_roi.frameNStart = frameN  # exact frame index
                uber_travel_time_roi.tStart = t  # local t and not account for scr refresh
                uber_travel_time_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_travel_time_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_travel_time_roi.started')
                # update status
                uber_travel_time_roi.status = STARTED
                uber_travel_time_roi.setAutoDraw(True)
            
            # if uber_travel_time_roi is active this frame...
            if uber_travel_time_roi.status == STARTED:
                # update params
                pass
                # check whether uber_travel_time_roi has been looked in
                if uber_travel_time_roi.isLookedIn:
                    if not uber_travel_time_roi.wasLookedIn:
                        uber_travel_time_roi.timesOn.append(uber_travel_time_roi.clock.getTime()) # store time of first look
                        uber_travel_time_roi.timesOff.append(uber_travel_time_roi.clock.getTime()) # store time looked until
                    else:
                        uber_travel_time_roi.timesOff[-1] = uber_travel_time_roi.clock.getTime() # update time looked until
                    uber_travel_time_roi.wasLookedIn = True  # if uber_travel_time_roi is still looked at next frame, it is not a new look
                else:
                    if uber_travel_time_roi.wasLookedIn:
                        uber_travel_time_roi.timesOff[-1] = uber_travel_time_roi.clock.getTime() # update time looked until
                    uber_travel_time_roi.wasLookedIn = False  # if uber_travel_time_roi is looked at next frame, it is a new look
            else:
                uber_travel_time_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                uber_travel_time_roi.wasLookedIn = False  # if uber_travel_time_roi is looked at next frame, it is a new look
            
            # if uber_cost_roi is starting this frame...
            if uber_cost_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_cost_roi.frameNStart = frameN  # exact frame index
                uber_cost_roi.tStart = t  # local t and not account for scr refresh
                uber_cost_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_cost_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_cost_roi.started')
                # update status
                uber_cost_roi.status = STARTED
                uber_cost_roi.setAutoDraw(True)
            
            # if uber_cost_roi is active this frame...
            if uber_cost_roi.status == STARTED:
                # update params
                pass
                # check whether uber_cost_roi has been looked in
                if uber_cost_roi.isLookedIn:
                    if not uber_cost_roi.wasLookedIn:
                        uber_cost_roi.timesOn.append(uber_cost_roi.clock.getTime()) # store time of first look
                        uber_cost_roi.timesOff.append(uber_cost_roi.clock.getTime()) # store time looked until
                    else:
                        uber_cost_roi.timesOff[-1] = uber_cost_roi.clock.getTime() # update time looked until
                    uber_cost_roi.wasLookedIn = True  # if uber_cost_roi is still looked at next frame, it is not a new look
                else:
                    if uber_cost_roi.wasLookedIn:
                        uber_cost_roi.timesOff[-1] = uber_cost_roi.clock.getTime() # update time looked until
                    uber_cost_roi.wasLookedIn = False  # if uber_cost_roi is looked at next frame, it is a new look
            else:
                uber_cost_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                uber_cost_roi.wasLookedIn = False  # if uber_cost_roi is looked at next frame, it is a new look
            
            # if uber_stars_roi is starting this frame...
            if uber_stars_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_stars_roi.frameNStart = frameN  # exact frame index
                uber_stars_roi.tStart = t  # local t and not account for scr refresh
                uber_stars_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_stars_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_stars_roi.started')
                # update status
                uber_stars_roi.status = STARTED
                uber_stars_roi.setAutoDraw(True)
            
            # if uber_stars_roi is active this frame...
            if uber_stars_roi.status == STARTED:
                # update params
                pass
                # check whether uber_stars_roi has been looked in
                if uber_stars_roi.isLookedIn:
                    if not uber_stars_roi.wasLookedIn:
                        uber_stars_roi.timesOn.append(uber_stars_roi.clock.getTime()) # store time of first look
                        uber_stars_roi.timesOff.append(uber_stars_roi.clock.getTime()) # store time looked until
                    else:
                        uber_stars_roi.timesOff[-1] = uber_stars_roi.clock.getTime() # update time looked until
                    uber_stars_roi.wasLookedIn = True  # if uber_stars_roi is still looked at next frame, it is not a new look
                else:
                    if uber_stars_roi.wasLookedIn:
                        uber_stars_roi.timesOff[-1] = uber_stars_roi.clock.getTime() # update time looked until
                    uber_stars_roi.wasLookedIn = False  # if uber_stars_roi is looked at next frame, it is a new look
            else:
                uber_stars_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                uber_stars_roi.wasLookedIn = False  # if uber_stars_roi is looked at next frame, it is a new look
            
            # if uber_gender_roi is starting this frame...
            if uber_gender_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_gender_roi.frameNStart = frameN  # exact frame index
                uber_gender_roi.tStart = t  # local t and not account for scr refresh
                uber_gender_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_gender_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_gender_roi.started')
                # update status
                uber_gender_roi.status = STARTED
                uber_gender_roi.setAutoDraw(True)
            
            # if uber_gender_roi is active this frame...
            if uber_gender_roi.status == STARTED:
                # update params
                pass
                # check whether uber_gender_roi has been looked in
                if uber_gender_roi.isLookedIn:
                    if not uber_gender_roi.wasLookedIn:
                        uber_gender_roi.timesOn.append(uber_gender_roi.clock.getTime()) # store time of first look
                        uber_gender_roi.timesOff.append(uber_gender_roi.clock.getTime()) # store time looked until
                    else:
                        uber_gender_roi.timesOff[-1] = uber_gender_roi.clock.getTime() # update time looked until
                    uber_gender_roi.wasLookedIn = True  # if uber_gender_roi is still looked at next frame, it is not a new look
                else:
                    if uber_gender_roi.wasLookedIn:
                        uber_gender_roi.timesOff[-1] = uber_gender_roi.clock.getTime() # update time looked until
                    uber_gender_roi.wasLookedIn = False  # if uber_gender_roi is looked at next frame, it is a new look
            else:
                uber_gender_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                uber_gender_roi.wasLookedIn = False  # if uber_gender_roi is looked at next frame, it is a new look
            
            # if uber_record_roi is starting this frame...
            if uber_record_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_record_roi.frameNStart = frameN  # exact frame index
                uber_record_roi.tStart = t  # local t and not account for scr refresh
                uber_record_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_record_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_record_roi.started')
                # update status
                uber_record_roi.status = STARTED
                uber_record_roi.setAutoDraw(True)
            
            # if uber_record_roi is active this frame...
            if uber_record_roi.status == STARTED:
                # update params
                pass
                # check whether uber_record_roi has been looked in
                if uber_record_roi.isLookedIn:
                    if not uber_record_roi.wasLookedIn:
                        uber_record_roi.timesOn.append(uber_record_roi.clock.getTime()) # store time of first look
                        uber_record_roi.timesOff.append(uber_record_roi.clock.getTime()) # store time looked until
                    else:
                        uber_record_roi.timesOff[-1] = uber_record_roi.clock.getTime() # update time looked until
                    uber_record_roi.wasLookedIn = True  # if uber_record_roi is still looked at next frame, it is not a new look
                else:
                    if uber_record_roi.wasLookedIn:
                        uber_record_roi.timesOff[-1] = uber_record_roi.clock.getTime() # update time looked until
                    uber_record_roi.wasLookedIn = False  # if uber_record_roi is looked at next frame, it is a new look
            else:
                uber_record_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                uber_record_roi.wasLookedIn = False  # if uber_record_roi is looked at next frame, it is a new look
            
            # *respuesta* updates
            waitOnFlip = False
            
            # if respuesta is starting this frame...
            if respuesta.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                respuesta.frameNStart = frameN  # exact frame index
                respuesta.tStart = t  # local t and not account for scr refresh
                respuesta.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(respuesta, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'respuesta.started')
                # update status
                respuesta.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(respuesta.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(respuesta.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if respuesta.status == STARTED and not waitOnFlip:
                theseKeys = respuesta.getKeys(keyList=['1','2','3'], ignoreKeys=["escape"], waitRelease=False)
                _respuesta_allKeys.extend(theseKeys)
                if len(_respuesta_allKeys):
                    respuesta.keys = _respuesta_allKeys[-1].name  # just the last key pressed
                    respuesta.rt = _respuesta_allKeys[-1].rt
                    respuesta.duration = _respuesta_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial
        trial.tStop = globalClock.getTime(format='float')
        trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial.stopped', trial.tStop)
        task.addData('cam_inicio_viaje_roi.numLooks', cam_inicio_viaje_roi.numLooks)
        if cam_inicio_viaje_roi.numLooks:
           task.addData('cam_inicio_viaje_roi.timesOn', cam_inicio_viaje_roi.timesOn)
           task.addData('cam_inicio_viaje_roi.timesOff', cam_inicio_viaje_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           cam_inicio_viaje_roi.dwellTime = 0.0
           for i in range(len(cam_inicio_viaje_roi.timesOn)):
               cam_inicio_viaje_roi.dwellTime += cam_inicio_viaje_roi.timesOff[i] - cam_inicio_viaje_roi.timesOn[i]
           task.addData('cam_inicio_viaje_roi.dwellTime', cam_inicio_viaje_roi.dwellTime)
        else:
           task.addData('cam_inicio_viaje_roi.timesOn', "")
           task.addData('cam_inicio_viaje_roi.timesOff', "")
        task.addData('cam_travel_time_roi.numLooks', cam_travel_time_roi.numLooks)
        if cam_travel_time_roi.numLooks:
           task.addData('cam_travel_time_roi.timesOn', cam_travel_time_roi.timesOn)
           task.addData('cam_travel_time_roi.timesOff', cam_travel_time_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           cam_travel_time_roi.dwellTime = 0.0
           for i in range(len(cam_travel_time_roi.timesOn)):
               cam_travel_time_roi.dwellTime += cam_travel_time_roi.timesOff[i] - cam_travel_time_roi.timesOn[i]
           task.addData('cam_travel_time_roi.dwellTime', cam_travel_time_roi.dwellTime)
        else:
           task.addData('cam_travel_time_roi.timesOn', "")
           task.addData('cam_travel_time_roi.timesOff', "")
        task.addData('cam_cost_roi.numLooks', cam_cost_roi.numLooks)
        if cam_cost_roi.numLooks:
           task.addData('cam_cost_roi.timesOn', cam_cost_roi.timesOn)
           task.addData('cam_cost_roi.timesOff', cam_cost_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           cam_cost_roi.dwellTime = 0.0
           for i in range(len(cam_cost_roi.timesOn)):
               cam_cost_roi.dwellTime += cam_cost_roi.timesOff[i] - cam_cost_roi.timesOn[i]
           task.addData('cam_cost_roi.dwellTime', cam_cost_roi.dwellTime)
        else:
           task.addData('cam_cost_roi.timesOn', "")
           task.addData('cam_cost_roi.timesOff', "")
        task.addData('cam_dens_roi.numLooks', cam_dens_roi.numLooks)
        if cam_dens_roi.numLooks:
           task.addData('cam_dens_roi.timesOn', cam_dens_roi.timesOn)
           task.addData('cam_dens_roi.timesOff', cam_dens_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           cam_dens_roi.dwellTime = 0.0
           for i in range(len(cam_dens_roi.timesOn)):
               cam_dens_roi.dwellTime += cam_dens_roi.timesOff[i] - cam_dens_roi.timesOn[i]
           task.addData('cam_dens_roi.dwellTime', cam_dens_roi.dwellTime)
        else:
           task.addData('cam_dens_roi.timesOn', "")
           task.addData('cam_dens_roi.timesOff', "")
        task.addData('cam_sec_roi.numLooks', cam_sec_roi.numLooks)
        if cam_sec_roi.numLooks:
           task.addData('cam_sec_roi.timesOn', cam_sec_roi.timesOn)
           task.addData('cam_sec_roi.timesOff', cam_sec_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           cam_sec_roi.dwellTime = 0.0
           for i in range(len(cam_sec_roi.timesOn)):
               cam_sec_roi.dwellTime += cam_sec_roi.timesOff[i] - cam_sec_roi.timesOn[i]
           task.addData('cam_sec_roi.dwellTime', cam_sec_roi.dwellTime)
        else:
           task.addData('cam_sec_roi.timesOn', "")
           task.addData('cam_sec_roi.timesOff', "")
        task.addData('metro_inicio_viaje_roi.numLooks', metro_inicio_viaje_roi.numLooks)
        if metro_inicio_viaje_roi.numLooks:
           task.addData('metro_inicio_viaje_roi.timesOn', metro_inicio_viaje_roi.timesOn)
           task.addData('metro_inicio_viaje_roi.timesOff', metro_inicio_viaje_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           metro_inicio_viaje_roi.dwellTime = 0.0
           for i in range(len(metro_inicio_viaje_roi.timesOn)):
               metro_inicio_viaje_roi.dwellTime += metro_inicio_viaje_roi.timesOff[i] - metro_inicio_viaje_roi.timesOn[i]
           task.addData('metro_inicio_viaje_roi.dwellTime', metro_inicio_viaje_roi.dwellTime)
        else:
           task.addData('metro_inicio_viaje_roi.timesOn', "")
           task.addData('metro_inicio_viaje_roi.timesOff', "")
        task.addData('metro_travel_time_roi.numLooks', metro_travel_time_roi.numLooks)
        if metro_travel_time_roi.numLooks:
           task.addData('metro_travel_time_roi.timesOn', metro_travel_time_roi.timesOn)
           task.addData('metro_travel_time_roi.timesOff', metro_travel_time_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           metro_travel_time_roi.dwellTime = 0.0
           for i in range(len(metro_travel_time_roi.timesOn)):
               metro_travel_time_roi.dwellTime += metro_travel_time_roi.timesOff[i] - metro_travel_time_roi.timesOn[i]
           task.addData('metro_travel_time_roi.dwellTime', metro_travel_time_roi.dwellTime)
        else:
           task.addData('metro_travel_time_roi.timesOn', "")
           task.addData('metro_travel_time_roi.timesOff', "")
        task.addData('metro_cost_roi.numLooks', metro_cost_roi.numLooks)
        if metro_cost_roi.numLooks:
           task.addData('metro_cost_roi.timesOn', metro_cost_roi.timesOn)
           task.addData('metro_cost_roi.timesOff', metro_cost_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           metro_cost_roi.dwellTime = 0.0
           for i in range(len(metro_cost_roi.timesOn)):
               metro_cost_roi.dwellTime += metro_cost_roi.timesOff[i] - metro_cost_roi.timesOn[i]
           task.addData('metro_cost_roi.dwellTime', metro_cost_roi.dwellTime)
        else:
           task.addData('metro_cost_roi.timesOn', "")
           task.addData('metro_cost_roi.timesOff', "")
        task.addData('metro_dens_roi.numLooks', metro_dens_roi.numLooks)
        if metro_dens_roi.numLooks:
           task.addData('metro_dens_roi.timesOn', metro_dens_roi.timesOn)
           task.addData('metro_dens_roi.timesOff', metro_dens_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           metro_dens_roi.dwellTime = 0.0
           for i in range(len(metro_dens_roi.timesOn)):
               metro_dens_roi.dwellTime += metro_dens_roi.timesOff[i] - metro_dens_roi.timesOn[i]
           task.addData('metro_dens_roi.dwellTime', metro_dens_roi.dwellTime)
        else:
           task.addData('metro_dens_roi.timesOn', "")
           task.addData('metro_dens_roi.timesOff', "")
        task.addData('metro_users_roi.numLooks', metro_users_roi.numLooks)
        if metro_users_roi.numLooks:
           task.addData('metro_users_roi.timesOn', metro_users_roi.timesOn)
           task.addData('metro_users_roi.timesOff', metro_users_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           metro_users_roi.dwellTime = 0.0
           for i in range(len(metro_users_roi.timesOn)):
               metro_users_roi.dwellTime += metro_users_roi.timesOff[i] - metro_users_roi.timesOn[i]
           task.addData('metro_users_roi.dwellTime', metro_users_roi.dwellTime)
        else:
           task.addData('metro_users_roi.timesOn', "")
           task.addData('metro_users_roi.timesOff', "")
        task.addData('uber_inicio_viaje_roi.numLooks', uber_inicio_viaje_roi.numLooks)
        if uber_inicio_viaje_roi.numLooks:
           task.addData('uber_inicio_viaje_roi.timesOn', uber_inicio_viaje_roi.timesOn)
           task.addData('uber_inicio_viaje_roi.timesOff', uber_inicio_viaje_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           uber_inicio_viaje_roi.dwellTime = 0.0
           for i in range(len(uber_inicio_viaje_roi.timesOn)):
               uber_inicio_viaje_roi.dwellTime += uber_inicio_viaje_roi.timesOff[i] - uber_inicio_viaje_roi.timesOn[i]
           task.addData('uber_inicio_viaje_roi.dwellTime', uber_inicio_viaje_roi.dwellTime)
        else:
           task.addData('uber_inicio_viaje_roi.timesOn', "")
           task.addData('uber_inicio_viaje_roi.timesOff', "")
        task.addData('uber_travel_time_roi.numLooks', uber_travel_time_roi.numLooks)
        if uber_travel_time_roi.numLooks:
           task.addData('uber_travel_time_roi.timesOn', uber_travel_time_roi.timesOn)
           task.addData('uber_travel_time_roi.timesOff', uber_travel_time_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           uber_travel_time_roi.dwellTime = 0.0
           for i in range(len(uber_travel_time_roi.timesOn)):
               uber_travel_time_roi.dwellTime += uber_travel_time_roi.timesOff[i] - uber_travel_time_roi.timesOn[i]
           task.addData('uber_travel_time_roi.dwellTime', uber_travel_time_roi.dwellTime)
        else:
           task.addData('uber_travel_time_roi.timesOn', "")
           task.addData('uber_travel_time_roi.timesOff', "")
        task.addData('uber_cost_roi.numLooks', uber_cost_roi.numLooks)
        if uber_cost_roi.numLooks:
           task.addData('uber_cost_roi.timesOn', uber_cost_roi.timesOn)
           task.addData('uber_cost_roi.timesOff', uber_cost_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           uber_cost_roi.dwellTime = 0.0
           for i in range(len(uber_cost_roi.timesOn)):
               uber_cost_roi.dwellTime += uber_cost_roi.timesOff[i] - uber_cost_roi.timesOn[i]
           task.addData('uber_cost_roi.dwellTime', uber_cost_roi.dwellTime)
        else:
           task.addData('uber_cost_roi.timesOn', "")
           task.addData('uber_cost_roi.timesOff', "")
        task.addData('uber_stars_roi.numLooks', uber_stars_roi.numLooks)
        if uber_stars_roi.numLooks:
           task.addData('uber_stars_roi.timesOn', uber_stars_roi.timesOn)
           task.addData('uber_stars_roi.timesOff', uber_stars_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           uber_stars_roi.dwellTime = 0.0
           for i in range(len(uber_stars_roi.timesOn)):
               uber_stars_roi.dwellTime += uber_stars_roi.timesOff[i] - uber_stars_roi.timesOn[i]
           task.addData('uber_stars_roi.dwellTime', uber_stars_roi.dwellTime)
        else:
           task.addData('uber_stars_roi.timesOn', "")
           task.addData('uber_stars_roi.timesOff', "")
        task.addData('uber_gender_roi.numLooks', uber_gender_roi.numLooks)
        if uber_gender_roi.numLooks:
           task.addData('uber_gender_roi.timesOn', uber_gender_roi.timesOn)
           task.addData('uber_gender_roi.timesOff', uber_gender_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           uber_gender_roi.dwellTime = 0.0
           for i in range(len(uber_gender_roi.timesOn)):
               uber_gender_roi.dwellTime += uber_gender_roi.timesOff[i] - uber_gender_roi.timesOn[i]
           task.addData('uber_gender_roi.dwellTime', uber_gender_roi.dwellTime)
        else:
           task.addData('uber_gender_roi.timesOn', "")
           task.addData('uber_gender_roi.timesOff', "")
        task.addData('uber_record_roi.numLooks', uber_record_roi.numLooks)
        if uber_record_roi.numLooks:
           task.addData('uber_record_roi.timesOn', uber_record_roi.timesOn)
           task.addData('uber_record_roi.timesOff', uber_record_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           uber_record_roi.dwellTime = 0.0
           for i in range(len(uber_record_roi.timesOn)):
               uber_record_roi.dwellTime += uber_record_roi.timesOff[i] - uber_record_roi.timesOn[i]
           task.addData('uber_record_roi.dwellTime', uber_record_roi.dwellTime)
        else:
           task.addData('uber_record_roi.timesOn', "")
           task.addData('uber_record_roi.timesOff', "")
        # check responses
        if respuesta.keys in ['', [], None]:  # No response was made
            respuesta.keys = None
        task.addData('respuesta.keys',respuesta.keys)
        if respuesta.keys != None:  # we had a response
            task.addData('respuesta.rt', respuesta.rt)
            task.addData('respuesta.duration', respuesta.duration)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTask as finished
        if hasattr(thisTask, 'status'):
            thisTask.status = FINISHED
        # if awaiting a pause, pause now
        if task.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            task.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'task'
    task.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
