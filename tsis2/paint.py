
import pygame
import math
from datetime import datetime
from tools import flood_fill

pygame.init()

WIDTH = 1000
HEIGHT = 750
TOOLBAR_HEIGHT = 150

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (160, 50, 200)
GRAY = (210, 210, 210)

colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE]
current_color = BLACK

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

font = pygame.font.SysFont("Arial", 16)
text_font = pygame.font.SysFont("Arial", 24)

tools = [
    "Pencil",
    "Line",
    "Rectangle",
    "Circle",
    "Eraser",
    "Square",
    "Right Triangle",
    "Equilateral Triangle",
    "Rhombus",
    "Fill",
    "Text"
]

current_tool = "Pencil"

brush_sizes = [2, 5, 10]
brush_size = 5

drawing = False
start_pos = None
previous_pos = None
current_pos = None

text_active = False
text_content = ""
text_position = None

clock = pygame.time.Clock()
running = True


def draw_shape(surface, tool, color, start, end, size):

    x1, y1 = start
    x2, y2 = end

    if tool == "Line":
        pygame.draw.line(surface, color, start, end, size)

    elif tool == "Rectangle":
        rect = pygame.Rect(x1, y1, x2 - x1, y2 - y1)
        rect.normalize()
        pygame.draw.rect(surface, color, rect, size)

    elif tool == "Circle":
        radius = int(math.hypot(x2 - x1, y2 - y1))

        if radius > 0:
            pygame.draw.circle(surface, color, start, radius, size)

    elif tool == "Square":
        side = min(abs(x2 - x1), abs(y2 - y1))

        square_x = x1 if x2 >= x1 else x1 - side
        square_y = y1 if y2 >= y1 else y1 - side

        rect = pygame.Rect(square_x, square_y, side, side)
        pygame.draw.rect(surface, color, rect, size)

    elif tool == "Right Triangle":
        points = [
            start,
            (x2, y1),
            end
        ]

        pygame.draw.polygon(surface, color, points, size)

    elif tool == "Equilateral Triangle":
        width = x2 - x1
        height = int(abs(width) * math.sqrt(3) / 2)

        direction = -1 if y2 <= y1 else 1

        points = [
            start,
            (x2, y1),
            (x1 + width // 2, y1 + direction * height)
        ]

        pygame.draw.polygon(surface, color, points, size)

    elif tool == "Rhombus":
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        points = [
            (center_x, y1),
            (x2, center_y),
            (center_x, y2),
            (x1, center_y)
        ]

        pygame.draw.polygon(surface, color, points, size)


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if text_active:

                if event.key == pygame.K_RETURN:
                    if text_content:
                        text_image = text_font.render(
                            text_content, True, current_color
                        )
                        canvas.blit(text_image, text_position)

                    text_active = False
                    text_content = ""

                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                    text_content = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_content = text_content[:-1]

                else:
                    if event.unicode.isprintable():
                        text_content += event.unicode

            else:

                if event.key == pygame.K_1:
                    brush_size = 2

                elif event.key == pygame.K_2:
                    brush_size = 5

                elif event.key == pygame.K_3:
                    brush_size = 10

                elif event.key == pygame.K_s and (
                    pygame.key.get_mods() & pygame.KMOD_CTRL
                ):
                    filename = datetime.now().strftime(
                        "drawing_%Y%m%d_%H%M%S.png"
                    )
                    pygame.image.save(canvas, filename)
                    print("Saved:", filename)

        elif event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            if y < TOOLBAR_HEIGHT:

                if y < 50:

                    for i, color in enumerate(colors):
                        button = pygame.Rect(
                            10 + i * 45, 10, 35, 35
                        )

                        if button.collidepoint(x, y):
                            current_color = color

                    if 300 <= x <= 370:
                        brush_size = 2
                    elif 375 <= x <= 445:
                        brush_size = 5
                    elif 450 <= x <= 520:
                        brush_size = 10

                else:

                    for i, name in enumerate(tools):
                        button = pygame.Rect(
                            5 + i * 90, 65, 86, 40
                        )

                        if button.collidepoint(x, y):
                            current_tool = name

            else:

                canvas_pos = (x, y - TOOLBAR_HEIGHT)

                if current_tool == "Fill":
                    flood_fill(canvas, canvas_pos, current_color)

                elif current_tool == "Text":
                    text_active = True
                    text_content = ""
                    text_position = canvas_pos

                else:
                    drawing = True
                    start_pos = canvas_pos
                    previous_pos = canvas_pos
                    current_pos = canvas_pos

                    if current_tool == "Pencil":
                        pygame.draw.circle(
                            canvas,
                            current_color,
                            canvas_pos,
                            max(1, brush_size // 2)
                        )

        elif event.type == pygame.MOUSEMOTION:

            x, y = event.pos

            if drawing and y >= TOOLBAR_HEIGHT:

                current_pos = (x, y - TOOLBAR_HEIGHT)

                if current_tool == "Pencil":
                    pygame.draw.line(
                        canvas,
                        current_color,
                        previous_pos,
                        current_pos,
                        brush_size
                    )

                elif current_tool == "Eraser":
                    pygame.draw.line(
                        canvas,
                        WHITE,
                        previous_pos,
                        current_pos,
                        brush_size * 3
                    )

                previous_pos = current_pos

        elif event.type == pygame.MOUSEBUTTONUP:

            if drawing and start_pos is not None:

                x, y = event.pos

                if y >= TOOLBAR_HEIGHT:
                    end_pos = (x, y - TOOLBAR_HEIGHT)

                    if current_tool not in ["Pencil", "Eraser"]:
                        draw_shape(
                            canvas,
                            current_tool,
                            current_color,
                            start_pos,
                            end_pos,
                            brush_size
                        )

            drawing = False
            start_pos = None
            previous_pos = None
            current_pos = None

    screen.fill(GRAY)

    pygame.draw.rect(
        screen,
        GRAY,
        (0, 0, WIDTH, TOOLBAR_HEIGHT)
    )

    for i, color in enumerate(colors):
        button = pygame.Rect(10 + i * 45, 10, 35, 35)
        pygame.draw.rect(screen, color, button)

        if current_color == color:
            pygame.draw.rect(screen, WHITE, button, 2)

    size_label = font.render("Brush size:", True, BLACK)
    screen.blit(size_label, (285, 18))

    for i, size in enumerate(brush_sizes):
        button = pygame.Rect(370 + i * 75, 10, 65, 35)

        pygame.draw.rect(screen, WHITE, button)

        if brush_size == size:
            pygame.draw.rect(screen, BLUE, button, 3)
        else:
            pygame.draw.rect(screen, BLACK, button, 1)

        size_text = font.render(str(size) + " px", True, BLACK)
        screen.blit(size_text, (button.x + 12, button.y + 9))

    for i, name in enumerate(tools):
        button = pygame.Rect(5 + i * 90, 65, 86, 40)

        pygame.draw.rect(screen, WHITE, button)

        if current_tool == name:
            pygame.draw.rect(screen, BLUE, button, 3)
        else:
            pygame.draw.rect(screen, BLACK, button, 1)

        tool_text = font.render(name, True, BLACK)
        screen.blit(tool_text, (button.x + 3, button.y + 12))

    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    if drawing and current_tool == "Line" and current_pos:
        preview = canvas.copy()

        pygame.draw.line(
            preview,
            current_color,
            start_pos,
            current_pos,
            brush_size
        )

        screen.blit(preview, (0, TOOLBAR_HEIGHT))

    if text_active:
        text_image = text_font.render(
            text_content, True, current_color
        )

        screen.blit(
            text_image,
            (text_position[0], text_position[1] + TOOLBAR_HEIGHT)
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()


