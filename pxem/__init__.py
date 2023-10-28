class Pxem:
    """
    .Sh NAME
    .Nm Pxem
    .Nd Implementation of esolang Pxem
    .Sh EXAMPLE
    .Bd -literal

    >>> # Hello, world!
    >>> filename = "Hello, world!.pxe"
    >>> Pxem(filename).run()
    Hello, world!
    >>> # Arithmetic
    >>> filename = "\u0001\u0002.+.n"
    >>> Pxem(filename).run()
    3
    >>> # Read content as both literal and subroutine
    >>> filename = ".f.p.e"
    >>> content = "asdf.P"
    >>> Pxem(filename, source=content).run()
    asdf.Pasdf
    >>> 

    .El 
    .Sh DESCRIPTION
    The
    .Nm
    class is an implementation of Pxem.
    Given
    .Fa filename:str
    and optionally
    .Fa content:optional[str]=None
    of file source, they are immediately compiled.
    The
    .Fn run
    method runs the compiled program.
    By default,
    .Va sys.stdin
    and
    .Va sys.stdout
    are used for I/O.
    """

    COMMANDS = {
            "pP": _print,
            "oO": _output,
            "nN": _numeric,
            "iI": _input,
            "_":  __input,
            "cC": _copy,
            "sS": _suteru,
            "vV": _reverse,
            "fF": _file,
            "eE": _execute,
            "rR": _random,
            "wWxXyYzZ": _wxyz,
            "aA": _a,
            "tT": _t,
            "mM": _m,
            "dD": _d,
            "+-!$%": _arithmetic,
    }

    def __init__(self, filename:str, *, source:optional[str]=None, is_empty_true:bool=False):
        # === Methods
        
        # Holds original filename as path; shall be preserved in case the interpreter wants to
        # open the file on demand.
        self.filename = filename

        # is None: has not loaded
        # type() == str: has loaded
        self.source   = source


        

        self.main_routine = self.compile(filename)

    def compile(self, src:str):
        ... # TODO
        
    # .+ .- .! .$ .%
    def _arithmetic(self, opr):
        try:
            *self.lst, x, y = self.lst # or raise ValueError
            self.lst.append(opr(x, y))
            ...
            raise NotImplementedError # TODO
        except ValueError:
            pass

    def _print(self):
        s = "".join([chr(c) for c in self.lst])
        print(s, end="")

    def _output(self):
        try:
            *self.lst, c = self.lst # or raise ValueError
            print(s, end="")
        except ValueError:
            pass

    def _numeric(self):
        try:
            *self.lst, n = self.lst # or raise ValueError
            print(str(n), end="")
        except ValueError:
            pass

    def _input(self):
        # TODO how do I implement
        ...

    def __input(self):
        # TODO input
        ...

    def _copy(self):
        try:
            *self.lst, x = self.lst
            self.lst.append(x)
        except ValueError:
            pass

    # actually it is like DISCARD
    def _suteru(self):
        try:
            self.lst.pop()
        except IndexError:
            pass

    def _reverse(self):
        self.lst = list(reversed(self.lst))

    def _file(self):
        self.lst += self.src

    def _execute(self):
        # TODO how?
        ...

    def _random(self):
        try:
            *self.lst, r = self.lst
            r = _obtw_randint(r)
            self.lst.append(r)
        except ValueError:
            pass

    # WTFWTFWTF
    def _wxyz(self, n):
        # TODO how
        ...

    def _a(self):
        # TODO how
        ...

    def _t(self):
        # TODO how
        ...

    def _m(self):
        # TODO how
        ...

    def _d(self):
        self.ip = None
        ...
