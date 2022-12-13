import pygame as pg
import sys
import random

def check_bound(obj_rct, scrn_rct): #移動するオブジェクトとスクリーンの衝突判定
    # 第一引数：こうかとんや爆弾のレクト、第2引数：スクリーンレクト
    # 範囲内：+1、範囲外：-1を変える
    yoko, tate = 1, 1
    if obj_rct.left < scrn_rct.left or obj_rct.right > scrn_rct.right:
        yoko = -1
    if obj_rct.top < scrn_rct.top or obj_rct.bottom > scrn_rct.bottom:
        tate = -1
    return yoko, tate

def create_bomb(scrn_rct):
    # 爆弾を生成する関数
    # 引数：生成するスクリーンレクト
    global bomb_list
    bomb_sfc = pg.Surface((20, 20)) #爆弾生成
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    vx, vy = 3, 3
    bomb_list.append([bomb_sfc, bomb_rct, vx, vy])


def main():
    global game_flag

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
    r = 10 #爆弾半径
    pg.draw.circle(bomb_sfc, (255, 0, 0), (r, r), r)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    vx, vy = +1, +1 #爆弾の移動速度
    ch_b1 = False #爆弾強化オブジェクトの判定フラッグ
    ch_b2 = False #爆弾強化オブジェクトの判定フラッグ
    mv = 1 #こうかとんの移動速度

    obj_sfc = pg.Surface((80, 80)) #オブジェクト
    obj_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(obj_sfc, (255, 255, 0), (40, 40), 80)
    obj_rct = obj_sfc.get_rect()
    obj_rct.centerx = random.randint(0, scrn_rct.width)
    obj_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(obj_sfc, obj_rct)

    b1obj_sfc = pg.Surface((150, 150)) #オブジェクト
    b1obj_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(b1obj_sfc, (255, 0, 0), (75, 75), 150)
    b1obj_rct = b1obj_sfc.get_rect()
    b1obj_rct.centerx = random.randint(0, scrn_rct.width)
    b1obj_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(b1obj_sfc, b1obj_rct)

    b2obj_sfc = pg.Surface((150, 150)) #オブジェクト
    b2obj_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(b2obj_sfc, (255, 0, 0), (75, 75), 150)
    b2obj_rct = b2obj_sfc.get_rect()
    b2obj_rct.centerx = random.randint(0, scrn_rct.width)
    b2obj_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(b2obj_sfc, b2obj_rct)


    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        scrn_sfc.blit(obj_sfc, obj_rct)
        scrn_sfc.blit(b1obj_sfc, b1obj_rct)
        scrn_sfc.blit(b2obj_sfc, b2obj_rct)

        for bomb_obj in bomb_list:
            scrn_sfc.blit(bomb_obj[0], bomb_obj[1])
            yoko, tate = check_bound(bomb_obj[1], scrn_rct)
            bomb_obj[2] *= yoko
            bomb_obj[3] *= tate
            bomb_obj[1].move_ip(bomb_obj[2], bomb_obj[3])
            scrn_sfc.blit(bomb_obj[0], bomb_obj[1])


        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            key_dict = pg.key.get_pressed()

            # ゲームの開始
            if key_dict[pg.K_s]: game_flag = True
    
        if game_flag: #ゲーム中のみこうかとんと爆弾が動く
            # こうかとんの移動
            if key_dict[pg.K_UP]: tori_rct.centery -= mv
            if key_dict[pg.K_DOWN]: tori_rct.centery += mv
            if key_dict[pg.K_LEFT]: tori_rct.centerx -= mv
            if key_dict[pg.K_RIGHT]: tori_rct.centerx += mv
            if check_bound(tori_rct, scrn_rct) != (1, 1): #こうかとんがスクリーン外に出ようとしたら移動をキャンセル
                if key_dict[pg.K_UP]: tori_rct.centery += mv
                if key_dict[pg.K_DOWN]: tori_rct.centery -= mv
                if key_dict[pg.K_LEFT]: tori_rct.centerx += mv
                if key_dict[pg.K_RIGHT]: tori_rct.centerx -= mv

            scrn_sfc.blit(tori_sfc, tori_rct)

            # if key_dict[pg.K_SPACE]: # 爆弾生成
            #     create_bomb(scrn_rct)
            #     bomb_rct1.centerx = random.randint(0, scrn_rct.width)
            #     bomb_rct1.centery = random.randint(0, scrn_rct.height)
            #     scrn_sfc.blit(bomb_sfc1, bomb_rct1)

            # 爆弾の移動
            yoko, tate = check_bound(bomb_rct, scrn_rct)
            vx *= yoko
            vy *= tate
            bomb_rct.move_ip(vx, vy)
            scrn_sfc.blit(bomb_sfc, bomb_rct)

        # 衝突ゲームオーバー判定
        if tori_rct.colliderect(bomb_rct):
            game_flag = False
            tori_sfc = pg.image.load("fg/8.png") #鳥作成
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
            scrn_sfc.blit(tori_sfc, tori_rct)
            scrn_sfc.blit(bomb_sfc, bomb_rct)

        # 強化スポット衝突判定
        if tori_rct.colliderect(obj_rct):
            mv = 3 #移動速度を1->3に変更

        # 爆弾強化オブジェクト衝突判定(一度のみ)
        if tori_rct.colliderect(b1obj_rct):
            if ch_b1 != True: #一度のみ移動量を増やす
                vx += 1.5
                vy += 2.5
                create_bomb(scrn_rct)
                ch_b1 = True
        if tori_rct.colliderect(b2obj_rct):
            if ch_b2 != True: #一度のみ移動量を増やす
                vx += 2.5
                vy += 1.5
                create_bomb(scrn_rct)
                ch_b2 = True

        pg.display.update()

        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    bomb_list = []
    game_flag = False
    main()
    pg.quit()
    sys.exit()