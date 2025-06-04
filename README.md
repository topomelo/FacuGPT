# FacuGPT Game Projects

This repository contains sample projects created with **ChatGPT**. The latest addition is a simple Mario-inspired platformer created with Pygame.

## Projects

- `mario_clone/` - Minimal side-scrolling platformer. See the directory for details.
- `file_reader.py` - Versatile script that reads and overwrites several common file formats.
  Use it with `read` or `write` commands:

  ```bash
  python file_reader.py read <path>
  python file_reader.py write <path> [new_contents_file]
  ```
- `text_editor.py` - Simple Tkinter GUI for opening and editing files using the same reader and writer functions. Supports undo with **Ctrl+Z**.

Install the optional dependencies listed in `requirements.txt` to enable features like Excel, PDF and DOCX support:

```bash
pip install -r requirements.txt
```
