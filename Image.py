import pygame
pygame.init()
screen_width,screen_height = 500,400
display_surface = pygame.display.set_mode((screen_width,screen_height ))
pygame.display.set_caption("Adding an image!!")
spaceimg = pygame.transform.scale(pygame.image.load("Picture.jpg").convert_alpha(),(200,200))
space_rect = spaceimg.get_rect(center= (screen_width//2,screen_height//2 -30 ))
def game_loop():
    clock = pygame.time.Clock()
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(spaceimg , space_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__' :
    game_loop()
mainloop()