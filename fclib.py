"""Function and Classes library module."""

import colorama


def printq(*objects, mude=False, **kwargs) -> None:
    """A builtins function print with power switch.
    If mude is True, print nothing.
    """

    if not mude:
        print(*objects, **kwargs)


def notice(
        string: str = "OK",
        bodycolor: str = "GREEN",
        borders: str = "[]",
        bordercolor: str = None,
        long: int = 4,
        fillchar: str = " ",
        inupper: bool = True
) -> str:
    """Return a colorful notice, default 'green ok': [  OK  ]."""

    if long % 2 != 0:
        long += 1

    if len(string) > long:
        string = string[:long]

    if inupper:
        message = string.upper()
    else:
        message = string

    bodycolor = bodycolor.upper()
    if bordercolor is not None:
        bordercolor = bordercolor.upper()

    message = message.center(long, fillchar)

    colorama.just_fix_windows_console()
    available_colors = [color for color in dir(colorama.Fore)
                        if not color.startswith("_")]

    if bodycolor not in available_colors:
        raise ValueError("unknown color, only %s" % str(available_colors))

    elif bordercolor is not None and bordercolor not in available_colors:
        raise ValueError("unknown color, only %s" % str(available_colors))

    if bordercolor is not None:
        lborder = "%s%s%s" % (
            colorama.Fore.__getattribute__(bordercolor),
            borders[0],
            colorama.Style.RESET_ALL
        )
        rborder = "%s%s%s" % (
            colorama.Fore.__getattribute__(bordercolor),
            borders[1],
            colorama.Style.RESET_ALL
        )

    else:
        lborder = borders[0]
        rborder = borders[1]

    body = "%s%s%s" % (
        colorama.Fore.__getattribute__(bodycolor),
        message,
        colorama.Style.RESET_ALL
    )

    return lborder + body + rborder
