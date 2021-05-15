# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

from win10toast import ToastNotifier


def notify(app, content):
    try:
        toast = ToastNotifier()
        toast.show_toast(app, content, duration=5)
    except:
        pass
