import requests
import threading


def download_image(name):
    response = requests.get(
        url="https://picsum.photos/370/250",
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
    )

    with open(f'image_{name}.jpg', 'wb') as file:
        file.write(response.content)


def threading_f():
    thread_list = []
    for x in range(1, 10 + 1):
        thread_list.append(threading.Thread(target=download_image, args=(f"thread_{x}",), kwargs={}))

    for i in thread_list:
        i.start()

    for i in thread_list:
        i.join()


if __name__ == '__main__':
    threading_f()
