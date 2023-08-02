import rotatescreen
import time

screen = rotatescreen.get_primary_display()
start = screen.current_orientation

for i in range(1, 21):
  position = abs((start - i * 90) % 360)
  screen.rotate_to(position)
  time.sleep(0.2)
