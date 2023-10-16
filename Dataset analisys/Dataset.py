import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dataset.csv')  # Replace 'your_dataset.csv' with the actual filename

fig, axes = plt.subplots(2, 3, figsize=(15, 10))


# CGPA x PlacementStatus
sns.boxplot(x='PlacementStatus', y='CGPA', data=data, ax=axes[0, 0])
axes[0, 0].set_title('1. CGPA vs Placement Status')

# Estagios x PlacementStatus
sns.countplot(x='Internships', hue='PlacementStatus', data=data, ax=axes[0, 1])
axes[0, 1].set_title('2. Internships vs Placement Status')

# Projetos x PlacementStatus
sns.countplot(x='Projects', hue='PlacementStatus', data=data, ax=axes[0, 2])
axes[0, 2].set_title('3. Projects vs Placement Status')

# Soft Skills x PlacementStatus
sns.boxplot(x='PlacementStatus', y='SoftSkillsRating', data=data, ax=axes[1, 1])
axes[1, 1].set_title('4. Soft Skills Rating vs Placement Status')

# Media CGPA, Soft Skills, Projetos, Estagios x PlacementStatus
data['Average'] = data[['CGPA', 'SoftSkillsRating', 'Projects', 'Internships']].mean(axis=1)
sns.barplot(x='PlacementStatus', y='Average', data=data, ax=axes[1, 2])
axes[1, 2].set_title('5. Average (CGPA, Soft Skills, Projects, Internships) vs Placement Status')

plt.tight_layout()

plt.show()