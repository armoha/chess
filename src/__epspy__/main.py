## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _RELIMP(path, mod_name):
    import inspect, pathlib, importlib.util
    p = pathlib.Path(inspect.getabsfile(inspect.currentframe())).parent
    for s in path.split("."):
        if s == "":  p = p.parent
        else:  p = p / s
    try:
        spec = importlib.util.spec_from_file_location(mod_name, p / (mod_name + ".py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except FileNotFoundError:
        loader = EPSLoader(mod_name, str(p / (mod_name + ".eps")))
        spec = importlib.util.spec_from_loader(mod_name, loader)
        module = loader.create_module(spec)
        loader.exec_module(module)
    return module

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _VARR(items):
    k = EUDVArray(len(items))()
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName

    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

    def __iadd__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov + v)

    def __isub__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov - v)

    def __imul__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov * v)

    def __ifloordiv__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov // v)

    def __iand__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov & v)

    def __ior__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov | v)

    def __ixor__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov ^ v)

class _ARRW:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

    def __lshift__(self, r):
        self.obj[self.index] = r

    def __iadd__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov + v

    def __isub__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov - v

    def __imul__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov * v

    def __ifloordiv__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov // v

    def __iand__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov & v

    def __ior__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov | v

    def __ixor__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov ^ v

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _LVAR(vs):
    ret, ops = [], []
    for v in FlattenList(vs):
        if IsEUDVariable(v) and v.IsRValue():
            ret.append(v.makeL())
        else:
            nv = EUDVariable()
            ret.append(nv)
            ops.append((nv, SetTo, v))
    if ops:
        SeqCompute(ops)
    return List2Assignable(ret)

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 1) import loc;
import loc
# (Line 3) function onPluginStart() {
@EUDTracedFunc
def onPluginStart():
    # (Line 4) setcurpl(Player1);
    EUDTraceLog(4)
    f_setcurpl(Player1)
    # (Line 7) loc.moveCLoc(1, 2); CreateUnit(1, 'Pawn', 'cLoc', P7);
    EUDTraceLog(7)
    loc.f_moveCLoc(1, 2)
    # (Line 8) loc.moveCLoc(2, 2); CreateUnit(1, 'Pawn', 'cLoc', P7);
    EUDTraceLog(7)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P7))
    EUDTraceLog(8)
    loc.f_moveCLoc(2, 2)
    # (Line 9) loc.moveCLoc(3, 2); CreateUnit(1, 'Pawn', 'cLoc', P7);
    EUDTraceLog(8)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P7))
    EUDTraceLog(9)
    loc.f_moveCLoc(3, 2)
    # (Line 10) loc.moveCLoc(4, 2); CreateUnit(1, 'Pawn', 'cLoc', P7);
    EUDTraceLog(9)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P7))
    EUDTraceLog(10)
    loc.f_moveCLoc(4, 2)
    # (Line 11) loc.moveCLoc(5, 2); CreateUnit(1, 'Pawn', 'cLoc', P7);
    EUDTraceLog(10)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P7))
    EUDTraceLog(11)
    loc.f_moveCLoc(5, 2)
    # (Line 12) loc.moveCLoc(6, 2); CreateUnit(1, 'Pawn', 'cLoc', P7);
    EUDTraceLog(11)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P7))
    EUDTraceLog(12)
    loc.f_moveCLoc(6, 2)
    # (Line 13) loc.moveCLoc(7, 2); CreateUnit(1, 'Pawn', 'cLoc', P7);
    EUDTraceLog(12)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P7))
    EUDTraceLog(13)
    loc.f_moveCLoc(7, 2)
    # (Line 14) loc.moveCLoc(8, 2); CreateUnit(1, 'Pawn', 'cLoc', P7);
    EUDTraceLog(13)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P7))
    EUDTraceLog(14)
    loc.f_moveCLoc(8, 2)
    # (Line 16) loc.moveCLoc(1, 1); CreateUnit(1, 'Rook', 'cLoc', P7);
    EUDTraceLog(14)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P7))
    EUDTraceLog(16)
    loc.f_moveCLoc(1, 1)
    # (Line 17) loc.moveCLoc(2, 1); CreateUnit(1, 'Knight', 'cLoc', P7);
    EUDTraceLog(16)
    DoActions(CreateUnit(1, 'Rook', 'cLoc', P7))
    EUDTraceLog(17)
    loc.f_moveCLoc(2, 1)
    # (Line 18) loc.moveCLoc(3, 1); CreateUnit(1, 'Bishop', 'cLoc', P7);
    EUDTraceLog(17)
    DoActions(CreateUnit(1, 'Knight', 'cLoc', P7))
    EUDTraceLog(18)
    loc.f_moveCLoc(3, 1)
    # (Line 19) loc.moveCLoc(4, 1); CreateUnit(1, 'King', 'cLoc', P7);
    EUDTraceLog(18)
    DoActions(CreateUnit(1, 'Bishop', 'cLoc', P7))
    EUDTraceLog(19)
    loc.f_moveCLoc(4, 1)
    # (Line 20) loc.moveCLoc(5, 1); CreateUnit(1, 'Queen', 'cLoc', P7);
    EUDTraceLog(19)
    DoActions(CreateUnit(1, 'King', 'cLoc', P7))
    EUDTraceLog(20)
    loc.f_moveCLoc(5, 1)
    # (Line 21) loc.moveCLoc(6, 1); CreateUnit(1, 'Bishop', 'cLoc', P7);
    EUDTraceLog(20)
    DoActions(CreateUnit(1, 'Queen', 'cLoc', P7))
    EUDTraceLog(21)
    loc.f_moveCLoc(6, 1)
    # (Line 22) loc.moveCLoc(7, 1); CreateUnit(1, 'Knight', 'cLoc', P7);
    EUDTraceLog(21)
    DoActions(CreateUnit(1, 'Bishop', 'cLoc', P7))
    EUDTraceLog(22)
    loc.f_moveCLoc(7, 1)
    # (Line 23) loc.moveCLoc(8, 1); CreateUnit(1, 'Rook', 'cLoc', P7);
    EUDTraceLog(22)
    DoActions(CreateUnit(1, 'Knight', 'cLoc', P7))
    EUDTraceLog(23)
    loc.f_moveCLoc(8, 1)
    # (Line 25) loc.moveCLoc(1, 7); CreateUnit(1, 'Pawn', 'cLoc', P8);
    EUDTraceLog(23)
    DoActions(CreateUnit(1, 'Rook', 'cLoc', P7))
    EUDTraceLog(25)
    loc.f_moveCLoc(1, 7)
    # (Line 26) loc.moveCLoc(2, 7); CreateUnit(1, 'Pawn', 'cLoc', P8);
    EUDTraceLog(25)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P8))
    EUDTraceLog(26)
    loc.f_moveCLoc(2, 7)
    # (Line 27) loc.moveCLoc(3, 7); CreateUnit(1, 'Pawn', 'cLoc', P8);
    EUDTraceLog(26)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P8))
    EUDTraceLog(27)
    loc.f_moveCLoc(3, 7)
    # (Line 28) loc.moveCLoc(4, 7); CreateUnit(1, 'Pawn', 'cLoc', P8);
    EUDTraceLog(27)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P8))
    EUDTraceLog(28)
    loc.f_moveCLoc(4, 7)
    # (Line 29) loc.moveCLoc(5, 7); CreateUnit(1, 'Pawn', 'cLoc', P8);
    EUDTraceLog(28)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P8))
    EUDTraceLog(29)
    loc.f_moveCLoc(5, 7)
    # (Line 30) loc.moveCLoc(6, 7); CreateUnit(1, 'Pawn', 'cLoc', P8);
    EUDTraceLog(29)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P8))
    EUDTraceLog(30)
    loc.f_moveCLoc(6, 7)
    # (Line 31) loc.moveCLoc(7, 7); CreateUnit(1, 'Pawn', 'cLoc', P8);
    EUDTraceLog(30)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P8))
    EUDTraceLog(31)
    loc.f_moveCLoc(7, 7)
    # (Line 32) loc.moveCLoc(8, 7); CreateUnit(1, 'Pawn', 'cLoc', P8);
    EUDTraceLog(31)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P8))
    EUDTraceLog(32)
    loc.f_moveCLoc(8, 7)
    # (Line 34) loc.moveCLoc(1, 8); CreateUnit(1, 'Rook', 'cLoc', P8);
    EUDTraceLog(32)
    DoActions(CreateUnit(1, 'Pawn', 'cLoc', P8))
    EUDTraceLog(34)
    loc.f_moveCLoc(1, 8)
    # (Line 35) loc.moveCLoc(2, 8); CreateUnit(1, 'Knight', 'cLoc', P8);
    EUDTraceLog(34)
    DoActions(CreateUnit(1, 'Rook', 'cLoc', P8))
    EUDTraceLog(35)
    loc.f_moveCLoc(2, 8)
    # (Line 36) loc.moveCLoc(3, 8); CreateUnit(1, 'Bishop', 'cLoc', P8);
    EUDTraceLog(35)
    DoActions(CreateUnit(1, 'Knight', 'cLoc', P8))
    EUDTraceLog(36)
    loc.f_moveCLoc(3, 8)
    # (Line 37) loc.moveCLoc(4, 8); CreateUnit(1, 'King', 'cLoc', P8);
    EUDTraceLog(36)
    DoActions(CreateUnit(1, 'Bishop', 'cLoc', P8))
    EUDTraceLog(37)
    loc.f_moveCLoc(4, 8)
    # (Line 38) loc.moveCLoc(5, 8); CreateUnit(1, 'Queen', 'cLoc', P8);
    EUDTraceLog(37)
    DoActions(CreateUnit(1, 'King', 'cLoc', P8))
    EUDTraceLog(38)
    loc.f_moveCLoc(5, 8)
    # (Line 39) loc.moveCLoc(6, 8); CreateUnit(1, 'Bishop', 'cLoc', P8);
    EUDTraceLog(38)
    DoActions(CreateUnit(1, 'Queen', 'cLoc', P8))
    EUDTraceLog(39)
    loc.f_moveCLoc(6, 8)
    # (Line 40) loc.moveCLoc(7, 8); CreateUnit(1, 'Knight', 'cLoc', P8);
    EUDTraceLog(39)
    DoActions(CreateUnit(1, 'Bishop', 'cLoc', P8))
    EUDTraceLog(40)
    loc.f_moveCLoc(7, 8)
    # (Line 41) loc.moveCLoc(8, 8); CreateUnit(1, 'Rook', 'cLoc', P8);
    EUDTraceLog(40)
    DoActions(CreateUnit(1, 'Knight', 'cLoc', P8))
    EUDTraceLog(41)
    loc.f_moveCLoc(8, 8)
    # (Line 42) }
    EUDTraceLog(41)
    DoActions(CreateUnit(1, 'Rook', 'cLoc', P8))
    # (Line 44) function afterTriggerExec () {

@EUDTracedFunc
def afterTriggerExec():
    # (Line 45) SetInvincibility(Enable, '(any unit)', AllPlayers, 'Anywhere');
    # (Line 46) const clickedUnitPtr = dwread_epd(EPD(0x6284E8));
    EUDTraceLog(45)
    DoActions(SetInvincibility(Enable, '(any unit)', AllPlayers, 'Anywhere'))
    EUDTraceLog(46)
    clickedUnitPtr = f_dwread_epd(EPD(0x6284E8))
    # (Line 48) if (clickedUnitPtr != 0) {
    _t1 = EUDIf()
    EUDTraceLog(48)
    if _t1(clickedUnitPtr == 0, neg=True):
        # (Line 49) const unitEPD = EPD(clickedUnitPtr);
        EUDTraceLog(49)
        unitEPD = EPD(clickedUnitPtr)
        # (Line 50) const unitX, unitY = dwbreak(dwread_epd(unitEPD + 0x28 / 4))[[0, 1]];
        EUDTraceLog(50)
        unitX, unitY = List2Assignable([_SRET(f_dwbreak(f_dwread_epd(unitEPD + 0x28 // 4)), [0, 1])])
        # (Line 51) const unitType = wread_epd(unitEPD + (0x64 / 4), 0);
        EUDTraceLog(51)
        unitType = f_wread_epd(unitEPD + (0x64 // 4), 0)
        # (Line 52) simpleprint(unitType, unitX, unitY);
        EUDTraceLog(52)
        f_simpleprint(unitType, unitX, unitY)
        # (Line 53) }
        # (Line 54) }
    EUDEndIf()
