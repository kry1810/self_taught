
class GirlFriend:
    def change_name(self, name):
        self.name = name

girl_friend = GirlFriend()



# Step 1: 属性を参照してみる。
girl_friend.change_name


# Step 2: 第一引数を省略して呼び出してみる。
girl_friend.change_name('サーバルちゃん')
girl_friend.name


# Step 3: 第一引数を省略しないで呼び出してみる。
girl_friend.change_name(girl_friend, 'サーバルちゃん')
