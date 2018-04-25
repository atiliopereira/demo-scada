import sys

import taurus
from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication

app = TaurusApplication(sys.argv)
panel = Qt.QWidget()
layout = Qt.QHBoxLayout()
panel.setLayout(layout)

from taurus.qt.qtgui.display import TaurusLabel

w1, w2, w3 = TaurusLabel(), TaurusLabel(), TaurusLabel()
layout.addWidget(w1)
layout.addWidget(w2)
layout.addWidget(w3)
w1.model, w1.bgRole = 'sys/taurustest/1/position#label', ''
w2.model = 'sys/taurustest/1/position#rvalue.magnitude'
w3.model, w3.bgRole = 'sys/taurustest/1/position#rvalue.units', ''

panel.show()
sys.exit(app.exec_())