#!/usr/bin/env python3
"""
cycle_case.py — Cicla la capitalizzazione del testo selezionato:
TUTTO MAIUSCOLO → tutto minuscolo → Solo Le Iniziali → TUTTO MAIUSCOLO → ...

Dipendenze: xdotool, xclip
"""

import subprocess
import time
import sys


def get_selected_text() -> str:
    """Legge il testo attualmente selezionato (primary selection)."""
    try:
        result = subprocess.run(
            ["xclip", "-selection", "primary", "-o"],
            capture_output=True, text=True, timeout=2
        )
        return result.stdout
    except Exception as e:
        print(f"Errore lettura selezione: {e}", file=sys.stderr)
        return ""


def set_clipboard(text: str) -> None:
    """Scrive il testo negli appunti (clipboard)."""
    subprocess.run(
        ["xclip", "-selection", "clipboard"],
        input=text, text=True, timeout=2
    )


def cycle_case(text: str) -> str:
    """Applica la trasformazione successiva nel ciclo."""
    if text == text.upper() and not text.islower():
        # TUTTO MAIUSCOLO → tutto minuscolo
        return text.lower()
    elif text == text.lower():
        # tutto minuscolo → Solo Le Iniziali Maiuscole
        return text.title()
    else:
        # Solo Le Iniziali (o qualsiasi altra cosa) → TUTTO MAIUSCOLO
        return text.upper()


def paste_text() -> None:
    """Simula Ctrl+V per incollare il testo trasformato."""
    time.sleep(0.05)
    subprocess.run(["xdotool", "key", "--clearmodifiers", "ctrl+v"])


def main():
    original = get_selected_text()

    if not original.strip():
        print("Nessun testo selezionato.", file=sys.stderr)
        sys.exit(1)

    transformed = cycle_case(original)
    set_clipboard(transformed)
    paste_text()


if __name__ == "__main__":
    main()
