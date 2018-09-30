import psutil

# CPU Modules

def cpu_count():
    return str(psutil.cpu_count(logical=False))

def cpu_clock():
    return (str(int(psutil.cpu_freq(percpu=False).current)) + " Mhz")

def cpu_utilization():
    return (str(psutil.cpu_percent(interval=1)) + "%")

# Power Modules:

def cpu_temp():
    temp_dict = psutil.sensors_temperatures(fahrenheit=True)
    temp_var = list(temp_dict)[1]
    temp_list = temp_dict[temp_var]
    current_temp = temp_list[0].current
    return (str(int(current_temp)) + "°")

def gpu_temp():
    temp_dict = psutil.sensors_temperatures(fahrenheit=True)
    temp_var = list(temp_dict)[0]
    temp_list = temp_dict[temp_var]
    current_temp = temp_list[0].current
    return (str(int(current_temp)) + "°")

def gpu_fan_speed():
    temp_dict = psutil.sensors_fans()
    temp_var = list(temp_dict)[0]
    temp_list = temp_dict[temp_var]
    current_rotation = temp_list[0].current
    return (str(current_rotation) + " RPM")

def cpu_fan_speed():
    temp_dict = psutil.sensors_fans()
    temp_var = list(temp_dict)[1]
    temp_list = temp_dict[temp_var]
    current_rotation = temp_list[1].current
    return (str(current_rotation) + " RPM")

# RAM Modules:

def ram_total():
    return (str(int(psutil.virtual_memory().total / (1024 * 1024))) + " MB")

def ram_used():
    return (str(int(psutil.virtual_memory().active / (1024 * 1024))) + " MB")

def ram_available():
    return (str(int(psutil.virtual_memory().available / (1024 * 1024))) + " MB")

def ram_utilization():
    return (str(int(psutil.virtual_memory().percent)) + "%")

# Storage Modules:

def storage_total():
    return (str(int(psutil.disk_usage('/').total / (1024 * 1024 * 1024))) + " GB")

def storage_used():
    return (str(int(psutil.disk_usage('/').used / (1024 * 1024 * 1024))) + " GB")

def storage_available():
    return (str(int(psutil.disk_usage('/').free / (1024 * 1024 * 1024))) + " GB")

def storage_utilization():
    return str(psutil.disk_usage('/').percent) + "%"