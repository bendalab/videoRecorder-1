__author__ = 'Jan Grewe'
try:
    from PyQt5 import QtCore, QtWidgets

except:
    print('Unfortunately, your system misses the PyQt5 packages.')
    quit()

from odml import *
from datetime import *

class MetadataEntry(QtWidgets.QWidget):
    """This class creates label-and-lineedit-combinations in the tabs and allows for feedback communication."""

    def __init__(self, prop, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.prop = prop.clone()

        self.label = QtWidgets.QLabel(self.prop.name + ':')
        self.line_edit = QtWidgets.QLineEdit(str(self.prop.value.value))
        if self.prop.value.dtype == 'date' and not self.prop.value.value:
            d = datetime.today()
            self.line_edit.setText('{0}-{1}-{2}'.format(d.year, d.month, d.day))
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        if self.prop.value.definition:
            self.setToolTip(self.prop.value.definition)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.line_edit.editingFinished.connect(self.data_changed)

    def data_changed(self):
        self.prop.value.value = self.line_edit.text()

    def get_property(self):
        return self.prop
