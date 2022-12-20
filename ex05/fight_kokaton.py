import random
import sys
import os
import schedule

import pygame as pg

main_dir = os.path.split(os.path.abspath(__file__))[0]
bombs = []#爆弾のリスト
del_bombs = []
game_flag = False

class Screen:
    def __init__(self, title, wh, img_path):
        """
        title:スクリーン名
        wh:スクリーンの大きさを指定するタプル
        img_path:背景画像のパス
        """
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self): #背景画像貼り付け
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -2],
        pg.K_DOWN:  [0, +2],
        pg.K_LEFT:  [-2, 0],
        pg.K_RIGHT: [+2, 0],
    }

    def __init__(self, img_path, ratio, xy):
        """
        img_path:こうかとん画像のパス
        ratio:拡大率
        xy:初期座標タプル
        """
        self.sfc = pg.image.load(img_path)  #"fg/6.png"
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen): #scrはScreenオブジェクト
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        #キーの押下に応じてこうかとんを移動する
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]

            #こうかとんが画面外に出ないようにする
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr) #こうかとんを貼りなおす


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        """
        color:色タプル
        rad:半径
        vxy:速度タプル
        scr:Screenオブジェクト
        """
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0+rad, scr.rct.width-rad)
        self.rct.centery = random.randint(0+rad, scr.rct.height-rad)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) 

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Del_bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0+rad, scr.rct.width-rad)
        self.rct.centery = random.randint(0+rad, scr.rct.height-rad)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Shugosin:
    def __init__(self, img_pass, ratio, bird:Bird):
        self.sfc = pg.image.load(img_pass)  #"fg/6.png"
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = bird.rct.centerx, bird.rct.centery

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
  



def create_bombs(scr:Screen): #爆弾生成
    global bombs
    vx=random.choice([-2, -1, +1, +2])
    vy=random.choice([-2, -1, +1, +2])
    bomb = Bomb((255, 0, 0), 10, (vx, vy), scr)
    bombs.append(bomb)


def create_delbombs(scr:Screen):
    global del_bombs
    if len(del_bombs) < 2:
        vx=random.choice([-1.5, -1, +1.5, +1])
        vy=random.choice([-1.5, -1, +1.5, +1])
        bomb = Bomb((255, 255, 0), 10, (vx, vy), scr)
        del_bombs.append(bomb)


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def load_sound(file):
    """音楽の読み込み"""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None


def load_image(file):
    """画像を読み込む関数"""
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert() 


def reset_bombs(delbom:Del_bomb):
    global bombs, del_bombs
    bombs.clear()
    del_bombs.remove(delbom)


def gard_bombs(bomb:Bomb):
    global bombs
    bombs.remove(bomb)


def main():
    global bombs, game_flag

    clock =pg.time.Clock()
    screen = Screen("逃げろこうかとん", (1600, 900), "fg/pg_bg.jpg")
    bird = Bird("fg/6.png", 2.0, (900, 400))
    shugo = Shugosin("ex05/data/alien3.png", 5.0, bird)

    #初期爆弾の生成
    for i in range(4):
        create_bombs(screen)
    
    #BGMの設定
    if pg.mixer:
        music = os.path.join(main_dir, "data", "house_lo.wav")
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    # Shot.images =  [load_image("shot.gif")] #弾の画像
    
    schedule.every(2).seconds.do(create_bombs,screen) #2秒ごとに爆弾生成関数を実行するようにスケジュールに登録
    boom_sound = load_sound("boom.wav")
    screen.blit()
    bird.blit(screen)

    while True:
        screen.blit() #背景画像の貼り付け
        bird.blit(screen)
        schedule.run_pending() #スケジュールの実行

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            key_dict = pg.key.get_pressed()
            # ゲームの開始
            if key_dict[pg.K_s]:
                game_flag = True
            if event.type == pg.K_SPACE:
                create_delbombs(screen)
            if event.type == pg.K_a:
                shugo.blit()
                if shugo.rct.colliderect(bomb.rct):
                    gard_bombs(bomb)
        if game_flag:
            bird.update(screen) #こうかとんを移動する

            for bomb in bombs:
                bomb.update(screen)
                if bird.rct.colliderect(bomb.rct):
                    game_flag = False
                    bird = Bird("fg/8.png", 2.0, (900, 400))

            for delbomb in del_bombs:
                delbomb.update(screen)
                if delbomb.rct.colliderect(bird.rct):
                    boom_sound.play()
                    reset_bombs(delbomb) #爆弾処理オブジェクトに触れた際出現中の爆弾を無くす

            if key_dict[pg.K_SPACE]:
                create_delbombs(screen)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()