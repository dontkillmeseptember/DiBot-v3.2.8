from misc.util import CronTrigger
from handlers.users.mailings import send_scheduled_messages, send_scheduled_messages_calendar, send_scheduled_messages_calendar_sad, send_scheduled_messages_sport

# Обработчик рассылок для каждого дня неделе, для вкладки "Рацион на неделю"
job_settings_ration = [
    {
        'func': send_scheduled_messages,
        'args': ("monday",),
        'trigger': CronTrigger(day_of_week='mon', hour=12, minute=30)
    },
    {
        'func': send_scheduled_messages,
        'args': ("tuesday",),
        'trigger': CronTrigger(day_of_week='tue', hour=12, minute=30)
    },
    {
        'func': send_scheduled_messages,
        'args': ("wednesday",),
        'trigger': CronTrigger(day_of_week='wed', hour=12, minute=30)
    },
    {
        'func': send_scheduled_messages,
        'args': ("thursday",),
        'trigger': CronTrigger(day_of_week='thu', hour=12, minute=30)
    },
    {
        'func': send_scheduled_messages,
        'args': ("friday",),
        'trigger': CronTrigger(day_of_week='fri', hour=12, minute=30)
    },
    {
        'func': send_scheduled_messages,
        'args': ("saturday",),
        'trigger': CronTrigger(day_of_week='sat', hour=12, minute=30)
    },
    {
        'func': send_scheduled_messages,
        'args': ("sunday",),
        'trigger': CronTrigger(day_of_week='sun', hour=12, minute=30)
    }
]

# Обработчик для упражнений
settings_sport = [
	{
		'func': send_scheduled_messages_sport,
		'trigger': CronTrigger(hour=10, minute=30)
	}
]

# Обработчик для каждого праздника
settings_calendar = [
    # Январь
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=1, day=7, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=1, day=13, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=1, day=14, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=1, day=25, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=1, day=27, hour=6, minute=30)
	},
    # Февраль
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=2, day=1, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=2, day=9, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=2, day=12, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=2, day=14, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=2, day=15, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=2, day=23, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=2, day=24, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=2, day=27, hour=6, minute=30)
	},
    # Март
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=3, day=8, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=3, day=9, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=3, day=14, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=3, day=16, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=3, day=21, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=3, day=23, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=3, day=27, hour=6, minute=30)
	},
    # Апрель
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=4, day=1, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=4, day=12, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar_sad,
        'trigger': CronTrigger(month=4, day=14, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=4, day=19, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar_sad,
        'trigger': CronTrigger(month=4, day=20, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=4, day=21, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=4, day=22, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar_sad,
        'trigger': CronTrigger(month=4, day=26, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=4, day=30, hour=6, minute=30)
	},
    # Май
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=5, day=1, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=5, day=5, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=5, day=9, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=5, day=17, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=5, day=19, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=5, day=23, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=5, day=25, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=5, day=26, hour=6, minute=30)
	},
    # Июнь
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=6, day=1, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=6, day=12, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=6, day=20, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=6, day=26, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar_sad,
        'trigger': CronTrigger(month=6, day=22, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar_sad,
        'trigger': CronTrigger(month=6, day=28, hour=6, minute=30)
	},
    # Июль
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=7, day=8, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=7, day=15, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=7, day=17, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=7, day=27, hour=6, minute=30)
	},
    # Август
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=8, day=5, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=8, day=6, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar_sad,
        'trigger': CronTrigger(month=8, day=9, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar_sad,
        'trigger': CronTrigger(month=8, day=12, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=8, day=14, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=8, day=27, hour=6, minute=30)
	},
    # Сентябрь
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=9, day=1, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=9, day=5, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=9, day=14, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=9, day=17, hour=6, minute=30)
	},
    # Октябрь
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=10, day=4, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=10, day=5, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=10, day=7, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=10, day=14, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=10, day=21, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=10, day=26, hour=6, minute=30)
	},
    # Ноябрь
    {
		'func': send_scheduled_messages_calendar_sad,
        'trigger': CronTrigger(month=11, day=5, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=11, day=9, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=11, day=16, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=11, day=17, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=11, day=18, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=11, day=29, hour=6, minute=30)
	},
    # Декабрь
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=12, day=3, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=12, day=10, hour=6, minute=30)
	},
    {
		'func': send_scheduled_messages_calendar,
        'trigger': CronTrigger(month=12, day=31, hour=6, minute=30)
	}
]