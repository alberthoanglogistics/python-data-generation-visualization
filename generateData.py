import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)
n_records = 400  

# Modal Split Duisport based on annual report (38% Truck, 42% Barge, and 20% Rail)
modes = np.random.choice(['Truck', 'Barge', 'Rail'], size=n_records, p=[0.38, 0.42, 0.20])

# Initialize lists
processing_times = []
teu_counts = []
delay_times = []
tonnes_list = []

for mode in modes:
    if mode == 'Truck':
        # Truck: 1-2 TEU, processing time 3-5 mins, delay 0-15 mins
        teu = np.random.choice([1, 2], p=[0.7, 0.3])
        teu_counts.append(teu)
        processing_times.append(np.round(np.random.uniform(3, 6), 2))
        delay_times.append(np.round(np.random.uniform(0, 15), 2))
        
        # Random weighted for each TEU from truck
        total_weight = sum(np.random.uniform(5, 22) for _ in range(teu))
        tonnes_list.append(np.round(total_weight, 2))
        
    elif mode == 'Barge':
        # Barge: 20-50 TEU, processing time 30-90 mins, river traffic delay 15-60 mins
        teu = np.random.randint(20, 50)
        teu_counts.append(teu)
        processing_times.append(np.round(np.random.uniform(30, 90), 2))
        barge_delay = 15 + np.random.exponential(scale=22.5)
        delay_times.append(np.round(barge_delay, 2))
        
        # Random weighted for each TEU from barge
        total_weight = sum(np.random.uniform(5, 22) for _ in range(teu))
        tonnes_list.append(np.round(total_weight, 2))
        
    else:  # Rail
        # Rail: 30-80 TEU, processing time 20-45 mins, railway schedule delay 30-60 mins
        teu = np.random.randint(30, 80)
        teu_counts.append(teu)
        processing_times.append(np.round(np.random.uniform(20, 45), 2))
        delay_times.append(np.round(np.random.exponential(scale=50), 2))
        
        # Random weighted for each TEU from rail
        total_weight = sum(np.random.uniform(5, 22) for _ in range(teu))
        tonnes_list.append(np.round(total_weight, 2))

# Create structured DataFrame
df_duisport_sim = pd.DataFrame({
    'ID': [f'IMP-{i+1:04d}' for i in range(n_records)],
    'Shipment_Mode': modes,
    'Container_TEU': teu_counts,
    'Weight_Tonnes': tonnes_list, # Random weight (5 - 22 tonnes/TEU)
    'Processing_Time_Min': processing_times,
    'Delay_Time_Min': delay_times
})

# Export to CSV for Plant Simulation and Python analytics
df_duisport_sim.to_csv('duisport_terminal_input.csv', index=False)
print("Successfully generated simulation dataset!")