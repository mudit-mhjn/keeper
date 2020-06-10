#this file creates a notification for a certain amount of time.

from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("TO-DO", "TO_DO_DETAIL", duration=10)

