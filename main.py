#=======================================================================
# Description:
# Entry point for the application
#=======================================================================
import sys

from PySide6.QtGui     import QIcon, QPixmap
from PySide6.QtCore    import QSize, Qt, QTimer, QThread, Signal
from PySide6.QtWidgets import QApplication, QSplashScreen

from mainwindow import MainWindow

class InitializationThread(QThread):
    """
    A thread class that performs initialization tasks by sleeping for a specified duration
    and emits a signal upon completion.

    Attributes:
    finished (Signal): A signal that is emitted when the thread has completed its execution.

    Methods:
    run(): Executes the thread's task, which involves sleeping for a total of 5 seconds
           (500 milliseconds per iteration for 10 iterations) and then emits the finished signal.
    """
    finished = Signal()

    def run(self):
        """
        Executes the thread's task by sleeping for 500 milliseconds in each of the 10 iterations.
        After completing the iterations, it emits the finished signal to indicate completion.
        """
        for i in range(10):
            self.msleep(500)

        self.finished.emit()

#=======================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Personal Media Manager")

    app_icon = QIcon()
    app_icon.addFile('images/icons/pmm-16.png', QSize(16,16))
    app_icon.addFile('images/icons/pmm-24.png', QSize(24,24))
    app_icon.addFile('images/icons/pmm-32.png', QSize(32,32))
    app_icon.addFile('images/icons/pmm-48.png', QSize(48,48))
    app_icon.addFile('images/icons/pmm-256.png', QSize(256,256))
    app.setWindowIcon(app_icon)

    splash_pix = QPixmap("images/banner.png")
    splash     = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    splash.show()

    widget = MainWindow()

    thread = InitializationThread()
    thread.finished.connect(splash.close)
    thread.finished.connect(widget.showMaximized)

    thread.start()

    sys.exit(app.exec())


#=======================================================================