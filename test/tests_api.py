from HttpRequestsService.http_requests_service import HttpRequestsService


class TestAPI:
    def test_get_request(self):
        get_request = HttpRequestsService()
        get_request.test_get_status_200()

    def test_create_tasks(self):
        create_tasks = HttpRequestsService()
        create_tasks.test_create_task()

    def test_update_task(self):
        update_task = HttpRequestsService()
        update_task.test_update_data()

    def test_list_tasks(self):
        list_tasks = HttpRequestsService()
        list_tasks.test_get_list_tasks()

    def test_delete_task(self):
        delete_task = HttpRequestsService()
        delete_task.test_delete_task()
