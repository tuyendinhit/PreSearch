# Auto Almost Everything
# Youtube Channel https://www.youtube.com/channel/UC4cNnZIrjAC8Q4mcnhKqPEQ
# Please read README.md carefully before use

from win10toast import ToastNotifier


def notify(app, content):
    try:
        toast = ToastNotifier()
        toast.show_toast(app, content, duration=5)
    except:
        pass
