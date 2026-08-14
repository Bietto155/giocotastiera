# 🎈 Giochiamo con la Tastiera!

Mini raccolta di giochi da tastiera pensata per bambini di **4 anni**.
Un unico file HTML: si apre con doppio clic, funziona **offline** e senza installare niente.

👉 [`gioco-tastiera.html`](gioco-tastiera.html)

## I quattro giochi

| Tasto | Gioco | Cosa impara |
|---|---|---|
| `1` | 🔤 **Le Lettere** | Riconoscere le lettere e trovarle sulla tastiera ("A come Ape") |
| `2` | 🍓 **Raccogli la Frutta** | Usare le frecce direzionali, coordinazione occhio-mano |
| `3` | 🔢 **Conta con Me** | Contare da 1 a 5 e associare la quantità al numero |
| `4` | ✨ **Tasti Magici** | Gioco libero: ogni tasto fa apparire un disegno e una nota musicale |
| `5` | 🏃 **Corri e Salta** | Il personaggio corre, si salta con lo `SPAZIO` per prendere le stelline ⭐ |

## Comandi

- `1` `2` `3` `4` `5` → scelgono il gioco dal menu
- `ESC` → torna sempre al menu
- `M` → accende/spegne i suoni
- `V` → accende/spegne la voce che legge le parole

## Pensato per i più piccoli

- **Non si può perdere**: nessun timer, nessun punteggio negativo. Se il tasto è
  sbagliato la lettera fa una scossetta e si riprova.
- **Rinforzo positivo**: ogni risposta giusta dà una ⭐; con 5 stelle arriva la
  coppa 🏆 con coriandoli e musichetta.
- **Voce in italiano** tramite la sintesi vocale del browser (se disponibile).
- **Suoni generati dal browser** (Web Audio): nessun file audio da scaricare.
- Rispetta l'impostazione di sistema *riduci animazioni*.

## Note tecniche

- Nessuna dipendenza, nessuna connessione a internet, nessun dato raccolto.
- Testato su Chromium. La voce richiede un browser con `speechSynthesis` e la
  voce italiana installata: se manca, il gioco funziona lo stesso in silenzio.
- Consiglio: aprire a **schermo intero** (`F11`) così il bimbo non tocca per
  sbaglio le altre finestre.
