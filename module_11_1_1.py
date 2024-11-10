import requests
import matplotlib.pyplot as plt
from matplotlib import image as matplotlib_image
import numpy as np
from PIL import Image
import os

URL = 'https://static-maps.yandex.ru/1.x/?l=map&size=650,450&ll=74.966385,46.833138&spn=60.0,60.0&pt=-13,16,vkbkm~-10,17,vkbkm~-6,18,vkbkm~-2,19,vkbkm~2,20,vkbkm~6,21,vkbkm~10,22,vkbkm~14,23,vkbkm~18,24,vkbkm~22,25,vkbkm~26,26,vkbkm~30,27,vkbkm~34,28,vkbkm~38,29,vkbkm~42,30,vkbkm~46,31,vkbkm~50,32,vkbkm~54,33,vkbkm~58,34,vkbkm~62,35,vkbkm~66,36,vkbkm~70,37,vkbkm~74,38,vkbkm~78,39,vkbkm~82,40,vkbkm~86,41,vkbkm~90,42,vkbkm~94,43,vkbkm~98,44,vkbkm~102,45,vkbkm~106,46,vkbkm~110,47,vkbkm~114,48,vkbkm~118,49,vkbkm~122,50,vkbkm~126,51,vkbkm~130,52,vkbkm~134,54,vkbkm~138,55,vkbkm~142,56,vkbkm~146,57,vkbkm~150,58,vkbkm~154,59,vkbkm~158,60,vkbkm~162,61,vkbkm~166,62,vkbkm~170,63,vkbkm~174,64,vkbkm~178,65,vkbkm~-17.472242,14.736348,vkgrm'
FNAME = 'temp_map.png'

def example_with_requests():
    global URL, FNAME
    try:
        response = requests.get(URL)
    except requests.ConnectionError as exc:
        print(f'Ошибка подключения к сети: {exc}')
        return
    print(f'http статус: {response.status_code} ({response.reason})')
    # Запись полученного изображения-карты в файл:
    with open(FNAME, "wb") as f:
        f.write(response.content)
    if os.path.isfile(FNAME):
        print(f'Файл {FNAME} сохранен.')

def example_with_matplotlib_and_numpy():
    global FNAME
    if not os.path.isfile(FNAME):
        print(f'Не удалось найти файл {FNAME}.')
        return
    xx = np.arange(0, 649, 0.5)
    w = 2 * np.pi / 649
    ysin = 224 * np.sin(xx * w) + 225
    ycos = 224 * np.cos(xx * w) + 225

    img = matplotlib_image.imread(FNAME)
    plt.title('Яндекс-карта: Дакар-Анадырь')
    plt.xlabel(u'Условные координаты X в пикселях')
    plt.ylabel(u'Условные координаты Y в пикселях')
    plt.imshow(img)
    plt.plot(xx, ysin)
    plt.plot(xx, ycos)
    plt.xlim((0, 650))
    plt.ylim((450, 0))
    # переназначаем глобальную:
    FNAME = 'Карта-Дакар-Анадырь.png'
    print(f'Сохраняем файл {FNAME} и выводим изображение в диаграмму.')
    plt.savefig(FNAME)
    plt.show()


def example_with_pillow_dithering():
    print(f'Файл с изображением: {FNAME}')
    img = Image.open(FNAME)
    img.show()
    x, y = img.size
    print(f'Разрешение рисунка: {x} x {y}')
    img = img.resize((x * 3, y * 3))  # кортеж в аргументе (xr, yr)
    img = img.convert('1')  # 'RGB' или 'L' - черно-белый, '1' - dithering
    img.show()
    img.save(FNAME[:-4] + '.dithered.png')

    def example_with_pillow_changing():
        fname = 'image_semenov_tsukanov.jpg'
        print(f'Файл с изображением: {fname}')
        img = Image.open(fname)
        img.show()
        x, y = img.size

        img = img.resize((x // 2, y // 2))  # кортеж в аргументе (xr, yr)
        # img = img.convert('RGB') # 'RGB' или 'L' - черно-белый, '1' - dithering
        buff_img = []
        for item in img.getdata():
            if item[0] > 127 and item[1] > 127 and item[2] > 127:
                buff_img.append((255, 0, 0))
            else:
                buff_img.append((0, item[1], 255 - item[2]))
        img.putdata(buff_img)

        img.show()
        img.save(fname[:-4] + '.edited.png')

    def main():
        funcs = [example_with_requests, example_with_matplotlib_and_numpy, example_with_pillow_dithering,
                 example_with_pillow_changing]
        for i, func in enumerate(funcs):
            msg = f'{i + 1} >> работаем с {func.__name__}():'
            print(f'\n{msg}\n' + '=' * len(msg) + '\n')
            func()

    if __name__ == '__main__':
        main()
