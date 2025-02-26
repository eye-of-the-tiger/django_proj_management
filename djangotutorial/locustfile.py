from locust import HttpUser, TaskSet, task, between
from django.urls import reverse

URLNAME = 'https://congenial-succotash-rv9w4r797wg2xrpj-8000.app.github.dev/admin/'
class WebsiteTasks(TaskSet):
    #  Минимальное и максимальное время "ожидания" пользователя между задачами (в секундах).
    wait_time = between(1, 3)

    @task(2)  # Вес задачи: задачи с большим весом выполняются чаще
    def index(self):
        """
        Тест главной страницы
        """
        self.client.get(URLNAME) # Замените 'home' на имя вашего URL

    @task(1)
    def view_product(self):
        """
        Тест просмотра страницы продукта
        """
        product_id = 1  # Пример ID продукта.  Нужно сделать динамическим в реальном тесте
        self.client.get(URLNAME) # Замените 'product_detail' на имя вашего URL

    @task(3)
    def login(self):
        """
        Тест логина пользователя
        """
        self.client.get('admin') # Замените 'login' на имя вашего URL
        # Если требуется POST-запрос для логина:
        # form_data = {'username': 'testuser', 'password': 'testpassword'} #Замените на ваши данные
        # self.client.post(reverse('login'), form_data)
    
    @task
    def login(self):
        """
        Тест логина пользователя (POST запрос)
        """
        login_url = 'login' # Замените 'login' на имя вашего URL
        form_data = {'username': 'admin', 'password': 'Passw0rd'} #Замените на ваши данные
        with self.client.post(login_url, form_data, catch_response=True) as response: # catch_response=True позволяет обрабатывать ответы с ошибками
            if response.status_code == 200:
                print("Login successful")
            else:
                response.failure("Login failed: " + str(response.status_code))

class WebsiteUser(HttpUser):
    """
    Определение пользователя locust.
    """
    host = "http://localhost:8000/admin/"  # Замените на ваш URL (Django dev server или production)
    tasks = [WebsiteTasks] # Набор задач, которые будет выполнять пользователь.
    wait_time = between(1,3) # Время ожидания перед выполнением каждой TaskSet (не Task)

