class Obuv:
    def __init__(self, tip_obuvi, vid_obuvi, cvet, tsena, proizvoditel, razmer):
        self.tip_obuvi = tip_obuvi
        self.vid_obuvi = vid_obuvi
        self.cvet = cvet
        self.tsena = tsena
        self.proizvoditel = proizvoditel
        self.razmer = razmer

    def __str__(self):
        return (f"Тип: {self.tip_obuvi}\n"
                f"Вид: {self.vid_obuvi}\n"
                f"Цвет: {self.cvet}\n"
                f"Цена: {self.tsena}\n"
                f"Производитель: {self.proizvoditel}\n"
                f"Размер: {self.razmer}")

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class ObuvController:
    def __init__(self, model):
        self.model = model

    def update_obuv(self, **kwargs):
        self.model.update_info(**kwargs)

    def get_obuv_info(self):
        return str(self.model)


class ObuvView:
    def display_obuv(self, obuv_info):
        print("Информация об обуви:")
        print(obuv_info)


# Создание модели
obuv = Obuv(tip_obuvi="мужская", vid_obuvi="кроссовки", cvet="черный", tsena=3000, proizvoditel="Nike", razmer=42)

# Создание контроллера
obuv_controller = ObuvController(obuv)

# Создание представления
obuv_view = ObuvView()

# Получение информации об обуви
obuv_info = obuv_controller.get_obuv_info()

# Отображение информации
obuv_view.display_obuv(obuv_info)

# Обновление информации
obuv_controller.update_obuv(cvet="белый", tsena=3500)

# Получение обновленной информации
updated_obuv_info = obuv_controller.get_obuv_info()

# Отображение обновленной информации
obuv_view.display_obuv(updated_obuv_info)




#класс рецепт
class Retsept:
    def __init__(self, nazvanie, avtor, tip_recepta, opisanie, video_sсылка, ingredienty, kuhnya):
        self.nazvanie = nazvanie
        self.avtor = avtor
        self.tip_recepta = tip_recepta
        self.opisanie = opisanie
        self.video_sсылка = video_sсылка
        self.ingredienty = ingredienty
        self.kuhnya = kuhnya

    def __str__(self):
        return (f"Название: {self.nazvanie}\n"
                f"Автор: {self.avtor}\n"
                f"Тип: {self.tip_recepta}\n"
                f"Описание: {self.opisanie}\n"
                f"Видео: {self.video_sсылка}\n"
                f"Ингредиенты: {', '.join(self.ingredienty)}\n"
                f"Кухня: {self.kuhnya}")

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class RetseptController:
    def __init__(self, model):
        self.model = model

    def update_recept(self, **kwargs):
        self.model.update_info(**kwargs)

    def get_recept_info(self):
        return str(self.model)


class RetseptView:
    def display_recept(self, recept_info):
        print("Информация о рецепте:")
        print(recept_info)


# Создание модели
recept = Retsept(nazvanie="Паста Карбонара", avtor="Итальянский шеф", tip_recepta="второе блюдо",
                 opisanie="Классическое итальянское блюдо с пастой и беконом.",
                 video_sсылка="https://youtube.com/пример",
                 ingredienty=["паста", "бекон", "яйцо", "сыр"], kuhnya="итальянская")

# Создание контроллера
recept_controller = RetseptController(recept)

# Создание представления
recept_view = RetseptView()

# Получение информации о рецепте
recept_info = recept_controller.get_recept_info()

# Отображение информации
recept_view.display_recept(recept_info)

# Обновление информации
recept_controller.update_recept(opisanie="Обновленное описание рецепта.", ingredienty=["паста", "бекон", "яйцо", "сыр", "петрушка"])

# Получение обновленной информации
updated_recept_info = recept_controller.get_recept_info()

# Отображение обновленной информации
recept_view.display_recept(updated_recept_info)

