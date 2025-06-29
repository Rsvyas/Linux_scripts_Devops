import subprocess

disk = subprocess.run(['df','/'], capture_output=True, text=True) 
#print(disk.stdout)
lines = disk.stdout.strip().split("\n")
usage_line = lines[-1]
#print(usage_line)
columns = usage_line.split()
#print(columns)
percentage_used = columns[-2]
#print(percentage_used)
percent_int = int(percentage_used.strip("%"))
if percent_int > 80:
    print("⚠️ ALERT: Disk usage is above 80%!")
else:
    print("✅ Disk usage is within safe limits.")
#print(percent_int)






