# -*- mode: python -*-

import sys 
myLibPath = './images'
sys.path.append(myLibPath)

block_cipher = None

a = Analysis(['puyo.py'],
             pathex=['C:\\Users\\IG17-138\\Documents\\tanaka\\Practice\\puyo'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree('images'),
          a.zipfiles,
          a.datas,
          name='puyo',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='application.ico')
