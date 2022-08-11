from controller import *


def main():
    try:
        app = QApplication([])
        window = Controller()
        window.show()
        app.exec_()
    except:
        print("Caution: Error has occurred")


if __name__ == '__main__':
    main()
