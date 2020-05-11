import Speaker from 'speaker'
import ffmpeg from 'fluent-ffmpeg'
import Volume from 'pcm-volume'
import {Midi} from '@tonejs/midi'
import {Note} from '@tonejs/midi/dist/Note'
import fs from 'fs'

function createSpeaker() {
  // eslint-disable-next-line @typescript-eslint/ban-ts-ignore
  // @ts-ignore
  return new Speaker({
    channels: 2,
    bitDepth: 16,
    sampleRate: 44100,
  })
}

function createStream(file: string, output: any) {
  return ffmpeg(file)
  .format('wav')
  .noVideo()
  .outputOptions(['-bitexact'])
  .stream(output)
}

class TrackStream {
  speaker: any;

  volume: any;

  stream: any;

  constructor(file: string) {
    this.speaker = createSpeaker()
    this.volume = new Volume()
    this.volume.pipe(this.speaker)
    this.stream = createStream(file, this.volume)
  }

  setVolume(vol: number) {
    this.volume.setVolume(vol)
  }
}

class Song {
  guitar: any;

  rhythm: any;

  song: any;

  midi: Midi;

  title: string;

  notes: Note[];

  songPath: string;

  constructor(songPath: string) {
    this.songPath = songPath
    this.guitar = new TrackStream(`${this.songPath}/guitar.ogg`)
    // Set guitar volume to 0 until player hits a button
    this.guitar.setVolume(0)

    this.rhythm = new TrackStream(`${this.songPath}/rhythm.ogg`)
    this.song = new TrackStream(`${this.songPath}/song.ogg`)

    this.midi = this.parseMidi()

    this.title = this.midi.name

    this.notes = this.parseNotes()
  }

  parseMidi() {
    const midiData = fs.readFileSync(`${this.songPath}/notes.mid`)
    return new Midi(midiData)
  }

  parseNotes() {
    for (let i = 0; i < this.midi.tracks.length; i++) {
      if (this.midi.tracks[i].name === 'PART GUITAR') {
        return this.midi.tracks[i].notes
      }
    }

    return []
  }
}

export default Song
