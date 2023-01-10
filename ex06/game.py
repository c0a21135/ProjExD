import pygame as pg
import sys
import random


class Trap:
    def __init__(self, file_pass):
        self.sfc = pg.image.load(file_pass)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.8)
        self.rct = self.sfc.get_rect()
        self.x = random.randint(3, DUNGEON_H-1)
        self.y = random.randint(3,  DUNGEON_W-1)
        if dungeon[self.x][self.y] == 0:
            dungeon[self.x][self.y] = 1

    # def move(self):　#移動する関数
    #     pass


class Player:
    pl_x = 4 #プレイヤー座標
    pl_y = 4 #プレイヤー座標

    def __init__(self, file_pass):
        self.img = pg.image.load(file_pass)
        self.img = pg.transform.rotozoom(self.img, 0, 0.8)
        self.hp = 100
        self.st = 500

    def damege(self): # ダメージを受けたときの処理
        self.hp -= 10 # hpが10減少する

    def move(self): # 移動に関する処理
        key = pg.key.get_pressed()
        if key[pg.K_UP] == 1:
            if dungeon[Player.pl_y-1][Player.pl_x] != 9: # 壁ではない時移動する
                Player.pl_y = Player.pl_y - 1
                if dungeon[Player.pl_y-1][Player.pl_x] == 1: #トラっプに乗った時
                    self.damege()
                return True
        if key[pg.K_DOWN] == 1:
            if dungeon[Player.pl_y+1][Player.pl_x] != 9:
                Player.pl_y = Player.pl_y + 1
                if dungeon[Player.pl_y+1][Player.pl_x] == 1:
                    self.damege()
                return True
        if key[pg.K_LEFT] == 1:
            if dungeon[Player.pl_y][Player.pl_x-1] != 9:
                Player.pl_x = Player.pl_x - 1
                if dungeon[Player.pl_y][Player.pl_x-1] == 1:
                    self.damege()
                return True
        if key[pg.K_RIGHT] == 1:
            if dungeon[Player.pl_y][Player.pl_x+1] != 9: 
                Player.pl_x = Player.pl_x + 1
                if dungeon[Player.pl_y][Player.pl_x+1] == 1:
                    self.damege() 
                return True
        return False

    def updata(self, screen): #プレイヤーに関する表示の更新
        ch = self.move() #座標の更新
        if ch: #移動した場合stを1消費する
            self.st -= 1

        font = pg.font.Font(None, 80) # 文字の描画
        txt = font.render(f"hp:{self.hp}", True, "WHITE")
        screen.blit(txt, (50, 50))
        font = pg.font.Font(None, 80)
        txt = font.render(f"st:{self.st}", True, "WHITE")
        screen.blit(txt, (50, 110))


def make_dungeon(): # ダンジョンの生成
    XP = [ 0, 1, 0,-1]
    YP = [-1, 0, 1, 0]
    #周りの壁
    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H-1][x] = 1
    for y in range(1, MAZE_H-1):
        maze[y][0] = 1
        maze[y][MAZE_W-1] = 1
    #中を何もない状態に
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            maze[y][x] = 0
    #柱
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
            maze[y][x] = 1
    #柱から上下左右に壁を作る
    for y in range(2, MAZE_H-2, 2):
        for x in range(2, MAZE_W-2, 2):
         d = random.randint(0, 3)
         if x > 2: # 二列目からは左に壁を作らない
             d = random.randint(0, 2)
         maze[y+YP[d]][x+XP[d]] = 1

    # 迷路からダンジョンを作る
    #全体を壁にする
    for y in range(DUNGEON_H):
        for x in range(DUNGEON_W):
            dungeon[y][x] = 9
    #部屋と通路の配置
    for y in range(1, MAZE_H-1):
        for x in range(1, MAZE_W-1):
            dx = x*3+1
            dy = y*3+1
            if maze[y][x] == 0:
                if random.randint(0, 99) < 20: # 部屋を作る
                    for ry in range(-1, 2):
                        for rx in range(-1, 2):
                            dungeon[dy+ry][dx+rx] = 0
                else: # 通路を作る
                    dungeon[dy][dx] = 0
                    if maze[y-1][x] == 0:
                        dungeon[dy-1][dx] = 0
                    if maze[y+1][x] == 0:
                        dungeon[dy+1][dx] = 0
                    if maze[y][x-1] == 0:
                        dungeon[dy][dx-1] = 0
                    if maze[y][x+1] == 0:
                        dungeon[dy][dx+1] = 0


def create_trap(num): # トラップクラスを生成
    global trap_list
    for i in range(num):
        trap_list.append(Trap("fg/8.png"))


def draw_dungeon(bg): # ダンジョンを描画する
    bg.fill(BLACK)

    for y in range(-9, 10): # 描画範囲の指定
        for x in range(-9, 10):
            X = (x+7)*OBJ_SIZE
            Y = (y+7)*OBJ_SIZE
            dx = player.pl_x + x
            dy = player.pl_y + y
            if 0 <= dx and dx < DUNGEON_W and 0 <= dy and dy < DUNGEON_H:
                if dungeon[dy][dx] == 0: # 道の場合
                    pg.draw.rect(bg, FLOOR, [X, Y, OBJ_SIZE, OBJ_SIZE])
                if dungeon[dy][dx] == 9:# 壁の場合
                    pg.draw.rect(bg, WALL, [X, Y, OBJ_SIZE, OBJ_SIZE])
                if dungeon[dy][dx] == 1: #トラップの場合
                    pg.draw.rect(bg, FLOOR, [X, Y, OBJ_SIZE, OBJ_SIZE])
                    bg.blit(trap_list[0].sfc, [X, Y])
            if x == 0 and y == 0: # 主人公の表示
                bg.blit(player.img, [X, Y-8])


def main():
    pg.init()
    pg.display.set_caption("ゲーム")
    screen = pg.display.set_mode((800, 800))
    clock = pg.time.Clock()

    make_dungeon()
    create_trap(30)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        draw_dungeon(screen)
        player.updata(screen)
        pg.display.update()
        clock.tick(5)

if __name__ == '__main__':
    BLACK = (0, 0, 0)
    FLOOR  = (128, 128, 255)
    WALL  = (96, 96, 96)

    MAZE_W = 15
    MAZE_H = 11
    maze = [] # 迷路のリスト
    OBJ_SIZE = 60 #1マスの大きさ

    for y in range(MAZE_H):
        maze.append([0]*MAZE_W)

    DUNGEON_W = MAZE_W*3
    DUNGEON_H = MAZE_H*3
    dungeon = [] # 小部屋が存在するダンジョンのリスト
    for y in range(DUNGEON_H):
        dungeon.append([0]*DUNGEON_W)

    player = Player("fg/3.png")
    trap_list = []

    main()
