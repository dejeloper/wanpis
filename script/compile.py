#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
from pathlib import Path
from datetime import datetime

# Configurar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ========== CONFIGURACIÓN ==========
PROJECT_NAME = "El viaje hacia la libertad"
CHAPTERS_PER_FILE = 20
# ==================================

def extract_chapter_number(filename):
    """Extrae el número del capítulo del nombre del archivo"""
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')

def get_chapters():
    """Obtiene y ordena todos los capítulos del root"""
    # El script está en script/ (root), así que root_dir es el mismo directorio padre
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent

    chapters = []
    chapters_dir = root_dir / 'Chapters'
    for file in chapters_dir.glob('Capítulo_*.txt'):
        chapters.append(file)

    # Ordenar por número de capítulo
    chapters.sort(key=lambda x: extract_chapter_number(x.name))
    return chapters

def clean_output_dir(output_dir):
    """Elimina todos los archivos .txt de la carpeta de salida"""
    if output_dir.exists():
        for file in output_dir.glob('*.txt'):
            file.unlink()
        print(f"[CLEAN] Carpeta limpiada\n")

def generate_dates_file(chapters, output_dir):
    """Genera un archivo con las fechas de creación de los capítulos"""
    extras_dir = Path(__file__).parent.parent / 'Extras'
    extras_dir.mkdir(parents=True, exist_ok=True)
    dates_file = extras_dir / 'fechas_capitulos.txt'

    with open(dates_file, 'w', encoding='utf-8') as f:
        f.write("LISTADO DE FECHAS DE CREACIÓN DE CAPÍTULOS\n")
        f.write("=" * 50 + "\n\n")

        for chapter_file in chapters:
            # Obtener fecha de creación (st_ctime en Windows, en otros OS puede variar)
            creation_time = datetime.fromtimestamp(chapter_file.stat().st_ctime)
            chapter_num = extract_chapter_number(chapter_file.name)
            date_str = creation_time.strftime("%d/%b/%Y")

            f.write(f"Capítulo {chapter_num:03d}: {date_str}\n")

    print(f"[DATES] Listado de fechas generado: fechas_capitulos.txt\n")

def compile_chapters():
    """Compila los capítulos en lotes"""
    chapters = get_chapters()

    if not chapters:
        print("[!] No se encontraron capítulos (Capítulo *.txt)")
        return

    # Directorio de salida: resumen/ (al lado de script/)
    script_dir = Path(__file__).parent
    output_dir = script_dir.parent / 'resumen'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Limpiar carpeta antes de compilar
    clean_output_dir(output_dir)

    # Generar archivo de fechas
    generate_dates_file(chapters, output_dir)

    print(f"[>>] Compilando {len(chapters)} capítulos...")
    print(f"[->] {CHAPTERS_PER_FILE} capítulos por archivo")
    print(f"[>>] Proyecto: {PROJECT_NAME}\n")

    # Agrupar capítulos en lotes
    for i in range(0, len(chapters), CHAPTERS_PER_FILE):
        batch = chapters[i:i + CHAPTERS_PER_FILE]
        start_num = extract_chapter_number(batch[0].name)
        end_num = start_num + CHAPTERS_PER_FILE - 1

        # Nombre del archivo compilado
        output_filename = f"{PROJECT_NAME} {start_num}-{end_num}.txt"
        output_path = output_dir / output_filename

        # Compilar contenido
        content = []
        # Agregar título al inicio
        title = f"{PROJECT_NAME} {start_num}-{end_num}"
        content.append(title)
        content.append('\n\n-\n')

        for idx, chapter_file in enumerate(batch):
            with open(chapter_file, 'r', encoding='utf-8') as f:
                chapter_content = f.read()
                content.append(chapter_content)
                # Separador entre capítulos (excepto al final)
                if idx < len(batch) - 1:
                    content.append('\n\n-\n')

        # Guardar archivo compilado
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(content))

        print(f"[OK] {output_filename}")

    print(f"\n[DONE] Compilación completada en resumen/")

if __name__ == "__main__":
    compile_chapters()
