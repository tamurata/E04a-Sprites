#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)
        
        self.animal_list = arcade.SpriteList()


    def setup(self):
       self.animal_sprite = arcade.Sprite("assets/Side/detail_crystal.png", 2.0)
       self.animal_sprite.center_x = 400
       self.animal_sprite.center_y = 300
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/detail_dirt.png", 2.0)
       self.animal_sprite.center_x = 500
       self.animal_sprite.center_y = 300
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/detail_tree.png", 2.0)
       self.animal_sprite.center_x = 450
       self.animal_sprite.center_y = 150
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/detail_rocks.png", 2.0)
       self.animal_sprite.center_x = 200
       self.animal_sprite.center_y = 100
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/snow_tile_bump.png", 2.0)
       self.animal_sprite.center_x = 650
       self.animal_sprite.center_y = 50
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/snow_tile_hill.png", 2.0)
       self.animal_sprite.center_x = 600
       self.animal_sprite.center_y = 400
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/snow_tile_riverFall.png", 2.0)
       self.animal_sprite.center_x = 450
       self.animal_sprite.center_y = 100
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/snow_tile_spawn.png", 2.0)
       self.animal_sprite.center_x = 350
       self.animal_sprite.center_y = 350
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/towerRound_base.png", 2.0)
       self.animal_sprite.center_x = 680
       self.animal_sprite.center_y = 133
       self.animal_list.append(self.animal_sprite)

       self.animal_sprite = arcade.Sprite("assets/Side/towerRound_crystals.png", 2.0)
       self.animal_sprite.center_x = 250
       self.animal_sprite.center_y = 550
       self.animal_list.append(self.animal_sprite)

    def on_draw(self):
        arcade.start_render()
        self.animal_list.draw()


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        self.animal_sprite.center_x = x
        self.animal_sprite.center_y = y

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()