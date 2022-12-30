class Game(object):

    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息")

    @classmethod
    def show_top_score(cls):
        print("历史记录%d" % cls.top_score)

    def start_game(self):
        # 注意在实例方法中，不能通过cls.**访问到类属性
        # 可以通过类名.**访问
        print("%s 开始游戏了" % self.player_name)
        print("%d" % Game.top_score)



# 1.查看游戏的帮助信息
Game.show_help()
# 2.查看历史最高分
Game.show_top_score()
# 3.创建游戏对象
game = Game("小明")
game.start_game()
