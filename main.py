import pygame
from pynput import keyboard, mouse

pygame.mixer.init()

mouse_click_sound = pygame.mixer.Sound("data/mouse_released.mp3")


def on_click(x, y, button, pressed):
    if pressed:
        mouse_click_sound.play()

mouse_listener = mouse.Listener(on_click=on_click)

mouse_listener.start()
mouse_listener.join()
