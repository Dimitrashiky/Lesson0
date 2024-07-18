class User:

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname
class Video:

    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __eq__(self, other):
        return self.title == other.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, item):
        for i in self.videos:
            if item == i:
                return True
    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break
        else:
            print('Пользователь не был найден')

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
            break
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None
    def add(self, *video):
        for video1 in video:
            if not self.__contains__(video1):
               self.videos.append(video1)

    def get_videos(self, naming: str):
        search_video = []
        for video in self.videos:
            if naming.lower() in video.title.lower():
                search_video.append(video.title)
        return search_video

    def watch_video(self, video_name):
        import time
        if self.current_user != None:
            for video in self.videos:
                if video_name == video.title:
                    current_video = video
                    break
            else:
                return 0
            if current_video.adult_mode == True and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return 0
            for second in range(1, current_video.duration + 1):
                time.sleep(1)
                print(second, end= " ")
            print("Конец видео")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 20)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт

print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
print(ur.users)










