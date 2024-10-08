def on_button_pressed_a():
    bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music._play_default_background(music.built_in_playable_melody(Melodies.CHASE),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.stop_melody(MelodyStopOptions.ALL)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

emptyObstacleY = 0
ticks = 0
bird: game.LedSprite = None
index = 0
obstacles: List[game.LedSprite] = []
bird = game.create_sprite(0, 2)
bird.set(LedSpriteProperty.BLINK, 300)

def on_forever():
    global emptyObstacleY, ticks
    while len(obstacles) > 0 and obstacles[0].get(LedSpriteProperty.X) == 0:
        obstacles.remove_at(0).delete()
    for obstacle2 in obstacles:
        obstacle2.change(LedSpriteProperty.X, -1)
    if ticks % 3 == 0:
        emptyObstacleY = randint(0, 4)
        for index2 in range(5):
            if index2 != emptyObstacleY:
                obstacles.append(game.create_sprite(4, index2))
    for obstacle3 in obstacles:
        if obstacle3.get(LedSpriteProperty.X) == bird.get(LedSpriteProperty.X) and obstacle3.get(LedSpriteProperty.Y) == bird.get(LedSpriteProperty.Y):
            game.game_over()
    ticks += 1
    basic.pause(1000)
basic.forever(on_forever)
