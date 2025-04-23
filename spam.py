from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

url = "https://raw.githubusercontent.com/lukakukhaleishvili/midtearm-machine-Learning-/main/luka_kukhaleishvili_1_73182468.csv"
df = pd.read_csv(url)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]


#2. ლოგისტიკური რეგრესიის მოდელი

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

coefficients = model.coef_[0]
feature_names = X.columns
for name, coef in zip(feature_names, coefficients):
    print(f"{name}: {coef:.4f}")

#3. მოდელის გადამოწმება
# პროგნოზირება
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")  
print(cm)

# დეტალური ანგარიში
print("\nClassification Report:")
print(classification_report(y_test, y_pred))



#4.  ფუნქცია: შემოწმება ელფოსტა სპამია თუ არა
def check_spam_manual(words, links, capital_words, spam_word_count):
    features = [[words, links, capital_words, spam_word_count]]
    prediction = model.predict(features)
    return "სპამი" if prediction[0] == 1 else "ლეგიტიმური"

print(check_spam_manual(words=100, links=2, capital_words=5, spam_word_count=10))  # სპამი
print(check_spam_manual(words=150, links=0, capital_words=1, spam_word_count=0))   # ლეგიტიმური


#5. მაგალითად სპამ მეილი:
words = 20
links = 1
capital_words = 7
spam_word_count = 5

print(check_spam_manual(words, links, capital_words, spam_word_count))


#6. მაგალითად ლეგიტიმური მეილი:
words = 35
links = 0
capital_words = 0
spam_word_count = 0

print(check_spam_manual(words, links, capital_words, spam_word_count))


#7. დააგენერირეთ რამდენიმე თვალსაჩინო გრაფიკი,
# წყვილთა გრაფიკი
sns.pairplot(df, hue='is_spam', palette='Set2')
plt.suptitle("წყვილთა გრაფიკი სპამის კლასების მიხედვით", y=1.02)
plt.tight_layout()
plt.savefig("pairplot.png")
plt.show()

# ჰისტოგრამა spam_word_count სვეტისთვის
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='spam_word_count', hue='is_spam', multiple='stack', palette='cool')
plt.title("Spam Word Count – სპამი vs ლეგიტიმური")
plt.xlabel("Spam Word Count")
plt.ylabel("რაოდენობა")
plt.savefig("hist_spam_words.png")
plt.show()

# Boxplot capital_words
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='is_spam', y='capital_words', palette='pastel')
plt.title("კაპიტალური სიტყვების რაოდენობა კლასების მიხედვით")
plt.xlabel("is_spam (0=ლეგიტიმური, 1=სპამი)")
plt.ylabel("Capital Words")
plt.savefig("boxplot_capital_words.png")
plt.show()