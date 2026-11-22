
import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((612, 409))
pygame.display.set_caption("Music Player")

background = pygame.image.load("./images/background.jpg")

songs = os.listdir("./tracks")
songs = [song for song in songs if song.lower().endswith((".mp3", ".wav", ".ogg"))]
songs.sort()

print(songs)

playingMusic = False
index = 0
done = False

font = pygame.font.SysFont("Arial", 24)

if songs:
    pygame.mixer.music.load("./tracks/" + songs[index])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                if songs:
                    pygame.mixer.music.play()
                    playingMusic = True

            elif event.key == pygame.K_SPACE:
                if playingMusic:
                    pygame.mixer.music.pause()
                    playingMusic = False
                else:
                    pygame.mixer.music.unpause()
                    playingMusic = True

            elif event.key == pygame.K_LEFT:
                if songs:
                    index = (index - 1) % len(songs)
                    pygame.mixer.music.load("./tracks/" + songs[index])
                    pygame.mixer.music.play()
                    playingMusic = True

            elif event.key == pygame.K_RIGHT:
                if songs:
                    index = (index + 1) % len(songs)
                    pygame.mixer.music.load("./tracks/" + songs[index])
                    pygame.mixer.music.play()
                    playingMusic = True

            elif event.key == pygame.K_q:
                done = True

    screen.blit(background, (0, 0))

    if songs:
        track_name = songs[index]

        track_text = font.render(
            "Current track: " + track_name,
            True,
            (255, 255, 255)
        )

        screen.blit(track_text, (20, 20))

        current_time = pygame.mixer.music.get_pos() // 1000

        minutes = current_time // 60
        seconds = current_time % 60

        time_text = font.render(
            f"Time: {minutes:02d}:{seconds:02d}",
            True,
            (255, 255, 255)
        )

        screen.blit(time_text, (20, 60))

    else:
        no_music = font.render(
            "No music files found",
            True,
            (255, 255, 255)
        )
        screen.blit(no_music, (20, 20))

    pygame.display.update()

pygame.quit()
