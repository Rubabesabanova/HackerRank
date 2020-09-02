def Layout(func):
    def wrapper():
        Header()
        func()
        Footer()

    return wrapper

def Header():
    print("Saytin header hissesinin kodlari")

def Footer():
    print("Saytin footer hissesinin kodlari")
@Layout
def Home():
    print("~:~::~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~::~:~Ana Sehifeye aid olan hisseler")
@Layout
def About():
    print("~:~::~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~::~:~Haqqimizda sehifesine aid olan hisseler")

About()
Home()


