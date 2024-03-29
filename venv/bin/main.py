#!/usr/bin/env python3


class Project:

    def __init__(self, project_name, max_row):
        self.patterns = []
        self.current_row = 0
        self.projectName = project_name
        self.all_rows = []
        self.max_row = max_row

    def read_row(self, row_num):
        row = []
        for p in self.patterns:
            row.append(', '.join(p.get_row(row_num)))
            row.append('sm')
        row.pop(len(row)-1)
        row_str = ', '.join(row)
        return row_str

    def add_all_rows(self):
        row_num = 0
        while row_num < self.max_row:
            row = panel.read_row(row_num)
            self.all_rows.append("Row " + str(row_num + 1) + ": " + row)
            row_num += 1

    def get_row(self, index):
        self.current_row = index
        data = self.all_rows[self.current_row]
        return data

    def add_pattern(self, pattern):
        self.patterns.append(pattern)


class Pattern:

    def __init__(self, name):
        self.name = name
        self.stitch_map = []
        self.multiples_of = 0
        self.multiples_change = 0
        self.max_row = 0

    def is_correct_stitch_count(self, count):
        return True if ((count % self.multiples_of) - self.multiples_change == 0) else False

    def add_row(self, row):
        self.stitch_map.append(row)
        self.max_row += 1

    def get_row(self, rowNumber):
        index = rowNumber % self.max_row
        return self.stitch_map[index]

    def set_multiples(self, multiple_of, multiple_change):
        self.multiples_of = multiple_of
        self.multiples_change = multiple_change


class TravelersKnapsackBack:

    def __init__(self):
        self.panel = Project('TravelersKnapsackBackPanel', 18 * 3)
        self.panel.add_pattern(bag.side_panels())
        self.panel.add_pattern(bag.make_waffle_pattern())
        self.panel.add_pattern(bag.make_double_leaf_pattern())
        self.panel.add_pattern(bag.make_waffle_pattern())
        self.panel.add_pattern(bag.side_panels())

    def make_waffle_pattern(self):
        waffle = Pattern('Waffle')
        waffle.add_row(['p2', '*RT', 'p2', 'rep from *'])
        waffle.add_row(['k2', '*p2', 'k2', 'rep from *'])
        waffle.add_row(['p1', '*k2tog', '[yo]twice', 'ssk', 'rep from * to last st', 'p1'])
        waffle.add_row(['p2', '*k1p1 in double yo', 'p2', 'rep from *'])
        waffle.add_row(['k2', '*p2', 'LT', 'rep from * to last 4 sts', 'p2', 'k2'])
        waffle.add_row(['p2', '*k2', 'p2', 'rep from *'])
        waffle.add_row(
            ['p1', 'yo', '*ssk', 'k2tog', '[yo]twice', 'rep from * to last 5 sts', 'ssk', 'k2tog', 'yo', 'p1'])
        waffle.add_row(['k1', '*p2', 'k1p1 into double yo', 'rep from * to last 4sts', 'p2', 'k2'])
        return waffle

    def make_double_leaf_pattern(self):
        dlp = Pattern('DoubleLeafPattern')
        dlp.add_row(
            ['p8', 'p2tog', 'k1', 'yo', 'k1', 'yo', 'k1', 'k1fb', 'k1''k1fb', 'k1', 'yo', 'k1', 'yo', 'k1', 'p2tog',
             'p8'])
        dlp.add_row(['k9', 'p5', 'k1', 'p3', 'k1', 'p5', 'p9'])
        dlp.add_row(
            ['p7', 'p2tog', 'k2', 'yo', 'k1', 'yo', 'k2', 'p1fb', 'k3', 'p1fb', 'k2', 'yo', 'k1', 'yo', 'k2', 'p2tog',
             'p7'])
        dlp.add_row(['k8', 'p7', 'k2', 'p3', 'k2', 'p7', 'k8'])
        dlp.add_row(
            ['p6', 'p2tog', 'k3', 'yo', 'k1', 'yo', 'k3', 'p1fb', 'p1', 'k3', 'p1', 'p1fb', 'k3', 'yo', 'k1', 'yo',
             'k3', 'p2tog', 'p6'])
        dlp.add_row(['k7', 'p9', 'k3', 'p3', 'k3', 'p9', 'k7'])
        dlp.add_row(
            ['p5', 'p2tog', 'k4', 'yo', 'k1', 'yo', 'k4', 'p1fb', 'p2', 'k3', 'p2', 'p1fb', 'k4', 'yo', 'k1', 'yo',
             'k4', 'p2tog', 'p5'])
        dlp.add_row(['k6', 'p11', 'k4', 'p3', 'k4', 'p11', 'k6'])
        dlp.add_row(
            ['p4', 'p2tog', 'ssk', 'k7', 'k2tog', 'p1fb', 'p3', 'k3', 'p3', 'p1fb', 'ssk', 'k7', 'k2tog', 'p2tog',
             'p4'])
        dlp.add_row(['k5', 'p9', 'k5', 'p3', 'k5', 'p9', 'k5'])
        dlp.add_row(
            ['p3', 'p2tog', 'ssk', 'k5', 'k2tog', 'p1fb', 'p4', 'k3', 'p4', 'p1fb', 'ssk', 'k5', 'k2tog', 'p2tog',
             'p3'])
        dlp.add_row(['k4', 'p7', 'k6', 'p3', 'k6', 'p7', 'k4'])
        dlp.add_row(
            ['p2', 'p2tog', 'ssk', 'k3', 'k2tog', 'p1fb', 'p5', 'k2', 'm1', 'k1', 'm1', 'k1', 'p5', 'p1fb', 'ssk', 'k2',
             'k2tog', 'p2tog', 'p2'])
        dlp.add_row(['k3', 'p5', 'k7', 'p5', 'k7', 'p5', 'k3'])
        dlp.add_row(
            ['p1', 'p2tog', 'ssk', 'k2', 'k2tog', 'p1fb', 'p6', 'k1', 'm1', 'k3', 'm1', 'k1', 'p6', 'p1fb', 'ssk', 'k2',
             'k2tog', 'p2tog', 'p1'])
        dlp.add_row(['k2', 'p3', 'k8', 'p7', 'k7', 'p3', 'k2'])
        dlp.add_row(
            ['p2', 'sl2', 'k1', 'p2 sso', 'p6', 'p2tog', 'k1', 'm1', 'k5', 'm1', 'k1', 'p2tog', 'p6', 'sl2', 'k1',
             'p2 sso', 'p2'])
        dlp.add_row(['k10', 'p9', 'k10'])
        return dlp

    def side_panels(self):
        side = Pattern('border')
        side.add_row(['k2'])
        side.add_row(['p2'])
        return side

    def get_panel(self):
        return self.panel


if __name__ == "__main__":
    bag = TravelersKnapsackBack()
    panel = bag.get_panel()



