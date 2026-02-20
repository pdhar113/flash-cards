# Flashy - French Flash Card App

A Python flash card application to help you learn French vocabulary built with Tkinter.

## Screenshots

| Front Card | Back Card |
|------------|-----------|
| ![Front Card](images/screenshots/Screenshot%202026-02-20%20164001.png) | ![Back Card](images/screenshots/Screenshot%202026-02-20%20164010.png) |

## Features

- Displays French words on flash cards
- Automatically flips to show English translation after 3 seconds
- Track your progress - known words are removed from the deck
- Progress is saved to `data/words_to_learn.csv`
- Clean, minimalist UI with green color scheme

## How It Works

1. A French word appears on the card
2. After 3 seconds, the card flips to reveal the English translation
3. Click the **checkmark** button if you know the word (removes it from the deck)
4. Click the **X** button to see the next word (keeps it in the deck for review)

## Project Structure

```
day-31-flash-card-project-start/
├── main.py                 # Main application code
├── data/
│   ├── french_words.csv    # Original word list (101 French-English pairs)
│   └── words_to_learn.csv  # Generated file tracking remaining words
├── images/
│   ├── card_front.png      # Front card image
│   ├── card_back.png       # Back card image
│   ├── right.png           # Checkmark button
│   └── wrong.png           # X button
└── README.md
```

## Requirements

- Python 3.x
- pandas

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install pandas
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage

- **Start learning:** Run `main.py` to begin
- **Know the word:** Click the green checkmark - the word is removed from your learning list
- **Don't know it:** Click the red X - the word stays in your deck for more practice
- **Reset progress:** Delete `data/words_to_learn.csv` to start over with all 101 words

## Technologies Used

- Python
- Tkinter (GUI)
- Pandas (CSV handling)


