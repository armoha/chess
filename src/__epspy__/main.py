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
# (Line 3) const boardArray = EUDArray(64);
boardArray = _CGFW(lambda: [EUDArray(64)], 1)[0]
# (Line 5) function placeBoard(x, y, unit: TrgUnit, player: TrgPlayer) {
@EUDTracedTypedFunc([None, None, TrgUnit, TrgPlayer])
def f_placeBoard(x, y, unit, player):
    # (Line 6) boardArray[(y - 1) * 8 + (x - 1)] = unit + 1000 * player;
    EUDTraceLog(6)
    _ARRW(boardArray, (y - 1) * 8 + (x - 1)) << (unit + 1000 * player)
    # (Line 7) loc.moveCLoc(x, y);
    EUDTraceLog(7)
    loc.f_moveCLoc(x, y)
    # (Line 8) CreateUnit(1, unit, 'cLoc', player);
    # (Line 9) }
    EUDTraceLog(8)
    DoActions(CreateUnit(1, unit, 'cLoc', player))
    # (Line 11) function removeBoard(x, y) {

@EUDTracedFunc
def f_removeBoard(x, y):
    # (Line 12) boardArray[(y - 1) * 8 + (x - 1)] = 0;
    EUDTraceLog(12)
    _ARRW(boardArray, (y - 1) * 8 + (x - 1)) << (0)
    # (Line 13) loc.moveCLoc(x, y);
    EUDTraceLog(13)
    loc.f_moveCLoc(x, y)
    # (Line 14) RemoveUnitAt(All, '(any unit)', 'cLoc', AllPlayers);
    # (Line 15) }
    EUDTraceLog(14)
    DoActions(RemoveUnitAt(All, '(any unit)', 'cLoc', AllPlayers))
    # (Line 17) function getBoard(x, y) {

@EUDTracedFunc
def f_getBoard(x, y):
    # (Line 18) const value = boardArray[(y - 1) * 8 + (x - 1)];
    EUDTraceLog(18)
    value = boardArray[(y - 1) * 8 + (x - 1)]
    # (Line 19) const player = value / 1000;
    EUDTraceLog(19)
    player = value // 1000
    # (Line 20) const unit = value % 1000;
    EUDTraceLog(20)
    unit = value % 1000
    # (Line 21) return player, unit;
    EUDTraceLog(21)
    EUDReturn(player, unit)
    # (Line 22) }
    # (Line 24) function initBoard () {

@EUDTracedFunc
def f_initBoard():
    # (Line 25) placeBoard(1, 2, 'Pawn', P7);
    EUDTraceLog(25)
    f_placeBoard(1, 2, 'Pawn', P7)
    # (Line 26) placeBoard(2, 2, 'Pawn', P7);
    EUDTraceLog(26)
    f_placeBoard(2, 2, 'Pawn', P7)
    # (Line 27) placeBoard(3, 2, 'Pawn', P7);
    EUDTraceLog(27)
    f_placeBoard(3, 2, 'Pawn', P7)
    # (Line 28) placeBoard(4, 2, 'Pawn', P7);
    EUDTraceLog(28)
    f_placeBoard(4, 2, 'Pawn', P7)
    # (Line 29) placeBoard(5, 2, 'Pawn', P7);
    EUDTraceLog(29)
    f_placeBoard(5, 2, 'Pawn', P7)
    # (Line 30) placeBoard(6, 2, 'Pawn', P7);
    EUDTraceLog(30)
    f_placeBoard(6, 2, 'Pawn', P7)
    # (Line 31) placeBoard(7, 2, 'Pawn', P7);
    EUDTraceLog(31)
    f_placeBoard(7, 2, 'Pawn', P7)
    # (Line 32) placeBoard(8, 2, 'Pawn', P7);
    EUDTraceLog(32)
    f_placeBoard(8, 2, 'Pawn', P7)
    # (Line 34) placeBoard(1, 1, 'Rook', P7);
    EUDTraceLog(34)
    f_placeBoard(1, 1, 'Rook', P7)
    # (Line 35) placeBoard(2, 1, 'Knight', P7);
    EUDTraceLog(35)
    f_placeBoard(2, 1, 'Knight', P7)
    # (Line 36) placeBoard(3, 1, 'Bishop', P7);
    EUDTraceLog(36)
    f_placeBoard(3, 1, 'Bishop', P7)
    # (Line 37) placeBoard(4, 1, 'King', P7);
    EUDTraceLog(37)
    f_placeBoard(4, 1, 'King', P7)
    # (Line 38) placeBoard(5, 1, 'Queen', P7);
    EUDTraceLog(38)
    f_placeBoard(5, 1, 'Queen', P7)
    # (Line 39) placeBoard(6, 1, 'Bishop', P7);
    EUDTraceLog(39)
    f_placeBoard(6, 1, 'Bishop', P7)
    # (Line 40) placeBoard(7, 1, 'Knight', P7);
    EUDTraceLog(40)
    f_placeBoard(7, 1, 'Knight', P7)
    # (Line 41) placeBoard(8, 1, 'Rook', P7);
    EUDTraceLog(41)
    f_placeBoard(8, 1, 'Rook', P7)
    # (Line 43) placeBoard(1, 7, 'Pawn', P8);
    EUDTraceLog(43)
    f_placeBoard(1, 7, 'Pawn', P8)
    # (Line 44) placeBoard(2, 7, 'Pawn', P8);
    EUDTraceLog(44)
    f_placeBoard(2, 7, 'Pawn', P8)
    # (Line 45) placeBoard(3, 7, 'Pawn', P8);
    EUDTraceLog(45)
    f_placeBoard(3, 7, 'Pawn', P8)
    # (Line 46) placeBoard(4, 7, 'Pawn', P8);
    EUDTraceLog(46)
    f_placeBoard(4, 7, 'Pawn', P8)
    # (Line 47) placeBoard(5, 7, 'Pawn', P8);
    EUDTraceLog(47)
    f_placeBoard(5, 7, 'Pawn', P8)
    # (Line 48) placeBoard(6, 7, 'Pawn', P8);
    EUDTraceLog(48)
    f_placeBoard(6, 7, 'Pawn', P8)
    # (Line 49) placeBoard(7, 7, 'Pawn', P8);
    EUDTraceLog(49)
    f_placeBoard(7, 7, 'Pawn', P8)
    # (Line 50) placeBoard(8, 7, 'Pawn', P8);
    EUDTraceLog(50)
    f_placeBoard(8, 7, 'Pawn', P8)
    # (Line 52) placeBoard(1, 8, 'Rook', P8);
    EUDTraceLog(52)
    f_placeBoard(1, 8, 'Rook', P8)
    # (Line 53) placeBoard(2, 8, 'Knight', P8);
    EUDTraceLog(53)
    f_placeBoard(2, 8, 'Knight', P8)
    # (Line 54) placeBoard(3, 8, 'Bishop', P8);
    EUDTraceLog(54)
    f_placeBoard(3, 8, 'Bishop', P8)
    # (Line 55) placeBoard(4, 8, 'King', P8);
    EUDTraceLog(55)
    f_placeBoard(4, 8, 'King', P8)
    # (Line 56) placeBoard(5, 8, 'Queen', P8);
    EUDTraceLog(56)
    f_placeBoard(5, 8, 'Queen', P8)
    # (Line 57) placeBoard(6, 8, 'Bishop', P8);
    EUDTraceLog(57)
    f_placeBoard(6, 8, 'Bishop', P8)
    # (Line 58) placeBoard(7, 8, 'Knight', P8);
    EUDTraceLog(58)
    f_placeBoard(7, 8, 'Knight', P8)
    # (Line 59) placeBoard(8, 8, 'Rook', P8);
    EUDTraceLog(59)
    f_placeBoard(8, 8, 'Rook', P8)
    # (Line 60) }
    # (Line 62) function onPluginStart() {

@EUDTracedFunc
def onPluginStart():
    # (Line 63) initBoard();
    EUDTraceLog(63)
    f_initBoard()
    # (Line 64) }
    # (Line 68) var lastClickedUnitPtr = 0;

lastClickedUnitPtr = EUDCreateVariables(1)
_IGVA([lastClickedUnitPtr], lambda: [0])
# (Line 70) function afterTriggerExec () {
@EUDTracedFunc
def afterTriggerExec():
    # (Line 71) SetInvincibility(Enable, '(any unit)', AllPlayers, 'Anywhere');
    # (Line 72) const clickedUnitPtr = dwread_epd(EPD(0x6284E8));
    EUDTraceLog(71)
    DoActions(SetInvincibility(Enable, '(any unit)', AllPlayers, 'Anywhere'))
    EUDTraceLog(72)
    clickedUnitPtr = f_dwread_epd(EPD(0x6284E8))
    # (Line 75) if (lastClickedUnitPtr != clickedUnitPtr) {
    _t1 = EUDIf()
    EUDTraceLog(75)
    if _t1(lastClickedUnitPtr == clickedUnitPtr, neg=True):
        # (Line 76) if (clickedUnitPtr != 0) {
        _t2 = EUDIf()
        EUDTraceLog(76)
        if _t2(clickedUnitPtr == 0, neg=True):
            # (Line 77) const unitEPD = EPD(clickedUnitPtr);
            EUDTraceLog(77)
            unitEPD = EPD(clickedUnitPtr)
            # (Line 78) const unitX, unitY = dwbreak(dwread_epd(unitEPD + 0x28 / 4))[[0, 1]];
            EUDTraceLog(78)
            unitX, unitY = List2Assignable([_SRET(f_dwbreak(f_dwread_epd(unitEPD + 0x28 // 4)), [0, 1])])
            # (Line 79) const unitCellX = (unitX - loc.c11x) / 64 + 1;
            EUDTraceLog(79)
            unitCellX = (unitX - loc.c11x) // 64 + 1
            # (Line 80) const unitCellY = (unitY - loc.c11y) / 64 + 1;
            EUDTraceLog(80)
            unitCellY = (unitY - loc.c11y) // 64 + 1
            # (Line 81) const unitPlayer = bread_epd(unitEPD + 0x4C / 4, 0);
            EUDTraceLog(81)
            unitPlayer = f_bread_epd(unitEPD + 0x4C // 4, 0)
            # (Line 82) const unitType = wread_epd(unitEPD + (0x64 / 4), 0);
            EUDTraceLog(82)
            unitType = f_wread_epd(unitEPD + (0x64 // 4), 0)
            # (Line 83) simpleprint(unitType, unitX, unitY);
            EUDTraceLog(83)
            f_simpleprint(unitType, unitX, unitY)
            # (Line 86) if (unitType == $U('Pawn')) {
            _t3 = EUDIf()
            EUDTraceLog(86)
            if _t3(unitType == EncodeUnit('Pawn')):
                # (Line 87) RemoveUnit('Cursor', Force2);
                # (Line 89) if (unitPlayer == $P7) {
                EUDTraceLog(87)
                DoActions(RemoveUnit('Cursor', Force2))
                _t4 = EUDIf()
                EUDTraceLog(89)
                if _t4(unitPlayer == 6):
                    # (Line 90) if (unitCellY == 2) {
                    _t5 = EUDIf()
                    EUDTraceLog(90)
                    if _t5(unitCellY == 2):
                        # (Line 91) if(getBoard(unitCellX, unitCellY + 2)[[0]] == 0) {
                        _t6 = EUDIf()
                        EUDTraceLog(91)
                        if _t6(f_getBoard(unitCellX, unitCellY + 2)[0] == 0):
                            # (Line 92) loc.moveCLoc(unitCellX, unitCellY + 2); CreateUnit(1, 'Cursor', 'cLoc', P7);
                            EUDTraceLog(92)
                            loc.f_moveCLoc(unitCellX, unitCellY + 2)
                            # (Line 93) }
                            EUDTraceLog(92)
                            DoActions(CreateUnit(1, 'Cursor', 'cLoc', P7))
                            # (Line 94) }
                        EUDEndIf()
                        # (Line 95) if (unitCellY < 8) {
                    EUDEndIf()
                    _t7 = EUDIf()
                    EUDTraceLog(95)
                    if _t7(unitCellY >= 8, neg=True):
                        # (Line 96) if(getBoard(unitCellX, unitCellY + 1)[[0]] == 0) {
                        _t8 = EUDIf()
                        EUDTraceLog(96)
                        if _t8(f_getBoard(unitCellX, unitCellY + 1)[0] == 0):
                            # (Line 97) loc.moveCLoc(unitCellX, unitCellY + 1); CreateUnit(1, 'Cursor', 'cLoc', P7);
                            EUDTraceLog(97)
                            loc.f_moveCLoc(unitCellX, unitCellY + 1)
                            # (Line 98) }
                            EUDTraceLog(97)
                            DoActions(CreateUnit(1, 'Cursor', 'cLoc', P7))
                            # (Line 99) if(unitCellX > 1 && getBoard(unitCellX - 1, unitCellY + 1)[[0]] == $P8) {
                        EUDEndIf()
                        _t9 = EUDIf()
                        EUDTraceLog(99)
                        if _t9(EUDSCAnd()(unitCellX <= 1, neg=True)(f_getBoard(unitCellX - 1, unitCellY + 1)[0] == 7)()):
                            # (Line 100) loc.moveCLoc(unitCellX - 1, unitCellY + 1); CreateUnit(1, 'Cursor', 'cLoc', P7);
                            EUDTraceLog(100)
                            loc.f_moveCLoc(unitCellX - 1, unitCellY + 1)
                            # (Line 101) }
                            EUDTraceLog(100)
                            DoActions(CreateUnit(1, 'Cursor', 'cLoc', P7))
                            # (Line 102) if(unitCellX < 8 && getBoard(unitCellX + 1, unitCellY + 1)[[0]] == $P8) {
                        EUDEndIf()
                        _t10 = EUDIf()
                        EUDTraceLog(102)
                        if _t10(EUDSCAnd()(unitCellX >= 8, neg=True)(f_getBoard(unitCellX + 1, unitCellY + 1)[0] == 7)()):
                            # (Line 103) loc.moveCLoc(unitCellX + 1, unitCellY + 1); CreateUnit(1, 'Cursor', 'cLoc', P7);
                            EUDTraceLog(103)
                            loc.f_moveCLoc(unitCellX + 1, unitCellY + 1)
                            # (Line 104) }
                            EUDTraceLog(103)
                            DoActions(CreateUnit(1, 'Cursor', 'cLoc', P7))
                            # (Line 105) }
                        EUDEndIf()
                        # (Line 106) }
                    EUDEndIf()
                    # (Line 108) if (unitPlayer == $P8) {
                EUDEndIf()
                _t11 = EUDIf()
                EUDTraceLog(108)
                if _t11(unitPlayer == 7):
                    # (Line 109) if (unitCellY == 7) {
                    _t12 = EUDIf()
                    EUDTraceLog(109)
                    if _t12(unitCellY == 7):
                        # (Line 110) if(getBoard(unitCellX, unitCellY - 2)[[0]] == 0) {
                        _t13 = EUDIf()
                        EUDTraceLog(110)
                        if _t13(f_getBoard(unitCellX, unitCellY - 2)[0] == 0):
                            # (Line 111) loc.moveCLoc(unitCellX, unitCellY - 2); CreateUnit(1, 'Cursor', 'cLoc', P8);
                            EUDTraceLog(111)
                            loc.f_moveCLoc(unitCellX, unitCellY - 2)
                            # (Line 112) }
                            EUDTraceLog(111)
                            DoActions(CreateUnit(1, 'Cursor', 'cLoc', P8))
                            # (Line 113) }
                        EUDEndIf()
                        # (Line 114) if (unitCellY > 1) {
                    EUDEndIf()
                    _t14 = EUDIf()
                    EUDTraceLog(114)
                    if _t14(unitCellY <= 1, neg=True):
                        # (Line 115) if(getBoard(unitCellX, unitCellY - 1)[[0]] == 0) {
                        _t15 = EUDIf()
                        EUDTraceLog(115)
                        if _t15(f_getBoard(unitCellX, unitCellY - 1)[0] == 0):
                            # (Line 116) loc.moveCLoc(unitCellX, unitCellY - 1); CreateUnit(1, 'Cursor', 'cLoc', P8);
                            EUDTraceLog(116)
                            loc.f_moveCLoc(unitCellX, unitCellY - 1)
                            # (Line 117) }
                            EUDTraceLog(116)
                            DoActions(CreateUnit(1, 'Cursor', 'cLoc', P8))
                            # (Line 118) if(unitCellX > 1 && getBoard(unitCellX - 1, unitCellY - 1)[[0]] == $P7) {
                        EUDEndIf()
                        _t16 = EUDIf()
                        EUDTraceLog(118)
                        if _t16(EUDSCAnd()(unitCellX <= 1, neg=True)(f_getBoard(unitCellX - 1, unitCellY - 1)[0] == 6)()):
                            # (Line 119) loc.moveCLoc(unitCellX - 1, unitCellY - 1); CreateUnit(1, 'Cursor', 'cLoc', P8);
                            EUDTraceLog(119)
                            loc.f_moveCLoc(unitCellX - 1, unitCellY - 1)
                            # (Line 120) }
                            EUDTraceLog(119)
                            DoActions(CreateUnit(1, 'Cursor', 'cLoc', P8))
                            # (Line 121) if(unitCellX < 8 && getBoard(unitCellX + 1, unitCellY - 1)[[0]] == $P7) {
                        EUDEndIf()
                        _t17 = EUDIf()
                        EUDTraceLog(121)
                        if _t17(EUDSCAnd()(unitCellX >= 8, neg=True)(f_getBoard(unitCellX + 1, unitCellY - 1)[0] == 6)()):
                            # (Line 122) loc.moveCLoc(unitCellX + 1, unitCellY - 1); CreateUnit(1, 'Cursor', 'cLoc', P8);
                            EUDTraceLog(122)
                            loc.f_moveCLoc(unitCellX + 1, unitCellY - 1)
                            # (Line 123) }
                            EUDTraceLog(122)
                            DoActions(CreateUnit(1, 'Cursor', 'cLoc', P8))
                            # (Line 124) }
                        EUDEndIf()
                        # (Line 125) }
                    EUDEndIf()
                    # (Line 126) }
                EUDEndIf()
                # (Line 128) else if (unitType == $U('Cursor')) {
            _t18 = EUDElseIf()
            EUDTraceLog(128)
            if _t18(unitType == EncodeUnit('Cursor')):
                # (Line 130) const lastUnitEPD = EPD(lastClickedUnitPtr);
                EUDTraceLog(130)
                lastUnitEPD = EPD(lastClickedUnitPtr)
                # (Line 131) const lastUnitX, lastUnitY = dwbreak(dwread_epd(lastUnitEPD + 0x28 / 4))[[0, 1]];
                EUDTraceLog(131)
                lastUnitX, lastUnitY = List2Assignable([_SRET(f_dwbreak(f_dwread_epd(lastUnitEPD + 0x28 // 4)), [0, 1])])
                # (Line 132) const lastUnitCellX = (lastUnitX - loc.c11x) / 64 + 1;
                EUDTraceLog(132)
                lastUnitCellX = (lastUnitX - loc.c11x) // 64 + 1
                # (Line 133) const lastUnitCellY = (lastUnitY - loc.c11y) / 64 + 1;
                EUDTraceLog(133)
                lastUnitCellY = (lastUnitY - loc.c11y) // 64 + 1
                # (Line 134) const lastUnitType = wread_epd(lastUnitEPD + (0x64 / 4), 0);
                EUDTraceLog(134)
                lastUnitType = f_wread_epd(lastUnitEPD + (0x64 // 4), 0)
                # (Line 136) removeBoard(unitCellX, unitCellY);
                EUDTraceLog(136)
                f_removeBoard(unitCellX, unitCellY)
                # (Line 137) placeBoard(unitCellX, unitCellY, lastUnitType, unitPlayer);
                EUDTraceLog(137)
                f_placeBoard(unitCellX, unitCellY, lastUnitType, unitPlayer)
                # (Line 138) removeBoard(lastUnitCellX, lastUnitCellY);
                EUDTraceLog(138)
                f_removeBoard(lastUnitCellX, lastUnitCellY)
                # (Line 139) RemoveUnit('Cursor', Force2);
                # (Line 140) }
                EUDTraceLog(139)
                DoActions(RemoveUnit('Cursor', Force2))
                # (Line 145) }
            EUDEndIf()
            # (Line 146) lastClickedUnitPtr = clickedUnitPtr;
        EUDEndIf()
        EUDTraceLog(146)
        lastClickedUnitPtr << (clickedUnitPtr)
        # (Line 147) }
        # (Line 148) }
    EUDEndIf()
