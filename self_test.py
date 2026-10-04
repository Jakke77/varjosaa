import tempfile
from PyQt6.QtCore import QSettings, Qt
from PyQt6.QtWidgets import QWidget
from widget import DesktopWidget, SettingsDialog, load_options

def run(app):
    with tempfile.TemporaryDirectory() as directory:
        owner = QWidget(); owner.settings = QSettings(directory+'/settings.ini',QSettings.Format.IniFormat)
        owner.widget_enabled = True
        owner.open_settings = lambda: None
        owner.settings.setValue('widget/weather_enabled',False)
        owner.desktop_widget = DesktopWidget(owner,owner.settings)
        widget = owner.desktop_widget
        widget.show();app.processEvents()
        assert widget.grab().toImage().pixelColor(0,0).alpha()==0
        dialog=SettingsDialog(owner)
        dialog.controls['weather_size'].setValue(22)
        assert widget.options['weather_size']==22
        dialog.reject()
        assert widget.options==load_options(owner.settings)
        widget.close();widget.deleteLater();owner.deleteLater();app.processEvents()
    print('Varjosaa self-test: PASS')
    print('Launcher mode: widget')
    return 0
