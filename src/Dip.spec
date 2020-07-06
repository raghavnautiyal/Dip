# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Dip.py'],
             pathex=['/Users/raghav/Desktop/School/PL_Conquests/Parser/DreamScript/src'],
             binaries=[('/System/Library/Frameworks/Tk.framework/Tk', 'tk'), ('/System/Library/Frameworks/Tcl.framework/Tcl', 'tcl')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Dip',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='/Users/raghav/Desktop/School/PL_Conquests/Parser/DreamScript/src/diplogo.icns')
app = BUNDLE(exe,
             name='Dip.app',
             icon='/Users/raghav/Desktop/School/PL_Conquests/Parser/DreamScript/src/diplogo.icns',
             bundle_identifier=None)
