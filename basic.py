import pygame, sys

pygame.init()

s_width = 1000
s_height = 900
screen = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption('Sound Board')
clock = pygame.time.Clock()

sound1 = pygame.mixer.Sound('soundboard_sounds/candyland.mp3')
sound2 = pygame.mixer.Sound('soundboard_sounds/fine.mp3')
sound3 = pygame.mixer.Sound('soundboard_sounds/fullsize.mp3')
sound4 = pygame.mixer.Sound('soundboard_sounds/gas.mp3')
sound5 = pygame.mixer.Sound('soundboard_sounds/letsgo.mp3')
sound6 = pygame.mixer.Sound('soundboard_sounds/letyougo.mp3')
sound7 = pygame.mixer.Sound('soundboard_sounds/movie.mp3')
sound8 = pygame.mixer.Sound('soundboard_sounds/steve.mp3')
sound9 = pygame.mixer.Sound('soundboard_sounds/tmp.mp3')

font = pygame.font.Font('Python/04B_19.TTF', 40)
text = font.render(('SoundBoard'), True, (0,0,0))
textRect = text.get_rect(center = (s_width //2, s_height // 2))

class BUTTON:
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self,screen,outline=None):
        if outline:
            pygame.draw.rect(screen,self.color,(self.x-2,self.y-2,self.width+4,self.height+4))
            
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

    def hover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False    


def gameWindow():

    screen.fill((231,165,33))
    # VERTICAL LINES
    pygame.draw.line(screen, (0,0,0), (250,0), (250, 900), 10)
    pygame.draw.line(screen, (0,0,0), (750,0), (750, 900), 10)
    
    # HORIZONTAL LINES
    pygame.draw.line(screen, (0,0,0), (0,225), (1000, 225), 10)
    pygame.draw.line(screen, (0,0,0), (0,675), (1000, 675), 10)

    # DRAW BUTTONS
    button.draw(screen, (255,255,255))
    button1.draw(screen, (255,255,255))
    button2.draw(screen, (255,255,255))
    button3.draw(screen, (255,255,255))
    mid_button.draw(screen, (255,255,255))
    button4.draw(screen, (255,255,255))
    button5.draw(screen, (255,255,255))
    button6.draw(screen, (255,255,255))
    button7.draw(screen, (255,255,255))

    screen.blit(text, textRect)

button = BUTTON((255,255,255), 0,0,245,220)
button1 = BUTTON((255,255,255), 0,230,245,220 * 2)
button2 = BUTTON((255,255,255), 0,680,245,220)
button3 = BUTTON((255,255,255), 255,0,245 *2,220)
mid_button = BUTTON((255,255,255), (s_width // 2) -245,(s_height // 2) - 220,245 * 2,220 * 2)
button4 = BUTTON((255,255,255), 755,0,245,220)
button5 = BUTTON((255,255,255), 755,230,245,220 * 2)
button6 = BUTTON((255,255,255), 255,s_height - 220,245 *2,220)
button7 = BUTTON((255,255,255), 755,680,245,220)



run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.hover(pos):
                sound1.play()
            elif button1.hover(pos):
                sound2.play()
            elif button2.hover(pos):
                sound3.play()
            elif button3.hover(pos):
                sound4.play()
            elif mid_button.hover(pos):
                sound5.play()
            elif button4.hover(pos):
                sound6.play()
            elif button5.hover(pos):
                sound7.play()
            elif button6.hover(pos):
                sound8.play()
            elif button7.hover(pos):
                sound9.play()
        if event.type == pygame.MOUSEMOTION:

            # BUTTON HOVERING
            if button.hover(pos):
                button.color = (123,123,123)
            else:
                button.color = (155,24,47)
            ###################
            if button1.hover(pos):
                button1.color = (155,24,47)
            else:
                button1.color = (61,214,235)
            ###################
            if button2.hover(pos):
                button2.color = (245,194,91)
            else:
                button2.color = (54,98,54)  
            ###################
            if button3.hover(pos):
                button3.color = (177,61,235)
            else:
                button3.color = (11,231,97) 
            ###################
            if mid_button.hover(pos):
                mid_button.color = (255,252,45)
            else:
                mid_button.color = (98,54,77)
            ###################
            if mid_button.hover(pos):
                mid_button.color = (255,252,45)
            else:
                mid_button.color = (98,54,77)
            ###################
            if button4.hover(pos):
                button4.color = (0,255,116)
            else:
                button4.color = (49,109,237)
            ###################
            if button5.hover(pos):
                button5.color = (218,25,3)
            else:
                button5.color = (3,112,235)
            ###################
            if button6.hover(pos):
                button6.color = (236,252,75)
            else:
                button6.color = (240,31,240)
              ###################
            if button7.hover(pos):
                button7.color = (255,2,0)
            else:
                button7.color = (2,255,0)
    gameWindow()
    pygame.display.update()