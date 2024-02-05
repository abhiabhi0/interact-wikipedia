# interact-wikipedia

This project provides api to interact with Wikipedia using wikipedia apis and analysis the text.

It contains two apis:

`/v1/word-frequency-analysis` returns the `n`most frequent words in the `topic`. `topic` and `n` are query parameters.

For eg.

```json
{
  "top_words": [
    {"word": "Python", "frequency": 100},
    {"word": "programming", "frequency": 80},
    {"word": "language", "frequency": 50},
    {"word": "community", "frequency": 40},
    {"word": "development", "frequency": 30}
  ]
}
```

`/v1/search-history` returns the topics searched and the result returned for each search.

For eg.

```json
[
  {
    "topic": "Python",
    "top_words": [
      {"word": "Python", "frequency": 100},
      {"word": "programming", "frequency": 80}
    ]
  },
  {
    "topic": "Artificial Intelligence",
    "top_words": [
      {"word": "chatbot", "frequency": 120},
      {"word": "gpt", "frequency": 90}
    ]
  }
]

```

To see the API specifications, you can copy the content of `oas.yml` and paste in [editor.swagger.io](https://editor.swagger.io/)