from codecarbon import EmissionsTracker
import time
import json

tracker = EmissionsTracker()
tracker.start()

print("Running workload...")
time.sleep(5)

emissions = tracker.stop()

print("Emissions:", emissions, "kg CO2")

# Save result for website
data = {"emissions": emissions}

with open("emissions.json", "w") as f:
    json.dump(data, f)
