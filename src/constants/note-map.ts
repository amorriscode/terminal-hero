// We map various MIDI notes to each of our buttons
// Each difficulty has its own octave mapped to it
// The numbers (96, 97, etc.) represent MIDI note values

export const EXPERT = {
  0: 96,    // C8
  1: 97,    // C#8
  2: 98,    // D8
  3: 99,    // D#8
  4: 100,   // E8
}

export const HARD = {
  0: 84,    // C7
  1: 85,    // C#7
  2: 86,    // D7
  3: 87,    // D#7
  4: 88,    // E7
}

export const MEDIUM = {
  0: 72,    // C6
  1: 73,    // C#6
  2: 74,    // D6
  3: 75,    // D#6
  4: 76,    // E6
}

export const EASY = {
  0: 60,    // C5
  1: 61,    // C#5
  2: 62,    // D5
  3: 63,    // D#5
  4: 64,    // E5
}
