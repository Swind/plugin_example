# -*- mode: python -*-
a = Analysis(['plugin_loader.py'],
             pathex=['/Users/Swind/Program/Python/plugin_example'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'plugin_loader'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
