# -*- coding: utf-8 -*-

# MIT License

# Copyright (c) 2020 Sandro Klippel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from .dockwidgetplugin import DockWidgetPlugin

__author__ = "Sandro Klippel"
__copyright__ = "Copyright 2020, Sandro Klippel"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Sandro Klippel"
__email__ = "sandroklippel at gmail.com"
__status__ = "Prototype"
__revision__ = '$Format:%H$'


class Plugin:
    """Plugin implementation
    """    

    def __init__(self, iface):
        """
        Constructor

        Args:
            iface (qgis.gui.QgisInterface): a reference to the QGIS GUI interface
        """        
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.dockwidget = None
        self.action = None
        self.icon = 'icon.png'
        self.name = 'Plugin'
        self.about = 'Dockable Plugin Template'

    def initGui(self):
        """
        This method is called by QGIS when the main GUI starts up or 
        when the plugin is enabled in the Plugin Manager.
        Only want to register the menu items and toolbar buttons here. 
        """        
        icon = QIcon(os.path.join(self.plugin_dir, self.icon))
        self.action = QAction(icon, self.name, self.iface.mainWindow())
        self.action.setWhatsThis(self.about)
        self.action.setStatusTip(self.about)
        self.action.setCheckable(True)
        self.action.triggered.connect(self.run)

        # for raster menu/toolbar
        # self.iface.addRasterToolBarIcon(self.action)
        # self.iface.addPluginToRasterMenu(self.name, self.action)

        # for plugin menu/toolbar
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(self.name, self.action)

        # for custom toolbar
        # self.toolbar = self.iface.addToolBar('Plugin')
        # self.toolbar.setObjectName('Plugin')
        # self.toolbar.addAction(self.action)

    def unload(self):
        """
        Will be executed when the plugin is disabled. 
        Either in the Plugin Manager or when QGIS shuts down.
        It removes the previously defined QAction object from
        the menu and remove the plugin icon from the toolbar.
        """

        # for raster menu/toolbar
        # self.iface.removePluginRasterMenu(self.name, self.action)
        # self.iface.removeRasterToolBarIcon(self.action)

        # for plugin menu/toolbar
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu(self.name, self.action)

        if self.dockwidget is not None:
            self.dockwidget.close()
            self.iface.removeDockWidget(self.dockwidget)
            del self.dockwidget

        # remove custom toolbar
        # if self.toolbar is not None:
            # del self.toolbar

    def run(self):
        """
        Executes the custom plugin functionality. [NOT REQUIRED]
        This method is called by the previously defined QAction object (callback), 
        which went into the toolbar icon and the menu entry.
        """
        if self.dockwidget is None:
            self.dockwidget = DockWidgetPlugin()
            self.iface.addDockWidget(Qt.RightDockWidgetArea , self.dockwidget)
            self.dockwidget.visibilityChanged.connect(self.visibility_changed)
            self.dockwidget.show()
        else:
            if self.dockwidget.isVisible():
                self.dockwidget.hide()
            else:
                self.dockwidget.show()

    def visibility_changed(self, change):
        """
        Change icon checked status with dockwidget visibility
        """
        self.action.setChecked(change)
        