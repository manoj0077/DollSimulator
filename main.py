import sys
import re
from doll import Doll
from exceptions import *
from square_table import SquareTable


def main():

    square_table = SquareTable(5)
    doll = Doll(square_table)
    cmds = ["MOVE", "LEFT", "RIGHT", "REPORT", "PLACE"]

    for line in sys.stdin:
        try:
            m = re.match(r"(\w+)( (.*))?", line)
            if not m:
                raise NotValidCommand('Command Not in Proper Format: "%s"' % line)
            cmd = m.group(1)
            if cmd in cmds:
                if cmd == "PLACE":
                    params = (m.group(3) or "").split(',')
                    if len(params) != 3:
                        raise NotValidCommand('Command Not in Proper Format: "%s"' % line)
                    doll.place(params)
                else:
                    getattr(doll,cmd.lower())()
            else:
                raise NotValidCommand('Given Command Not Supported: "%s"' % cmd)
        except Exception as e:
            #print(e)
            continue


if __name__ == "__main__":
    main()
