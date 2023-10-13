import asyncio
import discord

intents = discord.Intents.default()
intents.message_content = True
token = 'token'
client = discord.Client(intents=intents)
global song_playing
song_playing = False


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    global song_playing
    if message.content.startswith('!song Тайна хозяйки старинных часов'):
        if not song_playing:
            song_playing = True
            await message.channel.send(f'Тайна хозяйки старинных часов\nЗаказал: @{message.author}')
            await message.channel.send(f'Деревня укрылась средь жутких лесов,')
            await asyncio.sleep(4)
            await message.channel.send('Туда совершенно случайно попал')
            await asyncio.sleep(4)
            await message.channel.send('Один покупатель старинных часов,')
            await asyncio.sleep(4)
            await message.channel.send('Он их для музея повсюду искал.')
            await asyncio.sleep(4)
            await message.channel.send('Не мог он не удивиться')
            await asyncio.sleep(4)
            await message.channel.send('Хозяйке старого особняка')
            await asyncio.sleep(4)
            await message.channel.send('Красивая с виду девица –')
            await asyncio.sleep(4)
            await message.channel.send('Откуда в этой глуши она?!')
            await asyncio.sleep(4)
            await message.channel.send('Висели над камином старинные часы,')
            await asyncio.sleep(4)
            await message.channel.send('И стрелки замерли на них сто с лишним лет назад.')
            await asyncio.sleep(4)
            await message.channel.send('Девица не спускала с них свой очень странный взгляд,')
            await asyncio.sleep(4)
            await message.channel.send('Они давно стоят.')
            await asyncio.sleep(4)
            await message.channel.send('Но нет, неподкупна хозяйка была –')
            await asyncio.sleep(4)
            await message.channel.send('Часы отказалась она продавать.')
            await asyncio.sleep(4)
            await message.channel.send('И на ночь оставила гостя она,')
            await asyncio.sleep(4)
            await message.channel.send('Свою предложила мужчине кровать.')
            await asyncio.sleep(4)
            await message.channel.send('Но только она заснула,')
            await asyncio.sleep(4)
            await message.channel.send('Тихонько дверь притворив за собой,')
            await asyncio.sleep(4)
            await message.channel.send('В гостиную прошмыгнула')
            await asyncio.sleep(4)
            await message.channel.send('Фигура гостя во тьме ночной.')
            await asyncio.sleep(4)
            await message.channel.send('Висели над камином старинные часы')
            await asyncio.sleep(4)
            await message.channel.send('И стрелки замерли на них сто с лишним лет назад')
            await asyncio.sleep(4)
            await message.channel.send('И гость не отрывал от них свой любопытный взгляд')
            await asyncio.sleep(4)
            await message.channel.send('Они давно стоят.')
            await asyncio.sleep(4)
            await message.channel.send('Не сразу он в них неисправность нашел,')
            await asyncio.sleep(4)
            await message.channel.send('Лишь колокол в старых часах зазвонил –')
            await asyncio.sleep(4)
            await message.channel.send('Обратно он в спальню хозяйки пошел:')
            await asyncio.sleep(4)
            await message.channel.send('Мол, древнюю вещь ото сна пробудил!')
            await asyncio.sleep(4)
            await message.channel.send('В ответ она захрипела,')
            await asyncio.sleep(4)
            await message.channel.send('Был дикий ужас в ее глазах.')
            await asyncio.sleep(4)
            await message.channel.send('Часы звенели – она старела,')
            await asyncio.sleep(4)
            await message.channel.send('Пока не превратилась в прах.')
            await asyncio.sleep(4)
            await message.channel.send('Висели над камином старинные часы,')
            await asyncio.sleep(4)
            await message.channel.send('И стрелки замерли на них сто с лишним лет назад.')
            await asyncio.sleep(4)
            await message.channel.send('Девица не спускала с них свой очень странный взгляд,')
            await asyncio.sleep(4)
            await message.channel.send(
                'Они давно стоят.\n\nСпасибо за прослушивание!\nПо желанию вы можете поставить печеньку @banan890 и @kleshevp')
            with open('Король и Шут - Тайна хозяйки старинных часов.mp3', 'rb') as file:
                file_data = discord.File(file)
                await message.channel.send(file=file_data, content='Тайна хозяйки старинных часов')
            song_playing = False
    elif message.content.startswith('!song Танец злобного гения'):
        if not song_playing:
            song_playing = True
            await message.channel.send(f'Танец злобного гения\nЗаказал: @{message.author}')
            await message.channel.send('Проныра, озорник, ')
            await asyncio.sleep(4)
            await message.channel.send('Любитель книг,')
            await asyncio.sleep(4)
            await message.channel.send('Ловкач, игрок,')
            await asyncio.sleep(4)
            await message.channel.send('Жизнь между строк. ')
            await asyncio.sleep(4)
            await message.channel.send('И потому ')
            await asyncio.sleep(4)
            await message.channel.send('Открыт ему ')
            await asyncio.sleep(4)
            await message.channel.send('Незримый путь ')
            await asyncio.sleep(4)
            await message.channel.send('В любую суть. ')
            await asyncio.sleep(4)
            await message.channel.send('Танец злобного гения ')
            await asyncio.sleep(4)
            await message.channel.send('На страницах произведения. ')
            await asyncio.sleep(4)
            await message.channel.send('Это — игра, без сомнения, ')
            await asyncio.sleep(4)
            await message.channel.send('Обреченный ждет поражение! ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лала-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лала-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай. ')
            await asyncio.sleep(4)
            await message.channel.send('Подсыпать в душу яд ')
            await asyncio.sleep(4)
            await message.channel.send('Всегда он рад. ')
            await asyncio.sleep(4)
            await message.channel.send('Всего за час ')
            await asyncio.sleep(4)
            await message.channel.send('Прочтет он вас. ')
            await asyncio.sleep(4)
            await message.channel.send('Он волен взять ')
            await asyncio.sleep(4)
            await message.channel.send('И поменять ')
            await asyncio.sleep(4)
            await message.channel.send('Строку и с ней ')
            await asyncio.sleep(4)
            await message.channel.send('Смысл темы всей. ')
            await asyncio.sleep(4)
            await message.channel.send('Танец злобного гения ')
            await asyncio.sleep(4)
            await message.channel.send('На страницах произведения. ')
            await asyncio.sleep(4)
            await message.channel.send('Это — игра, без сомнения, ')
            await asyncio.sleep(4)
            await message.channel.send('Обреченный ждет поражение! ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лала-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лала-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай. ')
            await asyncio.sleep(4)
            await message.channel.send('Открыт роман, ')
            await asyncio.sleep(4)
            await message.channel.send('Читатель пьян, ')
            await asyncio.sleep(4)
            await message.channel.send('Разлив вино — ')
            await asyncio.sleep(4)
            await message.channel.send('Шагнул в окно. ')
            await asyncio.sleep(4)
            await message.channel.send('Танец злобного гения ')
            await asyncio.sleep(4)
            await message.channel.send('На страницах произведения. ')
            await asyncio.sleep(4)
            await message.channel.send('Это — игра, без сомнения, ')
            await asyncio.sleep(4)
            await message.channel.send('Обреченный ждет поражение! ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лала-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лала-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай. ')
            await asyncio.sleep(4)
            await message.channel.send('Танец злобного гения ')
            await asyncio.sleep(4)
            await message.channel.send('На страницах произведения. ')
            await asyncio.sleep(4)
            await message.channel.send('Это — игра, без сомнения, ')
            await asyncio.sleep(4)
            await message.channel.send('Обреченный ждет поражение! ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лала-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лала-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай ')
            await asyncio.sleep(4)
            await message.channel.send('Лала-ла-ла-лай.\n\nСпасибо за прослушивание!\nПо желанию вы можете поставить печеньку @banan890 и @kleshevp')
            with open('Король и Шут - Танец злобного гения.mp3', 'rb') as file:
                file_data = discord.File(file)
                await message.channel.send(file=file_data, content='Танец злобного гения')
            song_playing = False
    elif message.content.startswith('!song Прыгну со скалы'):
        if not song_playing:
            song_playing = True
            await message.channel.send(f'Прыгну со скалы\nЗаказал: @{message.author}')
            await message.channel.send('С головы сорвал ветер мой колпак,')
            await asyncio.sleep(4)
            await message.channel.send('Я хотел любви, но вышло всё не так,')
            await asyncio.sleep(4)
            await message.channel.send('Знаю я ничего в жизни не вернуть')
            await asyncio.sleep(4)
            await message.channel.send('И теперь у меня один лишь только путь.')
            await asyncio.sleep(4)
            await message.channel.send('Разбежавшись, прыгну со скалы,')
            await asyncio.sleep(4)
            await message.channel.send('Вот я был и вот меня не стало,')
            await asyncio.sleep(4)
            await message.channel.send('И когда об этом вдруг узнаешь ты,')
            await asyncio.sleep(4)
            await message.channel.send('Тогда поймешь, кого ты потеряла.')
            await asyncio.sleep(4)
            await message.channel.send('Быть таким, как все с детства не умел')
            await asyncio.sleep(4)
            await message.channel.send('Видимо такой в жизни мой удел,')
            await asyncio.sleep(4)
            await message.channel.send('А она, да что она? Вечно мне лгала')
            await asyncio.sleep(4)
            await message.channel.send('И меня никогда понять бы не смогла.')
            await asyncio.sleep(4)
            await message.channel.send('Разбежавшись, прыгну со скалы,')
            await asyncio.sleep(4)
            await message.channel.send('Вот я был и вот меня не стало,')
            await asyncio.sleep(4)
            await message.channel.send('И когда об этом вдруг узнаешь ты,')
            await asyncio.sleep(4)
            await message.channel.send('Тогда поймешь, кого ты потеряла.')
            await asyncio.sleep(4)
            await message.channel.send('Гордо скину плащ, в даль направлю взор,')
            await asyncio.sleep(4)
            await message.channel.send('Может она ждет? Вряд ли. Это вздор,')
            await asyncio.sleep(4)
            await message.channel.send('И издав дикий крик, камнем брошусь вниз')
            await asyncio.sleep(4)
            await message.channel.send('Это моей жизни заключительный каприз.')
            await asyncio.sleep(4)
            await message.channel.send('Разбежавшись, прыгну со скалы,')
            await asyncio.sleep(4)
            await message.channel.send('Вот я был и вот меня не стало,')
            await asyncio.sleep(4)
            await message.channel.send('И тогда себя возненавидишь ты,')
            await asyncio.sleep(4)
            await message.channel.send('Лишь осознав, кого ты потеряла.')
            await asyncio.sleep(4)
            await message.channel.send('Кого ты потеряла.')
            await asyncio.sleep(4)
            await message.channel.send('Кого ты потеряла.\n\nСпасибо за прослушивание!\nПо желанию вы можете поставить печеньку @banan890 и @kleshevp')
            with open('Король и Шут - Прыгну со скалы.mp3', 'rb') as file:
                file_data = discord.File(file)
                await message.channel.send(file=file_data, content='Прыгну со скалы')
            song_playing = False
    elif message.content.startswith('!song Лесник'):
        if not song_playing:
            song_playing = True
            await message.channel.send(f'Лесник\nЗаказал: @{message.author}')
            await message.channel.send('Замученный дорогой, я выбился из сил,')
            await asyncio.sleep(4)
            await message.channel.send('И в доме лесника я ночлега попросил.')
            await asyncio.sleep(4)
            await message.channel.send('С улыбкой добродушной старик меня впустил,')
            await asyncio.sleep(4)
            await message.channel.send('И жестом дружелюбным на ужин пригласил.')
            await asyncio.sleep(4)
            await message.channel.send('Будь как дома путник, я ни в чем не откажу,')
            await asyncio.sleep(4)
            await message.channel.send('Я ни в чем не откажу, я ни в чем не откажу!')
            await asyncio.sleep(4)
            await message.channel.send('Множество историй, коль желаешь расскажу,')
            await asyncio.sleep(4)
            await message.channel.send('Коль желаешь расскажу, коль желаешь расскажу!')
            await asyncio.sleep(4)
            await message.channel.send('На улице темнело, сидел я за столом.')
            await asyncio.sleep(4)
            await message.channel.send('Лесник сидел напротив, болтал о том, о сем.')
            await asyncio.sleep(4)
            await message.channel.send('Что нет среди животных у старика врагов,')
            await asyncio.sleep(4)
            await message.channel.send('Что нравится ему подкармливать волков.')
            await asyncio.sleep(4)
            await message.channel.send('Будь как дома путник, я ни в чем не откажу,')
            await asyncio.sleep(4)
            await message.channel.send('Я ни в чем не откажу, я ни в чем не откажу!')
            await asyncio.sleep(4)
            await message.channel.send('Множество историй, коль желаешь расскажу,')
            await asyncio.sleep(4)
            await message.channel.send('Коль желаешь расскажу, коль желаешь расскажу!')
            await asyncio.sleep(4)
            await message.channel.send('И волки среди ночи завыли под окном.')
            await asyncio.sleep(4)
            await message.channel.send('Старик заулыбался и вдруг покинул дом.')
            await asyncio.sleep(4)
            await message.channel.send('Но вскоре возвратился с ружьем на перевес:')
            await asyncio.sleep(4)
            await message.channel.send('"Друзья хотят покушать, пойдем приятель в лес!"')
            await asyncio.sleep(4)
            await message.channel.send('Будь как дома путник, я ни в чем не откажу,')
            await asyncio.sleep(4)
            await message.channel.send('Я ни в чем не откажу, я ни в чем не откажу!')
            await asyncio.sleep(4)
            await message.channel.send('Множество историй, коль желаешь расскажу,')
            await asyncio.sleep(4)
            await message.channel.send('Коль желаешь расскажу, коль желаешь расскажу!\n\nСпасибо за прослушивание!\nПо желанию вы можете поставить печеньку @banan890 и @kleshevp')
            with open('Король и Шут - Лесник.mp3', 'rb') as file:
                file_data = discord.File(file)
                await message.channel.send(file=file_data, content='Лесник')
            song_playing = False
    elif message.content.startswith('!song Кукла колдуна'):
        if not song_playing:
            song_playing = True
            await message.channel.send(f'Кукла колдуна\nЗаказал: @{message.author}')
            await message.channel.send('Темный, мрачный коридор,')
            await asyncio.sleep(4)
            await message.channel.send('Я на цыпочках, как вор,')
            await asyncio.sleep(4)
            await message.channel.send('Пробираюсь, чуть дыша,')
            await asyncio.sleep(4)
            await message.channel.send('Чтобы не спугнуть')
            await asyncio.sleep(4)
            await message.channel.send('Тех, кто спит уже давно,')
            await asyncio.sleep(4)
            await message.channel.send('Тех, кому не все равно,')
            await asyncio.sleep(4)
            await message.channel.send('В чью я комнату тайком')
            await asyncio.sleep(4)
            await message.channel.send('Желаю заглянуть,')
            await asyncio.sleep(4)
            await message.channel.send('Чтобы увидеть.')
            await asyncio.sleep(4)
            await message.channel.send('Как бессонница в час ночной')
            await asyncio.sleep(4)
            await message.channel.send('Меняет, нелюдимая, облик твой,')
            await asyncio.sleep(4)
            await message.channel.send('Чьих невольница ты идей?')
            await asyncio.sleep(4)
            await message.channel.send('Зачем тебе охотиться на людей?')
            await asyncio.sleep(4)
            await message.channel.send('Крестик на моей груди,')
            await asyncio.sleep(4)
            await message.channel.send('На него ты погляди')
            await asyncio.sleep(4)
            await message.channel.send('Что в тебе способен он')
            await asyncio.sleep(4)
            await message.channel.send('Резко изменить')
            await asyncio.sleep(4)
            await message.channel.send('Много книжек я читал,')
            await asyncio.sleep(4)
            await message.channel.send('Много фокусов видал')
            await asyncio.sleep(4)
            await message.channel.send('Свою тайну от меня не пытайся скрыть!')
            await asyncio.sleep(4)
            await message.channel.send('Я это видел!')
            await asyncio.sleep(4)
            await message.channel.send('Как бессонница в час ночной')
            await asyncio.sleep(4)
            await message.channel.send('Меняет, нелюдимая, облик твой,')
            await asyncio.sleep(4)
            await message.channel.send('Чьих невольница ты идей?')
            await asyncio.sleep(4)
            await message.channel.send('Зачем тебе охотиться на людей?')
            await asyncio.sleep(4)
            await message.channel.send('Очень жаль, что ты тогда мне поверить не смогла,')
            await asyncio.sleep(4)
            await message.channel.send('В то, что новый твой приятель не такой как все!')
            await asyncio.sleep(4)
            await message.channel.send('Ты осталась с ним вдвоем,')
            await asyncio.sleep(4)
            await message.channel.send('Не зная ничего о нем.')
            await asyncio.sleep(4)
            await message.channel.send('Что для всех опасен он, наплевать тебе')
            await asyncio.sleep(4)
            await message.channel.send('И ты попала!')
            await asyncio.sleep(4)
            await message.channel.send('К настоящему колдуну,')
            await asyncio.sleep(4)
            await message.channel.send('Он загубил таких как ты, не одну!')
            await asyncio.sleep(4)
            await message.channel.send('Словно куклой, в час ночной')
            await asyncio.sleep(4)
            await message.channel.send('Теперь он может управлять тобой!')
            await asyncio.sleep(4)
            await message.channel.send('Все происходит как в страшном сне.')
            await asyncio.sleep(4)
            await message.channel.send('И находиться здесь опасно мне! ')
            with open('Король и Шут - Кукла колдуна.mp3', 'rb') as file:
                file_data = discord.File(file)
                await message.channel.send(file=file_data, content='Кукла колдуна')
            song_playing = False
    else:
        pass


client.run(token)
