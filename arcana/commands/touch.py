from evennia.commands.default.muxcommand import MuxCommand


class CmdReach(MuxCommand):
   
    key = "+reach"
    locks = "cmd:all()"

    def func(self):
        self.caller.db.touch = 1
        if  self.caller.db.alive:
            self.caller.msg("You can now reach into the spirit world.")
        else:
            self.caller.msg("You can now reach into the physical world.")
