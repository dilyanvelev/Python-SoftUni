import speedtest

test = speedtest.SpeedTest()

down_speed = test.download() / 1_000_000  # Convert bits to megabits
up_speed = test.upload() / 1_000_000  # Convert bits to megabits

print("Download speed: {:.2f} Mbps".format(down_speed))
print("Upload speed: {:.2f} Mbps".format(up_speed))
