import subprocess
import winsound
import sys

def trigger_notification(title: str, message: str):
    """
    Triggers a native Windows 11 notification and plays a sound.
    Uses PowerShell to access the System.Windows.Forms.NotifyIcon class.
    """
    # 1. Play a standard alert sound
    # winsound.MB_ICONEXCLAMATION plays the standard Windows alert sound.
    try:
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        # Alternatively, we could do a custom beep: winsound.Beep(1000, 500)
    except Exception as e:
        print(f"Warning: Failed to play sound: {e}")

    # 2. Trigger the Toast / Balloon Notification via PowerShell
    # We use a short PowerShell script to generate a notification without needing external libraries.
    ps_script = f"""
    Add-Type -AssemblyName System.Windows.Forms
    $notify = New-Object System.Windows.Forms.NotifyIcon
    $notify.Icon = [System.Drawing.SystemIcons]::Information
    $notify.BalloonTipTitle = '{title}'
    $notify.BalloonTipText = '{message}'
    $notify.Visible = $True
    $notify.ShowBalloonTip(10000)
    Start-Sleep -Seconds 5
    $notify.Dispose()
    """
    
    try:
        # Run the powershell script in a subprocess
        subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_script],
            creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print(f"Warning: Failed to trigger Windows notification: {e}")
