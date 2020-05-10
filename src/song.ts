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

  notes: Note[];

  songPath: string;

  constructor(songPath: string) {
    this.songPath = songPath
    this.notes = []
  }

  async init() {
    this.guitar = new TrackStream(`${this.songPath}/guitar.ogg`)
    // Set guitar volume to 0 until player hits a button
    this.guitar.setVolume(0)

    this.rhythm = new TrackStream(`${this.songPath}/rhythm.ogg`)
    this.song = new TrackStream(`${this.songPath}/song.ogg`)

    this.notes = await this.parseMidi()
  }

  async parseMidi() {
    const midiData = fs.readFileSync(`${this.songPath}/notes.mid`)
    const midi = new Midi(midiData)

    midi.tracks.forEach(track => {
      if (track.name === 'PART GUITAR') {
        this.notes = track.notes
      }
    })

    return []
  }
}

export default Song
