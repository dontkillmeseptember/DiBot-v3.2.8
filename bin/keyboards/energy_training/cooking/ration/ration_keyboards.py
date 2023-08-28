from misc.loader import dp

from keyboards.energy_training.cooking.ration.ration_func import (
	process_callback_forward_tuesday,
	process_callback_backward_monday,
	process_callback_forward_wednesday,
	process_callback_backward_tuesday,
	process_callback_forward_thursday,
	process_callback_backward_wednesday,
	process_callback_forward_friday,
	process_callback_backward_thursday,
	process_callback_backward_friday,
	process_callback_forward_sunday,
    process_callback_forward_saturday,
	process_callback_backward_saturday,
    process_callback_backward_monday_two,
    process_callback_backward_tuesday_two,
    process_callback_backward_monday_three,
    process_callback_backward_wednesday_two,
    process_callback_backward_tuesday_three,
    process_callback_backward_monday_four,
	process_callback_backward_wednesday_three,
    process_callback_backward_tuesday_four,
    process_callback_backward_monday_five,
    process_callback_backward_thursday_two,
    process_callback_backward_friday_two,
    process_callback_backward_thursday_three,
    process_callback_backward_wednesday_four,
	process_callback_backward_tuesday_five,
	process_callback_backward_monday_six
)


dp.register_callback_query_handler(process_callback_forward_tuesday, lambda c: c.data == 'forward_tuesday')
dp.register_callback_query_handler(process_callback_backward_monday, lambda c: c.data == 'backward_monday')
dp.register_callback_query_handler(process_callback_backward_monday_two, lambda c: c.data == 'backward_monday_two')
dp.register_callback_query_handler(process_callback_forward_wednesday, lambda c: c.data == 'forward_wednesday')
dp.register_callback_query_handler(process_callback_backward_tuesday_two, lambda c: c.data == 'backward_tuesday_two')
dp.register_callback_query_handler(process_callback_backward_wednesday_two, lambda c: c.data == 'backward_wednesday_two')
dp.register_callback_query_handler(process_callback_backward_tuesday_three, lambda c: c.data == 'backward_tuesday_three')
dp.register_callback_query_handler(process_callback_backward_monday_four, lambda c: c.data == 'backward_monday_four')
dp.register_callback_query_handler(process_callback_backward_wednesday_three, lambda c: c.data == 'backward_wednesday_three')
dp.register_callback_query_handler(process_callback_backward_tuesday_four, lambda c: c.data == 'backward_tuesday_four')
dp.register_callback_query_handler(process_callback_backward_monday_five, lambda c: c.data == 'backward_monday_five')
dp.register_callback_query_handler(process_callback_backward_thursday_two, lambda c: c.data == 'backward_thursday_two')
dp.register_callback_query_handler(process_callback_backward_friday_two, lambda c: c.data == 'backward_friday_two')
dp.register_callback_query_handler(process_callback_backward_thursday_three, lambda c: c.data == 'backward_thursday_three')
dp.register_callback_query_handler(process_callback_backward_wednesday_four, lambda c: c.data == 'backward_wednesday_four')
dp.register_callback_query_handler(process_callback_backward_tuesday_five, lambda c: c.data == 'backward_tuesday_five')
dp.register_callback_query_handler(process_callback_backward_monday_six, lambda c: c.data == 'backward_monday_six')
dp.register_callback_query_handler(process_callback_backward_monday_three, lambda c: c.data == 'backward_monday_three')
dp.register_callback_query_handler(process_callback_backward_tuesday, lambda c: c.data == 'backward_tuesday')
dp.register_callback_query_handler(process_callback_forward_thursday, lambda c: c.data == 'forward_thursday')
dp.register_callback_query_handler(process_callback_backward_wednesday, lambda c: c.data == 'backward_wednesday')
dp.register_callback_query_handler(process_callback_forward_friday, lambda c: c.data == 'forward_friday')
dp.register_callback_query_handler(process_callback_backward_thursday, lambda c: c.data == 'backward_thursday')
dp.register_callback_query_handler(process_callback_forward_saturday, lambda c: c.data == 'forward_saturday')
dp.register_callback_query_handler(process_callback_backward_friday, lambda c: c.data == 'backward_friday')
dp.register_callback_query_handler(process_callback_forward_sunday, lambda c: c.data == 'forward_sunday')
dp.register_callback_query_handler(process_callback_backward_saturday, lambda c: c.data == 'backward_saturday')

