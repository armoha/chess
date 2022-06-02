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
# (Line 2) import moveRule.pawn;
from moveRule import pawn
# (Line 3) import moveRule.rook;
from moveRule import rook
# (Line 4) import moveRule.king;
from moveRule import king
# (Line 5) import moveRule.knight;
from moveRule import knight
# (Line 6) import moveRule.bishop;
from moveRule import bishop
# (Line 7) import moveRule.queen;
from moveRule import queen
# (Line 8) import board;
import board
# (Line 10) function onPluginStart() {
@EUDTracedFunc
def onPluginStart():
    # (Line 11) board.initBoard();
    EUDTraceLog(11)
    board.f_initBoard()
    # (Line 12) }
    # (Line 14) var lastClickedUnitPtr = 0;

lastClickedUnitPtr = EUDCreateVariables(1)
_IGVA([lastClickedUnitPtr], lambda: [0])
# (Line 15) var whoShouldPlay = $P7;
whoShouldPlay = EUDCreateVariables(1)
_IGVA([whoShouldPlay], lambda: [6])
# (Line 17) function afterTriggerExec () {
@EUDTracedFunc
def afterTriggerExec():
    # (Line 18) SetInvincibility(Enable, '(any unit)', AllPlayers, 'Anywhere');
    # (Line 19) const clickedUnitPtr = dwread_epd(EPD(0x6284E8));
    EUDTraceLog(18)
    DoActions(SetInvincibility(Enable, '(any unit)', AllPlayers, 'Anywhere'))
    EUDTraceLog(19)
    clickedUnitPtr = f_dwread_epd(EPD(0x6284E8))
    # (Line 22) if (lastClickedUnitPtr != clickedUnitPtr) {
    _t1 = EUDIf()
    EUDTraceLog(22)
    if _t1(lastClickedUnitPtr == clickedUnitPtr, neg=True):
        # (Line 23) if (clickedUnitPtr != 0) {
        _t2 = EUDIf()
        EUDTraceLog(23)
        if _t2(clickedUnitPtr == 0, neg=True):
            # (Line 24) const unitEPD = EPD(clickedUnitPtr);
            EUDTraceLog(24)
            unitEPD = EPD(clickedUnitPtr)
            # (Line 25) const unitX, unitY = dwbreak(dwread_epd(unitEPD + 0x28 / 4))[[0, 1]];
            EUDTraceLog(25)
            unitX, unitY = List2Assignable([_SRET(f_dwbreak(f_dwread_epd(unitEPD + 0x28 // 4)), [0, 1])])
            # (Line 26) const unitCellX = (unitX - loc.c11x) / 64 + 1;
            EUDTraceLog(26)
            unitCellX = (unitX - loc.c11x) // 64 + 1
            # (Line 27) const unitCellY = (unitY - loc.c11y) / 64 + 1;
            EUDTraceLog(27)
            unitCellY = (unitY - loc.c11y) // 64 + 1
            # (Line 28) const unitPlayer = bread_epd(unitEPD + 0x4C / 4, 0);
            EUDTraceLog(28)
            unitPlayer = f_bread_epd(unitEPD + 0x4C // 4, 0)
            # (Line 29) const unitType = wread_epd(unitEPD + (0x64 / 4), 0);
            EUDTraceLog(29)
            unitType = f_wread_epd(unitEPD + (0x64 // 4), 0)
            # (Line 31) if (unitPlayer == whoShouldPlay) {
            _t3 = EUDIf()
            EUDTraceLog(31)
            if _t3(unitPlayer == whoShouldPlay):
                # (Line 32) if (unitType == $U('Pawn')) {
                _t4 = EUDIf()
                EUDTraceLog(32)
                if _t4(unitType == EncodeUnit('Pawn')):
                    # (Line 33) RemoveUnit('Cursor', Force2);
                    # (Line 34) pawn.movePawn(unitPlayer, unitCellX, unitCellY);
                    EUDTraceLog(33)
                    DoActions(RemoveUnit('Cursor', Force2))
                    EUDTraceLog(34)
                    pawn.f_movePawn(unitPlayer, unitCellX, unitCellY)
                    # (Line 35) }
                    # (Line 37) if (unitType == $U('Rook')) {
                EUDEndIf()
                _t5 = EUDIf()
                EUDTraceLog(37)
                if _t5(unitType == EncodeUnit('Rook')):
                    # (Line 38) RemoveUnit('Cursor', Force2);
                    # (Line 39) rook.moveRook(unitPlayer, unitCellX, unitCellY);
                    EUDTraceLog(38)
                    DoActions(RemoveUnit('Cursor', Force2))
                    EUDTraceLog(39)
                    rook.f_moveRook(unitPlayer, unitCellX, unitCellY)
                    # (Line 40) }
                    # (Line 42) if (unitType == $U('Bishop')) {
                EUDEndIf()
                _t6 = EUDIf()
                EUDTraceLog(42)
                if _t6(unitType == EncodeUnit('Bishop')):
                    # (Line 43) RemoveUnit('Cursor', Force2);
                    # (Line 44) bishop.moveBishop(unitPlayer, unitCellX, unitCellY);
                    EUDTraceLog(43)
                    DoActions(RemoveUnit('Cursor', Force2))
                    EUDTraceLog(44)
                    bishop.f_moveBishop(unitPlayer, unitCellX, unitCellY)
                    # (Line 45) }
                    # (Line 47) if (unitType == $U('Queen')) {
                EUDEndIf()
                _t7 = EUDIf()
                EUDTraceLog(47)
                if _t7(unitType == EncodeUnit('Queen')):
                    # (Line 48) RemoveUnit('Cursor', Force2);
                    # (Line 49) queen.moveQueen(unitPlayer, unitCellX, unitCellY);
                    EUDTraceLog(48)
                    DoActions(RemoveUnit('Cursor', Force2))
                    EUDTraceLog(49)
                    queen.f_moveQueen(unitPlayer, unitCellX, unitCellY)
                    # (Line 50) }
                    # (Line 52) if (unitType == $U('King')) {
                EUDEndIf()
                _t8 = EUDIf()
                EUDTraceLog(52)
                if _t8(unitType == EncodeUnit('King')):
                    # (Line 53) RemoveUnit('Cursor', Force2);
                    # (Line 54) king.moveKing(unitPlayer, unitCellX, unitCellY);
                    EUDTraceLog(53)
                    DoActions(RemoveUnit('Cursor', Force2))
                    EUDTraceLog(54)
                    king.f_moveKing(unitPlayer, unitCellX, unitCellY)
                    # (Line 55) }
                    # (Line 57) if (unitType == $U('Knight')) {
                EUDEndIf()
                _t9 = EUDIf()
                EUDTraceLog(57)
                if _t9(unitType == EncodeUnit('Knight')):
                    # (Line 58) RemoveUnit('Cursor', Force2);
                    # (Line 59) knight.moveKnight(unitPlayer, unitCellX, unitCellY);
                    EUDTraceLog(58)
                    DoActions(RemoveUnit('Cursor', Force2))
                    EUDTraceLog(59)
                    knight.f_moveKnight(unitPlayer, unitCellX, unitCellY)
                    # (Line 60) }
                    # (Line 62) else if (unitType == $U('Cursor')) {
                _t10 = EUDElseIf()
                EUDTraceLog(62)
                if _t10(unitType == EncodeUnit('Cursor')):
                    # (Line 64) const lastUnitEPD = EPD(lastClickedUnitPtr);
                    EUDTraceLog(64)
                    lastUnitEPD = EPD(lastClickedUnitPtr)
                    # (Line 65) const lastUnitX, lastUnitY = dwbreak(dwread_epd(lastUnitEPD + 0x28 / 4))[[0, 1]];
                    EUDTraceLog(65)
                    lastUnitX, lastUnitY = List2Assignable([_SRET(f_dwbreak(f_dwread_epd(lastUnitEPD + 0x28 // 4)), [0, 1])])
                    # (Line 66) const lastUnitCellX = (lastUnitX - loc.c11x) / 64 + 1;
                    EUDTraceLog(66)
                    lastUnitCellX = (lastUnitX - loc.c11x) // 64 + 1
                    # (Line 67) const lastUnitCellY = (lastUnitY - loc.c11y) / 64 + 1;
                    EUDTraceLog(67)
                    lastUnitCellY = (lastUnitY - loc.c11y) // 64 + 1
                    # (Line 68) const lastUnitType = wread_epd(lastUnitEPD + (0x64 / 4), 0);
                    EUDTraceLog(68)
                    lastUnitType = f_wread_epd(lastUnitEPD + (0x64 // 4), 0)
                    # (Line 70) board.removeBoard(unitCellX, unitCellY);
                    EUDTraceLog(70)
                    board.f_removeBoard(unitCellX, unitCellY)
                    # (Line 71) board.placeBoard(unitCellX, unitCellY, lastUnitType, unitPlayer);
                    EUDTraceLog(71)
                    board.f_placeBoard(unitCellX, unitCellY, lastUnitType, unitPlayer)
                    # (Line 72) board.removeBoard(lastUnitCellX, lastUnitCellY);
                    EUDTraceLog(72)
                    board.f_removeBoard(lastUnitCellX, lastUnitCellY)
                    # (Line 73) RemoveUnit('Cursor', Force2);
                    # (Line 75) whoShouldPlay = (whoShouldPlay == $P7) ? $P8 : $P7;
                    EUDTraceLog(73)
                    DoActions(RemoveUnit('Cursor', Force2))
                    EUDTraceLog(75)
                    whoShouldPlay << (EUDTernary((whoShouldPlay == 6))(7)(6))
                    # (Line 76) }
                    # (Line 77) }
                EUDEndIf()
                # (Line 78) }
            EUDEndIf()
            # (Line 79) lastClickedUnitPtr = clickedUnitPtr;
        EUDEndIf()
        EUDTraceLog(79)
        lastClickedUnitPtr << (clickedUnitPtr)
        # (Line 80) }
        # (Line 81) }
    EUDEndIf()
