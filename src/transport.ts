import {Player} from 'midi-player-js'

class Transport {
  player: Player;

  constructor(songPath: string) {
    this.player = new Player()
    this.player.loadFile(`${songPath}/notes.mid`)
  }

  play() {
    this.player.play()
  }
}

export default Transport
