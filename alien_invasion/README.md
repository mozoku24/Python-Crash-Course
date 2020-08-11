# alien_invasion
Python Crash Course - alien_invasion


# 一、游戏的逻辑设置

| PY       | 组成           | 程序                       |
| -------- | -------------- | -------------------------- |
| 主程序   | alien_invasion | def run_game()；run_game() |
| 设置汇总 | settings       | class Settings()           |
| 统计汇总 | game_stats     | class GameStats()          |
| 模块     | ship           | class Ship(Sprite)         |
|          | alien          | class Alien(Sprite)        |
|          | bullet         | class Bullet(Sprite)       |
|          | button         | class Button()             |
|          | scoreboard     | class Scoreboard()         |
| 功能汇总 | game_function  | 各种def                    |

# 二、各个PY的内容描述

- **alien_invasion**

> （1）初始化游戏；
>
> （2）主循环：检测键盘和鼠标事件、每次循环重绘屏幕

- **settings**

> （1）游戏的静态设置init：屏幕、飞船、子弹、外星人、增速
>
> （2）初始动态设置def：飞船速度、子弹速度、外星人降落速度、飞船左右、打落外星人记分
>
> （3）提高速度def

- **game_stats**

> （1）初始化统计状态init：非活动状态、初始等级、最高分
>
> （2）可变统计状态def：剩余飞船数、得分

- **ship**

> （1）初始化飞船init：
>
> ​		super(Ship, self).__init__() —— *疑问：好像有Sprite的都有这个？*
>
> ​		加载飞船图像、飞船矩形、飞船位置于屏幕底部中央、左右移动标志
>
> （2）调整飞船位置def
>
> （3）绘制图像def
>
> （4）让飞船居中def

- **alien**

> （1）初始化外星人init：
>
> ​		super(Alien, self).__init__()
>
> ​		加载外星人图像、外星人矩形、初始位置、准确位置变量
>
> （2）绘制图像def
>
> （3）调整外星人位置def
>
> （4）判断外星人位置是否在屏幕边缘def

- **bullet**

> （1）初始化子弹init：
>
> ​		super(Bullet, self).__init__()
>
> ​		创建子弹图形、颜色、位置、速度
>
> （2）向上移动子弹def
>
> （3）绘制图像def

- **button**

> （1）初始化按钮init：按钮尺寸、颜色、字体、位置、文字图像
>
> （2）按钮上的文字图像def
>
> （3）绘制按钮def

- **scoreboard**

> （1）初始化init：字体、颜色、当前得分图像、最高得分图像、等级图像、剩余飞船图像
>
> （2）当前得分图像def，最高得分图像def，等级图像def
>
> （3）剩余飞船图像def：Group()
>
> （4）显示得分绘制飞船def：blit，draw

- **game_function**

> （1）import sys，from time import sleep
>
> （2）按键按下def，按键松开def，按键和鼠标事件def
>
> （3）单击play开始游戏def，更新屏幕图像def
>
> （4）删除已消失子弹def，发射子弹def，子弹与外星人碰撞def
>
> （5）创建一个外星人def，计算一行有多少外星人def，创建外星人群def，屏幕可容纳多少行外星人def
>
> ​		外星人到达边缘转向def，整群外星人下移def，外星人与飞船碰撞或者到达底部 def
>
> （6）最高得分def

# 三、PYGAME的运用

## 1）常用import：sys，time，pygame

```python
import sys
#sys.exit() 退出游戏

from time import sleep
#sleep(1) 延迟1秒

import pygame
import pygame.font
from pygame.sprite import Sprite
from pygame.sprite import Group
```

## 2）pygame.font：文字变图像框

```python
self.font = pygame.font.SysFont(None, 48) 
#从系统内加载字体设置，None默认字体

self.text_color = (30, 30, 30)
self.score_image = self.font.render(score_str, True, self.text_color,
                                    self.ai_settings.bg_color)
self.score_rect = self.score_image.get_rect()
#把文字变成图像pygame.font.Font.render()
#render(text, antialias, color, background=None)
#color例如(0, 0, 255) 表示蓝色
#返回的 Surface 对象将保持表示文本所需要的尺寸
#image.get_rect()获得图像框
```

## 3）pygame.sprite.Sprite：一组里的单个对象设定

```python
class Bullet(Sprite):
    def __init__(self,...): #省略其他参数
        super(Bullet, self).__init__() 
        #这句在有Sprite里都有
```

## 4）pygame.sprite.Group：组设定

```python
bullets = Group()
#生成一组子弹

for bullet in bullets.sprites():
    bullet.draw_bullet()
#逐个重绘子弹

bullets.empty()
#清空子弹

bullets.update()
#更新子弹位置

for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
        bullets.remove(bullet)
#删除已消失的子弹

if len(bullets) < ai_settings.bullets_allowed:
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)
#子弹组增加新子弹

collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
if collisions:
    for aliens in collisions.values():
        stats.score += ai_settings.alien_points * len(aliens)
#子弹组和外星人组碰撞

if pygame.sprite.spritecollideany(ship, aliens):
    ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
#当前飞船与外星人组碰撞
```

## 5）pygame

```python
pygame.init()
#初始化游戏

screen = pygame.display.set_mode((width, height))
#设置主屏幕大小
pygame.display.set_caption("Alien Invasion")
#设置主屏幕标题

image = pygame.image.load(r'E:\Temp\alien_invasion\images\ship.bmp')
#加载飞船图像
rect = image.get_rect()
#获取图像外接矩形
#矩形属性：rect.centerx、rect.bottom、rect.width、rect.height、rect.top、rect.center

screen.fill(color, rect)
#矩形颜色填充
screen.blit(image, rect)
#在指定位置绘制飞船，把rect的位置定好，screen是背景框，在screen上面画rect
pygame.draw
#可以直接画pygame.draw.rect、circle、arc等

rect = pygame.Rect(0, 0, width, height)
#在(0,0)处创建一个表示子弹的矩形
rect.centerx = ship.rect.centerx
rect.top = ship.rect.top
#设置子弹正确的位置
pygame.draw.rect(screen, color, rect)
#在屏幕上绘制子弹

pygame.mouse.get_pos()
#获取鼠标位置
button.rect.collidepoint(mouse_x, mouse_y)
#按钮框是否和鼠标点击位置重合，重合就说明点了按钮

pygame.event.get() #pygame里的事件
event.key == pygame.K_RIGHT #右箭头
event.key == pygame.K_LEFT #左箭头
event.key == pygame.K_SPACE #空格
event.key == pygame.K_q #q键

pygame.QUIT #退出
pygame.KEYDOWN #键盘按下
pygame.KEYUP #键盘弹起
pygame.MOUSEBUTTONDOWN #鼠标按下

pygame.mouse.set_visible(True) #鼠标是否可见

```

## 6）其他

```python
#运行主程序
def run_game():
    ###各种初始化###下面主循环
    pass
run_game()

#主程序中的主循环
while True:
    gf.check_events() # 监视键盘和鼠标事件
    if stats.game_active: #游戏中，每次循环时都重绘：飞船、子弹、外星人
        ship.update()
        gf.update_bullets()
        gf.update_aliens()
    gf.update_screen() #新开游戏

#响应按键和鼠标事件
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #退出
            sys.exit()  
        elif event.type == pygame.KEYDOWN: #键盘按下，见下
            check_keydown_events() 
        elif event.type == pygame.KEYUP: #键盘弹起，见下
            check_keyup_events()         
        elif event.type == pygame.MOUSEBUTTONDOWN: #鼠标按下
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button()
#键盘按下
def  check_keydown_events():
    if event.key == pygame.K_RIGHT: pass
    elif event.key == pygame.K_LEFT: pass
    elif event.key == pygame.K_SPACE: pass
    elif event.key == pygame.K_q: sys.exit()
#键盘弹起
def  check_keyup_events():
    if event.key == pygame.K_RIGHT: pass
    elif event.key == pygame.K_LEFT: pass 
```

