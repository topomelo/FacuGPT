"""Basic text editor GUI using Tkinter.

This script provides a simple graphical interface to open, edit, and save files
using the multi-format reader/writer from ``file_reader.py``. Only text-based
formats are supported for editing.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

import file_reader


def open_file(text_widget: tk.Text) -> Path | None:
    path_str = filedialog.askopenfilename()
    if not path_str:
        return None
    path = Path(path_str)
    try:
        content = file_reader.read_file(path)
    except Exception as exc:
        messagebox.showerror("Open error", str(exc))
        return None
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, content)
    text_widget.edit_reset()
    return path


def save_file(path: Path | None, text_widget: tk.Text) -> Path | None:
    if path is None:
        path_str = filedialog.asksaveasfilename()
        if not path_str:
            return None
        path = Path(path_str)
    content = text_widget.get("1.0", tk.END)
    try:
        file_reader.write_file(path, content)
    except Exception as exc:
        messagebox.showerror("Save error", str(exc))
        return None
    return path


def make_menu(root: tk.Tk, text: tk.Text) -> tuple[tk.Menu, dict[str, tk.BooleanVar]]:
    menu = tk.Menu(root)

    file_menu = tk.Menu(menu, tearoff=False)
    file_menu.add_command(label="Open", command=lambda: root.event_generate("<<Open>>"))
    file_menu.add_command(label="Save", command=lambda: root.event_generate("<<Save>>"))
    file_menu.add_command(label="Save As", command=lambda: root.event_generate("<<SaveAs>>"))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menu, tearoff=False)
    edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=lambda: text.edit_undo())
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
    edit_menu.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
    edit_menu.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Select All", command=lambda: text.event_generate("<<SelectAll>>"))
    menu.add_cascade(label="Edit", menu=edit_menu)

    return menu, {}


def main() -> None:
    root = tk.Tk()
    root.title("File Editor")
    text = tk.Text(root, wrap="word", undo=True)
    text.pack(fill="both", expand=True)

    current_path: Path | None = None

    def handle_open(event: tk.Event | None = None) -> None:
        nonlocal current_path
        path = open_file(text)
        if path is not None:
            current_path = path
            root.title(f"File Editor - {path}")

    def handle_save(event: tk.Event | None = None) -> None:
        nonlocal current_path
        path = save_file(current_path, text)
        if path is not None:
            current_path = path
            root.title(f"File Editor - {path}")

    def handle_save_as(event: tk.Event | None = None) -> None:
        nonlocal current_path
        path = save_file(None, text)
        if path is not None:
            current_path = path
            root.title(f"File Editor - {path}")

    root.bind("<<Open>>", handle_open)
    root.bind("<<Save>>", handle_save)
    root.bind("<<SaveAs>>", handle_save_as)
    root.bind("<Control-z>", lambda e: text.edit_undo())

    menu, _ = make_menu(root, text)
    root.config(menu=menu)

    root.mainloop()


if __name__ == "__main__":
    main()
