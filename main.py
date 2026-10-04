"""Varjosää standalone transparent desktop weather widget."""
import sys
import tempfile
from PyQt6.QtCore import QSettings, QStandardPaths, QLockFile, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QDialog
from widget import DesktopWidget, SettingsDialog, load_options
from instance import server_name, request_mode, start_server

STYLE = "QDialog { background: #101318; color: #dbe6ef; } QDialog QWidget { color: #dbe6ef; } QLineEdit, QSpinBox, QComboBox { background: #20252d; color: #dbe6ef; padding: 5px; border: 1px solid #25c5ff; } QPushButton { background: #20252d; color: #25c5ff; padding: 7px; }"

class Controller(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings()
        self.widget_enabled = True
        self.desktop_widget = DesktopWidget(self, self.settings)
        self.desktop_widget.show()
    def open_settings(self):
        dialog = SettingsDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            options = dialog.options()
            for key, value in options.items():
                self.settings.setValue('widget/' + key, value)
            self.desktop_widget.apply_options(options)
    def set_widget_enabled(self, enabled):
        self.desktop_widget.setVisible(enabled)


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName('Jakke77')
    app.setApplicationName('Varjosaa')
    app.setApplicationDisplayName('Varjosää')
    app.setQuitOnLastWindowClosed(False)
    app.setStyleSheet(STYLE)
    if '--self-test' in sys.argv:
        from self_test import run
        return run(app)
    name = server_name(QSettings().fileName())
    if request_mode(name, 'widget'):
        return 0
    lock = QLockFile(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.RuntimeLocation) + '/varjosaa.lock')
    if not lock.tryLock(1000):
        print('Varjosää on jo käynnissä.', file=sys.stderr)
        return 1
    owner = Controller()
    server = start_server(name, owner, lambda command: QTimer.singleShot(0, owner.open_settings))
    return app.exec()

if __name__ == '__main__':
    sys.exit(main())
