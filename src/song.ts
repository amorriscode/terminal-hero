import Speaker from 'speaker'
import ffmpeg from 'fluent-ffmpeg'
import Volume from 'pcm-volume'

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

  constructor(songPath: string) {
    this.guitar = new TrackStream(`${songPath}/guitar.ogg`)
    // Set guitar volume to 0 until player hits a button
    this.guitar.setVolume(0)

    this.rhythm = new TrackStream(`${songPath}/rhythm.ogg`)
    this.song = new TrackStream(`${songPath}/song.ogg`)
  }
}

export default Song
