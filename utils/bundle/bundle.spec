# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

FILE_DIR = Path(SPECPATH)
PROJECT_ROOT = FILE_DIR.parent.parent

CLI_ENTRYPOINT_SCRIPT = PROJECT_ROOT / 'src/main.py'

block_cipher = None


a = Analysis(
    [str(CLI_ENTRYPOINT_SCRIPT)],
    pathex=[''],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data,
    cipher=block_cipher,
)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PythonProject',
)