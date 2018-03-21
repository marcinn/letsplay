from .output import MplayerOutput
from . import Player, run_mpris_service


def init():
    output = MplayerOutput()
    player = Player()

    def play_via_mplayer():
        output.load(player.current.path)
        if player.is_playing:
            output.play()

    def play_next_on_stop():
        if player.is_playing:
            player.next()

    output.on('stop', play_next_on_stop)

    player.on('change', play_via_mplayer)
    player.on('pause', output.pause)
    player.on('play', output.play)

    run_mpris_service(player)
    return player
