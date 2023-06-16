import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course

token = 'vk1.a.EoDkns-CYbdvwyzBmHu6EfbwpafWsM8kJulcZerCe8IWYWYratvvQmeJfRnOZCwSV4fYKIbxJVZ0IfJRtaMPhq3EO_rUi7MsQyhR7Kq6XgRmgr6Ur4H5ug4qi2ddwfW9o3w5I7noeKfXKeWp3TJsOv24vQc9ELi3wQF68eFf1F3P1vXqeCSPk0KHY16n2LyJdQgPhd2DPpvVsWR6A_Wi4w'

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

courses = {
    '-к доллар': 'R01235',
    '-к евро': 'R01239',
    '-к юань': 'R01375',
}

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text
        user_id = event.user_id
        msg_id = event.message_id
        if msg.lower() == 'привет':
            vk.messages.send(user_id=user_id, random_id=msg_id, message='Привет!')
        elif msg.lower() == '-к доллар':
            response = f'{get_course(courses[msg])} рублей за 1 доллар'
            vk.messages.send(user_id=user_id, random_id=msg_id, message=response)
        elif msg.lower() == '-к евро':
            response = f'{get_course(courses[msg])} рублей за 1 евро'
            vk.messages.send(user_id=user_id, random_id=msg_id, message=response)
        elif msg.lower() == '-к юань':
            response = f'{get_course(courses[msg])} рублей за 1 юань'
            vk.messages.send(user_id=user_id, random_id=msg_id, message=response)
        else:
            vk.messages.send(user_id=user_id, random_id=msg_id, message='НЕ понял...')
