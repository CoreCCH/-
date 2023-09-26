class Flag(object):
    def __init__(self, parent=None):
        self.flagConveyerForward = False
        self.flagConveyerBackward = False
        self.flagConveyerUp = False
        self.flagConveyerDown = False
        self.FlagIsBlockUp = False
        self.FlagIsBlockDown = False

def clearAllFlag(flag):
    flag.flagConveyerForward = False
    flag.flagConveyerBackward = False
    flag.flagConveyerUp = False
    flag.flagConveyerDown = False

