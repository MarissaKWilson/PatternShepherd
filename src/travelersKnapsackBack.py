from pattern import Pattern
from project import Project

class TravelersKnapsackBack:

    def __init__(self):
        self.panel=Project('TravelersKnapsackBackPanel')
        self.panel.addPattern(self.make_waffle_pattern())
        self.panel.addPattern(self.make_double_leaf_pattern())
        self.panel.addPattern(self.make_waffle_pattern())

    def make_waffle_pattern(self):
        waffle=Pattern('Waffle')
        waffle.add_row(['p2','*RT','p2','rep from *'])
        waffle.add_row(['k2','*p2','k2','rep from *'])
        waffle.add_row(['p1','*k2tog','[yo]twice','ssk','rep from * to last st','p1'])
        waffle.add_row(['p2','*k1p1 in double yo','p2','rep from *'])
        waffle.add_row(['k2','*p2','LT','rep from * to last 4 sts','p2','k2'])
        waffle.add_row(['p2','*k2','p2','rep from *'])
        waffle.add_row(['p1','yo','*ssk','k2tog','[yo]twice','rep from * to last 5 sts','ssk','k2tog','yo','p1'])
        waffle.add_row(['k1','*p2','k1p1 into double yo','rep from * to last 4sts','p2','k2'])
        return waffle

    def make_double_leaf_pattern(self):
        dlp = Pattern('DoubleLeafPattern')
        dlp.add_row(['p8','p2tog','k1','yo','k1','yo','k1','k1fb','k1''k1fb','k1','yo','k1','yo','k1','p2tog','p8'])
        dlp.add_row(['k9','p5','k1','p3','k1','p5','p9'])
        dlp.add_row(['p7','p2tog','k2','yo','k1','yo','k2','p1fb','k3','p1fb','k2','yo','k1','yo','k2','p2tog','p7')]
        dlp.add_row(['k8','p7','k2','p3','k2','p7','k8'])
        dlp.add_row(['p6','p2tog','k3','yo','k1','yo','k3','p1fb','p1','k3','p1','p1fb','k3','yo','k1','yo','k3','p2tog','p6'])
        dlp.add_row(['k7','p9','k3','p3','k3','p9','k7'])
        dlp.add_row(['p5','p2tog','k4','yo','k1','yo','k4','p1fb','p2','k3','p2','p1fb','k4','yo','k1','yo','k4','p2tog','p5'])
        dlp.add_row(['k6','p11','k4','p3','k4','p11','k6'])
        dlp.add_row(['p4','p2tog','ssk','k7','k2tog','p1fb','p3','k3','p3','p1fb','ssk','k7','k2tog','p2tog','p4'])
        dlp.add_row(['k5','p9','k5','p3','k5','p9','k5'])
        dlp.add_row(['p3','p2tog','ssk','k5','k2tog','p1fb','p4','k3','p4','p1fb','ssk','k5','k2tog','p2tog','p3'])
        dlp.add_row(['k4','p7','k6','p3','k6','p7','k4'])
        dlp.add_row(['p2','p2tog','ssk','k3','k2tog','p1fb','p5','k2','m1','k1','m1','k1','p5','p1fb','ssk','k2','k2tog','p2tog','p2'])
        dlp.add_row(['k3','p5','k7','p5','k7','p5','k3'])
        dlp.add_row(['p1','p2tog','ssk','k2','k2tog','p1fb','p6','k1','m1','k3','m1','k1','p6','p1fb','ssk','k2','k2tog','p2tog','p1'])
        dlp.add_row(['k2','p3','k8','p7','k7','p3','k2'])
        dlp.add_row(['p2','sl2','k1','p2 sso','p6','p2tog','k1','m1','k5','m1','k1','p2tog','p6','sl2','k1','p2 sso','p2'])
        dlp.add_row(['k10','p9','k10'])
        return dlp