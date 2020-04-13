import {terminal as term, ScreenBuffer} from 'terminal-kit'
import {performance} from 'perf_hooks'
import ioHook from 'iohook'

const colors = ['green', 'red', 'yellow', 'blue', 'magenta']

let viewport: any = null
let fretboard: any = null
let strings: any = null
let buttons: any = null
let notes: any = null

const buttonState: any = {
  0: false,
  1: false,
  2: false,
  3: false,
  4: false,
}

function terminate() {
  term.hideCursor(false)
  term.grabInput(false)
  setTimeout(() => process.exit(), 100)
}

interface KeyEvent {
  keycode: number;
  type: string;
  ctrlKey: boolean;
}

function setButtonState(button: string, type: any) {
  if (type === 'keydown') {
    buttonState[button] = true
    return true
  }
  if (type === 'keyup') {
    buttonState[button] = false
    return false
  }
  return null
}

function handleKeys(event: KeyEvent) {
  // term(`Key press: ${event.keycode} - ${event.type} - ${event.ctrlKey}`)
  const aKeycode = 30
  const sKeycode = 31
  const dKeycode = 32
  const fKeycode = 33
  const gKeycode = 34
  const spaceKeycode = 57
  const qKeycode = 16
  // const cKeycode = 46

  switch (event.keycode) {
  case aKeycode:
    setButtonState('0', event.type)
    break
  case sKeycode:
    setButtonState('1', event.type)
    break
  case dKeycode:
    setButtonState('2', event.type)
    break
  case fKeycode:
    setButtonState('3', event.type)
    break
  case gKeycode:
    setButtonState('4', event.type)
    break
  case spaceKeycode:
    // TODO
    break
  // TODO add ctrl-c shortcut to terminate
  case qKeycode:
    terminate()
    break
  }
}

function createFretboard() {
  const width = 53
  const height = viewport.height - 10
  const xMargin = viewport.width - 53 - ((viewport.width - 53) / 2)
  fretboard = new ScreenBuffer({
    dst: viewport,
    width,
    height,
    x: xMargin,
    y: 5,
    noFill: true,
  })
  term('The fretboard size is %dx%d \n', fretboard.width, fretboard.height)
  term('The fretboard margin is %d \n', xMargin)

  fretboard.fill({attr: {color: 'gray', bgColor: 'black'}})

  for (let i = 0; i < fretboard.height; i++) {
    fretboard.put({
      x: 0,
      y: i % fretboard.height,
      attr: {color: 'gray', bgColor: 'black'},
    }, '|')
  }

  for (let i = 0; i < fretboard.height; i++) {
    fretboard.put({
      x: fretboard.width - 1,
      y: i % fretboard.height,
      attr: {color: 'gray', bgColor: 'black'},
    }, '|')
  }
}

function createFretlines() {
  const width = fretboard.width - 2
  const height = fretboard.height
  const fretHeight = 16
  term('We can show %d fretlines \n', (height - 1) / fretHeight)

  // fit as many fretlines as we can
  // every other line should be lighter
  // TODO fretlines will need to be synced with notes
  let freespace = height - 1
  while (freespace >= fretHeight) {
    for (let i = 1; i <= width; i++) {
      fretboard.put({
        x: i,
        y: freespace,
        attr: {color: 'gray', bgColor: 'black'},
      }, '-')
    }

    freespace -= fretHeight
  }
}

function createStrings() {
  const width = fretboard.width - 2
  const height = fretboard.height - 3
  strings = new ScreenBuffer({
    dst: viewport,
    width,
    height,
    x: fretboard.x + 1,
    y: fretboard.y,
    noFill: true,
  })
  term('The string size is %dx%d \n', strings.width, strings.height)

  strings.fill({attr: {color: 'gray', bgColor: 'black', transparency: true}})

  const stringCount = 5
  for (let j = 0; j < stringCount; j++) {
    for (let i = 0; i < strings.height; i++) {
      strings.put({
        x: 5 + (10 * j),
        y: i,
        attr: {color: 'gray', bgColor: 'black'},
      }, '|')
    }
  }
}

function createButtons() {
  const width = fretboard.width - 2
  const height = 3
  buttons = new ScreenBuffer({
    dst: viewport,
    width,
    height,
    x: fretboard.x,
    y: fretboard.height,
    noFill: true,
  })
  term('The button size is %dx%d \n', buttons.width, buttons.height)
  buttons.fill({attr: {color: 'gray', bgColor: 'black', transparency: true}})
}

function drawButtons() {
  const buttonCount = 5
  for (let j = 0; j < buttonCount; j++) {
    for (let i = 0; i < 3; i++) {
      const buttonIndex = `${j}`
      buttons.put({
        x: 1 + (10 * j) + 1,
        y: i,
        attr: {color: colors[j], bgColor: 'black', bold: buttonState[buttonIndex]},
      }, 'OOOOOOOOO')
    }
  }

  buttons.draw({blending: true})
}

function createNotes() {
  const width = fretboard.width - 2
  const height = 3
  notes = new ScreenBuffer({
    dst: viewport,
    width,
    height,
    x: fretboard.x,
    y: fretboard.y,
    noFill: true,
  })
  term('The button size is %dx%d \n', notes.width, notes.height)

  notes.fill({attr: {color: 'gray', bgColor: 'black', transparency: true}})

  const noteCount = 5
  for (let j = 0; j < noteCount; j++) {
    for (let i = 0; i < 3; i++) {
      notes.put({
        x: 1 + (10 * j) + 1,
        y: i,
        attr: {color: colors[j], bgColor: 'black'},
      }, 'MMMMMMMMM')
    }
  }
}

let frames = 0
let timestamp = performance.now()
function draw() {
  fretboard.draw()
  strings.draw({blending: true})
  notes.draw({blending: true})
  drawButtons()
  const stats = viewport.draw({delta: true})

  const frametime = performance.now() - timestamp
  const fps = 1000 / frametime

  term.moveTo.eraseLine.bgWhite.green(1, 1,
    'Q/Ctrl-C: Quit - Redraw stats: %d cells, %d moves, %d attrs, %d writes, %d frametime, %d fps\n',
    stats.cells, stats.moves, stats.attrs, stats.writes, frametime, fps
  )

  frames++
  timestamp = performance.now()
}

function nextPosition() {
  if (notes.y > fretboard.height) {
    notes.y = 0
    return notes.y
  }
  return notes.y++
}

function animate() {
  draw()
  nextPosition()
  setImmediate(animate)
}

export default function render() {
  term('The terminal size is %dx%d \n', term.width, term.height)

  viewport = new ScreenBuffer({
    dst: term,
  })

  createFretboard()
  createFretlines()
  createStrings()
  createButtons()
  createNotes()

  term.moveTo.eraseLine.bgWhite.green(1, 1, 'Q/Ctrl-C: Quit\n')
  term.hideCursor()
  term.grabInput(true)
  ioHook.on('keyup', handleKeys)
  ioHook.on('keydown', handleKeys)
  ioHook.start()

  animate()
}
