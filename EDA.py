import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Đọc file dữ liệu bạn vừa sinh ra
df = pd.read_csv('duisport_terminal_input.csv')

# Cài đặt giao diện biểu đồ cho đẹp mắt, chuyên nghiệp
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Duisport Terminal Simulation Dataset - Exploratory Data Analysis', fontsize=16, fontweight='bold', y=0.95)

# 1. Biểu đồ 1: Tỷ trọng Modal Split (Count Plot)
sns.countplot(data=df, x='Shipment_Mode', order=['Truck', 'Barge', 'Rail'], palette='Blues_r', ax=axes[0, 0])
axes[0, 0].set_title('1. Shipment Mode Distribution (Modal Split)')
axes[0, 0].set_xlabel('Transport Mode')
axes[0, 0].set_ylabel('Number of Shipments')

# 2. Biểu đồ 2: Thời gian xử lý theo phương thức (Box Plot)
sns.boxplot(data=df, x='Shipment_Mode', y='Processing_Time_Min', order=['Truck', 'Barge', 'Rail'], palette='Set2', ax=axes[0, 1])
axes[0, 1].set_title('2. Processing Time Comparison by Mode (Minutes)')
axes[0, 1].set_xlabel('Transport Mode')
axes[0, 1].set_ylabel('Processing Time (Min)')

# 3. Biểu đồ 3: Phân phối độ trễ (KDE Plot / Distribution)
sns.kdeplot(data=df, x='Delay_Time_Min', hue='Shipment_Mode', common_norm=False, fill=True, alpha=0.3, palette='tab10', ax=axes[1, 0])
axes[1, 0].set_title('3. Delay Time Distribution (Highlighting German Rail & Barge Risk)')
axes[1, 0].set_xlabel('Delay Time (Min)')
axes[1, 0].set_ylabel('Density')

# 4. Biểu đồ 4: Tổng trọng lượng hàng hóa theo phương thức (Bar Plot)
sns.barplot(data=df, x='Shipment_Mode', y='Weight_Tonnes', estimator=sum, order=['Truck', 'Barge', 'Rail'], palette='viridis', ci=None, ax=axes[1, 1])
axes[1, 1].set_title('4. Total Tonnage Handled by Each Transport Mode')
axes[1, 1].set_xlabel('Transport Mode')
axes[1, 1].set_ylabel('Total Weight (Tonnes)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Lưu file ảnh để đưa vào Portfolio/Báo cáo
plt.savefig('duisport_eda_dashboard.png', dpi=300)
print("Successfully generated EDA dashboard image: 'duisport_eda_dashboard.png'!")

plt.show()