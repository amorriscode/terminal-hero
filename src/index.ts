import {Command} from '@oclif/command'
import Song from './song'
import render from './terminal'

class TerminalHero extends Command {
  static description = 'Bringing musical skills and fast fingers to a terminal near you 🤘'

  static args = [{
    name: 'songPath',
    required: true,
    description: 'path to song folder',
  }]

  async run() {
    const {args} = this.parse(TerminalHero)

    const song = new Song(args.songPath)
    song.init()

    render()
  }
}

export = TerminalHero
