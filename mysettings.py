#-----------------------------------------------------------
#
# Plain Geometry Editor is a QGIS plugin to edit geometries
# using plain text editors (WKT, WKB)
#
# Copyright    : (C) 2013 Denis Rouzaud
# Email        : denis.rouzaud@gmail.com
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this progsram; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
#---------------------------------------------------------------------

from PyQt4.QtGui import QColor
from qgis.gui import QgsRubberBand

from qgissettingmanager import *

pluginName = "plaingeometryeditor"

class MySettings(SettingManager):
    def __init__(self):
        SettingManager.__init__(self, pluginName)

        self.addSetting("sketchGeometry", "bool", "global",  True)
        self.addSetting("featureRubberColor", "color", "global",  QColor(0, 0, 255))
        self.addSetting("featureRubberSize", "double", "global",  .6)
        self.addSetting("featureRubberAlpha", "integer", "global",  100)
        self.addSetting("currentPointRubberColor", "color", "global",  QColor(255, 0, 0))
        self.addSetting("currentPointRubberIcon", "integer", "global",  int(QgsRubberBand.ICON_BOX))
        self.addSetting("currentPointRubberSize", "integer", "global",  3)
        self.addSetting("displayPointRubber", "bool", "global",  True)
