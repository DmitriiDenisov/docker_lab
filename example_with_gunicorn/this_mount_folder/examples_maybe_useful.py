def button(bot, update):
    query = update.callback_query
    all_users[update.effective_chat.id]['language'] = query.data
    if query.data == 'English':
        query.edit_message_text(text="Selected English language")
    else:
        query.edit_message_text(text="Выбран Русский язык")

updater.dispatcher.add_handler(CallbackQueryHandler(button))

# df = pd.read_csv('../data/logs.txt', sep=",", header=0)