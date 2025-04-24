import pygame
import qrcode
from PIL import Image
# import io

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("QR Code Generator")

font = pygame.font.SysFont(None, 30)
input_box = pygame.Rect(50, 50, 500, 40)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
qr_surface = None

clock = pygame.time.Clock()

def generate_qr_surface(data):
    
    qr = qrcode.QRCode(version=1, box_size=5, border = 5)

    qr.add_data(data)
    qr.make()

    imp = qr.make_image(fill_color='black', back_color='white')
    imp.save('new.png')

    img = Image.open('new.png')
    img.show()
    image = pygame.image.load('new.png')
    # image = pygame.transform.scale(image, (300, 300))
    mess = 'QR Code generated!'
    
    return image

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    qr_surface = generate_qr_surface(text)
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill((255, 255, 255))
    txt_surface = font.render(text, True, color)
    width = max(500, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    write_link = font.render('Enter your link:', True, (0, 0, 0))
    screen.blit(write_link, (50, 20))
    pygame.draw.rect(screen, color, input_box, 2)

    if qr_surface:
        mess = font.render('QR Code generated!', True, (0, 0, 0))
        screen.blit(mess, (50, 100))
        qr_scaled = pygame.transform.scale(qr_surface, (200, 200))
        screen.blit(qr_scaled, (200, 150))

    pygame.display.flip()
    clock.tick(30)
