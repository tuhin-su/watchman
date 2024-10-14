from plyer import notification
import os

icon_path = os.path.join(os.path.dirname(__file__), "icon/icon.png")
print(icon_path)
# Show notification
def notify(msg):
    notification.notify(
        title="Watchman",
        message=str(msg),
        app_icon=icon_path,
        timeout=10, 
        toast=True
    )
