/*********** 
 * V1 *
 ***********/


// store info about the experiment session:
let expName = 'v1';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'pix',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(trialRoutineBegin());
flowScheduler.add(trialRoutineEachFrame());
flowScheduler.add(trialRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'fondo_eleccion.png', 'path': 'fondo_eleccion.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var trialClock;
var fondo_eleccion;
var caja_1_uber;
var caja_1_metro;
var caja_1_caminata;
var textbox_1_metro;
var textbox_2_metro;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  fondo_eleccion = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fondo_eleccion', units : 'norm', 
    image : 'fondo_eleccion.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.0, 0.0], 
    draggable: false,
    size : [2.0, 2.0],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  caja_1_uber = new visual.Rect ({
    win: psychoJS.window, name: 'caja_1_uber', units : 'norm', 
    width: [0.08854166667, 0.09259259259][0], height: [0.08854166667, 0.09259259259][1],
    ori: 0.0, 
    pos: [(- 0.40850694444277774), (- 0.3143518518505556)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  caja_1_metro = new visual.ShapeStim ({
    win: psychoJS.window, name: 'caja_1_metro', 
    vertices: [[-[0.16805555555555557, 0.1361111111111111][0]/2.0, -[0.16805555555555557, 0.1361111111111111][1]/2.0], [+[0.16805555555555557, 0.1361111111111111][0]/2.0, -[0.16805555555555557, 0.1361111111111111][1]/2.0], [0, [0.16805555555555557, 0.1361111111111111][1]/2.0]],
    ori: 0.0, 
    pos: [0.08541666666666668, 0.33055555555555555], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  caja_1_caminata = new visual.ShapeStim ({
    win: psychoJS.window, name: 'caja_1_caminata', 
    vertices: [[-[0.1597222222222222, 0.1111111111111111][0]/2.0, -[0.1597222222222222, 0.1111111111111111][1]/2.0], [+[0.1597222222222222, 0.1111111111111111][0]/2.0, -[0.1597222222222222, 0.1111111111111111][1]/2.0], [0, [0.1597222222222222, 0.1111111111111111][1]/2.0]],
    ori: 0.0, 
    pos: [0.08402777777777777, 0.11805555555555555], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -3, 
    interpolate: true, 
  });
  
  textbox_1_metro = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_1_metro',
    text: '9:00 am',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.5645833333333333, 0.33194444444444443], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.1763888888888889, 0.125],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  textbox_2_metro = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_2_metro',
    text: '10 min',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0.5673611111111111, 0.12013888888888889], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.17083333333333334, 0.12361111111111112],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var trialMaxDurationReached;
var trialMaxDuration;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialClock.reset();
    routineTimer.reset();
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(fondo_eleccion);
    trialComponents.push(caja_1_uber);
    trialComponents.push(caja_1_metro);
    trialComponents.push(caja_1_caminata);
    trialComponents.push(textbox_1_metro);
    trialComponents.push(textbox_2_metro);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fondo_eleccion* updates
    if (t >= 0.0 && fondo_eleccion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fondo_eleccion.tStart = t;  // (not accounting for frame time here)
      fondo_eleccion.frameNStart = frameN;  // exact frame index
      
      fondo_eleccion.setAutoDraw(true);
    }
    
    
    // if fondo_eleccion is active this frame...
    if (fondo_eleccion.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *caja_1_uber* updates
    if (t >= 0.0 && caja_1_uber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      caja_1_uber.tStart = t;  // (not accounting for frame time here)
      caja_1_uber.frameNStart = frameN;  // exact frame index
      
      caja_1_uber.setAutoDraw(true);
    }
    
    
    // if caja_1_uber is active this frame...
    if (caja_1_uber.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *caja_1_metro* updates
    if (t >= 0.0 && caja_1_metro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      caja_1_metro.tStart = t;  // (not accounting for frame time here)
      caja_1_metro.frameNStart = frameN;  // exact frame index
      
      caja_1_metro.setAutoDraw(true);
    }
    
    
    // if caja_1_metro is active this frame...
    if (caja_1_metro.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (caja_1_metro.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      caja_1_metro.tStop = t;  // not accounting for scr refresh
      caja_1_metro.frameNStop = frameN;  // exact frame index
      // update status
      caja_1_metro.status = PsychoJS.Status.FINISHED;
      caja_1_metro.setAutoDraw(false);
    }
    
    
    // *caja_1_caminata* updates
    if (t >= 0.0 && caja_1_caminata.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      caja_1_caminata.tStart = t;  // (not accounting for frame time here)
      caja_1_caminata.frameNStart = frameN;  // exact frame index
      
      caja_1_caminata.setAutoDraw(true);
    }
    
    
    // if caja_1_caminata is active this frame...
    if (caja_1_caminata.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (caja_1_caminata.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      caja_1_caminata.tStop = t;  // not accounting for scr refresh
      caja_1_caminata.frameNStop = frameN;  // exact frame index
      // update status
      caja_1_caminata.status = PsychoJS.Status.FINISHED;
      caja_1_caminata.setAutoDraw(false);
    }
    
    
    // *textbox_1_metro* updates
    if (t >= 0.0 && textbox_1_metro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_1_metro.tStart = t;  // (not accounting for frame time here)
      textbox_1_metro.frameNStart = frameN;  // exact frame index
      
      textbox_1_metro.setAutoDraw(true);
    }
    
    
    // if textbox_1_metro is active this frame...
    if (textbox_1_metro.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textbox_1_metro.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      textbox_1_metro.tStop = t;  // not accounting for scr refresh
      textbox_1_metro.frameNStop = frameN;  // exact frame index
      // update status
      textbox_1_metro.status = PsychoJS.Status.FINISHED;
      textbox_1_metro.setAutoDraw(false);
    }
    
    
    // *textbox_2_metro* updates
    if (t >= 0.0 && textbox_2_metro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_2_metro.tStart = t;  // (not accounting for frame time here)
      textbox_2_metro.frameNStart = frameN;  // exact frame index
      
      textbox_2_metro.setAutoDraw(true);
    }
    
    
    // if textbox_2_metro is active this frame...
    if (textbox_2_metro.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textbox_2_metro.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      textbox_2_metro.tStop = t;  // not accounting for scr refresh
      textbox_2_metro.frameNStop = frameN;  // exact frame index
      // update status
      textbox_2_metro.status = PsychoJS.Status.FINISHED;
      textbox_2_metro.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
