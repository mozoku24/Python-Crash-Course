# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:13:26 2020
@author: adabao

https://bitbucket.org/pygame/pygame/downloads/
python -m pip install --user pygame-1.9.2a0-cp35-none-win32.wh

项目1 外星人入侵
1 屏幕底部中央的飞船
2 箭头键左右移动飞船，空格键射击
3 外星人在天空，向下移动
4 射杀外星人，消灭干净，出现新的外星人，速度更快
5 外星人撞到玩家或到达底部，玩家生命-1，三次后结束

心得：
1 把所有setting放在一起，另存个文件，使用时import
"""

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    
    
    #开始游戏的主循环
    while True:
    
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            #每次循环时都重绘屏幕，让最近绘制的屏幕可见
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()