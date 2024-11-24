#=======================================================================
# Description:
# Entry point for the application
#=======================================================================
import sys

from PySide6.QtGui     import QIcon, QPixmap
from PySide6.QtCore    import QSize, Qt, QTimer
from PySide6.QtWidgets import QApplication, QSplashScreen

from mainwindow import MainWindow

#=======================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()

    app.setApplicationName("Personal Media Manager")

    app_icon = QIcon()
    app_icon.addFile('images/icons/pmm-16.png', QSize(16,16))
    app_icon.addFile('images/icons/pmm-24.png', QSize(24,24))
    app_icon.addFile('images/icons/pmm-32.png', QSize(32,32))
    app_icon.addFile('images/icons/pmm-48.png', QSize(48,48))
    app_icon.addFile('images/icons/pmm-256.png', QSize(256,256))
    app.setWindowIcon(app_icon)

    splash_pix = QPixmap("images/banner.png")

    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    splash.show()

    QTimer.singleShot(3000, splash.close)

    main_window = MainWindow()
    QTimer.singleShot(3000, widget.showMaximized)

    sys.exit(app.exec())


#=======================================================================