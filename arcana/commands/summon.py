from evennia.commands.default.muxcommand import MuxCommand


class CmdSummon(MuxCommand):
   
    key = "+summon"
    locks = "cmd:all()"

    def func(self):
        players = [con for con in self.caller.location.contents if con.has_player]
        for player in players:
            if(player.db.alive == 1):
                player.msg("The spirit world is drawing closer.")
            if(player.db.alive == 0):
                player.msg("The physical plane is drawing closer.")
            player.db.sight = 1
            player.db.touch = 1        
