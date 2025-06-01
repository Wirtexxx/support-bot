from abc import abstractmethod, ABCMeta

from aiogram.utils.markdown import hbold

# Add other languages and their corresponding codes as needed.
SUPPORTED_LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
}


class Text(metaclass=ABCMeta):
    """
    Abstract base class for handling text data in different languages.
    """

    def __init__(self, language_code: str) -> None:
        """
        Initializes the Text instance with the specified language code.

        :param language_code: The language code (e.g., "ru" or "en").
        """
        self.language_code = language_code if language_code in SUPPORTED_LANGUAGES.keys() else "en"

    @property
    @abstractmethod
    def data(self) -> dict:
        """
        Abstract property to be implemented by subclasses. Represents the language-specific text data.

        :return: Dictionary containing language-specific text data.
        """
        raise NotImplementedError

    def get(self, code: str) -> str:
        """
        Retrieves the text corresponding to the provided code in the current language.

        :param code: The code associated with the desired text.
        :return: The text in the current language.
        """
        return self.data[self.language_code][code]


class TextMessage(Text):
    """
    Subclass of Text for managing text messages in different languages,
    tailored for the Vortet Casino support bot.
    """

    @property
    def data(self) -> dict:
        """
        Provides language-specific text data for text messages,
        customized for Vortet Casino support.

        :return: Dictionary containing language-specific text data for text messages.
        """
        return {
            "en": {
                # Shown on /start: greeting + select language + link to support chat
                "select_language": (
                    f"👋 <b>Welcome</b>, {hbold('{full_name}')}!\n\n"
                    "This is the official support bot for <b>Vortet Casino</b>.\n"
                    "Please select your language below:\n\n"
                    "🇬🇧 English\n"
                    "🇷🇺 Русский\n\n"
                    "—\n"
                    "<a href=\"https://t.me/vortet\">Join to Channel</a>"
                ),
                "change_language": "<b>Change language:</b>\n\n🇬🇧 English\n🇷🇺 Русский",
                # Prompt user to ask about casino-related questions
                "main_menu": (
                    "<b>Type your question about Vortet Casino</b>, "
                    "and our support team will get back to you shortly:"
                ),
                "message_sent": "<b>Your message has been sent!</b> Our support team will reply soon.",
                "message_edited": (
                    "<b>Your message was edited only in your chat.</b> "
                    "To resend the updated text, please send it as a new message."
                ),
                "user_started_bot": (
                    f"A user {hbold('{name}')} has started the Vortet Casino Support Bot!\n\n"
                    "Available commands for admins:\n\n"
                    "• /ban\n"
                    "  Block or unblock a user.\n"
                    "<blockquote>Use this to prevent unwanted messages.</blockquote>\n\n"
                    "• /silent\n"
                    "  Toggle silent mode.\n"
                    "<blockquote>When enabled, the user will not receive any messages.</blockquote>\n\n"
                    "• /information\n"
                    "  Show user information.\n"
                    "<blockquote>Retrieve basic details about a user.</blockquote>"
                ),
                "user_restarted_bot": f"A user {hbold('{name}')} has restarted the Vortet Casino Support Bot!",
                "user_stopped_bot": f"A user {hbold('{name}')} has stopped the Vortet Casino Support Bot!",
                "user_blocked": (
                    "<b>User blocked!</b> Messages from this user will not be processed."
                ),
                "user_unblocked": (
                    "<b>User unblocked!</b> Messages from this user will be processed again."
                ),
                "blocked_by_user": (
                    "<b>Cannot send message!</b> The user has blocked the bot."
                ),
                "user_information": (
                    "<b>User Information:</b>\n"
                    "- <b>ID:</b> <code>{id}</code>\n"
                    "- <b>Name:</b> {full_name}\n"
                    "- <b>Status:</b> {state}\n"
                    "- <b>Username:</b> @{username}\n"
                    "- <b>Banned:</b> {is_banned}\n"
                    "- <b>Registered At:</b> {created_at}"
                ),
                "message_not_sent": (
                    "<b>Unable to send message!</b> An unexpected error occurred."
                ),
                "message_sent_to_user": "<b>Your message was delivered to the user!</b>",
                "silent_mode_enabled": (
                    "<b>Silent mode enabled!</b> "
                    "The user will not receive messages until silent mode is disabled."
                ),
                "silent_mode_disabled": (
                    "<b>Silent mode disabled!</b> "
                    "The user will receive all incoming messages."
                ),
            },
            "ru": {
                "select_language": (
                    f"👋 <b>Добро пожаловать</b>, {hbold('{full_name}')}!\n\n"
                    "Это официальный бот поддержки <b>казино Vortet</b>.\n"
                    "Пожалуйста, выберите язык ниже:\n\n"
                    "🇬🇧 English\n"
                    "🇷🇺 Русский\n\n"
                    "—\n"
                    "<a href=\"https://t.me/vortet\">Перейти в наш канал</a>"
                ),
                "change_language": "<b>Сменить язык:</b>\n\n🇬🇧 English\n🇷🇺 Русский",
                "main_menu": (
                    "<b>Задайте свой вопрос о казино Vortet</b>, "
                    "и наша служба поддержки ответит вам в ближайшее время:"
                ),
                "message_sent": "<b>Ваше сообщение отправлено!</b> Ожидайте ответа поддержки.",
                "message_edited": (
                    "<b>Ваше сообщение было отредактировано только в вашем чате.</b> "
                    "Чтобы отправить обновлённый текст, отправьте его как новое сообщение."
                ),
                "user_started_bot": (
                    f"Пользователь {hbold('{name}')} запустил(а) бот поддержки Vortet!\n\n"
                    "Доступные команды для администраторов:\n\n"
                    "• /ban\n"
                    "  Заблокировать или разблокировать пользователя.\n"
                    "<blockquote>Используйте, чтобы остановить нежелательные сообщения.</blockquote>\n\n"
                    "• /silent\n"
                    "  Включить/выключить тихий режим.\n"
                    "<blockquote>При включении пользователь не будет получать сообщения.</blockquote>\n\n"
                    "• /information\n"
                    "  Показать информацию о пользователе.\n"
                    "<blockquote>Получить основные данные о пользователе.</blockquote>"
                ),
                "user_restarted_bot": f"Пользователь {hbold('{name}')} перезапустил(а) бот поддержки Vortet!",
                "user_stopped_bot": f"Пользователь {hbold('{name}')} остановил(а) бот поддержки Vortet!",
                "user_blocked": (
                    "<b>Пользователь заблокирован!</b> Сообщения от этого пользователя не будут обрабатываться."
                ),
                "user_unblocked": (
                    "<b>Пользователь разблокирован!</b> Сообщения от этого пользователя снова обрабатываются."
                ),
                "blocked_by_user": (
                    "<b>Не удалось отправить сообщение!</b> Пользователь заблокировал бота."
                ),
                "user_information": (
                    "<b>Информация о пользователе:</b>\n"
                    "- <b>ID:</b> <code>{id}</code>\n"
                    "- <b>Имя:</b> {full_name}\n"
                    "- <b>Статус:</b> {state}\n"
                    "- <b>Username:</b> @{username}\n"
                    "- <b>Заблокирован:</b> {is_banned}\n"
                    "- <b>Зарегистрирован:</b> {created_at}"
                ),
                "message_not_sent": (
                    "<b>Не удалось отправить сообщение!</b> Произошла непредвиденная ошибка."
                ),
                "message_sent_to_user": "<b>Сообщение успешно доставлено пользователю!</b>",
                "silent_mode_enabled": (
                    "<b>Тихий режим включён!</b> "
                    "Пользователь не будет получать сообщения до отключения тихого режима."
                ),
                "silent_mode_disabled": (
                    "<b>Тихий режим выключен!</b> "
                    "Пользователь снова будет получать все сообщения."
                ),
            },
        }
