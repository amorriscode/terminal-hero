import {Command} from '@oclif/command'
import Song from './song'
import Transport from './transport'

class TerminalHero extends Command {
  static description = 'Bringing musical skills and fast fingers to a terminal near you 🤘'

  static args = [{
    name: 'songPath',
    required: true,
    description: 'path to song foler',
  }]

  async run() {
    const {args} = this.parse(TerminalHero)

    const transport = new Transport(args.songPath)
    const song = new Song(args.songPath)

    transport.play()
  }
}

export = TerminalHero
