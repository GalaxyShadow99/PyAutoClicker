# 🖱️ AutoClicker Python

Un petit script Python stylé (et terminal-friendly) qui simule automatiquement des pressions de touches à intervalles aléatoires. Utilise `pyautogui`, `keyboard` et `rich` pour offrir une expérience fluide avec une interface en console colorée !

---

## ✨ Fonctionnalités

- 🔁 Clique automatique sur une touche au choix.
- Configuration facile via un menu interactif.
- Intervalles de clics aléatoires (min / max en ms).
- 💾 Sauvegarde automatique de la config dans `datas.json`.
- 🎨 Interface console stylée avec `rich`.
- ⚠️ Lancement avec privilèges administrateur (requis pour certaines fonctions sur macOS/Linux).

---

## 📦 Dépendances

Installe les dépendances via pip :

```bash
pip install pyautogui keyboard rich
