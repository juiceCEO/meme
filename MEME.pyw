
from asyncio.windows_events import INFINITE
import webbrowser
import time

timer = 0
while timer < INFINITE:
    time.sleep (1)
    webbrowser.open ("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    timer = timer + 1