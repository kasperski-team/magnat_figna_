# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['shooter_game.py'],
    pathex=[],
    binaries=[],
    datas=[('asteroid.png', '.'), ('bullet.png', '.'), ('fire.ogg', '.'), ('galaxy.jpg', '.'), ('rocket.png', '.'), ('space.ogg', '.'), ('ufo.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SUPER PUPER SHOOTER',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='SUPER PUPER SHOOTER.app',
    icon=None,
    bundle_identifier=None,
)
