from aiogram import Router, F
from aiogram.filters import Command, MagicData
from aiogram.types import Message
from aiogram_newsletter.manager import ANManager

from app.bot.handlers.private.windows import Window
from app.bot.manager import Manager
from app.bot.utils.create_forum_topic import get_or_create_forum_topic
from app.bot.utils.redis import RedisStorage
from app.bot.utils.redis.models import UserData

router = Router()
router.message.filter(F.chat.type == "private")


@router.message(Command("start"))
async def handler(
        message: Message,
        manager: Manager,
        redis: RedisStorage,
        user_data: UserData,
) -> None:
    """
    Handles the /start command.

    Sends a sticker, then either shows the main menu (if language is set) or
    prompts for language selection. Finally, creates (or fetches) a forum topic.
    After displaying the menu, deletes both the original /start message and the sent sticker.
    """
    # Если язык уже задан — отправляем стикер и показываем главное меню
    if user_data.language_code:
        sticker_msg = await message.bot.send_sticker(
            chat_id=message.chat.id,
            sticker="CAACAgIAAxkBAAEOnqVoPFDGG4ku9yKPMSD4b2ilD3_hOAAC1XYAAk0f4UnF-LXTUdESoDYE"
        )
        await Window.main_menu(manager)
    else:
        # Иначе предлагаем выбрать язык
        sticker_msg = None
        await Window.select_language(manager)

    # Удаляем исходное сообщение /start
    await manager.delete_message(message)

    # Удаляем стикер (если он был отправлен)
    if sticker_msg:
        await manager.delete_message(sticker_msg)

    # Создаём или получаем forum topic для этого пользователя
    await get_or_create_forum_topic(message.bot, redis, manager.config, user_data)


@router.message(Command("language"))
async def handler(
        message: Message,
        manager: Manager,
        user_data: UserData
) -> None:
    """
    Handles the /language command.

    If the user has already selected a language, prompts the user to select a new language.
    Otherwise, prompts the user to select a language.
    """
    if user_data.language_code:
        await Window.change_language(manager)
    else:
        await Window.select_language(manager)
    await manager.delete_message(message)


@router.message(
    Command("newsletter"),
    MagicData(F.event_from_user.id == F.config.bot.DEV_ID),  # type: ignore
)
async def handler(
        message: Message,
        manager: Manager,
        an_manager: ANManager,
        redis: RedisStorage,
) -> None:
    """
    Handles the /newsletter command.
    """
    users_ids = await redis.get_all_users_ids()
    await an_manager.newsletter_menu(users_ids, Window.main_menu)
    await manager.delete_message(message)
