#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on noviembre 24, 2025, at 18:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2025.1.1')


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
from psychopy.hardware.eyetracker import EyetrackerControl

# Run 'Before Experiment' code from code
block_number = 1



# x_coords representa las columnas (2 datos)
x_coords = [
    -0.3135416667, 
    0.5625
]

# y_coords representa las filas (6 datos)
y_coords = [
    0.537037037, 
    0.3148148148, 
    0.09259259259, 
    -0.1296296296, 
    -0.3518518519, 
    -0.5740740741
]

# 2. Crear la matriz anidada usando la lista de comprensión que indicaste
# La estructura resultante es: una lista de 2 listas (columnas), 
# donde cada lista interna contiene 6 tuplas (x, y).
positions = [[(x, y) for y in y_coords] for x in x_coords]

position_time_box = [0.65625,-0.8944444444]

box_size = [0.2776041667,0.1101851852]
time_box_size = [0.234375,0.06018518519]


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
expName = 'v7'  # from the Builder filename that created this script
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
_winSize = [1920, 1080]
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
        originPath='C:\\Users\\CI6316 - Grupo 1\\Desktop\\2025-CI6316\\Experiment\\v7_lastrun.py',
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
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowGUI=True, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'norm'
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
    # enter 'rush' mode (raise CPU priority)
    if not PILOTING:
        core.rush(enable=True)
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
    block_number = 1
    
    
    
    # x_coords representa las columnas (2 datos)
    x_coords = [
        -0.3135416667, 
        0.5625
    ]
    
    # y_coords representa las filas (6 datos)
    y_coords = [
        0.537037037, 
        0.3148148148, 
        0.09259259259, 
        -0.1296296296, 
        -0.3518518519, 
        -0.5740740741
    ]
    
    # 2. Crear la matriz anidada usando la lista de comprensión que indicaste
    # La estructura resultante es: una lista de 2 listas (columnas), 
    # donde cada lista interna contiene 6 tuplas (x, y).
    positions = [[(x, y) for y in y_coords] for x in x_coords]
    
    position_time_box = [0.65625,-0.8944444444]
    
    box_size = [0.2776041667,0.1101851852]
    time_box_size = [0.234375,0.06018518519]
    
    
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
        image='fondo_actualizado.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    hora_inicio_viaje_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=position_time_box, draggable=False, units='norm',     letterHeight=0.05,
         size=time_box_size, borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='hora_inicio_viaje_text',
         depth=-2, autoLog=True,
    )
    metro_cost_text = visual.TextBox2(
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
         name='metro_cost_text',
         depth=-3, autoLog=True,
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
         depth=-4, autoLog=True,
    )
    metro_users_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[1][2]], draggable=False, units='norm',     letterHeight=0.04,
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
         depth=-5, autoLog=True,
    )
    metro_camaras_text = visual.TextBox2(
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
         name='metro_camaras_text',
         depth=-6, autoLog=True,
    )
    metro_guardias_text = visual.TextBox2(
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
         name='metro_guardias_text',
         depth=-7, autoLog=True,
    )
    metro_tech_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[1][5]], draggable=False, units='norm',     letterHeight=0.05,
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
         name='metro_tech_text',
         depth=-8, autoLog=True,
    )
    uber_cost_text = visual.TextBox2(
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
         name='uber_cost_text',
         depth=-9, autoLog=True,
    )
    uber_travel_time_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][1]], draggable=False, units='norm',     letterHeight=0.05,
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
         depth=-10, autoLog=True,
    )
    uber_driver_gender_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][2]], draggable=False, units='norm',     letterHeight=0.05,
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
         name='uber_driver_gender_text',
         depth=-11, autoLog=True,
    )
    uber_record_text = visual.TextBox2(
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
         name='uber_record_text',
         depth=-12, autoLog=True,
    )
    uber_stars_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][4]], draggable=False, units='norm',     letterHeight=0.05,
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
         depth=-13, autoLog=True,
    )
    uber_travels_text = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=[positions[0][5]], draggable=False, units='norm',     letterHeight=0.05,
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
         name='uber_travels_text',
         depth=-14, autoLog=True,
    )
    hora_inicio_viaje_roi = visual.ROI(win, name='hora_inicio_viaje_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=position_time_box, size=box_size, 
        anchor='center', ori=0.0, depth=-15
        )
    metro_cost_roi = visual.ROI(win, name='metro_cost_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][0]], size=box_size, 
        anchor='center', ori=0.0, depth=-16
        )
    metro_travel_time_roi = visual.ROI(win, name='metro_travel_time_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][1]], size=box_size, 
        anchor='center', ori=0.0, depth=-17
        )
    metro_users_roi = visual.ROI(win, name='metro_users_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][2]], size=box_size, 
        anchor='center', ori=0.0, depth=-18
        )
    metro_camaras_roi = visual.ROI(win, name='metro_camaras_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][3]], size=box_size, 
        anchor='center', ori=0.0, depth=-19
        )
    metro_guardias_roi = visual.ROI(win, name='metro_guardias_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][4]], size=box_size, 
        anchor='center', ori=0.0, depth=-20
        )
    metro_tech_roi = visual.ROI(win, name='metro_tech_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[1][5]], size=box_size, 
        anchor='center', ori=0.0, depth=-21
        )
    uber_cost_roi = visual.ROI(win, name='uber_cost_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][0]], size=box_size, 
        anchor='center', ori=0.0, depth=-22
        )
    uber_travel_time_roi = visual.ROI(win, name='uber_travel_time_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][1]], size=box_size, 
        anchor='center', ori=0.0, depth=-23
        )
    uber_driver_gender_roi = visual.ROI(win, name='uber_driver_gender_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][2]], size=box_size, 
        anchor='center', ori=0.0, depth=-24
        )
    uber_record_roi = visual.ROI(win, name='uber_record_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][3]], size=box_size, 
        anchor='center', ori=0.0, depth=-25
        )
    uber_stars_roi = visual.ROI(win, name='uber_stars_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][4]], size=box_size, 
        anchor='center', ori=0.0, depth=-26
        )
    uber_travels_roi = visual.ROI(win, name='uber_travels_roi', device=eyetracker,
        debug=False,
        shape='rectangle',
        pos=[positions[0][5]], size=box_size, 
        anchor='center', ori=0.0, depth=-27
        )
    respuesta = keyboard.Keyboard(deviceName='respuesta')
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    etRecord = EyetrackerControl(
        tracker=eyetracker,
        actionType='Start Only'
    )
    
    # --- Initialize components for Routine "end" ---
    etRecord_2 = EyetrackerControl(
        tracker=eyetracker,
        actionType='Stop Only'
    )
    
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
            components=[fondo, hora_inicio_viaje_text, metro_cost_text, metro_travel_time_text, metro_users_text, metro_camaras_text, metro_guardias_text, metro_tech_text, uber_cost_text, uber_travel_time_text, uber_driver_gender_text, uber_record_text, uber_stars_text, uber_travels_text, hora_inicio_viaje_roi, metro_cost_roi, metro_travel_time_roi, metro_users_roi, metro_camaras_roi, metro_guardias_roi, metro_tech_roi, uber_cost_roi, uber_travel_time_roi, uber_driver_gender_roi, uber_record_roi, uber_stars_roi, uber_travels_roi, respuesta, mouse, etRecord],
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
        
        hora_inicio_viaje_text.reset()
        hora_inicio_viaje_text.setText(hora)
        metro_cost_text.reset()
        metro_cost_text.setText(metro_cost)
        metro_travel_time_text.reset()
        metro_travel_time_text.setText(metro_travel_time)
        metro_users_text.reset()
        metro_users_text.setText(metro_users)
        metro_camaras_text.reset()
        metro_camaras_text.setText(metro_camaras)
        metro_guardias_text.reset()
        metro_guardias_text.setText(metro_guardias)
        metro_tech_text.reset()
        metro_tech_text.setText(metro_tech)
        uber_cost_text.reset()
        uber_cost_text.setText(uber_cost)
        uber_travel_time_text.reset()
        uber_travel_time_text.setText(uber_travel_time)
        uber_driver_gender_text.reset()
        uber_driver_gender_text.setText(uber_driver_gender)
        uber_record_text.reset()
        uber_record_text.setText(uber_record)
        uber_stars_text.reset()
        uber_stars_text.setText(uber_stars)
        uber_travels_text.reset()
        uber_travels_text.setText(uber_travels)
        # clear any previous roi data
        hora_inicio_viaje_roi.reset()
        # clear any previous roi data
        metro_cost_roi.reset()
        # clear any previous roi data
        metro_travel_time_roi.reset()
        # clear any previous roi data
        metro_users_roi.reset()
        # clear any previous roi data
        metro_camaras_roi.reset()
        # clear any previous roi data
        metro_guardias_roi.reset()
        # clear any previous roi data
        metro_tech_roi.reset()
        # clear any previous roi data
        uber_cost_roi.reset()
        # clear any previous roi data
        uber_travel_time_roi.reset()
        # clear any previous roi data
        uber_driver_gender_roi.reset()
        # clear any previous roi data
        uber_record_roi.reset()
        # clear any previous roi data
        uber_stars_roi.reset()
        # clear any previous roi data
        uber_travels_roi.reset()
        # create starting attributes for respuesta
        respuesta.keys = []
        respuesta.rt = []
        _respuesta_allKeys = []
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        gotValidClick = False  # until a click is received
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
            
            # *hora_inicio_viaje_text* updates
            
            # if hora_inicio_viaje_text is starting this frame...
            if hora_inicio_viaje_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hora_inicio_viaje_text.frameNStart = frameN  # exact frame index
                hora_inicio_viaje_text.tStart = t  # local t and not account for scr refresh
                hora_inicio_viaje_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hora_inicio_viaje_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'hora_inicio_viaje_text.started')
                # update status
                hora_inicio_viaje_text.status = STARTED
                hora_inicio_viaje_text.setAutoDraw(True)
            
            # if hora_inicio_viaje_text is active this frame...
            if hora_inicio_viaje_text.status == STARTED:
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
            
            # *metro_camaras_text* updates
            
            # if metro_camaras_text is starting this frame...
            if metro_camaras_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_camaras_text.frameNStart = frameN  # exact frame index
                metro_camaras_text.tStart = t  # local t and not account for scr refresh
                metro_camaras_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_camaras_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_camaras_text.started')
                # update status
                metro_camaras_text.status = STARTED
                metro_camaras_text.setAutoDraw(True)
            
            # if metro_camaras_text is active this frame...
            if metro_camaras_text.status == STARTED:
                # update params
                pass
            
            # *metro_guardias_text* updates
            
            # if metro_guardias_text is starting this frame...
            if metro_guardias_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_guardias_text.frameNStart = frameN  # exact frame index
                metro_guardias_text.tStart = t  # local t and not account for scr refresh
                metro_guardias_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_guardias_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_guardias_text.started')
                # update status
                metro_guardias_text.status = STARTED
                metro_guardias_text.setAutoDraw(True)
            
            # if metro_guardias_text is active this frame...
            if metro_guardias_text.status == STARTED:
                # update params
                pass
            
            # *metro_tech_text* updates
            
            # if metro_tech_text is starting this frame...
            if metro_tech_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_tech_text.frameNStart = frameN  # exact frame index
                metro_tech_text.tStart = t  # local t and not account for scr refresh
                metro_tech_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_tech_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_tech_text.started')
                # update status
                metro_tech_text.status = STARTED
                metro_tech_text.setAutoDraw(True)
            
            # if metro_tech_text is active this frame...
            if metro_tech_text.status == STARTED:
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
            
            # *uber_driver_gender_text* updates
            
            # if uber_driver_gender_text is starting this frame...
            if uber_driver_gender_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_driver_gender_text.frameNStart = frameN  # exact frame index
                uber_driver_gender_text.tStart = t  # local t and not account for scr refresh
                uber_driver_gender_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_driver_gender_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_driver_gender_text.started')
                # update status
                uber_driver_gender_text.status = STARTED
                uber_driver_gender_text.setAutoDraw(True)
            
            # if uber_driver_gender_text is active this frame...
            if uber_driver_gender_text.status == STARTED:
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
            
            # *uber_travels_text* updates
            
            # if uber_travels_text is starting this frame...
            if uber_travels_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_travels_text.frameNStart = frameN  # exact frame index
                uber_travels_text.tStart = t  # local t and not account for scr refresh
                uber_travels_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_travels_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_travels_text.started')
                # update status
                uber_travels_text.status = STARTED
                uber_travels_text.setAutoDraw(True)
            
            # if uber_travels_text is active this frame...
            if uber_travels_text.status == STARTED:
                # update params
                pass
            
            # if hora_inicio_viaje_roi is starting this frame...
            if hora_inicio_viaje_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                hora_inicio_viaje_roi.frameNStart = frameN  # exact frame index
                hora_inicio_viaje_roi.tStart = t  # local t and not account for scr refresh
                hora_inicio_viaje_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hora_inicio_viaje_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'hora_inicio_viaje_roi.started')
                # update status
                hora_inicio_viaje_roi.status = STARTED
                hora_inicio_viaje_roi.setAutoDraw(True)
            
            # if hora_inicio_viaje_roi is active this frame...
            if hora_inicio_viaje_roi.status == STARTED:
                # update params
                pass
                # check whether hora_inicio_viaje_roi has been looked in
                if hora_inicio_viaje_roi.isLookedIn:
                    if not hora_inicio_viaje_roi.wasLookedIn:
                        hora_inicio_viaje_roi.timesOn.append(hora_inicio_viaje_roi.clock.getTime()) # store time of first look
                        hora_inicio_viaje_roi.timesOff.append(hora_inicio_viaje_roi.clock.getTime()) # store time looked until
                    else:
                        hora_inicio_viaje_roi.timesOff[-1] = hora_inicio_viaje_roi.clock.getTime() # update time looked until
                    hora_inicio_viaje_roi.wasLookedIn = True  # if hora_inicio_viaje_roi is still looked at next frame, it is not a new look
                else:
                    if hora_inicio_viaje_roi.wasLookedIn:
                        hora_inicio_viaje_roi.timesOff[-1] = hora_inicio_viaje_roi.clock.getTime() # update time looked until
                    hora_inicio_viaje_roi.wasLookedIn = False  # if hora_inicio_viaje_roi is looked at next frame, it is a new look
            else:
                hora_inicio_viaje_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                hora_inicio_viaje_roi.wasLookedIn = False  # if hora_inicio_viaje_roi is looked at next frame, it is a new look
            
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
            
            # if metro_camaras_roi is starting this frame...
            if metro_camaras_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_camaras_roi.frameNStart = frameN  # exact frame index
                metro_camaras_roi.tStart = t  # local t and not account for scr refresh
                metro_camaras_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_camaras_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_camaras_roi.started')
                # update status
                metro_camaras_roi.status = STARTED
                metro_camaras_roi.setAutoDraw(True)
            
            # if metro_camaras_roi is active this frame...
            if metro_camaras_roi.status == STARTED:
                # update params
                pass
                # check whether metro_camaras_roi has been looked in
                if metro_camaras_roi.isLookedIn:
                    if not metro_camaras_roi.wasLookedIn:
                        metro_camaras_roi.timesOn.append(metro_camaras_roi.clock.getTime()) # store time of first look
                        metro_camaras_roi.timesOff.append(metro_camaras_roi.clock.getTime()) # store time looked until
                    else:
                        metro_camaras_roi.timesOff[-1] = metro_camaras_roi.clock.getTime() # update time looked until
                    metro_camaras_roi.wasLookedIn = True  # if metro_camaras_roi is still looked at next frame, it is not a new look
                else:
                    if metro_camaras_roi.wasLookedIn:
                        metro_camaras_roi.timesOff[-1] = metro_camaras_roi.clock.getTime() # update time looked until
                    metro_camaras_roi.wasLookedIn = False  # if metro_camaras_roi is looked at next frame, it is a new look
            else:
                metro_camaras_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                metro_camaras_roi.wasLookedIn = False  # if metro_camaras_roi is looked at next frame, it is a new look
            
            # if metro_guardias_roi is starting this frame...
            if metro_guardias_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_guardias_roi.frameNStart = frameN  # exact frame index
                metro_guardias_roi.tStart = t  # local t and not account for scr refresh
                metro_guardias_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_guardias_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_guardias_roi.started')
                # update status
                metro_guardias_roi.status = STARTED
                metro_guardias_roi.setAutoDraw(True)
            
            # if metro_guardias_roi is active this frame...
            if metro_guardias_roi.status == STARTED:
                # update params
                pass
                # check whether metro_guardias_roi has been looked in
                if metro_guardias_roi.isLookedIn:
                    if not metro_guardias_roi.wasLookedIn:
                        metro_guardias_roi.timesOn.append(metro_guardias_roi.clock.getTime()) # store time of first look
                        metro_guardias_roi.timesOff.append(metro_guardias_roi.clock.getTime()) # store time looked until
                    else:
                        metro_guardias_roi.timesOff[-1] = metro_guardias_roi.clock.getTime() # update time looked until
                    metro_guardias_roi.wasLookedIn = True  # if metro_guardias_roi is still looked at next frame, it is not a new look
                else:
                    if metro_guardias_roi.wasLookedIn:
                        metro_guardias_roi.timesOff[-1] = metro_guardias_roi.clock.getTime() # update time looked until
                    metro_guardias_roi.wasLookedIn = False  # if metro_guardias_roi is looked at next frame, it is a new look
            else:
                metro_guardias_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                metro_guardias_roi.wasLookedIn = False  # if metro_guardias_roi is looked at next frame, it is a new look
            
            # if metro_tech_roi is starting this frame...
            if metro_tech_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                metro_tech_roi.frameNStart = frameN  # exact frame index
                metro_tech_roi.tStart = t  # local t and not account for scr refresh
                metro_tech_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(metro_tech_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'metro_tech_roi.started')
                # update status
                metro_tech_roi.status = STARTED
                metro_tech_roi.setAutoDraw(True)
            
            # if metro_tech_roi is active this frame...
            if metro_tech_roi.status == STARTED:
                # update params
                pass
                # check whether metro_tech_roi has been looked in
                if metro_tech_roi.isLookedIn:
                    if not metro_tech_roi.wasLookedIn:
                        metro_tech_roi.timesOn.append(metro_tech_roi.clock.getTime()) # store time of first look
                        metro_tech_roi.timesOff.append(metro_tech_roi.clock.getTime()) # store time looked until
                    else:
                        metro_tech_roi.timesOff[-1] = metro_tech_roi.clock.getTime() # update time looked until
                    metro_tech_roi.wasLookedIn = True  # if metro_tech_roi is still looked at next frame, it is not a new look
                else:
                    if metro_tech_roi.wasLookedIn:
                        metro_tech_roi.timesOff[-1] = metro_tech_roi.clock.getTime() # update time looked until
                    metro_tech_roi.wasLookedIn = False  # if metro_tech_roi is looked at next frame, it is a new look
            else:
                metro_tech_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                metro_tech_roi.wasLookedIn = False  # if metro_tech_roi is looked at next frame, it is a new look
            
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
            
            # if uber_driver_gender_roi is starting this frame...
            if uber_driver_gender_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_driver_gender_roi.frameNStart = frameN  # exact frame index
                uber_driver_gender_roi.tStart = t  # local t and not account for scr refresh
                uber_driver_gender_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_driver_gender_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_driver_gender_roi.started')
                # update status
                uber_driver_gender_roi.status = STARTED
                uber_driver_gender_roi.setAutoDraw(True)
            
            # if uber_driver_gender_roi is active this frame...
            if uber_driver_gender_roi.status == STARTED:
                # update params
                pass
                # check whether uber_driver_gender_roi has been looked in
                if uber_driver_gender_roi.isLookedIn:
                    if not uber_driver_gender_roi.wasLookedIn:
                        uber_driver_gender_roi.timesOn.append(uber_driver_gender_roi.clock.getTime()) # store time of first look
                        uber_driver_gender_roi.timesOff.append(uber_driver_gender_roi.clock.getTime()) # store time looked until
                    else:
                        uber_driver_gender_roi.timesOff[-1] = uber_driver_gender_roi.clock.getTime() # update time looked until
                    uber_driver_gender_roi.wasLookedIn = True  # if uber_driver_gender_roi is still looked at next frame, it is not a new look
                else:
                    if uber_driver_gender_roi.wasLookedIn:
                        uber_driver_gender_roi.timesOff[-1] = uber_driver_gender_roi.clock.getTime() # update time looked until
                    uber_driver_gender_roi.wasLookedIn = False  # if uber_driver_gender_roi is looked at next frame, it is a new look
            else:
                uber_driver_gender_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                uber_driver_gender_roi.wasLookedIn = False  # if uber_driver_gender_roi is looked at next frame, it is a new look
            
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
            
            # if uber_travels_roi is starting this frame...
            if uber_travels_roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                uber_travels_roi.frameNStart = frameN  # exact frame index
                uber_travels_roi.tStart = t  # local t and not account for scr refresh
                uber_travels_roi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(uber_travels_roi, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'uber_travels_roi.started')
                # update status
                uber_travels_roi.status = STARTED
                uber_travels_roi.setAutoDraw(True)
            
            # if uber_travels_roi is active this frame...
            if uber_travels_roi.status == STARTED:
                # update params
                pass
                # check whether uber_travels_roi has been looked in
                if uber_travels_roi.isLookedIn:
                    if not uber_travels_roi.wasLookedIn:
                        uber_travels_roi.timesOn.append(uber_travels_roi.clock.getTime()) # store time of first look
                        uber_travels_roi.timesOff.append(uber_travels_roi.clock.getTime()) # store time looked until
                    else:
                        uber_travels_roi.timesOff[-1] = uber_travels_roi.clock.getTime() # update time looked until
                    uber_travels_roi.wasLookedIn = True  # if uber_travels_roi is still looked at next frame, it is not a new look
                else:
                    if uber_travels_roi.wasLookedIn:
                        uber_travels_roi.timesOff[-1] = uber_travels_roi.clock.getTime() # update time looked until
                    uber_travels_roi.wasLookedIn = False  # if uber_travels_roi is looked at next frame, it is a new look
            else:
                uber_travels_roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
                uber_travels_roi.wasLookedIn = False  # if uber_travels_roi is looked at next frame, it is a new look
            
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
                theseKeys = respuesta.getKeys(keyList=['a','b'], ignoreKeys=["escape"], waitRelease=False)
                _respuesta_allKeys.extend(theseKeys)
                if len(_respuesta_allKeys):
                    respuesta.keys = _respuesta_allKeys[-1].name  # just the last key pressed
                    respuesta.rt = _respuesta_allKeys[-1].rt
                    respuesta.duration = _respuesta_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            
            # *etRecord* updates
            
            # if etRecord is starting this frame...
            if etRecord.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                etRecord.frameNStart = frameN  # exact frame index
                etRecord.tStart = t  # local t and not account for scr refresh
                etRecord.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('etRecord.started', t)
                # update status
                etRecord.status = STARTED
                etRecord.start()
            if etRecord.status == STARTED:
                etRecord.tStop = t  # not accounting for scr refresh
                etRecord.tStopRefresh = tThisFlipGlobal  # on global time
                etRecord.frameNStop = frameN  # exact frame index
                etRecord.status = FINISHED
            
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
        task.addData('hora_inicio_viaje_roi.numLooks', hora_inicio_viaje_roi.numLooks)
        if hora_inicio_viaje_roi.numLooks:
           task.addData('hora_inicio_viaje_roi.timesOn', hora_inicio_viaje_roi.timesOn)
           task.addData('hora_inicio_viaje_roi.timesOff', hora_inicio_viaje_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           hora_inicio_viaje_roi.dwellTime = 0.0
           for i in range(len(hora_inicio_viaje_roi.timesOn)):
               hora_inicio_viaje_roi.dwellTime += hora_inicio_viaje_roi.timesOff[i] - hora_inicio_viaje_roi.timesOn[i]
           task.addData('hora_inicio_viaje_roi.dwellTime', hora_inicio_viaje_roi.dwellTime)
        else:
           task.addData('hora_inicio_viaje_roi.timesOn', "")
           task.addData('hora_inicio_viaje_roi.timesOff', "")
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
        task.addData('metro_camaras_roi.numLooks', metro_camaras_roi.numLooks)
        if metro_camaras_roi.numLooks:
           task.addData('metro_camaras_roi.timesOn', metro_camaras_roi.timesOn)
           task.addData('metro_camaras_roi.timesOff', metro_camaras_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           metro_camaras_roi.dwellTime = 0.0
           for i in range(len(metro_camaras_roi.timesOn)):
               metro_camaras_roi.dwellTime += metro_camaras_roi.timesOff[i] - metro_camaras_roi.timesOn[i]
           task.addData('metro_camaras_roi.dwellTime', metro_camaras_roi.dwellTime)
        else:
           task.addData('metro_camaras_roi.timesOn', "")
           task.addData('metro_camaras_roi.timesOff', "")
        task.addData('metro_guardias_roi.numLooks', metro_guardias_roi.numLooks)
        if metro_guardias_roi.numLooks:
           task.addData('metro_guardias_roi.timesOn', metro_guardias_roi.timesOn)
           task.addData('metro_guardias_roi.timesOff', metro_guardias_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           metro_guardias_roi.dwellTime = 0.0
           for i in range(len(metro_guardias_roi.timesOn)):
               metro_guardias_roi.dwellTime += metro_guardias_roi.timesOff[i] - metro_guardias_roi.timesOn[i]
           task.addData('metro_guardias_roi.dwellTime', metro_guardias_roi.dwellTime)
        else:
           task.addData('metro_guardias_roi.timesOn', "")
           task.addData('metro_guardias_roi.timesOff', "")
        task.addData('metro_tech_roi.numLooks', metro_tech_roi.numLooks)
        if metro_tech_roi.numLooks:
           task.addData('metro_tech_roi.timesOn', metro_tech_roi.timesOn)
           task.addData('metro_tech_roi.timesOff', metro_tech_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           metro_tech_roi.dwellTime = 0.0
           for i in range(len(metro_tech_roi.timesOn)):
               metro_tech_roi.dwellTime += metro_tech_roi.timesOff[i] - metro_tech_roi.timesOn[i]
           task.addData('metro_tech_roi.dwellTime', metro_tech_roi.dwellTime)
        else:
           task.addData('metro_tech_roi.timesOn', "")
           task.addData('metro_tech_roi.timesOff', "")
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
        task.addData('uber_driver_gender_roi.numLooks', uber_driver_gender_roi.numLooks)
        if uber_driver_gender_roi.numLooks:
           task.addData('uber_driver_gender_roi.timesOn', uber_driver_gender_roi.timesOn)
           task.addData('uber_driver_gender_roi.timesOff', uber_driver_gender_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           uber_driver_gender_roi.dwellTime = 0.0
           for i in range(len(uber_driver_gender_roi.timesOn)):
               uber_driver_gender_roi.dwellTime += uber_driver_gender_roi.timesOff[i] - uber_driver_gender_roi.timesOn[i]
           task.addData('uber_driver_gender_roi.dwellTime', uber_driver_gender_roi.dwellTime)
        else:
           task.addData('uber_driver_gender_roi.timesOn', "")
           task.addData('uber_driver_gender_roi.timesOff', "")
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
        task.addData('uber_travels_roi.numLooks', uber_travels_roi.numLooks)
        if uber_travels_roi.numLooks:
           task.addData('uber_travels_roi.timesOn', uber_travels_roi.timesOn)
           task.addData('uber_travels_roi.timesOff', uber_travels_roi.timesOff)
           # calculate and store dwell times i.e. the duration between look onsets and offsets
           uber_travels_roi.dwellTime = 0.0
           for i in range(len(uber_travels_roi.timesOn)):
               uber_travels_roi.dwellTime += uber_travels_roi.timesOff[i] - uber_travels_roi.timesOn[i]
           task.addData('uber_travels_roi.dwellTime', uber_travels_roi.dwellTime)
        else:
           task.addData('uber_travels_roi.timesOn', "")
           task.addData('uber_travels_roi.timesOff', "")
        # check responses
        if respuesta.keys in ['', [], None]:  # No response was made
            respuesta.keys = None
        task.addData('respuesta.keys',respuesta.keys)
        if respuesta.keys != None:  # we had a response
            task.addData('respuesta.rt', respuesta.rt)
            task.addData('respuesta.duration', respuesta.duration)
        # store data for task (TrialHandler)
        task.addData('mouse.x', mouse.x)
        task.addData('mouse.y', mouse.y)
        task.addData('mouse.leftButton', mouse.leftButton)
        task.addData('mouse.midButton', mouse.midButton)
        task.addData('mouse.rightButton', mouse.rightButton)
        task.addData('mouse.time', mouse.time)
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
    
    # --- Prepare to start Routine "end" ---
    # create an object to store info about Routine end
    end = data.Routine(
        name='end',
        components=[etRecord_2],
    )
    end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end
    end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end.tStart = globalClock.getTime(format='float')
    end.status = STARTED
    thisExp.addData('end.started', end.tStart)
    end.maxDuration = None
    # keep track of which components have finished
    endComponents = end.components
    for thisComponent in end.components:
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
    
    # --- Run Routine "end" ---
    end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *etRecord_2* updates
        if etRecord_2.status == NOT_STARTED:
            etRecord_2.frameNStart = frameN  # exact frame index
            etRecord_2.tStart = t  # local t and not account for scr refresh
            etRecord_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_2, 'tStartRefresh')  # time at next scr refresh
            etRecord_2.status = STARTED
        
        # if etRecord_2 is stopping this frame...
        if etRecord_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_2.tStartRefresh + 0-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_2.tStop = t  # not accounting for scr refresh
                etRecord_2.tStopRefresh = tThisFlipGlobal  # on global time
                etRecord_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_2.stopped', t)
                # update status
                etRecord_2.status = FINISHED
                etRecord_2.stop()
        
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
                currentRoutine=end,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end
    end.tStop = globalClock.getTime(format='float')
    end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end.stopped', end.tStop)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)
    # end 'rush' mode
    core.rush(enable=False)


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
