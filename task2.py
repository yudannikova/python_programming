sleep_time_minutes = int(input())
start_sleep_hour = int(input())
start_sleep_minutes = int(input())
min_per_hour = 60
min_total = sleep_time_minutes + start_sleep_hour * min_per_hour + start_sleep_minutes
wake_up_hour = min_total // min_per_hour
wake_up_minutes = min_total - wake_up_hour * min_per_hour
print (wake_up_hour)
print (wake_up_minutes)