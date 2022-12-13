import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900)) #スクリーン生成
    scrn_rct = scrn_sfc.get_rect()
    
    pgbg_sfc = pg.image.load("fg/pg_bg.jpg") #背景作成
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("fg/6.png") #鳥作成
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    bomb_sfc = pg.Surface((20, 20)) #爆弾生成
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 20)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key_dict = pg.key.get_pressed() #こうかとんの移動
        if key_dict[pg.K_UP]: tori_rct.centery -= 1
        if key_dict[pg.K_DOWN]: tori_rct.centery += 1
        if key_dict[pg.K_LEFT]: tori_rct.centerx -= 1
        if key_dict[pg.K_RIGHT]: tori_rct.centerx += 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        vx, vy = +1, +1 #爆弾の移動
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)

        pg.display.update()

        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()