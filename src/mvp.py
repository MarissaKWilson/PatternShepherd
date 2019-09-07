

class TravelersKnapsackBack:

    def __init__(self):
        self.panel = Project('TravelersKnapsackBackPanel', 54)
        self.panel.addPattern(self.make_border())
        self.panel.addPattern(self.make_waffle_pattern())
        self.panel.addPattern(self.make_double_leaf_pattern())
        self.panel.addPattern(self.make_waffle_pattern())
        self.panel.addPattern(self.make_border())

    def make_waffle_pattern(self):
        stitch_map = [['p2','*RT','p2','rep from *'],
        ['k2','*p2','k2','rep from *'],
        ['p1','*k2tog','[yo]twice','ssk','rep from * to last st','p1'],
        ['p2','*k1p1 in double yo','p2','rep from *'],
        ['k2','*p2','LT','rep from * to last 4 sts','p2','k2'],
        ['p2','*k2','p2','rep from *'],
        ['p1','yo','*ssk','k2tog','[yo]twice','rep from * to last 5 sts','ssk','k2tog','yo','p1'],
        ['k1','*p2','k1p1 into double yo','rep from * to last 4sts','p2','k2']]
        return Pattern('Waffle', stitch_map)

    def make_double_leaf_pattern(self):
        stitch_map=[['p8','p2tog','k1','yo','k1','yo','k1','k1fb','k1''k1fb','k1','yo','k1','yo','k1','p2tog','p8'],
        ['k9','p5','k1','p3','k1','p5','p9'],
        ['p7','p2tog','k2','yo','k1','yo','k2','p1fb','k3','p1fb','k2','yo','k1','yo','k2','p2tog','p7'],
        ['k8','p7','k2','p3','k2','p7','k8'],
        ['p6','p2tog','k3','yo','k1','yo','k3','p1fb','p1','k3','p1','p1fb','k3','yo','k1','yo','k3','p2tog','p6'],
        ['k7','p9','k3','p3','k3','p9','k7'],
        ['p5','p2tog','k4','yo','k1','yo','k4','p1fb','p2','k3','p2','p1fb','k4','yo','k1','yo','k4','p2tog','p5'],
        ['k6','p11','k4','p3','k4','p11','k6'],
        ['p4','p2tog','ssk','k7','k2tog','p1fb','p3','k3','p3','p1fb','ssk','k7','k2tog','p2tog','p4'],
        ['k5','p9','k5','p3','k5','p9','k5'],
        ['p3','p2tog','ssk','k5','k2tog','p1fb','p4','k3','p4','p1fb','ssk','k5','k2tog','p2tog','p3'],
        ['k4','p7','k6','p3','k6','p7','k4'],
        ['p2','p2tog','ssk','k3','k2tog','p1fb','p5','k2','m1','k1','m1','k1','p5','p1fb','ssk','k2','k2tog','p2tog','p2'],
        ['k3','p5','k7','p5','k7','p5','k3'],
        ['p1','p2tog','ssk','k2','k2tog','p1fb','p6','k1','m1','k3','m1','k1','p6','p1fb','ssk','k2','k2tog','p2tog','p1'],
        ['k2','p3','k8','p7','k7','p3','k2'],
        ['p2','sl2','k1','p2 sso','p6','p2tog','k1','m1','k5','m1','k1','p2tog','p6','sl2','k1','p2 sso','p2'],
        ['k10','p9','k10']]
        return  Pattern('Double Leaf Pattern', stitch_map)

    def make_border(self):
        stitch_map=[['k2'],['p2']]
        return Pattern('Border', stitch_map)

    def get_panel(self):
        return self.panel


class Project:

    def __init__(self, project_name, max_row):
        self.patterns = []
        self.currentRow = 0
        self.project_name = project_name
        self.max_row = max_row
        self.all_rows = []

    def read_row(self, rowNum):
        row = []
        for p in self.patterns:
            row.append(', '.join(p.get_row(rowNum)))
            row.append('sm')
        row.pop(len(row)-1)
        rowStr = ', '.join(row)
        return rowStr

    def get_row(self, row_num):
        self.currentRow = row_num
        return self.all_rows[row_num]

    def addPattern(self, pattern):
        self.patterns.append(pattern)

    def make_all_rows(self):
        current_row = 0
        while current_row < self.max_row:
            self.all_rows.append('Row ' + str(current_row+1) + ': ' + self.read_row(current_row))
            current_row+=1

    def read_all_rows(self):
        current_row = 0
        while current_row < self.max_row:
            print(self.all_rows[current_row])
            current_row+=1

class Pattern:

    def __init__(self, name, stitch_map):
        self.name = name
        self.stitch_map = stitch_map
        self.multiples_of = 0
        self.multiples_change = 0
        self.max_row = len(stitch_map)

    def is_correct_stitch_count(self, count):
        return True if ((count % self.multiples_of) - self.multiples_change == 0) else False

    def add_row(self, row):
        self.stitch_map.append(row)

    def get_row(self, rowNumber):
        index = rowNumber % self.max_row
        return self.stitch_map[index]

    def set_multiples(self, multiple_of, multiple_change):
        self.multiples_of = multiple_of
        self.multiples_change = multiple_change


if __name__=="__main__":
    bag = TravelersKnapsackBack()
    bag_panel = bag.get_panel()
    bag_panel.make_all_rows()

    row_num = int(input("N for next, P for previous, Q to quit\n Row number please...\n"))-1
    
    b_next = input(bag_panel.get_row(row_num))
    while b_next != 'Q':
        if b_next == 'N' or b_next == 'n':
            row_num+=1
        else:
            row_num-=1
        b_next = input(bag_panel.get_row(row_num))
        print(b_next)



