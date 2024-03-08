from discord import Locale
from discord.app_commands import TranslationContext, Translator, locale_str

TLANSLATION_DATA: dict[Locale, dict[str, str]]= {
	Locale.japanese: {
		'Plays the music specified by url. If music is already being played, it is inserted into the cue.': 'urlで指定された音楽を再生します。すでに音楽が再生されている場合はキューに挿入します。',
		'It is the same as the play command, except that it searches Youtube for the specified words.': '指定された語句でYoutubeを検索すること以外は、playコマンドと同じです。',
		'Connected to voice channel.': 'ボイスチャンネルに接続しました。',
		'Destination Channel': '接続先チャンネル',
		'You are not currently connecting to any voice channel.': 'あなたはボイスチャンネルに接続していません。',
		'Error!': 'エラーが発生しました。',
		'Starts playing the song.': '曲の再生を開始します。',
		'Song inserted into the queue.': '曲をキューに挿入しました。',
		'Video title': 'タイトル',
		'Video URL': '動画URL',
		'Stops the music currently playing and discards the cue.': '今再生している音楽を停止して、キューを破棄します。',
		"neko's Music Bot is not connected to the voice channel.": "neko's Music Botはボイスチャンネルに接続していません。",
		"The song was stopped and the queue was discarded.": "曲を停止し、キューを破棄しました。",
		"The song does not seem to be playing.": "曲が再生されていないようです。",
		"Skips the currently playing music and plays the next music in the queue.": "今再生している音楽をスキップして、キューに入っている次の音楽を再生します。",
		"Skipped one song.": "曲を一曲スキップしました。",
		"Pause the song.": "曲を一時停止しました。",
		"Song paused.": "曲を一時停止しました。",
		"Resume paused song.": "一時停止した音楽を再開します。",
		"Resumed songs that had been paused.": "一時停止していた曲を再開しました。",
		"You can check the available commands.": "使用できるコマンドを確認することができます。",
		"Disconnected from voice channel.": "ボイスチャンネルから切断しました。",
		"Disconnected channel": "切断したチャンネル",
		"Disconnected from voice channel.": "ボイスチャンネルからの接続が切れています",
		"Waiting for song playback": "曲の再生を待機中",
		"*Nico Nico Douga videos take a little time to play. Please understand.": "※ニコニコ動画の動画は再生に少し時間がかかります。ご了承ください。",
		"Playing": "再生中",
		"No songs in queue": "キューに入っている曲はありません",
		"You can check the songs in the queue.": "キュー内の曲を確認することができます。",
	},
	Locale.chinese: {
		'Plays the music specified by url. If music is already being played, it is inserted into the cue.': '播放指定的音乐。如果已经在播放音乐，则将其插入到队列中。',
		'It is the same as the play command, except that it searches Youtube for the specified words.': '与播放命令相同，只是它会在YouTube上搜索指定的词语。',
		'Connected to voice channel.': '已连接到语音频道。',
		'Destination Channel': '目标频道',
		'You are not currently connecting to any voice channel.': '您当前未连接到任何语音频道。',
		'Error!': '错误！',
		'Starts playing the song.': '开始播放歌曲。',
		'Song inserted into the queue.': '歌曲已插入队列。',
		'Video title': '视频标题',
		'Video URL': '视频网址',
		'Stops the music currently playing and discards the cue.': '停止当前播放的音乐并丢弃队列。',
		"neko's Music Bot is not connected to the voice channel.": "neko的音乐机器人未连接到语音频道。",
		"The song was stopped and the queue was discarded.": "歌曲已停止，队列已丢弃。",
		"The song does not seem to be playing.": "似乎没有播放歌曲。",
		"Skips the currently playing music and plays the next music in the queue.": "跳过当前播放的音乐并播放队列中的下一首音乐。",
		"Skipped one song.": "跳过了一首歌曲。",
		"Pause the song.": "暂停歌曲。",
		"Song paused.": "歌曲已暂停。",
		"Resume paused song.": "恢复已暂停的歌曲。",
		"Resumed songs that had been paused.": "恢复已暂停的歌曲。",
		"You can check the available commands.": "您可以检查可用的命令。",
		"Disconnected from voice channel.": "已断开与语音频道的连接。",
		"Disconnected channel": "断开的频道",
		"Disconnected from voice channel.": "已断开与语音频道的连接。",
		"Waiting for song playback": "等待歌曲播放",
		"*Nico Nico Douga videos take a little time to play. Please understand.": "*ニコニコ動画影片需要一點時間播放。請諒解。",
		"Playing": "正在播放",
		"No songs in queue": "队列中没有歌曲",
		"You can check the songs in the queue.": "您可以查看队列中的歌曲。",
	},
	Locale.taiwan_chinese: {
		'Plays the music specified by url. If music is already being played, it is inserted into the cue.': '播放指定的音樂URL。如果已經在播放音樂，則將其插入到佇列中。',
		'It is the same as the play command, except that it searches Youtube for the specified words.': '與播放指令相同，除了會在YouTube上搜尋指定的字詞外。',
		'Connected to voice channel.': '已連接至語音頻道。',
		'Destination Channel': '目標頻道',
		'You are not currently connecting to any voice channel.': '您目前尚未連接至任何語音頻道。',
		'Error!': '錯誤！',
		'Starts playing the song.': '開始播放歌曲。',
		'Song inserted into the queue.': '歌曲已插入佇列。',
		'Video title': '影片標題',
		'Video URL': '影片網址',
		'Stops the music currently playing and discards the cue.': '停止當前播放的音樂並丟棄佇列。',
		"neko's Music Bot is not connected to the voice channel.": "neko的音樂機器人未連接至語音頻道。",
		"The song was stopped and the queue was discarded.": "歌曲已停止並且佇列已丟棄。",
		"The song does not seem to be playing.": "似乎沒有播放歌曲。",
		"Skips the currently playing music and plays the next music in the queue.": "跳過當前播放的音樂並播放佇列中的下一首音樂。",
		"Skipped one song.": "已跳過一首歌曲。",
		"Pause the song.": "暫停歌曲。",
		"Song paused.": "歌曲已暫停。",
		"Resume paused song.": "恢復已暫停的歌曲。",
		"Resumed songs that had been paused.": "已恢復已暫停的歌曲。",
		"You can check the available commands.": "您可以查看可用的指令。",
		"Disconnected from voice channel.": "已斷開與語音頻道的連接。",
		"Disconnected channel": "斷開的頻道",
		"Disconnected from voice channel.": "已斷開與語音頻道的連接。",
		"Waiting for song playback": "等待歌曲播放",
		"*Nico Nico Douga videos take a little time to play. Please understand.": "*ニコニコ動画影片需要一點時間播放。請諒解。",
		"Playing": "正在播放",
		"No songs in queue": "佇列中沒有歌曲",
		"You can check the songs in the queue.": "您可以檢查隊列中的歌曲。",
	},
	Locale.korean: {
		'Plays the music specified by url. If music is already being played, it is inserted into the cue.': '지정된 URL의 음악을 재생합니다. 이미 음악이 재생 중인 경우에는 큐에 삽입됩니다.',
		'It is the same as the play command, except that it searches Youtube for the specified words.': '지정된 단어로 Youtube를 검색하는 것을 제외하고는 play 명령과 동일합니다.',
		'Connected to voice channel.': '음성 채널에 연결되었습니다.',
		'Destination Channel': '대상 채널',
		'You are not currently connecting to any voice channel.': '현재 음성 채널에 연결되어 있지 않습니다.',
		'Error!': '오류!',
		'Starts playing the song.': '노래를 재생합니다.',
		'Song inserted into the queue.': '노래가 큐에 삽입되었습니다.',
		'Video title': '비디오 제목',
		'Video URL': '비디오 URL',
		'Stops the music currently playing and discards the cue.': '현재 재생 중인 음악을 중지하고 큐를 폐기합니다.',
		"neko's Music Bot is not connected to the voice channel.": "neko의 음악 봇이 음성 채널에 연결되지 않았습니다.",
		"The song was stopped and the queue was discarded.": "노래가 중지되었고 큐가 폐기되었습니다.",
		"The song does not seem to be playing.": "노래가 재생되는 것 같지 않습니다.",
		"Skips the currently playing music and plays the next music in the queue.": "현재 재생 중인 음악을 건너뛰고 큐에있는 다음 음악을 재생합니다.",
		"Skipped one song.": "한 곡을 건너 뛰었습니다.",
		"Pause the song.": "노래를 일시 정지합니다.",
		"Song paused.": "노래가 일시 중지되었습니다.",
		"Resume paused song.": "일시 중지된 노래를 다시 재생합니다.",
		"Resumed songs that had been paused.": "일시 중지 된 노래를 다시 재생했습니다.",
		"You can check the available commands.": "사용 가능한 명령을 확인할 수 있습니다.",
		"Disconnected from voice channel.": "음성 채널에서 연결이 해제되었습니다.",
		"Disconnected channel": "연결이 해제된 채널",
		"Disconnected from voice channel.": "음성 채널에서의 연결이 해제되었습니다.",
		"Waiting for song playback": "노래 재생 대기 중",
		"*Nico Nico Douga videos take a little time to play. Please understand.": "* 니코니코 동영상은 재생하는 데 시간이 걸릴 수 있습니다. 양해 바랍니다.",
		"Playing": "재생 중",
		"No songs in queue": "큐에 노래가 없습니다",
		"You can check the songs in the queue.": "대기열에서 노래를 확인할 수 있습니다.",
	},
	Locale.ukrainian: {
		'Plays the music specified by url. If music is already being played, it is inserted into the cue.': 'Відтворює музику, вказану за URL. Якщо музика вже відтворюється, вона вставляється в чергу.',
		'It is the same as the play command, except that it searches Youtube for the specified words.': 'Це те саме, що й команда play, за винятком того, що вона шукає слова, вказані на Youtube.',
		'Connected to voice channel.': 'Підключено до голосового каналу.',
		'Destination Channel': 'Канал призначення',
		'You are not currently connecting to any voice channel.': 'Ви зараз не підключені до жодного голосового каналу.',
		'Error!': 'Помилка!',
		'Starts playing the song.': 'Починає відтворювати пісню.',
		'Song inserted into the queue.': 'Пісня вставлена в чергу.',
		'Video title': 'Назва відео',
		'Video URL': 'URL відео',
		'Stops the music currently playing and discards the cue.': 'Зупиняє відтворення поточної музики та видаляє чергу.',
		"neko's Music Bot is not connected to the voice channel.": "Музичний бот neko не підключений до голосового каналу.",
		"The song was stopped and the queue was discarded.": "Пісня була зупинена, а черга видалена.",
		"The song does not seem to be playing.": "Здається, що пісня не відтворюється.",
		"Skips the currently playing music and plays the next music in the queue.": "Пропускає поточну музику та відтворює наступну пісню в черзі.",
		"Skipped one song.": "Пропущено одну пісню.",
		"Pause the song.": "Призупинити пісню.",
		"Song paused.": "Пісня призупинена.",
		"Resume paused song.": "Відновити призупинену пісню.",
		"Resumed songs that had been paused.": "Відновлені пісні, які були призупинені.",
		"You can check the available commands.": "Ви можете перевірити доступні команди.",
		"Disconnected from voice channel.": "Відключено від голосового каналу.",
		"Disconnected channel": "Відключений канал",
		"Disconnected from voice channel.": "Відключено від голосового каналу.",
		"Waiting for song playback": "Очікування відтворення пісні",
		"*Nico Nico Douga videos take a little time to play. Please understand.": "*Відео Nico Nico Douga потребує трохи часу для відтворення. Будь ласка, розумійте.",
		"Playing": "Відтворення",
		"No songs in queue": "Немає пісень у черзі",
		"You can check the songs in the queue.": "Ви можете перевірити пісні у черзі.",
	},
	Locale.british_english: {
		'Plays the music specified by url. If music is already being played, it is inserted into the queue.': 'Plays the music specified by URL. If music is already being played, it is inserted into the queue.',
		'It is the same as the play command, except that it searches Youtube for the specified words.': 'It is the same as the play command, except that it searches YouTube for the specified words.',
		'Connected to voice channel.': 'Connected to voice channel.',
		'Destination Channel': 'Destination Channel',
		'You are not currently connecting to any voice channel.': 'You are not currently connected to any voice channel.',
		'Error!': 'Error!',
		'Starts playing the song.': 'Starts playing the song.',
		'Song inserted into the queue.': 'Song inserted into the queue.',
		'Video title': 'Video title',
		'Video URL': 'Video URL',
		'Stops the music currently playing and discards the cue.': 'Stops the music currently playing and discards the cue.',
		"neko's Music Bot is not connected to the voice channel.": "neko's Music Bot is not connected to the voice channel.",
		"The song was stopped and the queue was discarded.": "The song was stopped and the queue was discarded.",
		"The song does not seem to be playing.": "The song does not seem to be playing.",
		"Skips the currently playing music and plays the next music in the queue.": "Skips the currently playing music and plays the next music in the queue.",
		"Skipped one song.": "Skipped one song.",
		"Pause the song.": "Pause the song.",
		"Song paused.": "Song paused.",
		"Resume paused song.": "Resume paused song.",
		"Resumed songs that had been paused.": "Resumed songs that had been paused.",
		"You can check the available commands.": "You can check the available commands.",
		"Disconnected from voice channel.": "Disconnected from voice channel.",
		"Disconnected channel": "Disconnected channel",
		"Disconnected from voice channel.": "Disconnected from voice channel.",
		"Waiting for song playback": "Waiting for song playback",
		"*Nico Nico Douga videos take a little time to play. Please understand.": "*Nico Nico Douga videos take a little time to play. Please understand.",
		"Playing": "Playing",
		"No songs in queue": "No songs in queue",
		"You can check the songs in the queue.": "You can check the songs in the queue.",
	},
	Locale.russian: {
		'Plays the music specified by url. If music is already being played, it is inserted into the queue.': 'Воспроизводит музыку, указанную по URL. Если музыка уже играет, она вставляется в очередь.',
		'It is the same as the play command, except that it searches Youtube for the specified words.': 'Это то же самое, что и команда play, за исключением того, что она ищет на YouTube указанные слова.',
		'Connected to voice channel.': 'Подключено к голосовому каналу.',
		'Destination Channel': 'Канал назначения',
		'You are not currently connecting to any voice channel.': 'Вы в настоящее время не подключены к какому-либо голосовому каналу.',
		'Error!': 'Ошибка!',
		'Starts playing the song.': 'Начинает воспроизведение песни.',
		'Song inserted into the queue.': 'Песня добавлена в очередь.',
		'Video title': 'Название видео',
		'Video URL': 'URL видео',
		'Stops the music currently playing and discards the cue.': 'Останавливает воспроизведение текущей музыки и отменяет очередь.',
		"neko's Music Bot is not connected to the voice channel.": "Музыкальный бот neko не подключен к голосовому каналу.",
		"The song was stopped and the queue was discarded.": "Песня была остановлена, а очередь отменена.",
		"The song does not seem to be playing.": "Песня, кажется, не играет.",
		"Skips the currently playing music and plays the next music in the queue.": "Пропускает текущую музыку и воспроизводит следующую в очереди.",
		"Skipped one song.": "Пропущена одна песня.",
		"Pause the song.": "Приостановить песню.",
		"Song paused.": "Песня приостановлена.",
		"Resume paused song.": "Возобновить приостановленную песню.",
		"Resumed songs that had been paused.": "Возобновлены песни, которые были приостановлены.",
		"You can check the available commands.": "Вы можете проверить доступные команды.",
		"Disconnected from voice channel.": "Отключено от голосового канала.",
		"Disconnected channel": "Отключенный канал",
		"Disconnected from voice channel.": "Отключено от голосового канала.",
		"Waiting for song playback": "Ожидание воспроизведения песни",
		"*Nico Nico Douga videos take a little time to play. Please understand.": "*Видеоролики Nico Nico Douga занимают некоторое время на воспроизведение. Пожалуйста, поймите.",
		"Playing": "Воспроизведение",
		"No songs in queue": "Нет песен в очереди",
		"You can check the songs in the queue.": "Вы можете проверить песни в очереди.",
	},
}

FMT_TLANSLATION_DATA: dict[Locale, dict[str, str]] = {
	Locale.japanese: {
		'Rest assured, the error log has been sent automatically to the developer. The error log has been automatically sent to the developer. \nIf you need a support, please join the [support server](https://discord.gg/PN3KWEnYzX). \nThe following is a traceback of the ```python\n{traceback}\n```': '安心してください。エラーログは開発者に自動的に送信されました。\nサポートが必要な場合は、[サポートサーバー](https://discord.gg/PN3KWEnYzX) に参加してください。\n以下、トレースバックです。```python\n{traceback}\n```',
		'{entries_count} songs inserted into the queue.': '{entries_count}個の曲をキューに挿入しました。'
	},
}

class MyTranslator(Translator):
	async def translate(self, string: locale_str, locale: Locale, context: TranslationContext = None):
		if 'fmt_arg' in string.extras:
			fmt = FMT_TLANSLATION_DATA.get(locale, {}).get(string.message, string.message)
			return fmt.format(**(string.extras['fmt_arg']))
		elif TLANSLATION_DATA.get(locale, {}).get(string.message, None) != None:
			return TLANSLATION_DATA.get(locale, {}).get(string.message)
		else:
			return string.message
